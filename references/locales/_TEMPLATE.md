# <Language name> (<locale-id>) translation guide

<!--
Template for every locale guide. Keep the headings exactly. Target 120-180 lines.
Write for a translator agent that is fluent but has never shipped a Roblox game
in this language. Every rule must be specific and actionable; no filler, no
general advice that holds for every language. Cite sources in the last section.
English prose: straight quotes, no dashes (rephrase with a comma, colon or
parentheses). Examples use the language's own characters, always with its
real accents and script.
-->

## At a glance
| | |
|---|---|
| Roblox locale / column | `<locale-id>` (bare language column `<code>` only if this is the default variant) |
| Script, direction | <e.g. Latin, LTR> |
| Address the player as | <e.g. informal "tu"; never "vous"> |
| Text expansion vs English | <e.g. +20-35%, buttons up to +50%> |
| Plural categories (CLDR) | <e.g. one, many, other> |
| Model confidence | <high / medium / low>: <one line why> |
| Native review before shipping | <recommended / strongly recommended / optional> |

## Audience and register
<Who plays Roblox in this locale, how they talk, and the register a polished
game uses with them: pronoun and verb forms, imperative vs infinitive on
buttons, how exclamations and hype sound natural, what reads as stiff, school-
textbook or adult. Kid-safe.>

## Roblox and gaming vocabulary
<Table: English term | use in this locale | note. Cover at least: Robux, game
pass, developer product, experience/game, obby, tycoon, simulator, rebirth,
pet, egg/hatch, coins, gems, boost, multiplier, XP, level up, quest,
leaderboard, AFK, noob, OP, VIP, trade, inventory/backpack, daily reward,
codes, group, like/favorite, server, friends (Roblox renamed friends to
"connections" in some UI; say what this locale's Roblox UI shows). Say which
stay in English (and in which script), which translate, and which are written
both ways by real players. Prefer what Roblox's own UI in this language uses
for platform terms.>

## Grammar traps in UI strings
<Concrete rules with mini examples for: plurals with {count} (Roblox has no
plural selection, so give the safest neutral pattern), gender agreement when a
{player} or item name is inserted, grammatical case or particles around
placeholders, word order changes, articles/classifiers before inserted nouns,
compound nouns, capitalization of titles and buttons.>

## Typography and formatting
<Punctuation (spacing before ! ? : ;, inverted marks, full-width forms),
quotation marks, number and percent format, time/duration abbreviations,
ellipsis, line breaking (languages without spaces), bidi issues with numbers and
Latin names (RTL only), what to do with English keyboard keys like "E".>

## Do not translate / keep as is
<Locale-specific norms: brand names, Robux, game titles, product names, meme
words, keybinds, promo codes, usernames; when to transliterate instead; script
choice if the language has more than one.>

## Rendering on Roblox
<Does Roblox's default font stack render this script? Known risks (missing
glyphs, broken shaping, diacritics clipped by TextScaled, no word wrap). Say
what to verify in Studio. Say "unverified" if you could not confirm.>

## Mistakes machine translation makes here
<The 6-12 most common errors LLMs and MT make in this language for game UI:
false friends, calques, wrong register, variant mixing (e.g. Spain vs Latin
America), wrong script characters, over-literal idioms, wrong gaming terms.
Each with a bad -> good example.>

## Reference translations
<Translate every string in references/canonical-strings.json. Table:
key | translation | note (only when you adapted, kept English, or had a
choice). Keep every {param} exactly; keep <b> tags around the matching words;
respect max lengths.>

## Sources
<Numbered list of the pages you actually used: style guide, CLDR, Roblox
localized pages, dictionaries, community usage. One line each with URL.>
