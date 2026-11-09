# Pipeline files and formats

All paths are under the work folder (default `.roblox-i18n/` in the game
project). JSON is UTF-8. Keys are the LocalizationTable `Key`. An entry with
no Key uses its Source text as the key, or `Source | Context` when it has a
Context, because Roblox identifies such an entry by Source plus Context.

```
.roblox-i18n/
  config.json            source locale, input adapter and path
  source.json            the strings to translate
  existing.json          translations already in the table
  state.json             what this tool translated, with the source hash used
  audit.md               localizability findings (step 3)
  context.json           per-string context (context analyst)
  glossary.json          game terms and decisions (context analyst)
  plan.json              locales and batches for this run
  locales/<locale>/
    terms.json           this locale's renderings of glossary terms
    batch-01.todo.json   keys of the batch (written by `plan`)
    batch-01.in.json     translator input (written by `pack`)
    batch-01.draft.json  translator output
    batch-01.backin.json blind input for the back-translator (written by `backpack`)
    batch-01.back.json   back-translator output
    batch-01.reviewin.json reviewer input (written by `reviewpack`)
    batch-01.review.json reviewer output
    batch-01.resolve.json resolve-round output (optional)
    final.json           merged result for the locale (written by `apply`)
    history/NNN/         batch files of earlier runs (moved there by `plan`)
    disputes.json        translator vs reviewer disagreements (written by `apply --resolve`)
    decisions.json       orchestrator rulings: {"key": {"text", "reason", "needs_native"?, "keep"?}}
  out/                   exported files
  report.md
```

Commit `state.json`, `context.json` and `glossary.json` with the game so the
next run only translates what changed. The rest can be ignored by git.

The tool reads every file an agent wrote before the next agent runs
(`pack`, `backpack`, `reviewpack`, `apply`). It stops with the file name
and the problem when JSON is invalid, a key is missing, a text is empty or
a field has a value outside its list.

## source.json
```json
{"source_locale": "en-us",
 "strings": [{"key": "shop.buy", "source": "Buy", "context": "", "example": "",
   "hash": "3f2a9c0b1d7e", "keyless": false}]}
```
`hash` = first 12 hex chars of SHA-1 over `source + "\x1f" + context`.
`keyless` is true for an entry with no Key. `location` is added when the
table has a Location column (the object Roblox captured the text from).

## existing.json
`{"shop.buy": {"es": "Comprar", "fr-fr": "Acheter"}}`, with column names as found.

## context.json
```json
{"game": {"title": "...", "genre": "...", "core_loop": "...", "audience": "...", "tone": "..."},
 "strings": {"shop.buy": {"where": "under each shop item", "role": "button", "max": 8,
   "params": {}, "neighbors": ["shop.title"], "notes": ""}}}
```
`role` is one of: button, title, label, toast, dialog body, tutorial, prompt,
system chat, product name, item description, text box placeholder, toggle,
banner, popup, other. `max` is a character budget as a number (null if
unknown). `params` maps each `{name}` to `{"meaning": "...", "sample": "25"}`.
Every string needs `where` and `role`.

## glossary.json
```json
{"terms": [{"term": "Rebirth", "meaning": "reset coins and pets for a permanent multiplier",
  "decision": "translate", "reason": "core mechanic; players read it in their language", "notes": ""},
 {"term": "Pet Hatch Tycoon", "meaning": "game title", "decision": "keep", "reason": "brand"}]}
```
`decision`: `translate`, `keep` (byte-identical in every locale) or
`transliterate` (write it in the target script, e.g. katakana; same sound).
A locale guide can override `translate` -> `keep` for gaming words its
players keep in English; it can never override `keep`.

## batch-NN.todo.json (written by `plan`)
```json
{"locale": "es-mx", "batch": 1, "keys": ["shop.buy", "coins.count"], "mode": "translate"}
```
`mode` is `translate`, or `audit` (the draft is the existing translation and
only the back-translator and reviewer run).

## batch-NN.in.json (written by `pack`)
```json
{"locale": "es-mx", "locale_name": "Spanish (Mexico)", "batch": 1, "mode": "translate",
 "game": {"title": "...", "tone": "..."},
 "strings": {"shop.buy": {"source": "Buy", "where": "under each shop item", "role": "button", "max": 8,
   "neighbors": [{"key": "shop.title", "source": "Shop", "translation": "Tienda"}]}}}
```
Only the batch's own strings, so an agent never loads the whole table. A
neighbor carries `translation` when that string is already translated in
this locale and is not part of the run.

## terms.json (translator, first batch only)
`{"Rebirth": "Renacer", "Pet Hatch Tycoon": "Pet Hatch Tycoon"}`. Later
batches and the reviewer reuse it unchanged.

## batch-NN.draft.json (translator)
```json
{"shop.buy": {"text": "Comprar", "confidence": "high"},
 "pass.vip": {"text": "VIP", "keep": true, "note": "VIP is used as-is in Latin America", "confidence": "high"},
 "coins.count": {"text": "Monedas: {count}", "note": "avoids plural: count can be 1", "confidence": "high"}}
```
`confidence`: high, medium, low. `keep: true` marks text that is
deliberately the same as the source, or in Latin letters in a locale that
writes another script. `note` explains any non-literal choice.

## batch-NN.backin.json (written by `backpack`) and batch-NN.back.json (back-translator)
```json
{"s001": {"text": "Comprar", "role": "button", "where": "under each shop item"}}
```
```json
{"s001": "Buy", "s002": "Coins: {count} [reads like a label, not a sentence]"}
```
`s001` is the first key of the batch's todo list, `s002` the second. The
ids hide the keys, and `backpack` blanks the source text, glossary terms
and key names out of `where`. A trailing `[remark]` on a string the
reviewer passed is kept in `final.json` as `blind_remark`.

## batch-NN.reviewin.json (written by `reviewpack`)
The `in.json` entry of every string plus `text`, `note`, `confidence` and
`keep` from the draft, `back` from the back-translation, and `lint`: the
errors and warnings the linter has for the draft text.

## batch-NN.review.json (reviewer)
```json
{"shop.buy": {"verdict": "ok"},
 "egg.hatched": {"verdict": "fix", "text": "...", "category": "accuracy",
   "severity": "major", "reason": "..."}}
```
Categories and severities: `quality-rubric.md`. A fix can carry
`"keep": true`.

## batch-NN.resolve.json (resolve round)
`{"egg.hatched": {"accept": false, "text": "...", "reason": "..."}}`.
`accept: true` takes the reviewer's text; `false` proposes `text` with a
reason. `apply --resolve` keeps accepted fixes, writes the rest to
`disputes.json` for the orchestrator.

## final.json (written by `apply`)
```json
{"shop.buy": {"text": "Comprar", "confidence": "high", "source_hash": "3f2a9c0b1d7e",
  "status": "ok", "flags": []}}
```
`status`: ok, fixed (reviewer fix applied), resolved, disputed, decided
(orchestrator ruling), needs_native (held back: not exported, not linted).
`was` holds the human translation an audit fix replaces.

## Waves and budget
- One batch = up to 150 strings. A locale with 400 strings has 3 batches;
  its batches can run in parallel after batch 1 has written `terms.json`.
- Agent runs per batch: 3 (2 for an audit batch), plus 1 if a resolve round
  runs.
- Run up to 8 locales at once. If a run stops, `i18n.py status` shows which
  batch files exist; resume from the first missing one.
