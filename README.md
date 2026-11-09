# roblox-i18n

An agent skill that translates a Roblox game into one language, Roblox's 18
main languages, or all 50 locales Roblox supports. The text is written for
native players instead of converted word by word, and independent reviewer
agents check it before anything ships.

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
        back-translator .... sees ONLY the translation, never the English or the keys; says what it really says
        reviewer ........... compares source, translation, blind back-translation and lint; fixes with reasons
        resolve round ...... translator answers each major fix; leftovers go to you or a native speaker
        |
   6. lint ................. params, rich-text tags, numbers, script, zh-tw/zh-cn leaks, Zawgyi, length, keep-terms
   7. export ............... CSV split at 1,000 rows or 2 MB / Rojo CSV in place / Studio load chunks
   8. verify + report ...... check the written CSV; FormatByKey per locale in Studio; native-review list
```

Translators, back-translators and reviewers each read a small file the tool
builds for their batch, never the whole table, so a batch costs the same
context in a large game as in a small one. The tool also checks each file
an agent writes before the next agent starts, and names the file and the
problem when one is broken.

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
`pt` = pt-br, `fr` = fr-fr, `en` = en-us. The example's 54 columns were
loaded into a LocalizationTable in Studio and every locale, plus es-419,
es-ar, fr-be, pt-ao, zh-hk, zh-sg and en-au, resolved to the intended text.

One more Roblox trap the same test found: `FormatByKey("k", {price = 99})`
on `Buy for {price} Robux` renders `Buy for 99.00 Robux`. Pass numbers as
strings or write `{price:int}`; `{n:num}` is locale-aware (`1.250,50` in
German) but always prints two decimals. The skill's audit step flags this.

## Languages

Confidence and native-review advice come from each guide's independent
reviewer; render risk is how likely the script is to hit missing glyphs or
layout trouble in Roblox fonts (many display fonts have no Cyrillic, Greek or
Asian glyphs). The same data is in `data/locales.json`.

| Locale | Language | Tier | Confidence | Native review | Roblox render risk |
|---|---|---|---|---|---|
| `ar-001` | Arabic | main | medium | strongly recommended | medium |
| `zh-cn` | Chinese (Simplified) | main | high | recommended | medium |
| `zh-tw` | Chinese (Traditional) | main | high | recommended | medium |
| `en-gb` | English (United Kingdom) | main | high | optional | low |
| `en-us` | English (United States) | main | high | optional | none |
| `fr-ca` | French (Canada) | main | medium | recommended | low |
| `fr-fr` | French (France) | main | high | recommended | low |
| `de-de` | German | main | high | recommended | low |
| `hi-in` | Hindi | main | medium | strongly recommended | medium |
| `id-id` | Indonesian | main | medium | recommended | none |
| `it-it` | Italian | main | high | recommended | low |
| `ja-jp` | Japanese | main | high | recommended | low |
| `ko-kr` | Korean | main | high | recommended | low |
| `pl-pl` | Polish | main | medium | strongly recommended | low |
| `pt-br` | Portuguese (Brazil) | main | high | recommended | low |
| `pt-pt` | Portuguese (Portugal) | main | medium | recommended | low |
| `ru-ru` | Russian | main | high | recommended | medium |
| `es-mx` | Spanish (Mexico) | main | high | recommended | low |
| `es-es` | Spanish (Spain) | main | high | recommended | low |
| `th-th` | Thai | main | medium | strongly recommended | medium |
| `tr-tr` | Turkish | main | medium | recommended | medium |
| `vi-vn` | Vietnamese | main | medium | strongly recommended | medium |
| `sq-al` | Albanian | extended | medium | strongly recommended | low |
| `bn-bd` | Bengali | extended | medium | strongly recommended | medium |
| `bs-ba` | Bosnian | extended | medium | strongly recommended | medium |
| `bg-bg` | Bulgarian | extended | medium | strongly recommended | medium |
| `my-mm` | Burmese | extended | low | strongly recommended | medium |
| `hr-hr` | Croatian | extended | medium | strongly recommended | medium |
| `cs-cz` | Czech | extended | medium | strongly recommended | medium |
| `da-dk` | Danish | extended | medium | recommended | low |
| `nl-nl` | Dutch | extended | high | recommended | low |
| `et-ee` | Estonian | extended | medium | strongly recommended | low |
| `fil-ph` | Filipino | extended | medium | strongly recommended | low |
| `fi-fi` | Finnish | extended | medium | strongly recommended | low |
| `ka-ge` | Georgian | extended | low | strongly recommended | medium |
| `el-gr` | Greek | extended | medium | strongly recommended | medium |
| `hu-hu` | Hungarian | extended | medium | strongly recommended | medium |
| `kk-kz` | Kazakh | extended | medium | strongly recommended | high |
| `km-kh` | Khmer | extended | low | strongly recommended | medium |
| `lv-lv` | Latvian | extended | medium | strongly recommended | low |
| `lt-lt` | Lithuanian | extended | medium | strongly recommended | medium |
| `ms-my` | Malay | extended | medium | strongly recommended | low |
| `nb-no` | Norwegian Bokmal | extended | medium | recommended | low |
| `ro-ro` | Romanian | extended | medium | recommended | medium |
| `sr-rs` | Serbian | extended | medium | strongly recommended | medium |
| `si-lk` | Sinhala | extended | low | strongly recommended | medium |
| `sk-sk` | Slovak | extended | medium | strongly recommended | medium |
| `sl-sl` | Slovenian | extended | medium | strongly recommended | medium |
| `sv-se` | Swedish | extended | high | recommended | low |
| `uk-ua` | Ukrainian | extended | medium | strongly recommended | high |

## Install

Claude Code (macOS / Linux):

```bash
git clone https://github.com/WhoIsTyfur/roblox-i18n-skill ~/.claude/skills/roblox-i18n
```

Claude Code (Windows PowerShell):

```powershell
git clone https://github.com/WhoIsTyfur/roblox-i18n-skill "$env:USERPROFILE\.claude\skills\roblox-i18n"
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

