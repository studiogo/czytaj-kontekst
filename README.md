# Czytaj Kontekst — pamięć agenta (plugin Claude Code)

Prosty, polski system pamięci dla Twojego agenta (Claude Code). Daje mu trwałą pamięć:
kim jest, kogo obsługujesz i czego ma nie powtarzać — wszystko w zwykłych plikach `.md`,
które wczytują się na żądanie. Dla osób nietechnicznych. Bez kluczy API, bez kosztów.

> Materiał do Lekcji 2 kursu „Czytaj Kontekst". Pełne wyjaśnienie jest w nagraniu lekcji.

## Co potrzebujesz
- Claude Code (wersja 2.1.143 lub nowsza — sprawdź `/version`).
- Git — na Windowsie zainstaluj wg instrukcji z lekcji (`winget install Git.Git`).
  Na Macu zwykle już jest.

## Instalacja (2 komendy w Claude Code)
```
/plugin marketplace add studiogo/czytaj-kontekst
/plugin install pamiec-agenta@czytaj-kontekst
```
Potem zbuduj pliki pamięci:
```
/zbuduj-pamiec
```

## Co powstaje (w ~/.claude)
- `CLAUDE.md` — tożsamość agenta (uzupełnij o siebie). Tylko jeśli jeszcze go nie masz.
- `pamiec/MEMORY.md` — mapa (drogowskazy, nie magazyn).
- `pamiec/uwagi.md` — reguły z Twoich poprawek (wczytują się na starcie każdej sesji).
- `pamiec/klienci/przyklad-klienta.md` — wzór notatki o kliencie.
- `pamiec/JAK-TO-DZIALA.md` — krótka instrukcja.

## Jak używać
- **Pamięć na żądanie:** w `MEMORY.md` trzymasz tylko drogowskazy; szczegóły klienta agent czyta, gdy temat wraca.
- **Nauka:** poprawiasz agenta → mówisz „zapisz poprawkę" (`/zapisz-poprawke`) → reguła trafia do `uwagi.md`.
- **Higiena:** raz w tygodniu „przejrzyj uwagi" (`/przejrzyj-uwagi`).

## Co ten system robi, a czego nie
**Robi:** pamięta Twoje reguły i wczytuje je sam na starcie sesji; trzyma wiedzę o klientach do doczytania na żądanie.
**Nie robi:** nie czyta Twoich rozmów w tle, nie zgaduje reguł, nie wysyła nic na zewnątrz. Uczy się tylko z Twoich świadomych poprawek.

## Prywatność
Nie wpisuj haseł ani kluczy do plików pamięci — trzymaj tylko nazwę klucza; wartość w sejfie systemu
(Menedżer poświadczeń na Windowsie / Pęk kluczy na Macu).
