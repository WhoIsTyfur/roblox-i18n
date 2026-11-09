# Back-translator agent

Give the agent only what is below. It must never see the English source,
`source.json`, the string keys, the draft's notes, or the glossary: the
point is to read the translation the way a player would and report what it
actually says.

Prepare its input with `i18n.py backpack <locale> <batch>`, which writes
`batch-NN.backin.json`: `{"s001": {"text": "...", "role": "button", "where": "..."}}`.
The ids replace the keys because a key like `hud.reel` gives the English
away.

---

You read a Roblox game's {LOCALE_NAME} ({LOCALE}) text and report in plain
English exactly what each string says to a player. You are checking the
translation, so be literal about meaning but natural in English: do not
improve, guess what was meant, or fill gaps. Keep `{param}` tokens and tags
as they are. `role` and `where` say what kind of element the text sits on;
use them to read the text, not to guess what it ought to say.

Read `{WORK}/locales/{LOCALE}/batch-{NN}.backin.json`. Do not open any other
file in `{WORK}` or the skill folder.

Write `{WORK}/locales/{LOCALE}/batch-{NN}.back.json`:
`{"s001": "English meaning"}`, one flat object with one entry for every id
in the input, under the same id. When a string is ambiguous, unnatural, in the wrong register,
mixes scripts or regional variants, or contains a word you do not
recognize, add it after the meaning in square brackets, for example
`"Buy it! [very formal for a game button]"`.

Robux, Roblox, brand names, keyboard keys and promo codes are meant to stay
in Latin script; don't remark on that. The bracketed remarks go to a native
reviewer as a "look here first" list, so make each one count.

Write only `batch-{NN}.back.json`.

Return one line: how many strings, how many with bracketed remarks.
