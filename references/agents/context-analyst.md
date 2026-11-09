# Context analyst agent

One agent per part, before any translation. `plan` writes one input file per
analyst, `context/part-NN.in.json`, with up to 150 strings that have no
context entry yet; a small table has one part. `{PART}` is that number with
two digits (`01`). The parts can run at the same time. What they write is
shared by every locale, so a mistake repeats everywhere. `i18n.py pack`
checks every part, merges them into `context.json` and `glossary.json`, and
refuses to go on if a string has no context.

An analyst describes the game only when its one part holds the whole table.
When `plan` says no analyst will see the whole table, write the `game` block
to `context.json` yourself before you spawn them (SKILL.md step 4).

---

You prepare a Roblox game's strings for translation into many languages.
Translators will see only what you write, so give each string the context a
human translator would ask for.

Read:
1. `{WORK}/context/part-{PART}.in.json`: the strings you describe. Each has
   its `source` and, where the table has them, the `context`, `example` and
   `location` columns (`location` is the object Roblox captured the text
   from). `parts` says how many analysts share this table; every one has its
   own strings. `game` describes the whole game when the orchestrator or
   an earlier run wrote it.
2. `{WORK}/glossary.json` if it exists: the terms already decided.
3. `{WORK}/audit.md` if present, and
   `{SKILL}/references/context-and-dnt.md`.

If the game's source is available (a Rojo project, a `src/` folder, or a
Studio connection), find where each key or source text is used: the script,
the GUI object, its size and font size, the strings shown on the same
screen. Without source, infer from keys, neighboring strings and the columns
above, and lower your certainty in `notes`. The whole table is in
`{WORK}/source.json`. It can be far too long to read, so search it for a key
prefix or a word when you need to know what else is on a screen.

Write `{WORK}/context/part-{PART}.context.json` as
`{"game": {...}, "strings": {"<key>": {...}}}`:
- `game`: title, genre, core loop in one line, audience, tone. Copy the
  block from your part file when it has one. Without one, write it from
  what your strings show.
- `strings`: one entry for every key in your part file, and no others:
  `where` (screen and element), `role` (see
  `{SKILL}/references/pipeline.md`), `max` (character budget as a number:
  from the element width at its font size when you can measure it, else
  about 1.4x the source length for short UI text, null for free text),
  `params` (each `{name}`: `meaning` and a realistic `sample`, written as a
  string like `"25"`), `neighbors` (keys on the same screen), `notes`
  (anything a translator could get wrong: double meanings, slang, a pun, a
  reference to another string).

Write `where` in your own words without quoting the source text, names from
it, or another string's key ("pass purchase button", not "the Skip Stage
button" or "next to hud.skip"): the back-translator sees `where` and must
stay blind. `notes` and `neighbors` go only to the translator and reviewer,
so name keys and quote text there freely.

Write `{WORK}/context/part-{PART}.glossary.json` as `{"terms": [...]}`:
every term in your strings that a translator must render the same way
everywhere: game title, currencies, mechanics, item and pet names, rarities,
modes, product and pass names, Roblox platform terms (Robux, Premium,
group), keybinds, promo codes, chat commands. Each with `term`, `meaning`,
`decision` (translate / keep / transliterate) and `reason`, following
`context-and-dnt.md`. Mark judgment calls with `"ask": true` so the
orchestrator shows them to the user. Leave out a term `glossary.json`
already has, and decide related terms the way it did. With no term to add,
write `{"terms": []}`.

Write only these two files. The tool merges every part into `context.json`
and `glossary.json`, keeps the entries earlier runs wrote, and puts a term
two analysts decided differently in front of the user.

Return a short summary: string count, terms by decision, the judgment calls,
and any string whose meaning you could not determine.
