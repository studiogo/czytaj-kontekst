---
description: Instaluje prosty system pamięci agenta w ~/.claude (kopiuje szablony z pluginu, nic nie nadpisuje bez zgody).
---

Zbuduj użytkownikowi system pamięci, kopiując szablony z tego pluginu do katalogu domowego Claude Code.

Wykonaj DOKŁADNIE:
1. Ustal katalog domowy Claude Code: `~/.claude` (na Windowsie: `%USERPROFILE%\.claude`).
2. Utwórz katalogi, jeśli nie istnieją: `~/.claude/pamiec` oraz `~/.claude/pamiec/klienci`.
3. Skopiuj pliki z `${CLAUDE_PLUGIN_ROOT}/templates/` do `~/.claude/`, zachowując strukturę:
   - `templates/CLAUDE.md` → `~/.claude/CLAUDE.md` — TYLKO jeśli plik nie istnieje.
     Jeśli istnieje, NIE nadpisuj. Pokaż użytkownikowi treść szablonu i zaproponuj,
     które linie dokleić do jego `CLAUDE.md` (zwłaszcza sekcję „Gdzie co leży (mapa pamięci)").
   - `templates/pamiec/MEMORY.md` → `~/.claude/pamiec/MEMORY.md` — jeśli nie istnieje.
   - `templates/pamiec/uwagi.md` → `~/.claude/pamiec/uwagi.md` — jeśli nie istnieje.
   - `templates/pamiec/JAK-TO-DZIALA.md` → `~/.claude/pamiec/JAK-TO-DZIALA.md` — jeśli nie istnieje.
   - `templates/pamiec/klienci/przyklad-klienta.md` → `~/.claude/pamiec/klienci/przyklad-klienta.md` — jeśli nie istnieje.
4. Pliki, które już istniały, wypisz jako „pominięto (już jest)". Niczego nie nadpisuj bez wyraźnej zgody.
5. Na koniec powiedz prosto, po polsku:
   - co powstało (lista plików),
   - że na starcie KAŻDEJ sesji reguły z `pamiec/uwagi.md` wczytają się same,
   - że teraz warto uzupełnić `~/.claude/CLAUDE.md` o swoją tożsamość (kim agent, ton, zasady),
   - że nową regułę dopisuje się słowami „zapisz poprawkę".

Nie instaluj żadnych zależności. Nie pisz skryptów. Użyj zwykłego odczytu i zapisu plików.
