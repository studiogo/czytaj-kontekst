# Jak działa ten system pamięci (1 strona)

Agent domyślnie zaczyna każdą rozmowę „od zera". Ten system daje mu trwałą pamięć —
to zwykłe pliki tekstowe, które agent czyta. Warstwy:

1. TOŻSAMOŚĆ — `~/.claude/CLAUDE.md`. Kim agent jest: język, ton, twarde zasady.
   Claude Code czyta to ZAWSZE, w każdym folderze. Dlatego ma być krótki.

2. MAPA — `pamiec/MEMORY.md`. Spis treści: „o kliencie X czytaj w pliku Y". Same drogowskazy.
   Szczegóły agent dociąga dopiero, gdy temat wróci. To jest „pamięć na żądanie".

3. DETALE — `pamiec/klienci/<nazwa>.md` i inne pliki. Cała wiedza o kliencie/projekcie.

4. TWOJE REGUŁY — `pamiec/uwagi.md`. Twoje poprawki jako krótkie reguły, które Ty kontrolujesz
   i widzisz. Wstrzykują się na starcie KAŻDEJ sesji. Nową dopisujesz, mówiąc „zapisz poprawkę".
   Raz w tygodniu „przejrzyj uwagi" (łączy duplikaty, usuwa nieaktualne).

5. AUTO-PAMIĘĆ (wbudowana w Claude Code) — niezależnie od tego systemu Claude Code SAM zapisuje
   Twoje korekty i preferencje do `~/.claude/projects/<projekt>/memory/` i sam je przypomina.
   Bez klucza, bez konfiguracji. Czyli agent uczy się sam — a `uwagi.md` daje Ci dodatkowo
   reguły, które widzisz i możesz edytować.

6. HISTORIA ROZMÓW — powiedz „szukaj w historii", a agent przeszuka Twoje dawne rozmowy
   (zapisy w `~/.claude/projects/`) po słowie-kluczu lub dacie i streści, o czym była mowa.

7. SZUKANIE PO ZNACZENIU (opcjonalne, keyless) — włącz raz: „włącz szukanie po znaczeniu"
   (`/wlacz-szukanie-znaczeniowe`). Stawia mały lokalny model (~30 MB, bez Ollamy, bez klucza).
   Potem: „szukaj po znaczeniu: …" (`/szukaj-znaczenie`) znajdzie temat, nawet gdy nie pamiętasz
   dokładnego słowa. Wymaga Pythona.

Bezpieczeństwo: NIE wpisuj haseł ani kluczy do tych plików. Trzymaj tylko NAZWĘ klucza;
wartość w sejfie systemu (Menedżer poświadczeń na Windowsie / Pęk kluczy na Macu).

Podgląd w Obsidianie (opcjonalnie): otwórz folder `~/.claude/pamiec` jako vault
(„Open folder as vault") — zobaczysz pliki i graf połączeń. To tylko ładny widok, niczego nie zmienia.
