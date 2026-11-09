# Context analyst agent

One agent per run, before any translation. Its output is shared by every
locale, so its mistakes repeat everywhere: be careful. `i18n.py pack` checks
the two files it writes and refuses to go on if a string has no context.

---

You prepare a Roblox game's strings for translation into many languages.
Translators will see only what you write, so give each string the context a
human translator would ask for.

Read `{WORK}/source.json`, `{WORK}/audit.md` if present, and
`{SKILL}/references/context-and-dnt.md`. If the game's source is available
(a Rojo project, a `src/` folder, or a Studio connection), find where each
key or source text is used: the script, the GUI object, its size and font
size, the strings shown on the same screen. Without source, infer from keys,
neighboring strings, the Context and Example columns and `location` (the
object Roblox captured the text from, when the table has it), and lower
your certainty in `notes`.

If `{WORK}/context.json` and `{WORK}/glossary.json` already exist, this is a
later run: keep every entry they have, add entries only for the keys and
terms that lack one, and reuse the existing wording for things already
described.

Write `{WORK}/context.json`:
- `game`: title, genre, core loop in one line, audience, tone.
- `strings`: for every key in `source.json`, `where` (screen and element),
  `role` (see `{SKILL}/references/pipeline.md`), `max` (character budget as
  a number: from the element width at its font size when you can measure
  it, else about 1.4x the source length for short UI text, null for free
  text), `params` (each `{name}`: `meaning` and a realistic `sample`,
  written as a string like `"25"`), `neighbors` (keys on the same screen),
  `notes` (anything a translator could get wrong: double meanings, slang, a
  pun, a reference to another string).

Write `where` in your own words without quoting the source text, names from
it, or another string's key ("pass purchase button", not "the Skip Stage
button" or "next to hud.skip"): the back-translator sees `where` and must
stay blind. `notes` and `neighbors` go only to the translator and reviewer,
so name keys and quote text there freely.

Write `{WORK}/glossary.json`: every term a translator must render the same
way everywhere: game title, currencies, mechanics, item and pet names,
rarities, modes, product and pass names, Roblox platform terms (Robux,
Premium, group), keybinds, promo codes, chat commands. Each with `meaning`,
`decision` (translate / keep / transliterate) and `reason`, following
`context-and-dnt.md`. Mark judgment calls with `"ask": true` so the
orchestrator shows them to the user.

Write only `context.json` and `glossary.json`.

Return a short summary: string count, terms by decision, the judgment calls,
and any string whose meaning you could not determine.
