# Context and what not to translate

## Context a translator needs
For every string: where it shows, what kind of element it is, how much room
it has, what each `{param}` will contain, and what else is on the screen.
Without it, short strings are guesses:

| Source | Possible meanings |
|---|---|
| Play | start the game (button); play a song (toggle); a theater play (noun) |
| Free | costs nothing; set free a pet; unoccupied slot |
| Claim | take a reward; claim a plot of land (tycoon); an assertion |
| Back | go back (button); your back (body) |
| Rebirth / Prestige | reset with a permanent bonus -- a mechanic, not religion |
| Spin | spin the wheel (gamble-style reward) vs spin attack |
| Lucky | "luck" stat in RNG games vs good fortune in a sentence |
| Equip / Equipped | action button vs state label -- different forms in many languages |

A one-word string whose meaning is not certain from context gets a note in
`context.json` and, if it matters, a question to the user.

## Decide per term: translate, keep, or transliterate

**Keep (byte-identical in every locale):**
- The game title, studio and group names, unless the user has an official
  localized title.
- `Robux`. Roblox keeps it in every language.
- Usernames and display names; they are parameters, never table text.
- Promo codes (`FREEPETS`), chat commands (`/e dance`), admin commands.
- Keyboard keys and button glyphs (`E`, `Shift`, `LMB`, `ButtonA`). Translate
  the words around them.
- Brand names and real product names; names of other Roblox games.
- Meme words and slang that the target players use in English. The locale
  guide's vocabulary table decides this per language (for example many
  locales keep "noob", "OP", "AFK" and "VIP").

**Translate:**
- Every mechanic, stat, currency word and UI word players should
  understand: coins, gems, rebirth, pets, eggs, boost, quest, inventory.
- Item, pet and rarity names that are ordinary words (Dragon, Legendary,
  Lucky Potion), unless the user treats them as brand names.
- Product and pass names that describe what they do (`2x Coins`,
  `Auto Collect`), unless the user wants them identical for marketing.

**Transliterate:**
- Invented names that should keep their sound in a non-Latin script, where
  that is the norm (Japanese often writes invented names in katakana;
  Russian and Arabic players usually see them in Latin). The locale guide
  says which.

**Ask the user (mark `"ask": true`):**
- Invented proper names (a pet called "Fluffernaut", a world called
  "Candy Realm"): translate the meaning or keep the name?
- Product names used in ads or thumbnails.
- Anything that looks like a pun or in-joke.

## Strings that should not be in the table
Found during the audit; report them, don't translate them:
- Text captured from dynamic labels: usernames, numbers, timers, chat,
  player-made text. They waste Roblox translation quota and leak into
  auto-translate.
- Fragments of a concatenated sentence ("You have", "coins left"). The fix
  is one key with `{params}` in the game code.
- Text inside images. It needs localized images, not table entries.

## Plurals and gender
Roblox picks one string per key; there is no plural or gender selection.
- Prefer label form: `Coins: {count}`, `Level {level}`.
- Or wording that is correct for every value in that language (the locale
  guide gives the pattern).
- Never write `coin(s)`-style hacks unless the guide says the language uses
  them in UI.
- For a `{player}` of unknown gender, use the guide's neutral pattern.
