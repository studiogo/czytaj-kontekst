# Czytaj Kontekst — pamięć agenta (plugin Claude Code)

Prosty, polski system pamięci dla Twojego agenta (Claude Code). Daje mu trwałą pamięć:
kim jest, kogo obsługujesz, czego ma nie powtarzać — w zwykłych plikach `.md`, wczytywanych
na żądanie. Dla osób nietechnicznych. Bez kluczy API, bez kosztów.

> Materiał do Lekcji 2 kursu „Czytaj Kontekst". Pełne wyjaśnienie jest w nagraniu lekcji.

## Co potrzebujesz
- Claude Code (wersja 2.1.143 lub nowsza — sprawdź `/version`).
- Git — na Windowsie zainstaluj wg instrukcji z lekcji (`winget install Git.Git`). Na Macu zwykle już jest.
- Python — TYLKO jeśli chcesz wyszukiwanie po znaczeniu (na Windowsie: `winget install Python.Python.3.12`). Reszta działa bez Pythona.

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
- **Uczenie (automatyczne):** po turze plugin sam wyłapuje Twoje poprawki z rozmowy i dopisuje je jako reguły do `uwagi.md` (Haiku, keyless). Możesz też dopisać ręcznie: „zapisz poprawkę" (`/zapisz-poprawke`). Reguły wczytują się na starcie każdej sesji.
- **Higiena:** raz w tygodniu „przejrzyj uwagi" (`/przejrzyj-uwagi`).
- **Historia rozmów:** „szukaj w historii" (`/szukaj-historii`) — agent przeszukuje Twoje wcześniejsze rozmowy po słowie-kluczu/dacie i streszcza, o czym była mowa.

## Co się dzieje SAMO
- **Plugin uczy się sam:** po turze (throttle ~30 min) wyłapuje Twoje poprawki z rozmowy i dopisuje reguły do `uwagi.md` (lokalny `claude -p`, Haiku, keyless), które wczytują się na starcie kolejnej sesji.
- **Natywna auto-pamięć Claude Code** (od 2.1.59) działa OBOK: sama zapisuje korekty/preferencje do `~/.claude/projects/<projekt>/memory/` i przypomina na starcie. Bez klucza, na Windowsie też.

Plugin dokłada do tego: **Twoje widoczne, edytowalne reguły (`uwagi.md`)** + **mapę na żądanie** + **szukanie (po słowie i po znaczeniu)**.

## Szukanie „po znaczeniu" (semantyczne — keyless, bez Ollamy)
`/szukaj-historii` szuka po słowie-kluczu. Szukanie po ZNACZENIU (gdy nie pamiętasz dokładnego słowa)
włączasz RAZ komendą `/wlacz-szukanie-znaczeniowe` — stawia mały lokalny model (~30 MB), bez Ollamy, bez klucza API.
Potem szukasz: `/szukaj-znaczenie "<o co chodzi>"`. Indeksuje pliki pamięci; żeby dołączyć dawne rozmowy,
poproś o odświeżenie indeksu z rozmowami. Wymaga zainstalowanego Pythona.

## Co ten system robi, a czego nie
**Robi:** pamięta Twoje reguły i wczytuje je sam na starcie; trzyma wiedzę o klientach do doczytania na żądanie; pozwala przeszukać dawne rozmowy.
**Nie robi:** nie wysyła nic na zewnątrz — auto-łapanie poprawek działa lokalnie, przez Twój własny Claude Code (`claude -p`, keyless), nie przez zewnętrzne API.

## Prywatność
Nie wpisuj haseł ani kluczy do plików pamięci — trzymaj tylko nazwę klucza; wartość w sejfie systemu
(Menedżer poświadczeń na Windowsie / Pęk kluczy na Macu)