# Czytaj Kontekst — pamięć agenta (plugin Claude Code)

Prosty, polski system pamięci dla Twojego agenta (Claude Code). Daje mu trwałą pamięć:
kim jest, kogo obsługujesz, czego ma nie powtarzać — w zwykłych plikach `.md`, wczytywanych
na żądanie. Dla osób nietechnicznych. Bez kluczy API, bez kosztów.

> Materiał do Lekcji 2 kursu „Czytaj Kontekst". Pełne wyjaśnienie jest w nagraniu lekcji.

## Co potrzebujesz
- Claude Code (wersja 2.1.143 lub nowsza — sprawdź `/version`).
- Git — na Windowsie zainstaluj wg instrukcji z lekcji (`winget install Git.Git`). Na Macu zwykle już jest.

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
- **Twoje reguły:** poprawiasz agenta → mówisz „zapisz poprawkę" (`/zapisz-poprawke`) → reguła trafia do `uwagi.md` i jest wstrzykiwana na starcie każdej sesji.
- **Higiena:** raz w tygodniu „przejrzyj uwagi" (`/przejrzyj-uwagi`).
- **Historia rozmów:** „szukaj w historii" (`/szukaj-historii`) — agent przeszukuje Twoje wcześniejsze rozmowy po słowie-kluczu/dacie i streszcza, o czym była mowa.

## Co się dzieje SAMO (wbudowane w Claude Code)
Claude Code (od 2.1.59) ma **natywną auto-pamięć**: sam zapisuje Twoje korekty i preferencje
do `~/.claude/projects/<projekt>/memory/` i sam je przypomina na starcie. Bez klucza, bez konfiguracji,
na Windowsie też. Ten plugin działa OBOK tego i dokłada to, czego natywne nie ma:
**Twoje widoczne, edytowalne reguły (`uwagi.md`)** + **mapę pamięci na żądanie** + **szukanie w historii**.

## Szukanie „po znaczeniu" (opcjonalny dodatek, w przygotowaniu)
`/szukaj-historii` szuka po słowie-kluczu. Szukanie po ZNACZENIU (gdy nie pamiętasz dokładnego słowa)
to osobny, opcjonalny dodatek — keyless, bez Ollamy (mały model lokalny). Dokładamy go po testach na Windows.

## Co ten system robi, a czego nie
**Robi:** pamięta Twoje reguły i wczytuje je sam na starcie; trzyma wiedzę o klientach do doczytania na żądanie; pozwala przeszukać dawne rozmowy.
**Nie robi:** sam plugin nie czyta Twoich rozmów w tle ani nie wysyła nic na zewnątrz (auto-zapis korekt robi natywna pamięć Claude Code, lokalnie).

## Prywatność
Nie wpisuj haseł ani kluczy do plików pamięci — trzymaj tylko nazwę klucza; wartość w sejfie systemu
(Menedżer poświadczeń na Windowsie / Pęk kluczy na Macu).