`examples/lantern-lake/` is a full run on a made-up fishing game with 40
strings, translated into all 49 target locales (1,960 translations) by 156
agent runs. Every intermediate file is there: context, glossary, drafts,
blind back-translations, reviews, resolve rounds, the final CSV and the
report.

- Reviewers fixed 41 strings; 8 locales needed a resolve round; 2
  disputes were ruled on in `decisions.json`.
- Blind back-translators raised 276 remarks; the ones a reviewer passed
  are listed in `report.md` as the first things a native speaker should check.
- Final lint: 49 locales, 0 errors, 0 warnings.
- The run also found and fixed three bugs in the tool itself.

The example is a record of that run, so its batch files show the layout of
the day: agents read `context.json` directly, and the back-translators'
input was keyed by the real keys. Today's runs add `batch-NN.in.json` and
`batch-NN.reviewin.json` and hide the keys from the back-translator. The
tests replay the example through the current tool and expect the same
`translated.csv`.

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
- One context analyst describes every string. That is tested at 40 strings;
  a table of many hundreds needs the analyst run in parts, which the skill
  does not automate yet.

## Tool reference

```
python scripts/i18n.py locales <single|main|all> [target]
python scripts/i18n.py ingest csv <file> [--rojo] [--source en-us]
python scripts/i18n.py ingest studio <dump.json ...>
python scripts/i18n.py plan <mode> [target] [--retranslate] [--audit] [--batch 150]
python scripts/i18n.py pack
python scripts/i18n.py backpack <locale> <batch>
python scripts/i18n.py reviewpack <locale> <batch>
python scripts/i18n.py apply <locale> [--resolve]
python scripts/i18n.py lint [locale ...]
python scripts/i18n.py check <exported.csv>
python scripts/i18n.py export csv --out <file> | --rojo <file> [--columns locale|language]
python scripts/i18n.py export studio [--table GameStrings]
python scripts/i18n.py studio dump|verify
python scripts/i18n.py status | report
```

Tests: `python -m unittest discover -s tests`. They cover the tool and run
its linter over every guide's reference translations.

## Contributing

The most valuable contribution is a native speaker improving a guide in
`references/locales/`: a gaming word players really use, a wrong rule, a
better reference translation. Open a pull request with the change and, if
you can, a source. Run the tests first: they fail when a guide loses a
heading, a reference row or a `{param}`.
