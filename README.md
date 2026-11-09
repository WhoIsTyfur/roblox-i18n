# roblox-i18n

An agent skill that translates a Roblox game into one language, Roblox's 18
main languages, or all 50 locales Roblox supports -- written for native
players, not converted word by word, and checked by independent reviewer
agents before anything ships.

Works with Claude Code and any agent that reads `SKILL.md` skills and can
start subagents.

## Why

Literal translation is the default failure of game localization. A button
that says "Claim" becomes a legal claim, "Rebirth" becomes a religious
rebirth, a kids' game addresses players like a bank, Latin American players
get Spain Spanish, Traditional Chinese players see Simplified characters,
and `{count} Coins` reads wrong when the count is 1. Roblox's automatic
translation fills blank entries, but it sees one string at a time with no
idea where it shows or who reads it.

This skill gives every string its context, decides up front what must not
be translated, and puts three separate agents on every language.

## Modes

| You say | Mode | Locales |
|---|---|---|
| "Translate my game into Spanish" | `single spanish` | es-es and es-mx (`single es-mx` for one) |
| "Translate into the main languages" | `main` | every Roblox locale of the 18 languages Roblox auto-translates: 22 locales (21 targets from English) |
| "Translate into every language" | `all` | all 50 Roblox locales (49 targets) |

The 18 main languages: Arabic, Chinese (Simplified and Traditional), English
(US and UK), French (France and Canada), German, Hindi, Indonesian, Italian,
Japanese, Korean, Polish, Portuguese (Brazil and Portugal), Russian, Spanish
(Spain and Mexico), Thai, Turkish, Vietnamese. `all` adds Albanian, Bengali,
Bokmal, Bosnian, Bulgarian, Burmese, Croatian, Czech, Danish, Dutch,
Estonian, Filipino, Finnish, Georgian, Greek, Hungarian, Kazakh, Khmer,
Latvian, Lithuanian, Malay, Romanian, Serbian, Sinhala, Slovak, Slovenian,
Swedish and Ukrainian.

## How it works

```
 your strings (Creator Hub CSV / Rojo CSV / live Studio)
        |
   1. ingest + plan ........ only new or changed strings; human work is never overwritten
   2. localizability audit . concatenated sentences, dynamic text, plural traps
   3. context analyst ...... where each string shows, its length budget, what each {param} holds
                             + glossary: translate / keep / transliterate, with reasons
   4. you approve .......... the glossary and keep-list (one mistake there repeats in 49 languages)
        |
   5. per locale, in waves:
        translator ......... uses that language's guide; notes every non-literal choice
        back-translator .... sees ONLY the translation, never the English; says what it really says
        reviewer ........... compares source, translation and blind back-translation; fixes with reasons
        resolve round ...... translator answers each major fix; leftovers go to you or a native speaker
        |
   6. lint ................. params, rich-text tags, script, zh-tw/zh-cn leaks, Zawgyi, length, keep-terms
   7. export ............... CSV split at 1,000 rows / Rojo CSV in place / Studio load chunks
   8. verify + report ...... FormatByKey per locale in Studio; strings flagged for native review
```

### The language guides

`references/locales/` holds one guide per locale, 50 in all. Each was
researched by its own agent (Microsoft language style guides, CLDR plural
rules, Roblox's own wording in that language, how players there actually
talk) and then fact-checked and corrected by a second, independent agent.
Each covers: how to address the player, which gaming words stay in English,
grammar traps around `{params}`, typography, Roblox font rendering risks,
the mistakes machine translation makes in that language, and reference
translations of 34 typical Roblox strings.

### Knowing what not to translate

Game titles, `Robux`, usernames, promo codes, chat commands and keyboard
keys stay as they are. Meme and gaming words follow what players in each
locale really use: many keep "AFK", "VIP" or "noob" in English, some don't.
Invented names (a fish called "Lantern Eel") are a judgment call the skill
puts to you. Rules: `references/context-and-dnt.md`.

### Which columns Roblox actually reads

