#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
naucz-sie.py — AUTOMATYCZNE samouczenie (hook Stop).

Po turze (z throttlingiem) czyta zapis bieżącej rozmowy, sam wyłapuje poprawki/instrukcje
użytkownika i dopisuje je jako krótkie reguły do ~/.claude/pamiec/uwagi.md.
„Drugą AI" jest lokalny `claude -p` (model haiku) — BEZ klucza API (używa Claude Code,
którego user już ma). Reguły wczytuje na starcie hook SessionStart (wczytaj-uwagi.sh).

Zabezpieczenia:
  - PAMIEC_SKIP_HOOK=1 ustawiane przy wołaniu `claude -p` -> brak pętli hooków.
  - throttle 30 min (nie analizuje po każdej turze).
  - milczy (exit 0) gdy brak uwagi.md (plugin może być przed /zbuduj-pamiec) lub gdy błąd.
  - dedup: nie dopisuje reguły, która już jest.

Tryb testowy bez modelu: PAMIEC_TEST_OUT="- reguła" (użyte zamiast wołania claude).
Ręczne odpalenie na żywo (do demo): python naucz-sie.py --teraz
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SKIP = "PAMIEC_SKIP_HOOK"
HOME = Path.home()
UWAGI = HOME / ".claude" / "pamiec" / "uwagi.md"
STATE = HOME / ".claude" / "pamiec" / ".naucz-last-run"
PROJECTS = HOME / ".claude" / "projects"
THROTTLE_S = 1800   # 30 min
MODEL = "haiku"
ANCHOR = "<!-- Tu dopisywane są nowe reguły. Nie kasuj tej linii. -->"


def _newest_transcript(exclude=None):
    files = glob.glob(str(PROJECTS / "*" / "*.jsonl"))
    if exclude:
        files = [f for f in files if exclude not in os.path.basename(f)]
    if not files:
        return None
    files.sort(key=lambda f: os.path.getmtime(f), reverse=True)
    return files[0]


def _collect(transcript):
    msgs = []
    try:
        for ln in Path(transcript).read_text(encoding="utf-8", errors="replace").splitlines()[-200:]:
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
            if c:
                msgs.append(("UŻYTKOWNIK" if o.get("type") == "user" else "AGENT") + ": " + c)
    except Exception:
        return ""
    return "\n".join(msgs[-30:])[-10000:]


def _ask_claude(convo, existing):
    out = os.environ.get("PAMIEC_TEST_OUT")
    if out is not None:
        return out
    prompt = (
        "Przeczytaj rozmowę. Wyłap TYLKO poprawki i instrukcje użytkownika do agenta "
        "(typu: nie rób tak / zawsze X / pamiętaj Y / pisz inaczej). Każdą zapisz jako jedno "
        "krótkie zdanie po polsku, w trybie rozkazującym, zaczynając wiersz od myślnika. "
        "Pomiń rzeczy jednorazowe. NIE powtarzaj reguł, które już są niżej. "
        "Jeśli nic nowego: napisz dokładnie BRAK.\n\n"
        "ISTNIEJĄCE REGUŁY:\n" + (existing or "(brak)") + "\n\nROZMOWA:\n" + convo + "\n\nReguły albo BRAK:"
    )
    env = dict(os.environ)
    env[SKIP] = "1"
    exe = shutil.which("claude") or "claude"
    cmd = (["cmd", "/c", exe, "-p", "--model", MODEL] if os.name == "nt"
           else [exe, "-p", "--model", MODEL])
    try:
        return subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                              env=env, timeout=120).stdout or ""
    except Exception:
        return ""


def _norm(s):
    return re.sub(r"[^a-ząćęłńóśźż0-9]+", " ", s.lower()).strip()


def run(verbose=False):
    if os.environ.get(SKIP):
        return 0
    if not UWAGI.exists():            # brak pamięci -> nie twórz, milcz
        if verbose:
            print("Brak uwagi.md — najpierw /zbuduj-pamiec.")
        return 0
    # throttle (poza trybem --teraz)
    if not verbose:
        try:
            if STATE.exists() and (time.time() - float(STATE.read_text().strip() or "0")) < THROTTLE_S:
                return 0
        except Exception:
            pass
    data = {}
    try:
        raw = sys.stdin.read() if (not sys.stdin.isatty()) else ""
        if raw.strip():
            data = json.loads(raw)
    except Exception:
        data = {}
    transcript = data.get("transcript_path")
    sid = data.get("session_id")
    if not transcript or not Path(transcript).exists():
        transcript = _newest_transcript(exclude=sid)
    if not transcript or not Path(transcript).exists():
        return 0
    convo = _collect(transcript)
    if len(convo) < 40:
        return 0
    existing = UWAGI.read_text(encoding="utf-8")
    out = _ask_claude(convo, existing)
    rules = [l.strip(" -*•\t") for l in out.splitlines() if l.strip().startswith(("- ", "* ", "•"))]
    en = _norm(existing)
    fresh = [r for r in rules if len(r) > 5 and _norm(r) not in en]
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(str(time.time()), encoding="utf-8")
    if fresh:
        block = "\n".join("- " + r for r in fresh)
        if ANCHOR in existing:
            existing = existing.replace(ANCHOR, ANCHOR + "\n" + block, 1)
        else:
            existing = existing.rstrip() + "\n" + block + "\n"
        UWAGI.write_text(existing, encoding="utf-8")
    if verbose:
        if fresh:
            print("Nauczyłem się nowych reguł:")
            for r in fresh:
                print("  - " + r)
        else:
            print("Nic nowego do nauki (albo reguły już były).")
    return 0


if __name__ == "__main__":
    sys.exit(run(verbose="--teraz" in sys.argv[1:]))
