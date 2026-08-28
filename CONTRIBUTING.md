# Jak pomóc przy tej wtyczce

Ta wtyczka jest materiałem do kursu „Czytaj Kontekst”. Ma być zrozumiała dla osób nietechnicznych i działać na świeżo zainstalowanym Claude Code, na Windowsie i na Macu. To wyznacza, co jest tu cenne, a co odpada.

## Najcenniejsze zgłoszenie: „u mnie nie zadziałało”

Wtyczka wpina hooki i tworzy pliki w katalogu domowym, więc psuje się w miejscach, których autor u siebie nie zobaczy. Jeśli któryś z pięciu kroków instalacji nie przeszedł, opisz to — nawet jeśli nie wiesz dlaczego. To jest tu najbardziej wartościowe.

W zgłoszeniu podaj:

- system (Windows czy Mac) i wersję Claude Code (`/version`),
- który krok zawiódł i co dokładnie wypisał ekran (wklej tekst, nie opis),
- wynik `/hooks` — czy widać `SessionStart → wczytaj-uwagi.sh` i `Stop → naucz-sie.py`,
- czy masz Pythona (`python --version` albo `python3 --version`), jeśli rzecz dotyczy szukania po znaczeniu,
- czy Twoja ścieżka domowa ma polskie znaki albo spację.

Nie wklejaj własnych plików pamięci. W `uwagi.md` i w notatkach o klientach siedzą nazwy Twoich klientów, stan Twoich projektów i Twoje ustalenia — zgłoszenie na GitHubie jest publiczne i zostaje tam na zawsze. Jeśli musisz coś z nich pokazać, wytnij sam fragment i pozamieniaj nazwy na „Klient A”.

Zamiast zrzutu ekranu wklej tekst z terminala. Tekst da się przeszukać i skopiować, obrazek nie.

## Co jeszcze przyjmę chętnie

- Poprawki w opisach komend i w README — zwłaszcza miejsca, w których instrukcja zakłada wiedzę, której początkujący nie ma.
- Literówki i błędy językowe.
- Zgłoszenie, że polecenie z README nie działa słowo w słowo tak, jak jest napisane.
- Doniesienie, że wtyczka nadpisała albo skasowała czyjś plik. To traktuję najpoważniej ze wszystkiego.

## Czego nie przyjmę

- Rozbudowy o rzeczy wymagające klucza API, konta w zewnętrznej usłudze albo opłaty. Cała wtyczka ma działać bez klucza i bez kosztów.
- Zależności instalowanych menedżerem pakietów. Poza opcjonalnym Pythonem do szukania po znaczeniu nie dokładamy nic.
- Wysyłania czegokolwiek na zewnątrz. Pamięć zostaje na dysku użytkownika.
- Przepisania wtyczki na inny język programowania albo na inną architekturę. To materiał do lekcji, ma zostać czytelny dla kogoś, kto pierwszy raz widzi kod.
- Zmiany słownictwa na angielskie. Komendy, pliki i komunikaty są po polsku celowo.

## Zmiany w kodzie

1. Odgałęź repozytorium i pracuj na osobnej gałęzi.
2. Sprawdź zmianę na czystej instalacji: usuń wtyczkę, zainstaluj ją od nowa i przejdź pięć kroków z README. Wtyczka, która działa tylko u autora, jest zepsuta.
3. Jeśli ruszasz hooki albo skrypty w `bin/`, sprawdź je na Windowsie w Git Bash. Lista rzeczy do przejścia jest w `WINDOWS-TEST.md`.
4. Nie wpisuj do plików ścieżek ze swoim katalogiem domowym ani swojego imienia. Wtyczka mówi „użytkownik”.
5. W opisie zmiany napisz, co się dzieje u kogoś, kto ma już swoją pamięć — czy jego pliki zostają nietknięte.

## Język

Piszemy prostą polszczyzną: krótkie zdania, zero żargonu bez wyjaśnienia, zero emoji w tekście ciągłym. Adresat to osoba, która wczoraj pierwszy raz otworzyła terminal.

## Bezpieczeństwo

Jeśli znajdziesz coś, co ujawnia cudze dane albo pozwala wykonać kod z zewnątrz, nie zakładaj publicznego zgłoszenia. Napisz na hodorowicz.l@gmail.com.
