---
description: Przeszukuje Twoje wcześniejsze rozmowy z Claude Code i streszcza, o czym była mowa (po słowie-kluczu lub dacie). Bez bazy i bez modelu.
---

Użytkownik chce sobie przypomnieć, o czym rozmawialiście wcześniej.

Wykonaj:
1. Ustal, czego szuka: słowo-klucz/temat i/lub przedział czasu (np. „dwa tygodnie temu").
   Jeśli nie podał — zapytaj jednym zdaniem.
2. Przeszukaj zapisy wcześniejszych rozmów Claude Code (pliki `.jsonl`). Leżą w katalogu domowym:
   - Mac/Linux: `~/.claude/projects/<...>/*.jsonl`
   - Windows: `%USERPROFILE%\.claude\projects\<...>\*.jsonl`
   Szukaj po treści (grep) po słowach-kluczach; przy pytaniu o datę — filtruj po dacie pliku.
3. Otwórz najtrafniejsze pliki i streść PROSTO: kiedy (data), o czym była rozmowa, jakie zapadły ustalenia.
   Podaj 1–3 trafienia, od najświeższych. Zacytuj krótko fragment, jeśli pomaga.
4. Jeśli nic nie znajdziesz — powiedz wprost i zaproponuj inne słowo-klucz.

To zwykłe przeszukanie zapisów rozmów — nie potrzebujesz żadnej bazy ani modelu.
(Szukanie „po znaczeniu" — gdy nie pamiętasz dokładnego słowa — to osobny, opcjonalny dodatek; patrz JAK-TO-DZIALA.md.)
