# Example: Lantern Lake Fishing

A made-up Roblox fishing game with 40 UI strings, run through the whole
skill into all 49 target locales. Nothing here was edited by hand except the
glossary checkpoint answers and two orchestrator rulings.

| File | What it is |
|---|---|
| `source.csv` | the input, as a developer would export it (Key, Source, Context, Example) |
| `translated.csv` | the output: one column per locale plus bare `es`, `pt`, `fr`, `en` |
| `work/audit.md` | localizability findings (plural traps, "Press E", pre-formatted values) |
| `work/context.json` | per-string context from the context analyst |
| `work/glossary.json` | translate / keep decisions, with the checkpoint answers |
| `work/locales/<locale>/terms.json` | that locale's renderings of the glossary terms |
| `work/locales/<locale>/batch-01.draft.json` | translator output, with notes on every non-literal choice |
| `work/locales/<locale>/batch-01.back.json` | blind back-translation (the agent never saw the English) |
| `work/locales/<locale>/batch-01.review.json` | reviewer verdicts and fixes |
| `work/locales/<locale>/batch-01.resolve.json` | resolve round, where one ran |
| `work/locales/<locale>/decisions.json` | orchestrator rulings (et-ee) |
| `work/locales/<locale>/final.json` | the merged result `export` reads |
| `work/report.md` | per-locale summary and the strings a native speaker should check first |

Spanish was run first (`plan single spanish`), then `plan all` translated
only the 47 remaining locales, which also exercised incremental mode.

Compare a locale's `back.json` with `source.csv` to see what the blind reader
understood, then its `review.json` to see what the reviewer did about it.

This is a record of one run, so the batch files show the layout the skill
had that day. Translators and reviewers read `context.json` and
`source.json` directly, and each `backin.json` is keyed by the real keys
(`hud.reel`), which hinted at the English. The skill now writes
`batch-NN.in.json` and `batch-NN.reviewin.json` for those agents and gives
the back-translator ids like `s001` instead. `tests/test_example.py`
replays this folder through the current tool and expects the same
`final.json` files and the same `translated.csv`.
