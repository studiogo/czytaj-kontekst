---
description: Włącza wyszukiwanie pamięci PO ZNACZENIU (semantyczne, keyless, bez Ollamy). Jednorazowy krok — stawia venv i pobiera mały model.
---

Użytkownik chce włączyć wyszukiwanie po znaczeniu (przydatne, gdy nie pamięta dokładnego słowa).

Wykonaj:
1. Znajdź instalator `wlacz-szukanie.py` w plikach tego pluginu:
   - Mac/Linux: `find ~/.claude/plugins -name wlacz-szukanie.py 2>/dev/null | head -1`
   - Windows (PowerShell): `Get-ChildItem -Path $env:USERPROFILE\.claude\plugins -Recurse -Filter wlacz-szukanie.py | Select -First 1 -ExpandProperty FullName`
2. Uruchom go SYSTEMOWYM Pythonem (nie z venv):
   - Mac/Linux: `python3 "<ścieżka>"`
   - Windows: `python "<ścieżka>"`
   To potrwa 1–2 min przy pierwszym razie: tworzy venv, instaluje `model2vec`+`numpy`, pobiera mały model (~30 MB), buduje pierwszy indeks. Pokazuj użytkownikowi postęp.
3. Jeśli zwróci błąd o Pythonie — powiedz wprost, że potrzebny jest Python (na Windows: `winget install Python.Python.3.12`), i zatrzymaj się tutaj.
4. Po sukcesie powiedz prosto: wyszukiwanie po znaczeniu włączone; szuka się, mówiąc „szukaj po znaczeniu: …".

Nie instaluj Ollamy ani niczego globalnie — wszystko ląduje w `~/.claude/pamiec/.szukaj/`.
