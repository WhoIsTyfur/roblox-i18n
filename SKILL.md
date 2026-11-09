---
name: roblox-i18n
description: Translate a Roblox game's text into one language, Roblox's main languages (the 18 it auto-translates, 22 locales) or all 50 locales Roblox supports, with one translator, one blind back-translator and one independent reviewer agent per locale, per-language guides, a do-not-translate glossary and deterministic lint, then write the result to a Creator Hub CSV, a Rojo LocalizationTable CSV or live Studio. Use when the user says "translate my game", "localize", "add Spanish", "every language", "all languages", "main languages", "i18n", "LocalizationTable", "translation CSV", "review our translations", or a feature adds UI text to a game that is already translated.
---
# roblox-i18n

Translate a Roblox game so each player reads text written for them, not text
converted word by word. Correctness beats speed: every locale gets its own
translator, a blind back-translator and an independent reviewer, guided by a
per-language guide in `references/locales/`.

`<skill>` below means the folder holding this file. The tool is
`python <skill>/scripts/i18n.py` (Python 3.9+, standard library only). Work
files go to `.roblox-i18n/` in the game project (`--work` to change).
File formats: `references/pipeline.md`.

## Modes
| Ask | Command arg | Targets |
|---|---|---|
| one language | `single <language or locale>` | `spanish` -> es-es + es-mx; `es-mx` -> only es-mx |
| main languages | `main` | the 18 languages Roblox auto-translates, every Roblox locale of them: 22 locales, minus the source |
| everything | `all` | all 50 Roblox locales, minus the source |

`i18n.py locales <mode> [target]` prints the exact set. Unsure which mode the
user means? Ask once; default `single` for one named language.

## Steps

1. **Find the strings.** Pick the adapter (`references/adapters/`):
   - CSV exported from Creator Hub (Localization > table > Download CSV) or
     Studio Localization Tools: `i18n.py ingest csv <file>`.
   - Rojo project with `.csv` LocalizationTables: `i18n.py ingest csv <file> --rojo`.
   - Live Studio over an MCP with `execute_luau`: `references/adapters/studio-mcp.md`.
   Check: `i18n.py status` shows the string count and existing translations
   per locale. Zero strings means the wrong file or table; stop and ask.

2. **Plan the run.** `i18n.py plan <mode> [target]` picks what needs work:
   new strings, strings whose source changed, missing locales. Existing human
   translations are kept (`--retranslate` to redo, `--audit` to review them
   instead). It prints locales, batches (150 strings each) and agent runs.
   For `main` or `all`, tell the user the agent count and get a yes before
   step 5.

3. **Localizability audit.** Read the strings and, when the game source is
   available, the code that shows them. Write `.roblox-i18n/audit.md`:
   - dynamic text captured as source (usernames, numbers, timers, chat): it
     does not belong in the table; list it for removal;
   - sentences built by concatenation in code (`"You have " .. n .. " coins"`):
     cannot be translated well; propose a key with `{params}`;
   - one-word strings with two meanings ("Play", "Free", "Close") that need
     a Context or Example;
   - count strings ("{n} Coins") that need plural-neutral wording;
   - two translated words inserted side by side ("a {rarity} {pet}"), which
     gendered languages cannot make agree;
   - device-specific text ("Press E", "Click") that is wrong on phone,
     console and VR; a ProximityPrompt already shows the right key;
   - values the code pre-formats in English (`2d 4h`, `12.4`), which
     translators cannot localize;
   - numbers passed to a plain `{param}`: `FormatByKey` renders a Lua
     number as `99.00` (tested in Studio). Pass a string, or use
     `{price:int}`; `{n:num}` groups digits per locale (`1.250,50` in
     German) but always shows two decimals;
   - text baked into images or decals.
   Report only; change game code only if the user asks.

4. **Context, glossary, tone.** Spawn one agent with
   `references/agents/context-analyst.md`. It writes `context.json` (where
   each string shows, UI role, length budget, parameter meanings and sample
   values, strings on the same screen) and `glossary.json` (every game term
   with a translate / keep / transliterate decision and reason). Rules:
   `references/context-and-dnt.md`.
   **Checkpoint:** show the user the tone line, the keep-list and any term
   whose decision was a judgment call; apply their edits. Skip only if they
   said not to ask. A wrong glossary entry repeats in every language.

