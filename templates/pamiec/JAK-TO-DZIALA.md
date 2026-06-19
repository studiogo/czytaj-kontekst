# Jak działa ten system pamięci (1 strona)

Agent domyślnie zaczyna każdą rozmowę „od zera". Ten system daje mu trwałą pamięć —
to zwykłe pliki tekstowe, które agent czyta. Cztery warstwy:

1. TOŻSAMOŚĆ — `~/.claude/CLAUDE.md`. Kim agent jest: język, ton, twarde zasady.
   Claude Code czyta to ZAWSZE, w każdym folderze. Dlatego ma być krótki.

2. MAPA — `pamiec/MEMORY.md`. Spis treści: „o kliencie X czytaj w pliku Y". Same drogowskazy.
   Szczegóły agent dociąga dopiero, gdy temat wróci. To jest „pamięć na żądanie".

3. DETALE — `pamiec/klienci/<nazwa>.md` i inne pliki. Cała wiedza o kliencie/projekcie.

4. NAUKA — `pamiec/uwagi.md`. Twoje poprawki jako krótkie reguły. Plugin „pamięć agenta"
   wstrzykuje ten plik na starcie KAŻDEJ sesji, więc agent zawsze zna Twoje reguły.
   Nową regułę dopisujesz, mówiąc „zapisz poprawkę". Raz w tygodniu „przejrzyj uwagi"
   (łączy duplikaty, usuwa nieaktualne).

Czego ten system NIE robi sam: nie czyta Twoich rozmów w tle i nie zgaduje reguł.
Uczy się tylko wtedy, gdy go poprawisz i powiesz „zapisz poprawkę" — prosto i przewidywalnie.

Bezpieczeństwo: NIE wpisuj haseł ani kluczy do tych plików. Trzymaj tylko NAZWĘ klucza;
wartość w sejfie systemu (Menedżer poświadczeń na Windowsie / Pęk kluczy na Macu).

Podgląd w Obsidianie (opcjonalnie): otwórz folder `~/.claude/pamiec` jako vault
(„Open folder as vault") — zobaczysz pliki i graf połączeń. To tylko ładny widok, niczego nie zmienia.
