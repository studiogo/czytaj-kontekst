---
name: pamiec-agenta
description: Prosty polski system pamięci agenta — tożsamość (CLAUDE.md), mapa na żądanie (MEMORY.md), notatki klientów i pętla nauki (uwagi.md), instalowany globalnie w ~/.claude. Use when użytkownik mówi „zbuduj pamięć", „zainstaluj pamięć", „zapisz poprawkę", „przejrzyj uwagi", albo pyta jak działa pamięć agenta / pamięć na żądanie.
---

# Pamięć agenta (PL) — prosty system pamięci na żądanie

System pamięci dla osób nietechnicznych. Zwykłe pliki `.md` w `~/.claude` = trwała „pamięć" agenta.
Cztery warstwy + pętla nauki. Bez drugiej AI, bez wyszukiwarki, bez kluczy API, bez kosztów.

## Warstwy
1. Tożsamość — `~/.claude/CLAUDE.md`: kim agent jest, język, ton, twarde zasady. Ładuje się zawsze.
2. Mapa — `~/.claude/pamiec/MEMORY.md`: drogowskazy, gdzie czego szukać. Nie magazyn.
3. Detale na żądanie — `~/.claude/pamiec/klienci/<nazwa>.md`: agent doczytuje, gdy temat wraca.
4. Nauka — `~/.claude/pamiec/uwagi.md`: reguły z poprawek. Wstrzykiwane na starcie każdej sesji.

## Instalacja systemu
Powiedz „zbuduj pamięć" (komenda `/zbuduj-pamiec`). Agent skopiuje szablony z pluginu do `~/.claude`:
`CLAUDE.md` (tylko jeśli go jeszcze nie ma — nie nadpisuje Twojego), `pamiec/MEMORY.md`, `pamiec/uwagi.md`,
`pamiec/klienci/przyklad-klienta.md`, `pamiec/JAK-TO-DZIALA.md`. Po instalacji uzupełnij `CLAUDE.md` o swoją tożsamość.

## Pętla nauki (jak agent się uczy)
- Poprawiasz agenta → mówisz „zapisz poprawkę" (`/zapisz-poprawke`) → dopisuje JEDNĄ krótką regułę do `uwagi.md`.
- Reguły z `uwagi.md` wczytują się SAME na starcie każdej sesji (hook pluginu) — agent zawsze je zna.
- Raz w tygodniu „przejrzyj uwagi" (`/przejrzyj-uwagi`) — łączy duplikaty, usuwa nieaktualne, pilnuje długości.
- NIE czyta rozmów w tle i nie zgaduje reguł — uczy się tylko z Twoich świadomych poprawek.

## Pamięć na żądanie (ważne)
W `MEMORY.md` trzymaj tylko drogowskaz do klienta. Plik klienta otwieraj DOPIERO, gdy w rozmowie
wróci jego nazwa lub temat. Mniej w oknie kontekstu = trafniejszy agent.

## Higiena
- `CLAUDE.md` i `MEMORY.md` trzymaj krótkie (cel: `MEMORY.md` ≤ ~200 linii). Detale → osobne pliki.
- Sekretów (hasła, klucze) NIE wpisuj do plików — tylko NAZWĘ klucza; wartość w sejfie systemu
  (Menedżer poświadczeń na Windowsie / Pęk kluczy na Macu).

## Podgląd w Obsidianie (opcjonalnie)
Otwórz `~/.claude/pamiec` jako vault w Obsidianie — zobaczysz pliki i graf. To ten sam folder, tylko ładny widok.