5. **Translate, per locale.** Waves of up to 8 locales at a time. For each
   locale and batch, three separate agents, in order:
   1. **Translator** (`references/agents/translator.md`) -> `draft.json`.
   2. **Back-translator** (`references/agents/back-translator.md`): run
      `i18n.py backpack <locale> <batch>` first; the agent reads only that
      file (draft text and UI roles, never the source) -> `back.json`.
   3. **Reviewer** (`references/agents/reviewer.md`) -> `review.json`.
   Never let one agent do two of these roles for the same locale.
   Then `i18n.py apply <locale>` builds `final.json` and lints it.
   **Resolve round** (only if the reviewer marked a major issue, or lint
   failed): a fresh translator agent gets the draft, review and lint output
   and answers each disputed key (`references/agents/translator.md`,
   "Resolve round"); `i18n.py apply <locale> --resolve`. Where translator and
   reviewer still disagree (`disputes.json`), decide yourself from both
   reasons and write `decisions.json` (`{"key": {"text", "reason"}}`, or
   `"needs_native": true` to hold the string back), then apply again. At
   most two rounds; leftovers are flagged for a native speaker, never
   shipped silently.

6. **Check everything.** `i18n.py lint` across all locales: placeholders and
   rich-text tags match the source, no empty values, expected script present,
   no Simplified characters in zh-tw (or Traditional in zh-cn), no Zawgyi in
   Burmese, no cedilla s/t in Romanian, glossary keep-terms intact, lengths
   within budget, no unexplained copies of the source. Fix every error;
   warnings need a reason in the report.

7. **Write it back.** Same adapter as step 1:
   - `i18n.py export csv --out <file>`: Creator Hub upload files, split at
     1,000 changed rows each (Roblox's per-upload limit).
   - `i18n.py export csv --rojo <file>`: rewrites the Rojo CSV in place.
   - `i18n.py export studio`: Luau chunks for `execute_luau`
     (`references/adapters/studio-mcp.md`).
   Column scheme (tested in Studio): one column per target locale, plus the
   bare language column (`es`, `pt`, `fr`, `en`) for languages with several
   Roblox locales, holding the default variant (es-mx, pt-br, fr-fr, en-us).
   Without it, a player in Argentina or Belgium gets an arbitrary sibling.

8. **Verify and report.** Re-ingest the written file and run `lint` again.
   On the Studio path, `i18n.py studio verify` writes `verify-NN.luau`
   snippets; run each (`FormatByKey` every key per locale, plus the es-419,
   fr-be and pt-ao fallbacks) and fix any mismatch. `i18n.py report` writes
   `.roblox-i18n/report.md`: per locale, string count, confidence, the
   strings flagged for a native speaker, and Roblox rendering risks. Show
   the user that summary.

## Hand-off (tell the user)
- Upload the CSVs in Creator Hub > Localization (or publish the place for
  Studio/Rojo tables). Saving or publishing is the user's call.
- Add the target languages under Localization > Settings if they are not
  there yet.
- Turn off Automatic Text Capture or clear captured dynamic strings if the
  audit found any.
- Locales marked "native review" in `data/locales.json` or the report should
  get a native speaker's pass before a big launch. Roblox lets you add
  translators in Creator Hub.
- Numbers, times and units: the table only fills `{params}`; values the
  code formats (`1,250`, `12.4`, `3h 20m`) stay English. Recommend making
  each format a key (`time.hm` = `{h}h {m}m`, translated like any string)
  and grouping digits per locale (each guide's "Typography" section gives
  the separators). Change game code only if the user asks.
- Fonts: many Roblox display fonts (Builder Sans, Fredoka One, Luckiest
  Guy) have no Cyrillic, Greek or Asian glyphs, so Roblox falls back to
  another face. `render_risk` in `data/locales.json` and each guide say what
  to check.
- Rendering: open a test in Studio with the Player Emulator set to a risky
  script (Burmese, Khmer, Sinhala, Thai, Arabic) and look at long strings.
  Ask before opening Play; it takes over the screen.

## Rules
- **Meaning over words.** Write what a native player of that age would
  expect to read in a polished game. Restructure sentences, change idioms,
  drop or add words. Never keep English word order to be safe.
- **Context first.** Never translate a string without its context entry.
  "Play" on a menu button, "Play" as a music toggle and "Play" as a noun are
  three different translations.
- **Know when not to translate.** Game titles, Robux, usernames, promo
  codes, chat commands, keyboard keys, meme words players use in English.
  The locale guide says which gaming words players keep in English; follow
  it over a dictionary.
- **Parameters are sacred.** `{name}` tokens stay byte-identical (move them
  anywhere). Roblox has no plural or gender selection, so phrase around it:
  "Coins: {count}" beats a wrong plural. Rich-text tags (`<b>`) wrap the
  matching words.
- **Variants are separate translations.** es-mx is not es-es with words
  swapped; zh-tw is not converted zh-cn. Each comes from the source.
- **Never overwrite human work** unless the user asked (`--retranslate`).
- **Honest confidence.** Low-resource languages (see `data/locales.json`)
  get flagged for native review in the report, every time.
- Never use machine-translation APIs or Roblox auto-translate as the
  translation; agents write it, reviewers check it.
