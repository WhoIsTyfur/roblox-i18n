# Pipeline files and formats

All paths are under the work folder (default `.roblox-i18n/` in the game
project). JSON is UTF-8. Keys are the LocalizationTable `Key`; entries with
no Key use their Source text as the key.

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
    batch-01.todo.json   input for the batch (written by `plan`)
    batch-01.draft.json  translator output
    batch-01.backin.json blind input for the back-translator (written by `backpack`)
    batch-01.back.json   back-translator output
    batch-01.review.json reviewer output
    batch-01.resolve.json resolve-round output (optional)
    final.json           merged result for the locale (written by `apply`)
    disputes.json        translator vs reviewer disagreements (written by `apply --resolve`)
    decisions.json       orchestrator rulings: {"key": {"text", "reason", "needs_native"?}}
  out/                   exported files
  report.md
```

Commit `state.json`, `context.json` and `glossary.json` with the game so the
next run only translates what changed. The rest can be ignored by git.

## source.json
```json
{"source_locale": "en-us",
 "strings": [{"key": "shop.buy", "source": "Buy", "context": "", "example": "", "hash": "3f2a9c0b1d7e"}]}
```
`hash` = first 12 hex chars of SHA-1 over `source + "\x1f" + context`.

## existing.json
`{"shop.buy": {"es": "Comprar", "fr-fr": "Acheter"}}` -- column names as found.

## context.json
```json
{"game": {"title": "...", "genre": "...", "audience": "...", "tone": "..."},
 "strings": {"shop.buy": {"where": "under each shop item", "role": "button", "max": 8,
   "params": {}, "neighbors": ["shop.title"], "notes": ""}}}
```
`role` is one of: button, title, label, toast, dialog body, tutorial, prompt,
system chat, product name, item description, text box placeholder, toggle,
banner, popup, other. `max` is a character budget (null if unknown).
`params` maps each `{name}` to its meaning and a sample value.

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

## terms.json (translator, first batch only)
`{"Rebirth": "Renacer", "Pet Hatch Tycoon": "Pet Hatch Tycoon"}` -- later
batches and the reviewer reuse it unchanged.

## batch-NN.draft.json (translator)
```json
{"shop.buy": {"text": "Comprar", "confidence": "high"},
 "pass.vip": {"text": "VIP", "keep": true, "note": "VIP is used as-is in Latin America", "confidence": "high"},
 "coins.count": {"text": "Monedas: {count}", "note": "avoids plural: count can be 1", "confidence": "high"}}
```
`confidence`: high, medium, low. `keep: true` marks a deliberate copy of the
source. `note` explains any non-literal choice.

## batch-NN.back.json (back-translator)
`{"shop.buy": "Buy", "coins.count": "Coins: {count}"}`

## batch-NN.review.json (reviewer)
```json
{"shop.buy": {"verdict": "ok"},
 "egg.hatched": {"verdict": "fix", "text": "...", "category": "accuracy",
   "severity": "major", "reason": "..."}}
```
Categories and severities: `quality-rubric.md`.

## batch-NN.resolve.json (resolve round)
`{"egg.hatched": {"accept": false, "text": "...", "reason": "..."}}` --
`accept: true` takes the reviewer's text; `false` proposes `text` with a
reason. `apply --resolve` keeps accepted fixes, writes the rest to
`disputes.json` for the orchestrator.

## final.json (written by `apply`)
```json
{"shop.buy": {"text": "Comprar", "confidence": "high", "source_hash": "3f2a9c0b1d7e",
  "status": "ok", "flags": []}}
```
`status`: ok, fixed (reviewer fix applied), resolved, disputed, needs_native.

## Waves and budget
- One batch = up to 150 strings. A locale with 400 strings has 3 batches;
  its batches can run in parallel after batch 1 has written `terms.json`.
- Agent runs per batch: 3, plus 1 if a resolve round runs.
- Run up to 8 locales at once. If a run stops, `i18n.py status` shows which
  batch files exist; resume from the first missing one.
