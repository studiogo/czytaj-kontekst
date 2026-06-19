# Test na czystym Windows 11 (przed wysłaniem kursantom)

Cel: potwierdzić, że plugin instaluje się i hook działa na czystym Windows 11 z Git,
bez Pythona i bez Node. Ground truth — nie ufamy dokumentacji „na słowo".

## Środowisko
- Czysty Windows 11 (VM). Zainstalowane: Claude Code (≥ 2.1.143) + Git (z Git Bash).
- BRAK: osobnego Pythona, Node.

## Kroki
1. `/version` → potwierdź ≥ 2.1.143.
2. `/plugin marketplace add studiogo/czytaj-kontekst` → dodaje się bez błędu (klonuje przez git).
3. `/plugin install pamiec-agenta@czytaj-kontekst` → instaluje; `/reload-plugins` jeśli trzeba.
4. Hook SessionStart zarejestrowany BEZ ręcznej edycji `settings.json` (sprawdź `/hooks` lub restart sesji).
5. PRZED `/zbuduj-pamiec` (brak pamięci): nowa sesja startuje, hook MILCZY — żadnego błędu na ekranie.
6. `/zbuduj-pamiec` → tworzy `~/.claude/pamiec/*` (+ `CLAUDE.md` jeśli brak). Polskie znaki w plikach OK (UTF-8).
7. Dopisz regułę: powiedz coś + „zapisz poprawkę" → reguła ląduje w `uwagi.md`.
8. Nowa sesja (`/clear` lub restart): reguła z `uwagi.md` jest wstrzyknięta do kontekstu (zapytaj agenta o nią).
9. Polskie znaki (ąęćłńóśźż) w uwagach NIE psują konsoli ani wstrzyknięcia.
10. Ścieżka domowa ze znakiem PL (np. `C:\Users\Łukasz`) — hook działa.

## Wynik
- [ ] Instalacja bez błędu gita
- [ ] Hook rejestruje się sam (bez ręcznego settings.json)
- [ ] Milczy przy braku pamięci
- [ ] `/zbuduj-pamiec` tworzy pliki, polskie znaki OK
- [ ] `uwagi.md` wstrzykiwane na starcie sesji
- [ ] Zero potrzeby Pythona/Node
