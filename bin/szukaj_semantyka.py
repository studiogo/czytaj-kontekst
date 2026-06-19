#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
szukaj_semantyka.py — wyszukiwanie pamięci agenta PO ZNACZENIU (keyless, bez Ollamy).

Model: model2vec (statyczne embeddingi, czysty numpy — bez ONNX/torch).
Indeksuje pliki pamięci (~/.claude/pamiec/**/*.md) oraz, opcjonalnie, zapisy
wcześniejszych rozmów (~/.claude/projects/*/*.jsonl). Zapis indeksu: numpy + jsonl.
Bez bazy serwerowej, bez klucza API.

Tryby:
  index   [--rozmowy] [--wszystko] [--limit-plikow N]   zbuduj/odśwież indeks
  search  "zapytanie" [--k 5]                            szukaj po znaczeniu

Wszystko lokalnie w ~/.claude/pamiec/.szukaj/ (embeddings.npy, chunks.jsonl, meta.json).
"""
import argparse
import glob
import json
import os
import sys
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # Windows cp1250 -> UTF-8
except Exception:
    pass

HOME = Path.home()
PAMIEC = HOME / ".claude" / "pamiec"
SZUKAJ = PAMIEC / ".szukaj"
EMB_PATH = SZUKAJ / "embeddings.npy"
CHUNKS_PATH = SZUKAJ / "chunks.jsonl"
META_PATH = SZUKAJ / "meta.json"
PROJECTS = HOME / ".claude" / "projects"

MODEL_NAME = "minishlab/potion-base-8M"   # ~30 MB, statyczny, keyless
CHUNK_CHARS = 800                          # docelowy rozmiar kawałka tekstu
TRANSCRIPT_DAYS = 14                        # domyślnie indeksuj rozmowy z ostatnich 14 dni
TRANSCRIPT_FILES_CAP = 120                  # i nie więcej niż tyle plików (chyba że --wszystko)


def _brak_zaleznosci(e):
    print("Wyszukiwanie po znaczeniu nie jest jeszcze włączone "
          "(brak biblioteki: %s)." % e)
    print("Uruchom najpierw komendę: /wlacz-szukanie-znaczeniowe")
    sys.exit(3)


def _load_model():
    try:
        from model2vec import StaticModel
    except Exception as e:  # noqa
        _brak_zaleznosci(e)
    cache = SZUKAJ / "model"
    cache.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(cache))
    return StaticModel.from_pretrained(MODEL_NAME)


# ── chunking ──────────────────────────────────────────────────────────────────
def _chunk_text(text):
    """Dziel po pustych liniach, sklejaj do ~CHUNK_CHARS, pomiń bardzo krótkie."""
    out, buf = [], ""
    for para in text.replace("\r\n", "\n").split("\n\n"):
        para = para.strip()
        if not para:
            continue
        if len(buf) + len(para) + 2 <= CHUNK_CHARS:
            buf = (buf + "\n\n" + para) if buf else para
        else:
            if buf:
                out.append(buf)
            buf = para if len(para) <= CHUNK_CHARS else para[:CHUNK_CHARS]
    if buf:
        out.append(buf)
    return [c for c in out if len(c) >= 25]


def _zbierz_pamiec():
    items = []
    if not PAMIEC.exists():
        return items
    for p in PAMIEC.rglob("*.md"):
        if ".szukaj" in p.parts:
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        rel = str(p.relative_to(PAMIEC))
        for ch in _chunk_text(txt):
            items.append({"text": ch, "source": "pamiec/" + rel,
                          "date": time.strftime("%Y-%m-%d", time.localtime(p.stat().st_mtime)),
                          "kind": "pamiec"})
    return items


def _zbierz_rozmowy(wszystko=False, limit_plikow=None):
    items = []
    files = glob.glob(str(PROJECTS / "*" / "*.jsonl"))
    if not files:
        return items
    files.sort(key=lambda f: os.path.getmtime(f), reverse=True)
    if not wszystko:
        prog = time.time() - TRANSCRIPT_DAYS * 86400
        files = [f for f in files if os.path.getmtime(f) >= prog]
        cap = limit_plikow or TRANSCRIPT_FILES_CAP
        files = files[:cap]
    for f in files:
        data = str(time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(f))))
        try:
            for ln in Path(f).read_text(encoding="utf-8", errors="replace").splitlines():
                ln = ln.strip()
                if not ln:
                    continue
                try:
                    o = json.loads(ln)
                except Exception:
                    continue
                if o.get("type") not in ("user", "assistant"):
                    continue
                c = o.get("message", {}).get("content", "")
                if isinstance(c, list):
                    c = " ".join(b.get("text", "") for b in c
                                 if isinstance(b, dict) and b.get("type") == "text")
                c = (c or "").strip()
                if len(c) < 25:
                    continue
                who = "Ty" if o.get("type") == "user" else "Agent"
                items.append({"text": c[:CHUNK_CHARS], "source": "rozmowa",
                              "date": data, "kind": "rozmowa", "kto": who})
        except Exception:
            continue
    return items


# ── index / search ──────────────────────────────────────────────────────────
def do_index(rozmowy=False, wszystko=False, limit_plikow=None):
    import numpy as np
    SZUKAJ.mkdir(parents=True, exist_ok=True)
    t = time.time()
    items = _zbierz_pamiec()
    if rozmowy or wszystko:
        items += _zbierz_rozmowy(wszystko=wszystko, limit_plikow=limit_plikow)
    if not items:
        print("Nie ma czego indeksować — najpierw zbuduj pamięć (/zbuduj-pamiec).")
        return 0
    model = _load_model()
    emb = model.encode([it["text"] for it in items])
    emb = np.asarray(emb, dtype="float32")
    norms = np.linalg.norm(emb, axis=1, keepdims=True)
    emb = emb / np.clip(norms, 1e-9, None)   # znormalizowane -> cosine = iloczyn skalarny
    np.save(EMB_PATH, emb)
    with open(CHUNKS_PATH, "w", encoding="utf-8") as fh:
        for it in items:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")
    META_PATH.write_text(json.dumps(
        {"model": MODEL_NAME, "dim": int(emb.shape[1]), "count": len(items),
         "rozmowy": bool(rozmowy or wszystko)}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print(f"[OK] Zindeksowano {len(items)} kawałków "
          f"({sum(1 for i in items if i['kind']=='pamiec')} z pamięci, "
          f"{sum(1 for i in items if i['kind']=='rozmowa')} z rozmów) "
          f"w {time.time()-t:.1f}s.")
    return 0


def do_search(query, k=5):
    import numpy as np
    if not EMB_PATH.exists() or not CHUNKS_PATH.exists():
        print("Indeks pusty. Uruchom najpierw: /wlacz-szukanie-znaczeniowe")
        return 3
    emb = np.load(EMB_PATH)
    chunks = [json.loads(l) for l in CHUNKS_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    model = _load_model()
    q = np.asarray(model.encode([query])[0], dtype="float32")
    q = q / max(float(np.linalg.norm(q)), 1e-9)
    sims = emb @ q
    order = sims.argsort()[::-1][:max(1, k)]
    print(f"Najtrafniejsze po znaczeniu dla: „{query}”\n")
    for rank, i in enumerate(order, 1):
        it = chunks[i]
        snippet = it["text"].replace("\n", " ")
        if len(snippet) > 240:
            snippet = snippet[:240] + "…"
        zrodlo = it["source"] + (f" ({it.get('kto')})" if it.get("kto") else "")
        print(f"{rank}. [{round(float(sims[i]),3)}] {it['date']} · {zrodlo}\n   {snippet}\n")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Wyszukiwanie pamięci po znaczeniu (keyless).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pi = sub.add_parser("index")
    pi.add_argument("--rozmowy", action="store_true", help="dołącz zapisy rozmów (ostatnie dni)")
    pi.add_argument("--wszystko", action="store_true", help="indeksuj WSZYSTKIE rozmowy (może być wolne)")
    pi.add_argument("--limit-plikow", type=int, default=None)
    ps = sub.add_parser("search")
    ps.add_argument("query")
    ps.add_argument("--k", type=int, default=5)
    a = ap.parse_args()
    if a.cmd == "index":
        return do_index(rozmowy=a.rozmowy, wszystko=a.wszystko, limit_plikow=a.limit_plikow)
    if a.cmd == "search":
        return do_search(a.query, k=a.k)
    return 1


if __name__ == "__main__":
    sys.exit(main())
