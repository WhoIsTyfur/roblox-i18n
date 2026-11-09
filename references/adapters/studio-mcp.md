# Adapter: live Roblox Studio over MCP

For a place open in Studio with an MCP server that exposes `execute_luau`
(the official Roblox Studio MCP does). Everything runs in Edit mode; nothing
opens Play.

## In
1. `i18n.py studio dump [--table GameStrings] [--offset 0 --limit 400]`
   prints a Luau snippet. Run it with `execute_luau`. The result is JSON with
   every LocalizationTable path in `LocalizationService` and one page of
   entries. If `missing` is set, pick the right table from `tables` and run
   again with `--table`.
2. Save each page's JSON to `.roblox-i18n/studio-dump-N.json`; repeat with
   `--offset 400`, `800`, ... until `offset + 400 >= total`.
3. `i18n.py ingest studio .roblox-i18n/studio-dump-*.json`.

If the game has no table yet (text only through AutoLocalize or hard-coded
strings), the inventory comes from the GUI and scripts instead: walk
`StarterGui` and `ReplicatedStorage` for TextLabel/TextButton/TextBox text
with AutoLocalize on, and the string modules the scripts use. Build a CSV
(`Key,Source,Context,Example`) from that and use the CSV adapter.

## Context
Over the MCP the context analyst can read scripts (`script_search`,
`script_read`) and inspect GUI objects for size, `TextScaled` and font size,
which gives real length budgets.

## Out
1. `i18n.py export studio [--table GameStrings]` writes
   `.roblox-i18n/out/studio/load-NN.luau`. Each chunk merges its entries into
   the table (`GetEntries` -> merge -> `SetEntries`, existing translations
   for other locales kept) inside one ChangeHistory recording, so Undo works.
2. Run every chunk with `execute_luau` in order and read each return line.
3. Do not save or publish the place; tell the user it is ready and let them.

A table under `LocalizationService` ships with the place and is used by
AutoLocalize and by `GetTranslatorForPlayerAsync`. If the game also uses the
cloud table for the same strings, keep one home per string.

## Verify
`i18n.py studio verify` writes `verify-NN.luau` (6 locales each). Each calls
`LocalizationService:GetTranslatorForLocaleAsync(locale)` and
`FormatByKey(key, sampleArgs)` for every translated key and compares the
result with the expected text; it also checks fallback locales es-419,
fr-be and pt-ao. Every mismatch or throw is a bug: a missing column, a
renamed `{param}`, or a key that differs from the table.
