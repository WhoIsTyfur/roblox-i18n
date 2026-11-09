# Adapter: Creator Hub CSV

For games whose strings live in the cloud localization table (filled by
Automatic Text Capture, uploads or the Translator Portal).

## In
1. Creator Hub > your experience > Localization > the table > Download CSV
   (or Studio > Localization Tools > Download).
2. `i18n.py ingest csv <file> [--source <locale>]`. Columns `Key`, `Source`,
   `Context`, `Example` and `Location` are read case-insensitively; every
   column that looks like a language code or locale is read as existing
   translations; any other column is carried through untouched. `Location`
   (the object Automatic Text Capture took the text from) goes to the
   context analyst.

## Out
`i18n.py export csv --out <file>` writes only the changed rows, all columns
kept, split into files of at most 1,000 changed rows and under 2 MB
(Roblox's limits per upload). Upload each file in Creator Hub > Localization > the table >
Upload CSV, in order. Uploaded translations become manual and locked, so
Roblox auto-translate will not overwrite them.

Columns: one per target locale plus bare `es`, `pt`, `fr`, `en` for the
default variants (see SKILL.md step 7). The language-codes page says tables
accept language codes or locale IDs; the fallback behavior was verified on
engine LocalizationTables in Studio, not on a Creator Hub upload. If an
upload rejects locale columns, re-export with `--columns language` (one
column per language, default variant) and tell the user regional variants
were merged.

## Limits (Roblox)
- 10,000 entries per table, 2 MB per CSV file, 1,000 added or changed
  entries per upload.
- Source plus Context must be unique, and Key must be unique. An entry with
  no Key is matched by Source plus Context, so two "Play" rows with
  different Context values stay two strings.
- Removing a translation cell from an upload deletes that translation;
  `export` never empties a cell that had text.