Tested in Studio on a LocalizationTable (2026-11-08):

- an exact locale column (`es-mx`) always wins;
- a player in a locale with no column (es-419, es-ar, fr-be, pt-ao, en-au)
  gets the bare language column (`es`, `fr`, `pt`, `en`) if there is one;
- with no bare column, Roblox picks an arbitrary sibling: Argentina got
  Spain Spanish, Belgium got Canadian French;
- zh-hk resolves to zh-tw and zh-sg to zh-cn.

So the skill writes one column per locale plus a bare column for the default
variant of each multi-locale language: `es` = es-mx (Latin America),
`pt` = pt-br, `fr` = fr-fr, `en` = en-us.

## Install

Claude Code (macOS / Linux):

```bash
git clone https://github.com/WhoIsTyfur/roblox-i18n ~/.claude/skills/roblox-i18n
```

Claude Code (Windows PowerShell):

```powershell
git clone https://github.com/WhoIsTyfur/roblox-i18n "$env:USERPROFILE\.claude\skills\roblox-i18n"
```

Other agents: put the folder wherever your agent loads skills from, or tell
it to read `SKILL.md`.

Needs Python 3.9+ (standard library only). For the live-Studio path, a
Roblox Studio MCP server with `execute_luau` (the official Roblox Studio MCP
works).

## Use

Ask in plain words:

- "Translate my game into Japanese."
- "Localize the game into Roblox's main languages."
- "Translate to every language Roblox supports."
- "Review the translations we already have." (audit mode)
- "I added three new strings, translate them." (only the new ones run)

Give it the Creator Hub CSV, the Rojo CSV path, or point it at the open
Studio place. You get back upload-ready CSVs (or the Rojo file updated, or
the Studio table loaded), plus `report.md` with per-locale confidence and
every string a native speaker should look at.

## Cost

Three agent runs per locale per 150 strings, plus one context analyst, plus
a resolve round where a reviewer found a major problem.

| Mode | Locales | Agent runs (150 strings) |
|---|---|---|
| single | 1-2 | 4-7 |
| main | 21 | about 64 |
| all | 49 | about 148 |

The skill states the count and asks before `main` or `all`. Later runs only
translate what changed.

## Example

`examples/lantern-lake/` is a full run on a made-up fishing game: the
source CSV, every intermediate file (drafts, blind back-translations,
reviews, resolve rounds) and the final CSV and report for all 49 target
locales.

## Limits

- Models are much stronger in some languages than others. Burmese, Khmer,
  Sinhala, Kazakh and Georgian in particular need a native speaker's pass
  before a big launch; `data/locales.json` and every report say which
  locales are flagged.
- Some scripts may not render in every Roblox font. Check long strings in
  Studio with the Player Emulator set to that language.
- The column fallback above was verified on engine LocalizationTables
  (Studio and Rojo). Creator Hub CSV uploads were not tested with locale
  columns; if an upload rejects them, `export csv --columns language` writes
  one column per language.
- Roblox has no plural or gender selection; the skill phrases around it.

## Tool reference

```
python scripts/i18n.py locales <single|main|all> [target]
python scripts/i18n.py ingest csv <file> [--rojo] [--source en-us]
python scripts/i18n.py ingest studio <dump.json ...>
python scripts/i18n.py plan <mode> [target] [--retranslate] [--audit] [--batch 150]
python scripts/i18n.py backpack <locale> <batch>
python scripts/i18n.py apply <locale> [--resolve]
python scripts/i18n.py lint [locale ...]
python scripts/i18n.py export csv --out <file> | --rojo <file> [--columns locale|language]
python scripts/i18n.py export studio [--table GameStrings]
python scripts/i18n.py studio dump|verify
python scripts/i18n.py status | report
```

Tests: `python -m unittest discover -s tests`.

## Contributing

The most valuable contribution is a native speaker improving a guide in
`references/locales/`: a gaming word players really use, a wrong rule, a
better reference translation. Open a pull request with the change and, if
you can, a source.

## License

MIT. See [LICENSE](LICENSE).
