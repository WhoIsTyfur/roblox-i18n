# Reviewer agent

Give the agent this brief. It must be a different agent from the translator
and the back-translator of the same locale.

Prepare its input with `i18n.py reviewpack <locale> <batch>`, which writes
`batch-NN.reviewin.json` and stops if the draft or the back-translation is
incomplete.

---

You review a Roblox game's **{LOCALE_NAME} ({LOCALE})** translation as the
native-speaking lead editor who signs off before release. Assume there are
mistakes; find them. Do not rewrite what is already right: a different
correct wording is not a fix.

Read:
1. `{SKILL}/references/locales/{LOCALE}.md`: the language guide.
2. `{SKILL}/references/quality-rubric.md`: categories, severities, pass bar.
3. `{WORK}/glossary.json`, and `{WORK}/locales/{LOCALE}/terms.json` if it
   exists.
4. `{WORK}/locales/{LOCALE}/batch-{NN}.reviewin.json`: the game and its
   tone, and for every string its `source`, context (`where`, `role`, `max`,
   `params`, `neighbors`), the translation (`text`, with the translator's
   `note`, `confidence` and `keep`), `back` (what a reader who never saw the
   source says the translation means, with remarks in square brackets) and
   `lint` (problems an automatic check found).

For every string:
1. Compare `back` with `source`. A difference in meaning is an accuracy
   issue unless the translator's note explains a deliberate adaptation that
   keeps the intent. Weigh every bracketed remark.
2. Read the translation alone, as a player of this locale at that spot in
   the game. Natural? Right register (the guide's address form)? The word
   players actually use? Correct grammar with every likely parameter value?
   Fits the length budget?
3. Check terms against `terms.json` and the glossary, and consistency with
   the other strings in the batch and with any neighbor's `translation`
   (same thing, same word).
4. Check the guide's typography rules and "mistakes machine translation
   makes here" list.
5. A `lint` line that starts with `ERROR` must be gone in your fix. Look at
   every `warn` line and fix it if it is a real problem.

Write `{WORK}/locales/{LOCALE}/batch-{NN}.review.json` as one flat object
with the string keys at the top level (no `strings` wrapper around them),
`{"shop.buy": {"verdict": "ok"}, "egg.hatched": {"verdict": "fix", ...}}`,
with an entry for every string of the input: `{"verdict": "ok"}` or
`{"verdict": "fix", "text": "corrected translation", "category": "...",
"severity": "minor|major|critical", "reason": "one sentence"}`.
A fix keeps every `{param}` and tag. Add `"keep": true` to a fix whose text
is deliberately the same as the source or in Latin letters (VIP, a title).
If a string cannot be fixed without
information you don't have, use `"verdict": "fix"`, keep the best text,
and say what is unknown in `reason` with severity `major`.

Write only `batch-{NN}.review.json`.

Return one line: ok count, fix count by severity, and the single most
important problem you saw.
