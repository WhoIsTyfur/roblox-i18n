# Adapter: Rojo LocalizationTable CSV

For projects synced with Rojo, where a `.csv` file in the source tree becomes
a `LocalizationTable` (header `Key,Source,Context,Example,<languages>`).

## In
`i18n.py ingest csv path/to/Strings.csv --rojo`. Find the files with a search
for `*.csv` under the Rojo tree whose first line starts with `Key,Source` or
`Source,`. One run per file; give each its own `--work` folder if a project
has several tables.

## Context
The game code is in the repo, so the context analyst should search for each
key (`FormatByKey("shop.buy"`, the string module, `GetString`) and for
`AutoLocalize` text set in GUI files (`.model.json`, `.rbxmx`) to fill
`where`, `role` and `max`.

## Out
`i18n.py export csv --rojo path/to/Strings.csv` rewrites the file in place:
all rows, original column order, new locale columns appended, the file's own
BOM and line endings kept. Review the diff, then let the user commit; Rojo
syncs it on the next build. Rojo reads the file as-is, so the column scheme
is the engine behavior verified in Studio: exact locale columns plus bare
`es`, `pt`, `fr`, `en` default columns.
