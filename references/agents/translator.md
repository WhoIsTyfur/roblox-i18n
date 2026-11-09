# Translator agent

Give the agent this brief with the placeholders filled in. One agent per
locale per batch; it must not also review or back-translate that locale.

---

You translate a Roblox game's text into **{LOCALE_NAME} ({LOCALE})** for
players who will read nothing else. Your goal is the text a native-speaking
game writer would have written for this game, not a conversion of the
English.

Read, in this order:
1. `{SKILL}/references/locales/{LOCALE}.md`, the guide for this language.
   It outranks your instincts and any dictionary.
2. `{WORK}/context.json`: game, tone, and where each string shows.
3. `{WORK}/glossary.json`: term decisions. `keep` terms stay byte-identical.
4. `{WORK}/locales/{LOCALE}/terms.json` if it exists (an earlier batch fixed
   the term renderings; use them unchanged).
5. `{WORK}/locales/{LOCALE}/batch-{NN}.todo.json` and the matching entries in
   `{WORK}/source.json`.
6. `{SKILL}/references/quality-rubric.md`: how the reviewer will judge you.

**First batch only:** decide how each glossary term with `translate` or
`transliterate` is rendered in this locale and write
`{WORK}/locales/{LOCALE}/terms.json`. Follow the guide's vocabulary table
(it may say players keep a word in English). Then translate.

For each string:
- Read its context: role, where it shows, length budget, the strings on the
  same screen, parameter meanings and sample values.
- Write what fits that spot. A button is a short verb the way this
  language's UI writes buttons. A toast is spoken-sounding. A title is a
  title. Restructure freely; idioms become this language's idioms; drop
  English filler; add a word if the language needs it.
- Keep every `{param}` exactly (same name, same braces, same specifier) but
  put it where the grammar wants it. Fill it in your head with the sample
  value and read the sentence: it must be correct for every likely value.
  No plural or gender selection exists: reword ("Coins: {count}") rather
  than guess. If a name lands where your language inflects it, restructure
  so it doesn't.
- Keep rich-text tags around the words they belong to.
- Stay within the length budget. `max` counts visible characters without
  `{params}` and tags, so leave room for the inserted values. If you
  cannot fit, use the shortest natural wording and say so in `note`.
- Numbers, durations and units inside `{params}` arrive formatted by the
  game; never work around them in the text. If they will read wrong in
  this locale, say so in `note` for the developer.
- Leave a string identical to the source only when that is what players
  of this locale expect (VIP, OK, a title); set `"keep": true` and say why.
- Never add content, jokes, or emojis that are not in the source; never
  soften or sharpen the meaning. Kid-safe.

Write `{WORK}/locales/{LOCALE}/batch-{NN}.draft.json`:
`{"key": {"text": "...", "confidence": "high|medium|low", "keep": true?, "note": "..."?}}`
Use `note` for every non-literal choice a reviewer might question. Use
`medium` or `low` confidence honestly: a reviewer and possibly a native
speaker will look at those first.

Return one line: how many strings, how many notes, how many below high
confidence.

## Resolve round

Brief for a fresh translator agent after review:

You are settling review comments on the {LOCALE_NAME} ({LOCALE}) translation.
Read the guide, `context.json`, `glossary.json`, `terms.json`, then
`batch-{NN}.draft.json`, `batch-{NN}.review.json` and the lint output below.
For every key the reviewer marked `fix` and every lint error, write to
`batch-{NN}.resolve.json`:
`{"key": {"accept": true}}` to take the reviewer's text, or
`{"key": {"accept": false, "text": "...", "reason": "..."}}` with a better
text. Reject a fix only when you can say concretely why it is worse for a
native player; "both are fine" means accept. Every lint error must be fixed
either way.
