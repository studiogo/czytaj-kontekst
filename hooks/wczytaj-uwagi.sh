#!/usr/bin/env sh
# SessionStart hook: wczytuje reguły z ~/.claude/pamiec/uwagi.md do kontekstu sesji.
# Milczy (exit 0), gdy pliku nie ma lub jest pusty — plugin może być zainstalowany
# zanim user odpali /zbuduj-pamiec. Wyjście: JSON z hookSpecificOutput.additionalContext.
# Cross-OS: Mac/Linux (sh) oraz Windows z Git Bash (bo git jest wymagany przez kurs).

UWAGI_FILE="$HOME/.claude/pamiec/uwagi.md"
LIMIT_CHARS="${CZYTAJ_KONTEKST_LIMIT_CHARS:-8000}"

# brak pliku albo pusty -> cisza
if [ ! -s "$UWAGI_FILE" ]; then
  exit 0
fi

# Budujemy additionalContext linia-po-linii z LITERALNYM "\n" (backslash+n),
# bez prawdziwych znaków nowej linii — żeby wynik był zawsze poprawnym JSON-em.
awk -v limit="$LIMIT_CHARS" '
function esc(s) {
  sub(/\r$/, "", s)            # usuń CR z plików Windows (CRLF)
  gsub(/\\/, "\\\\", s)        # backslash MUSI być pierwszy
  gsub(/"/, "\\\"", s)         # cudzysłów
  gsub(/\t/, "\\t", s)         # tabulator
  return s
}
BEGIN {
  prefix = "PAMIĘĆ AGENTA — reguły, których masz pilnować:\\n\\n"
  text = prefix
  truncated = 0
}
{
  line = esc($0) "\\n"
  if (length(text) + length(line) > limit) { truncated = 1; exit }
  text = text line
}
END {
  if (text == prefix) exit 0
  if (truncated) text = text "[Ucięto dalsze uwagi, bo plik jest za długi.]\\n"
  printf("{\"hookSpecificOutput\":{\"hookEventName\":\"SessionStart\",\"additionalContext\":\"%s\"}}\n", text)
}
' "$UWAGI_FILE"

exit 0
