# English (United Kingdom) (en-gb) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `en-gb` only; the bare `en` column holds the US default. Since locale support launched (2025-11-24) a player gets `en-gb` only by picking "English (United Kingdom)" (the name in Roblox's locale API; the Settings label itself unverified) in Account Settings > Language or the Experience Language menu. Region never picks it: a UK player left on English (United States) reads `en-us` |
| Script, direction | Latin, LTR |
| Address the player as | "you", with contractions, exactly as the US source does |
| Text expansion vs English | 0-3%; a few swaps add 1-3 letters (colour, favourite, trousers) |
| Plural categories (CLDR) | one, other (ordinals: one, two, few, other), same as US |
| Model confidence | high: the risk is over- or under-Britishising, not comprehension |
| Native review before shipping | optional; have a UK speaker skim jokes, food, clothes and school words |

## Audience and register
- This is adaptation, not translation: start from the `en-us` column (not the raw source; it already fixes plural and a/an traps) and change only what a UK player would notice as American. Most strings stay word for word identical (all 34 reference strings do).
- UK players aged 9-16 use the same global gaming English as US kids. A 2025 UK bank's parent glossary lists AFK, noob, GG, buff, nerf, grind, lag, XP, TP and spawn unchanged. Keep them.
- Register: friendly, direct "you", contractions (can't, don't, you'll), short fragments. Microsoft's UK voice also prefers contractions and fragments: "Need more coins? Hatch faster!"
- Keep the source's exclamation marks and hype words (Awesome! Epic! Let's go!); do not add more. Microsoft's UK guide discourages "!" in software UI, but that is productivity-app advice, not a kids' game.
- Never add British flavour the source lacks: no "innit", "bruv", "mate", "cheers", "blimey", "proper", no posh or Cockney voice. It reads as parody. Bad: "Cheers, mate! Your pets are proper mint!" Good: "Nice! Your pets are awesome!"
- Family and school words are where UK kids spot US English: Mom -> Mum, math -> maths, 5th grade -> Year 6, recess -> break time, vacation -> holiday, semester -> term.
- Kid-safe traps (harmless in the US, rude or odd in the UK): "fanny pack" -> "bum bag" ("fanny" is vulgar in the UK); "pants" means underwear -> "trousers"; "shag rug" -> "fluffy rug"; "spunky" -> "plucky"; "pissed" means drunk -> "angry"; never use "bloody" as an intensifier.

## Roblox and gaming vocabulary
| English (US source) | en-gb | Note |
|---|---|---|
| Robux | Robux | brand; never "Robuxes" or "R$" in prose |
| Premium | Premium (legacy) / Roblox Plus | new Premium sign-ups ended when Roblox Plus launched on 2026-04-30; write "Plus" only if the game checks for it |
| VIP | VIP | pass name, unchanged |
| game pass | pass / game pass | follow the source; Roblox's docs now say "passes" |
| developer product | developer product | players see the product's own name, not this term |
| experience / game | game | Roblox's docs body text says "game"; players say game |
| obby, tycoon, simulator | obby (obbies), tycoon, simulator / sim | unchanged |
| rebirth, pet, egg, hatch | rebirth, pet, egg, hatch | unchanged |
| coins, gems, boost, multiplier | same | "2x" and "x2" both seen; keep the source's form |
| XP, level up, quest | same | past tense "levelled up" (double l) |
| leaderboard | leaderboard | "#1" on a board is fine |
| AFK, noob, OP, GG, sus | same | Latin letters, source casing |
| trade, server | trade, server | unchanged |
| inventory / backpack | inventory / backpack | Backpack is Roblox's own term; don't swap in "rucksack" |
| daily reward, codes | same | "Codes" panel title unchanged |
| group | community | Roblox's player UI says "Communities" since Nov 2024; same as the `en-us` column. "group" only if the game's other UI still says group |
| like / favorite | like / favourite | UK spelling in your strings, even though Roblox's own Favorite button stays US for `en-gb` players (see Rendering) |
| friends | friends | Roblox said "Connections" in 2025, back to "Friends" in April 2026; never "connections" |
| armor, defense, color, gray | armour, defence, colour, grey | common game words that do change |
| catalog | catalogue | generic only; Roblox's store is "Marketplace" |

