#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wlacz-szukanie.py — JEDNORAZOWE włączenie wyszukiwania po znaczeniu (semantycznego).

Używa TYLKO biblioteki standardowej (działa systemowym Pythonem, bez żadnych paczek).
Robi:
  1) tworzy własny venv w ~/.claude/pamiec/.szukaj/venv,
  2) instaluje do niego model2vec + numpy (keyless, bez Ollamy),
  3) kopiuje obok skrypt wyszukiwania (szukaj_semantyka.py),
  4) buduje pierwszy indeks pamięci.

Po tym kroku działa komenda „szukaj po znaczeniu" (/szukaj-znaczenie).
Cross-OS: Mac/Linux i Windows (Git Bash / PowerShell — używa systemowego pythona).
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HOME = Path.home()
SZUKAJ = HOME / ".claude" / "pamiec" / ".szukaj"
VENV = SZUKAJ / "venv"
SRC = Path(__file__).resolve().parent / "szukaj_semantyka.py"


def venv_python(venv):
    if os.name == "nt":
        return venv / "Scripts" / "python.exe"
    return venv / "bin" / "python"


def main():
    print("Włączam wyszukiwanie po znaczeniu (to potrwa ~1–2 min przy pierwszym razie)...")
    SZUKAJ.mkdir(parents=True, exist_ok=True)

    # 1. venv
    if not venv_python(VENV).exists():
        print("  - tworzę środowisko (venv)...")
        try:
            subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)
        except Exception as e:
            print(f"  [BŁĄD] Nie udało się utworzyć venv: {e}")
            print("  Sprawdź, czy Python działa: python --version")
            return 1
    py = venv_python(VENV)

    # 2. paczki
    print("  - instaluję model2vec + numpy (keyless, bez Ollamy)...")
    try:
        subprocess.run([str(py), "-m", "pip", "install", "-q", "--disable-pip-version-check",
                        "model2vec", "numpy"], check=True)
    except Exception as e:
        print(f"  [BŁĄD] Instalacja paczek nie powiodła się: {e}")
        return 1

    # 3. skrypt wyszukiwania obok venv (stała ścieżka)
    if SRC.exists():
        shutil.copy2(SRC, SZUKAJ / "szukaj_semantyka.py")
        print("  - skopiowano skrypt wyszukiwania")
    else:
        print(f"  [BŁĄD] Nie znaleziono {SRC.name} obok instalatora.")
        return 1

    # 4. pierwszy indeks (pamięć; pobierze też mały model ~30 MB)
    print("  - buduję pierwszy indeks pamięci (pobiera mały model ~30 MB)...")
    try:
        subprocess.run([str(py), str(SZUKAJ / "szukaj_semantyka.py"), "index"], check=True)
    except Exception as e:
        print(f"  [BŁĄD] Indeksowanie nie powiodło się: {e}")
        return 1

    print("\n[GOTOWE] Wyszukiwanie po znaczeniu włączone.")
    print("Użycie: powiedz „szukaj po znaczeniu: <o co chodzi>” (komenda /szukaj-znaczenie).")
    print("Aby dołączyć dawne rozmowy do indeksu: poproś o odświeżenie indeksu z rozmowami.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
