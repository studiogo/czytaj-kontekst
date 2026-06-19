---
description: Szuka w pamięci i dawnych rozmowach PO ZNACZENIU (nie po dokładnym słowie). Wymaga wcześniejszego /wlacz-szukanie-znaczeniowe.
---

Użytkownik chce znaleźć coś po znaczeniu (np. „o czym mówiliśmy w sprawie kawiarni", choć słowo „kawiarnia" mogło nie paść).

Wykonaj:
1. Ustal zapytanie (czego szuka). Jeśli nie podał — zapytaj jednym zdaniem.
2. Uruchom wyszukiwanie skryptem w stałej lokalizacji, Pythonem z venv:
   - Mac/Linux: `~/.claude/pamiec/.szukaj/venv/bin/python ~/.claude/pamiec/.szukaj/szukaj_semantyka.py search "<zapytanie>" --k 5`
   - Windows: `%USERPROFILE%\.claude\pamiec\.szukaj\venv\Scripts\python.exe %USERPROFILE%\.claude\pamiec\.szukaj\szukaj_semantyka.py search "<zapytanie>" --k 5`
3. Jeśli zwróci, że indeks pusty / nie włączono — powiedz, żeby najpierw odpalić `/wlacz-szukanie-znaczeniowe`.
4. Pokaż wyniki prosto: dla każdego trafienia data, źródło i fragment; na końcu streść w 1–2 zdaniach, co z tego wynika.

Żeby przeszukać też dawne ROZMOWY (nie tylko pliki pamięci), najpierw odśwież indeks z rozmowami:
`~/.claude/pamiec/.szukaj/venv/bin/python ~/.claude/pamiec/.szukaj/szukaj_semantyka.py index --rozmowy`
