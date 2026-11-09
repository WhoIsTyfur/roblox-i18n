# Lithuanian (lt-lt) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `lt-lt` (the only Lithuanian locale; no bare `lt` column) |
| Script, direction | Latin with ą č ę ė į š ų ū ž, LTR |
| Address the player as | informal singular "tu" ("Spausk", "Grįžk", "Gausi"); never "jūs"/"Jūs" except to the whole server |
| Text expansion vs English | about +10-30% on sentences (this file's reference set: +10% after compressing); short words double ("Buy" -> "Pirkti", "On" -> "Įjungta", so 5-char slots need "Įj.") |
| Plural categories (CLDR) | one (1, 21, 31, 101; not 11), few (2-9, 22-29; not 12-19), many (fractions only: 1,5), other (0, 10-20, 30, 100) |
| Model confidence | medium: smaller language; models break case endings around {params}, use gendered participles for "you", and calque English; no Lithuanian Roblox UI to copy terms from |
| Native review before shipping | strongly recommended |

## Audience and register
Players are Lithuanian kids in Lithuania and abroad (UK, Ireland, Norway). Roblox itself has no Lithuanian UI: its locale API (checked 2026-11-08) enables `lt_lt` for in-experience content only, not for the app or sign-up; its client string table carries 20 languages and no `lt` column; roblox.com/lt serves English; and Roblox does not auto-translate Lithuanian. Players read the Roblox app in English, so your table is the only Lithuanian they see, and English platform words (Robux, Premium, VIP) are already familiar.
- Who reads this column: the in-game Settings menu lets a player pick any language the game lists as supported (Roblox docs), so add Lithuanian under Supported Languages. Lithuanian is not an account language, and whether a Lithuanian device locale selects `lt-lt` on its own is unverified: assume most kids start on English and switch by hand.
- Use "tu" everywhere. The Microsoft guide prescribes lowercase "jūs" for software (but informal address for Copilot's chat prompts), and Minecraft's Lithuanian file uses "jūs" ("Jūs mirėte!", "Spauskite"); in a kids' game "jūs" reads like a manual. Pick "tu" and never mix the two in one game. Plural "jūs" (-kite) only for the whole server: "Prisijunkite prie renginio!".
- Buttons and commands: infinitive, as Lithuanian software does (Microsoft "Įrašyti viską", Minecraft "Atšaukti", "Pirkti dabar!"): "Žaisti", "Pirkti", "Atsiimti". Titles: nouns ("Parduotuvė", "Nustatymai", "Dienos prizas").
- Toasts, dialogs, tutorials: 2nd person singular. Present "-i" (turi, gauni), past "-ai/-ei" (laimėjai, gavai), future "-si" (gausi, prarasi), "kad" + "-tum" (kad uždirbtum), imperative "-k" (grįžk, pirk, įvesk, parduok).
- Drop "tavo" when the meaning holds; Microsoft notes Lithuanian uses possessives far less than English: "Kuprinė pilna!", not "Tavo kuprinė yra pilna!".
- Hype that sounds native: "Valio!", "Šaunu!", "Puiku!", "Oho!", "Sveikiname!" (the standard form even to one player). One "!" is enough.
- Stiff or adult (Microsoft's avoid list and verbal-over-nominal rule): "Norėdami...", "Prašome...", "Jūsų", "atlikti pirkimą" -> "pirkti", "suteikti pagalbą" -> "padėti", "priimti sprendimą" -> "nuspręsti", "taip pat" -> "irgi". Do not open sentences with "Ir" or "Bet".
- Diminutives make pets cute and are natural for kids: "Triušiukas", "Kačiukas", "Šuniukas".
- Slang ("OP", "AFK", "nūbas") only in flavor text, never in system messages. Kid-safe.

## Roblox and gaming vocabulary
Roblox's UI for these players is English, so "Roblox UI" below means the English label they see.
| English | lt-LT | Note |
|---|---|---|
| Robux | Robux | Uninflected after a number, like a currency code: "100 Robux", "Pirkti už 100 Robux". Lithuanian Wikipedia writes „Robux“ in running text; players inflect "robuksai, robuksų" in chat (unverified) |
| Premium | Premium | "Roblox Premium"; never translated |
| game pass | name the pass: "VIP", "Monetos x2" | No settled Lithuanian word. Avoid "žaidimo leidimas": "leidimas" is a permit and also an edition ("antrasis leidimas"). Tab title "Privalumai" (perks, unverified); players say "gamepass" (unverified) |
| developer product | prekė | Shop tab "Prekės"; otherwise name the item |
| experience / game | žaidimas | Never "patirtis" (calque of Roblox's "experience") |
| obby, tycoon, simulator | obby, tycoon, simuliatorius | "kliūčių ruožas" if you must translate obby; titles stay English |
| rebirth | atgimimas; button "Atgimti" | Players may keep "rebirth" (unverified) |
| pet | augintinis (pl. augintiniai) | Masculine. "naminis gyvūnėlis" is too long for UI |
| egg / hatch | kiaušinis / išsiristi (the pet), atidaryti kiaušinį (the player) | "išperėti" is what a hen does; never use it for the player |
| coins / gems | monetos / brangakmeniai or deimantai | Pick gems by the icon; one word per game |
| boost | bonusas | "+10 % bonusas", "2x bonusas" |
| multiplier | daugiklis | "Daugiklis: 2x" |
| XP | XP / patirtis | Minecraft LT: "patirties lygis"; "XP" on a HUD |
| level / level up | lygis / "Naujas lygis!" | Never "Lygis aukštyn!" |
| quest | užduotis (pl. užduotys) | "Dienos užduotys" |
| leaderboard | lyderių lentelė; board title "Lyderiai" | "Geriausi žaidėjai" is 17 chars |
| AFK, noob, OP, GG | AFK, nūbas (unverified), OP, GG | Keep the Latin acronyms |
| VIP | VIP | "VIP serveris" |
| trade | mainai / mainytis | Minecraft LT: "Mainai"; "prekyba" means commerce |
| inventory / backpack | inventorius / kuprinė | Minecraft LT: "Inventorius"; kuprinė is feminine ("Kuprinė pilna") |
| daily reward | dienos prizas | Button "Atsiimti"; "apdovanojimas" is long and formal |
| codes | kodai | "Įvesk kodą" |
| group | bendruomenė | Roblox renamed Groups to Communities, and the English UI kids see says Community; "grupė" is shorter and also understood |
| like / favorite | „Patinka“ / pridėti prie mėgstamiausių (unverified) | Roblox shows only a thumbs-up icon; "Patinka" is the Like word Lithuanians know from YouTube and Facebook |
| server | serveris | Locative "serveryje"; Minecraft LT: "Šis serveris yra pilnas!" |
| friends / connections | draugai | Roblox's English UI says Connections; never "ryšiai". Minecraft LT: "Draugai" |
| shop | parduotuvė | 10 chars; "Prekės" when tighter |

## Grammar traps in UI strings
- **Plurals with {count}.** "1 moneta, 21 moneta; 2 monetos, 22 monetos; 0, 10-20, 30 monetų; 1,5 monetos". A 12 takes "monetų", a 22 takes "monetos": one string cannot cover it. Use Microsoft's label pattern ("Dalyvių: |0"): "Monetų: {count}", "Trūksta monetų: {amount}!". Also safe: impersonal "Liko: {count}", unit abbreviations ("po 3 val."), and uninflected "Robux". Never "{count} monetų".
- **Gender lives in participles and adjectives, not verbs.** Finite verbs are gender-neutral: "{player} prisijungė", "Laimėjai!". Participles are not: "pasiruošęs/pasiruošusi", "norėdamas/norėdama", "sugrįžęs". Rewrite: "Esi pasiruošęs?" -> "Ar pasiruošei?"; "Sveikas sugrįžęs!" -> "Su sugrįžimu!"; "Spausk E, norėdamas atidaryti" -> "Spausk E, kad atidarytum". The "-us" gerund is genderless too: "Paspaudus E, atsidarys parduotuvė".
- **Greetings.** "Sveikas, {player}!" assumes a boy and wants the vocative ("Tomai"). Use "Labas, {player}!".
- **Case around placeholders.** Inserted names and items arrive in the nominative. Give the case to a noun in front, as Microsoft's modifier rule does: "Mainai su {player}" -> "Mainai su žaidėju {player}"; "Gavai {item}" -> "Gavai: {item}" or "Naujas daiktas: {item}". Put {player} as the subject where you can: "{player} nori su tavimi mainytis".
- **Adjective agreement.** A translated {rarity} ("Legendinis") is masculine and clashes with a feminine pet ("lapė", "pelėda"). Keep it apart: "Išsirito {pet} ({rarity})!". Or name pets with masculine nouns (lapinas, katinas, triušiukas) so "{rarity} {pet}" always agrees. Rarity tags: Paprastas, Retas, Epinis, Legendinis, Mitinis.
- **Compound nouns.** English noun stacks become genitive + noun: "Coin Boost" -> "Monetų bonusas", "Pet Shop" -> "Augintinių parduotuvė", "Lucky Potion" -> "Sėkmės eliksyras".
- **Word order.** Free, but put the new information last: "Iki pabaigos: {time}", "Grįžk po {time}".
- **Capitalization.** Only the first word of titles and buttons: "Dienos prizas", not "Dienos Prizas". Months and weekdays lowercase: "iki gruodžio 24 d.". Text after a colon continues lowercase (Microsoft).

## Typography and formatting
- No space before ! ? : ; (same as English).
- Quotation marks „...“ (U+201E, U+201C): „Patinka“. Never English "..." around Lithuanian words.
- Dash: spaced en dash " – " for a pause or a dropped "yra": "Šis kardas – OP!". Ranges unspaced: "5–10". Microsoft: the em dash is not used in Lithuanian.
- Ellipsis with no space before it: "Kraunama...".
- Numbers: thousands separator is a non-breaking space U+00A0, also in four-digit numbers (CLDR minimum grouping 1): "1 250", "1 000 000"; decimal comma: "1,5x". "1,250" reads as one and a quarter. Game code must format {count}, {amount}, {multiplier}.
- Percent: standard Lithuanian spaces it (CLDR "10 %" with U+00A0; Lithuanian Wikipedia "45 %"): "+{percent} %". Casual game text often drops the space (Minecraft LT "100%"); "+10%" is acceptable in a tight HUD slot, but pick one form per game. The spaces in this guide's examples are real U+00A0; copy them. Fredoka One, Sarpanch, Balthazar and Roman Antique have no U+00A0 glyph: use a plain space in those fonts.
- Durations (CLDR short): "3 val. 20 min.", "45 sek.", "2 d. 5 val."; narrow: "3 h 20 min.", "45 s". Never English "3h 20m": "m." means years ("2026 m.").
- Clock: 24-hour "14:05". Dates: "2026-11-08" (Microsoft) or "lapkričio 8 d.".
- Abbreviations end with a period ("pvz.", "val.", "min."); acronyms take none ("XP", "VIP").
- Keyboard keys stay as printed: "Spausk E", "Shift", "Enter" (Minecraft LT: "Paspauskite Enter"). Toggles in 5-char slots: "Įj." / "Išj." (Minecraft LT abbreviations).

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, XP, GG and the game title. In running text put a product or game name in „...“ (Microsoft rule; Lithuanian Wikipedia writes „Robux“): žaidimas „Pet Hatch Tycoon“. Standalone titles and logos take no quotes.
- Usernames and display names: never translate, inflect or add endings ("Tomui" from "Tomas"); let a noun carry the case.
- Promo codes exactly as typed, ASCII: "FREEPETS". Never add diacritics.
- In-game item and pet names: translate ("Sėkmės eliksyras", "Drakonas") unless they are brand names.
- Latin script only, with every diacritic. Stripped "Zaisti", "Parduotuve" look broken, and "į" vs "i" changes words.

## Rendering on Roblox
- Lithuanian needs ą č ę ė į š ų ū ž and capitals (Latin Extended-A, two UTF-8 bytes each).
- The font files of Roblox's Windows client (cmap check, 2026-11-08) cover all 18 letters plus „ “ – in Builder Sans, Builder Extended, Builder Mono, Montserrat (Gotham), Source Sans Pro, Roboto, Arimo, Luckiest Guy, Bangers, Press Start 2P, Titillium Web, Oswald, Nunito, Ubuntu, Merriweather, Michroma, Jura, Sarpanch, Kalam, Patrick Hand, Indie Flower, Amatic SC and Special Elite.
- Missing glyphs (cmap rechecked 2026-11-08): Fredoka One, Permanent Marker, Creepster, Highway Gothic, Accanthis ADF, Balthazar and Roman Antique lack ą č ę ė į ų ū (Roman Antique also ž); Comic Neue Angular and Inconsolata lack ė į ų ū (Inconsolata also –); Denk One lacks all 18. U+00A0 is missing from Fredoka One, Sarpanch, Balthazar and Roman Antique.
- What Roblox draws instead: the pl-pl review saw in Studio (2026-11-08) that Fredoka One's missing ą ę come from a thin sans fallback, not empty boxes, so one word mixes two fonts; Lithuanian's other letters should behave the same (unverified). Fredoka One is common in simulator UIs: switch lt-lt text, or the whole game, to Builder Sans Bold, Luckiest Guy or Bangers.
- Luau `string.upper` changes ASCII only: "žaisti" -> "žAISTI". Write capitals into the table ("ŽAISTI").
- `#text` counts bytes ("Parduotuvė" is 10 characters, 11 bytes); check max lengths with `utf8.len`.
- Ogoneks below ą ę į ų and marks above Ė Č Š Ž may clip in tight TextScaled labels (unverified).
- Verify in Studio: Player Emulator locale `lt-lt`; paste "ĄČĘĖĮŠŲŪŽ ąčęėįšųūž „Patinka“ 1 250 – 10 %" into every FontFace; open the tight strings: shop.title (10/10), event.ends_in (28/28), pass.buy_price, inventory.full (56/60), social.like_reward (52/55).

## Mistakes machine translation makes here
| Mistake | Bad | Good |
|---|---|---|
| Calque of Roblox's "experience" | Prisijunk prie patirties | Prisijunk prie žaidimo |
| "Free" as "not busy" | Laisvas eliksyras | Nemokamas eliksyras |
| "Claim" as a legal claim | Reikalauti | Atsiimti |
| "Event" as an incident | Įvykis baigiasi po 2 d. | Renginys baigsis po 2 d. |
| Mixing jūs and tu | Spauskite E ... Grįžk rytoj! | Spausk E ... Grįžk rytoj! |
| Imperative on buttons | Žaisk / Pirk | Žaisti / Pirkti |
| Gendered "you" | Esi pasiruošęs? / Sveikas sugrįžęs! | Ar pasiruošei? / Su sugrįžimu! |
| Number + noun | Reikia dar {amount} monetų | Trūksta monetų: {amount}! |
| Nominative name after a preposition | Mainai su {player} | Mainai su žaidėju {player} |
| Hen verb, Title Case | Tu išperėjai Retą Drakoną! | Išsirito Drakonas (Retas)! |
| English number and time format | 1,250 monetų, 3h 20m | 1 250, 3 val. 20 min. |
| Stripped diacritics | Parduotuve, Zaisti | Parduotuvė, Žaisti |

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Žaisti | Infinitive button |
| shop.title | Parduotuvė | Exactly 10/10; "Prekės" if the font is wide |
| shop.buy | Pirkti | |
| reward.claim | Atsiimti | |
| rebirth.button | Atgimti | |
| rebirth.confirm | Atgimti dabar? Prarasi monetas, bet gausi nuolatinį {multiplier}x bonusą. | Code formats 1.5 as "1,5" |
| coins.need_more | Trūksta monetų: {amount}! | Colon keeps 1, 2, 10 correct |
| coins.count | Monetų: {count} | Genitive label (Microsoft pattern); a bare "{count}" next to the icon also works |
| egg.hatched | Išsirito {pet} ({rarity})! | Parentheses avoid gender agreement |
| rarity.legendary | Legendinis | Masculine, agrees with "augintinis" |
| pet.name.dragon | Drakonas | "Slibinas" is the folk-tale dragon |
| chat.player_joined | {player} prisijungė prie žaidimo | Minecraft LT wording; past tense is genderless |
| trade.request | {player} nori su tavimi mainytis | |
| prompt.open_shop | Spausk E – atidaryti | Compact UI form, 20/22. "Spausk E, kad atidarytum" reads better but is 24/22: use it where the label has room. With Roblox's default ProximityPrompt, put "Atidaryti" in ActionText and let Roblox draw the key (right on gamepad and touch too) |
| pass.buy_price | Pirkti už {price} Robux | 23/22 counting the literal "{price}"; 19-20 with a real 3-4 digit price. Robux stays uninflected |
| pass.coins2x | Monetos x2 | Avoids case on "2x monetų" |
| pass.vip | VIP | |
| reward.daily_title | Dienos prizas | |
| reward.come_back | Grįžk po {time} ir gausi kitą prizą! | {time} as "3 val. 20 min." |
| codes.placeholder | Įvesk kodą | |
| codes.invalid | Kodas neteisingas arba nebegalioja. | Microsoft: error messages end with a period |
| social.like_reward | Paspausk „Patinka“ ir gauk nemokamą <b>Sėkmės eliksyrą</b>! | Item inflected to accusative inside the tags; 52/55. Roblox's button is an unlabeled thumbs-up; „Patinka“ names the familiar Like action. Minecraft LT names its Potion of Luck "Sėkmės eliksyras" |
| social.group_reward | Prisijunk prie mūsų bendruomenės ir gauk dovaną! | 48/55. "bendruomenė" matches Roblox's Communities; "dovana" (gift) carries "free" ("nemokamą prizą" ran to 56/55) |
| afk.warning | Esi AFK! Pajudėk, kad toliau uždirbtum! | |
| leaderboard.title | Lyderiai | "Geriausi žaidėjai" is 17/16 |
| level.up | Naujas lygis! Dabar tavo lygis: {level}. | Colon avoids ordinal agreement |
| tutorial.sell | Įeik į šviečiantį ratą, kad parduotum augintinius. | |
| inventory.full | Kuprinė pilna! Parduok augintinių, kad atsirastų vietos. | Partitive genitive "augintinių" = some pets |
| settings.music | Muzika | |
| settings.on | Įj. | "Įjungta" is 7/5; Minecraft LT abbreviates the same way |
| loading | Kraunama... | Neuter passive participle, as Microsoft's "Diegiama" |
| event.ends_in | Iki pabaigos: {time} | Drops "Event": the banner already shows it. 25/28 with "2 d. 5 val.", 28/28 with "3 val. 20 min."; "Renginys baigsis po {time}" overflows |
| item.op | Šis kardas – OP! | Dash replaces "yra" |
| friends.boost | +{percent} % bonusas už kiekvieną draugą serveryje | Non-breaking space before % |

## Sources
1. Microsoft Lithuanian localization style guide (PDF): https://aka.ms/lithuanian-styleguide
2. Microsoft localization style guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. CLDR plural rules: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-core/supplemental/plurals.json
4. CLDR Lithuanian number symbols and percent pattern: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/lt/numbers.json
5. CLDR Lithuanian duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/lt/units.json
6. Roblox language codes (lt-lt): https://create.roblox.com/docs/production/localization/language-codes
7. Roblox client CoreScript string table, mirrored (no Lithuanian column): https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/translations/CoreScriptLocalization.csv
8. roblox.com under /lt/ serves English: https://www.roblox.com/lt/games/920587237/Adopt-Me
9. Lithuanian Wikipedia, Roblox: https://lt.wikipedia.org/wiki/Roblox
10. Minecraft Java Edition Lithuanian strings (community translation): minecraft/lang/lt_lt.json from the launcher asset index, read locally 2026-11-08 (no public URL)
11. Roblox Windows client fonts: %LOCALAPPDATA%/Roblox/Versions/<version>/content/fonts, cmap glyph check run locally 2026-11-08 (no public URL)
12. Roblox locale API (lt_lt: in-experience content only, not full app or sign-up): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
13. Roblox Creator Docs, Localize with scripting (in-game Settings language switcher): https://create.roblox.com/docs/production/localization/localize-with-scripting
14. Lithuanian Wikipedia, Procentas (spaced "45 %"): https://lt.wikipedia.org/wiki/Procentas
15. This skill's Polish guide, Studio fallback-font check 2026-11-08: references/locales/pl-pl.md