Everyday US words to swap, only when the source uses them (standard dictionary pairs; Microsoft's list confirms favourite, centre, mobile phone, shopping centre, cinema):

| Theme | US -> UK |
|---|---|
| Family, school | Mom -> Mum, math -> maths, 5th grade -> Year 6, recess -> break, principal -> head teacher, cafeteria -> canteen |
| Food | candy -> sweets, cotton candy -> candyfloss, fries -> chips, chips -> crisps, popsicle -> ice lolly, cookie -> biscuit (big soft cookies stay cookies) |
| Clothes | pants -> trousers, sneakers -> trainers, sweater -> jumper, vest -> waistcoat, diaper -> nappy |
| Home, town | apartment -> flat, trash -> rubbish, trash can -> bin, elevator -> lift, flashlight -> torch, mall -> shopping centre, line -> queue, yard -> garden, cell phone -> mobile |
| Cars, sport | gas -> petrol, parking lot -> car park, trunk -> boot, hood -> bonnet, tire -> tyre, highway -> motorway, sidewalk -> pavement, soccer -> football |
| Seasons | fall -> autumn ("Autumn Event"), "on the weekend" -> "at the weekend" |

Keep the US words UK kids use themselves: awesome, cool, epic, cash, movie, cookie, truck ("Monster Truck"), cop ("Cops and Robbers").

## Grammar traps in UI strings
- Spelling is the main job. -our: colour, favourite, armour, honour, behaviour. -re: centre, metre, theatre. -ise and -yse: customise, organise, recognise, analyse, paralyse. Use -ise throughout (Microsoft's UK samples write optimise, personalise), not Oxford -ize.
- Never -ise: prize, size, seize, capsize. "Claim your prize!" stays; "prise" means to lever something open.
- Double l before -ed, -ing, -er: levelled, travelled, cancelled, fuelled, labelled, traveller. Single l in enrol, fulfil, skilful.
- Noun vs verb: practice / practise ("Practice Mode", "Practise your jumps!"); licence / license. Also defence, offence, grey, tyre, axe, pyjamas.
- program stays for software and code; programme only for a show or event schedule. "dialog box" stays in computing; story text is "dialogue".
- "gotten" -> "got": "You've got a new pet!" Keep the source's learned/burned (both are UK); "dove" -> "dived", "snuck" -> "sneaked".
- Plurals with {count}: CLDR one/other, same as US, and tables have no plural selection. Copy the `en-us` column's label patterns: "Coins: {count}", "Not enough coins! Need {amount} more." If a game's `en-us` column is still the raw "{count} Coins", rewrite both columns the same way and tell the source owner; never let `en-gb` alone keep "1 Coins".
- Articles before {rarity}: "a {rarity}" gives "a Epic" for vowel-initial rarities. Use the `en-us` rewrite, "New pet: {rarity} {pet}!"; "a/an" stays only before a fixed word ("a permanent {multiplier}x boost").
- {player} has no gender in English; when a pronoun is needed use "they/their": "{player} left their base".
- Team nouns: UK allows "Red Team are winning", but keep the source's singular ("Red Team wins!"); both read naturally.
- Prepositions: Monday through Friday -> Monday to Friday; fill out -> fill in; different than -> different from (or "to", which Microsoft's UK guide uses); wait on (meaning wait for) -> wait for; out the window -> out of the window.
- Hyphenate compound adjectives before a noun, per Microsoft UK: "limited-time event", "double-coin weekend"; not after it: "the event is limited time".
- Capitalisation: keep the source's casing on buttons and titles ("Daily Reward" stays title case). Microsoft's UK guide says UI labels follow the source.
- Floors: US "first floor" is UK "ground floor". Adapt that in prose; keep numbered labels ("Floor 2") as they are.

## Typography and formatting
- Quotes: double quotes are fine (Microsoft says modern UK usage favours them). Full stops and commas go outside unless they belong to the quote: Type "FREEPETS". (US: Type "FREEPETS.")
- No serial comma: "coins, gems and pets" (US: "coins, gems, and pets"). Keep it only if the list is ambiguous without it.
- No full stop after Mr, Mrs, Dr (GOV.UK style), and by the same rule St: "Mr Whiskers", "Dr Boom". No comma after "e.g." or "i.e." (Microsoft UK).
- Numbers: same as US, 1,250 and 2.5; never reformat a {count}.
- Dates: day before month, "8 November", "Sat 8 Nov". Never "11/08" (a UK player reads 11 August).
- Clock times: "5pm", "5:30pm" or "17:00", not "5:00 PM". Durations "3h 20m" and "2d 5h" are unchanged.
- Currency: real money is "£4.99", but never write prices into strings; Roblox shows them. In-game cash shown as "$" in the source stays "$": it is game art, not a price.
- "#" is "hash" in the UK ("pound" means £): "pound key" -> "hash key". Microsoft's UK guide writes "No. 586" for a numbered item, but "#1" as a leaderboard rank stays.
- "Loading..." unchanged. Dashes: avoid them in UI strings, as in `en-us`; if the source has one, keep it.
- Keys: "Press E", "Space", "Shift", "Enter" unchanged.
- Units: games use studs. Real units, if any: miles and mph for roads, metres, kg, degrees C.

## Do not translate / keep as is
- Roblox, Robux, Premium, Roblox Studio and every platform feature as Roblox spells it.
- Game titles, even with US spelling: "Tower Defense Simulator", "Pet Hatch Tycoon". A title is a brand.
- Promo codes and anything typed: a code FAVORITE100 stays exactly that, even in a sentence that says "favourite".
- Usernames, display names, {params}, `<b>` tags, keybinds.
- Item and pet names: plain descriptive names take UK spelling ("Gray Cat" -> "Grey Cat", "Gold Armor" -> "Gold Armour") when the name lives only in the table. Keep the US form if it is baked into a decal or model, typed in chat commands or trade search, or is a coined brand-like name ("Colorblast").
- Gaming acronyms and memes: noob, OP, GG, AFK, W, L, sus.
- Strings identical to `en-us` still get a filled cell in the `en-gb` column.

## Rendering on Roblox
- Latin with plain ASCII plus "£" (U+00A3, Latin-1); no accents, shaping or line-breaking issues, so nothing clips that the US text would not. "£" in every Roblox font is unverified but expected, and strings rarely need it.
- Expansion is a few letters at most; still check 5-10 character buttons after a swap.
- Only your game's text turns British. Roblox's locale API enables `en_gb` for in-game text but not for the Roblox app, so platform UI ("Favorite", "Communities") stays US English for these players (inferred from the API, not seen in the app).
- Reach: only players who picked the UK locale read this column. The 2025-11-25 DevForum update said the new locales were briefly missing from the in-game switcher; whether every client offers them today is unverified.
- Worth shipping: yes. It is a main-tier locale and costs a copy of the `en-us` column plus a few swaps. Fill every key, or leave `en-gb` out of the game's languages entirely.
- Blank cells: `FormatByKey` can error on a missing entry; Roblox's TranslationHelper sample then falls back to the source-language translator. What AutoLocalize shows for a blank `en-gb` cell is unverified.
- Scripts: read `Player.LocaleId` or the Translator from `GetTranslatorForPlayerAsync`, never `LocalizationService.RobloxLocaleId`: that is the CoreGui locale, and DevForum reports (2024-2025) show it returning `en-us` for UK accounts. Test in Studio with the Player Emulator set to `en-gb`.
- `DateTime:FormatLocalTime(format, player.LocaleId)` comes out day-first only for players actually on `en-gb`.

## Mistakes machine translation makes here
1. Inventing Britishness: "Ta, mate! Proper brilliant hatch, innit!" -> "Nice hatch!" (the source, unchanged).
2. Over-correcting -ize: "Claim your prise!" -> "Claim your prize!"; "Pick a sise" -> "Pick a size".
3. Missing the swaps it should make: "Pick your favorite color" -> "Pick your favourite colour"; "Gray Wolf" -> "Grey Wolf"; "Armor Shop" -> "Armour Shop".
4. Single l: "Leveled up!" -> "Levelled up!"; "Trade canceled" -> "Trade cancelled".
5. Practice/practise mix-up: "Practice your jumps!" -> "Practise your jumps!"; "Practise Mode" -> "Practice Mode".
6. "programme" for software: "Update the programme" -> "Update the program".
7. "gotten": "You've gotten 3 eggs!" -> "You've got 3 eggs!"
8. US words that are rude or wrong in the UK: "Equip the fanny pack" -> "Equip the bum bag"; "Buy cool pants" -> "Buy cool trousers".
9. Changing what must stay: "Enter code FAVOURITE100" when the code is FAVORITE100; "Tower Defence Simulator" as a title -> "Tower Defense Simulator".
10. US punctuation and dates: Type "YES." -> Type "YES".; "Mr. Bacon" -> "Mr Bacon"; "Ends Nov 30, 5:00 PM" -> "Ends 30 Nov, 5pm".
11. US seasons and food: "Fall Update" -> "Autumn Update"; "Sell fries and chips" -> "Sell chips and crisps".

## Reference translations
All 34 match the `en-us` guide's column word for word: none has a US spelling, US-only word or US date. Four rows rephrase the raw source exactly as `en-us` does (plural, a/an and community fixes); copy them, never fork. Other notes say why the obvious "British" edit is wrong.

| key | translation | note |
|---|---|---|
| menu.play | Play | |
| shop.title | Shop | |
| shop.buy | Buy | |
| reward.claim | Claim | |
| rebirth.button | Rebirth | |
| rebirth.confirm | Rebirth now? You'll lose your coins but get a permanent {multiplier}x boost. | no comma before "but", as in the source |
| coins.need_more | Not enough coins! Need {amount} more. | as en-us; the source gives "1 more coins" |
| coins.count | Coins: {count} | as en-us; "{count} Coins" shows "1 Coins" |
| egg.hatched | New pet: {rarity} {pet}! | as en-us; "a {rarity}" gives "a Epic" |
| rarity.legendary | Legendary | |
| pet.name.dragon | Dragon | |
| chat.player_joined | {player} joined the game | "has joined" also fine; not worth a fork |
| trade.request | {player} wants to trade with you | |
| prompt.open_shop | Press E to open | |
| pass.buy_price | Buy for {price} Robux | |
| pass.coins2x | 2x Coins | |
| pass.vip | VIP | |
| reward.daily_title | Daily Reward | source title case kept |
| reward.come_back | Come back in {time} for your next reward! | |
| codes.placeholder | Enter code | |
| codes.invalid | That code is invalid or expired. | |
| social.like_reward | Like the game to get a free <b>Lucky Potion</b>! | |
| social.group_reward | Join our community to unlock a free reward! | as en-us; Roblox's player UI says Communities. "group" only if the game's other UI does |
| afk.warning | You're AFK. Move to keep earning! | AFK kept |
| leaderboard.title | Top Players | |
| level.up | Level up! You're now level {level}. | |
| tutorial.sell | Walk into the glowing circle to sell your pets. | |
| inventory.full | Your backpack is full! Sell pets to make room. | not "rucksack" |
| settings.music | Music | |
| settings.on | On | |
| loading | Loading... | |
| event.ends_in | Event ends in {time} | |
| item.op | This sword is OP! | OP kept; UK kids use it |
| friends.boost | +{percent}% boost for each friend in your server | "friend" is Roblox's current term again |

## Sources
1. Microsoft Localization Style Guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
2. Microsoft English (United Kingdom) Style Guide, 2024 PDF: https://download.microsoft.com/download/9/8/8/98834e3c-f0be-40c9-af56-35a0cc1ab65f/eng-gbr-StyleGuide.pdf
3. Unicode CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. Wikipedia, American and British English spelling differences: https://en.wikipedia.org/wiki/American_and_British_English_spelling_differences
5. Roblox DevForum, Locale Support for Translations (2025-11-24): https://devforum.roblox.com/t/locale-support-for-translations/4095306
6. Roblox DevForum, Incorrect LocaleIds reported in game: https://devforum.roblox.com/t/incorrect-localeids-reported-in-game/2935500
7. Roblox DevForum, Localization API update for the in-experience language switcher: https://devforum.roblox.com/t/localization-api-update-for-upcoming-in-experience-language-switcher/1974795
8. Roblox DevForum, Friends Are Back (2026-04-02): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
9. Roblox DevForum, Introducing Roblox Communities (Nov 2024): https://devforum.roblox.com/t/introducing-roblox-communities/3268307
10. Roblox Creator Hub, Passes: https://create.roblox.com/docs/production/monetization/game-passes
11. Roblox Creator Hub, Language codes: https://create.roblox.com/docs/production/localization/language-codes
12. HSBC UK, Gaming Jargon Buster (2025): https://www.hsbc.co.uk/content/dam/hsbc/gb/pdf/financial-education/gaming-jargon-buster.pdf
13. GOV.UK A to Z style guide (Mr/Dr without full stops, -ise, 5:30pm, day-month dates): https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/
14. Roblox locale API (en_gb: enabled for in-game text, not the app): https://locale.roblox.com/v1/locales/supported-locales-for-creators
15. Roblox Creator Hub, LocalizationService (RobloxLocaleId is the CoreGui locale): https://create.roblox.com/docs/reference/engine/classes/LocalizationService
16. Roblox Creator Hub, Localize with scripting (TranslationHelper fallback): https://create.roblox.com/docs/production/localization/localize-with-scripting
17. Roblox Newsroom, Introducing Roblox Plus (2026-04): https://about.roblox.com/newsroom/2026/04/introducing-roblox-plus-subscription
