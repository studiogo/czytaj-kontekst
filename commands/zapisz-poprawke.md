---
description: Dopisuje jedną krótką regułę z ostatniej poprawki użytkownika do ~/.claude/pamiec/uwagi.md.
---

Użytkownik właśnie Cię poprawił i chce, żeby to zapamiętać na stałe.

Wykonaj:
1. Z bieżącej rozmowy ustal OSTATNIĄ poprawkę/instrukcję użytkownika (np. „nie rób tak", „zawsze X", „pisz inaczej").
   Jeśli nie jest jasne, którą poprawkę zapisać — zapytaj jednym zdaniem.
2. Sformułuj JEDNĄ krótką regułę po polsku, w trybie rozkazującym (np. „Nie skracaj cytatów ze źródeł").
3. Otwórz `~/.claude/pamiec/uwagi.md`. Dopisz regułę bezpośrednio POD linią:
   `<!-- Tu dopisywane są nowe reguły. Nie kasuj tej linii. -->`
   (świeże reguły na górze). Jeśli pliku nie ma — najpierw zbuduj pamięć (`/zbuduj-pamiec`).
4. Nie duplikuj — jeśli identyczna reguła już jest, nie dopisuj drugi raz, tylko to powiedz.
5. Potwierdź jednym zdaniem, jaką regułę dopisałeś. Reguła zadziała od następnej sesji
   (wczyta się sama na starcie).
