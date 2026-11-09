# Filipino (fil-ph) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `fil-ph` (language code `fil`; the only Filipino locale, so no bare `fil` column). Never `tl` |
| Script, direction | Latin, LTR; 28-letter alphabet with Ñ and the digraph NG; accent marks (á, à, â) only in dictionaries, never in game UI |
| Address the player as | informal "ka", "mo", "ikaw"; never "kayo", "ninyo", "po" or "opo" for one player |
| Text expansion vs English | +5-35% on sentences (the reference set averages +14%, kept low by Taglish nouns); one-word buttons often double ("Buy" -> "Bilhin", "Play" -> "Maglaro") |
| Plural categories (CLDR) | cardinal one, other ("other" = numbers ending in 4, 6 or 9, whose Tagalog words take the linker "na": "apat na"); ordinal one, other |
| Model confidence | medium: grammar is solid, but models swing between textbook Tagalog and English with a Tagalog word sprinkled in, and drop "si"/"ni" around names |
| Native review before shipping | strongly recommended |

## Audience and register
- Players are Filipino kids and teens who are bilingual from school and talk about games in Taglish: Filipino grammar carrying English game words. Roblox itself shows them English (its locale API enables `fil_ph` for in-game text only, not the app; see Rendering), so English game nouns are what they know.
- Address one player with "ka" / "mo" / "ikaw". Microsoft's Filipino guide asks for "ka" and "iyo", not "kayo" or "inyo", and says "po" / "opo" make text too formal. "Kayo" / "ninyo" are right only when talking to everyone in the server: "Ingat kayo, may boss na!".
- "Tayo" / "natin" (we, including the player) for hype: "Tara, laro tayo!". "Kami" / "namin" (we, not the player) for the studio: "Sumali sa community namin".
- Buttons are short verbs. Object-focus form when the button acts on a thing on screen: "Bilhin", "Kunin", "Ibenta", "I-claim". Mag- infinitive for an activity: "Maglaro", "Mag-rebirth", "Mag-trade".
- Buttons and prompts take the bare verb: "Ilagay ang code", not "Pakilagay ang code". Use "paki-" only where the English says "please" (Microsoft's own error samples write "Pakisubukang muli"), and never add "po".
- Natural hype: "Astig!", "Ang galing!", "Grabe!", "Panalo!", "Tara na!", "Yehey!". The exclamative "Ang [adj] ng [noun]!" sounds native: "Ang OP ng espadang ito!". Keep the source's end punctuation: no "!" where the English has a period, never "!!".
- Kid-safe: never "tangina", "gago", "bobo", "tanga", "ulol" or "pakyu", even softened or bleeped. "Noob" and "bano" only in jokey flavor text, never aimed at the player.

**How much English (Taglish).**
- Grammar is always Filipino: verbs, pronouns, markers (ang, ng, sa, si, ni), particles (na, pa, lang) and linkers. English function words ("you", "your", "and", "or", "for", "now", "after", "next") never appear.
- Keep in English the game and platform nouns a Filipino Roblox YouTuber would say in English (vocabulary table): coins, gems, pet, rebirth, boost, level, server, event, code, Robux. English spelling stays ("coins", never "koyns").
- English verbs gamers use take Filipino affixes with a hyphen: "mag-trade", "i-claim", "naka-hatch", "i-like", "nag-level up".
- Translate everyday words that kids say in Tagalog anyway: libre (free), bilhin (buy), ibenta (sell), maglaro (play), kaibigan (friend), espada (sword), bilog (circle), puno (full), mali (wrong), susunod (next).
- Too much English: "Join our community para sa free reward!". Too little: "Sumapi sa aming pamayanan upang makamit ang libreng gantimpala!". Right: "Sumali sa community namin para sa libreng reward!".
- Short panel titles players already say in English may stay English ("Shop", "Daily Reward", "Top Players"), but every sentence must read as Filipino. "Tindahan" is everyday Tagalog and also fine; "Mga Nangunguna" reads more formal. Native reviewer decides, then one choice per game.

## Roblox and gaming vocabulary
Roblox shows Filipino players English, so platform terms follow Roblox's English UI.

| English | fil-ph | note |
|---|---|---|
| Robux | Robux | invariable: "100 Robux"; never "Robuks" |
| game pass | game pass | "Bilhin ang game pass"; players also write "gamepass" |
| developer product | (the item's name) | players never see the term |
| experience / game | game, laro | never "karanasan" (life experience); tl.wikipedia calls Roblox titles "laro" |
| obby / tycoon / simulator | obby / tycoon / simulator | keep |
| rebirth | Rebirth, mag-rebirth | never "muling pagsilang" (religious rebirth, renaissance) |
| pet | pet, mga pet | "alaga" is fine in prose; "alagang hayop" too long for UI |
| egg / hatch | egg / mag-hatch, naka-hatch | keep "Egg" in item names ("itlog" also means testicles and a zero score in slang); never "pisain"/"pinisa": "pisa" means both hatched and crushed, and the transitive verb reads as crush |
| coins / gems | coins / gems | "barya" is real loose change; "hiyas" is bookish |
| boost / multiplier | boost / multiplier | names use "2x": "2x Coins", "{n}x boost" |
| XP / level up | XP / mag-level up | "Level up! Level 10 ka na." |
| quest | quest | "misyon" also understood; pick one per game |
| leaderboard | leaderboard, Top Players | "Mga Nangunguna" correct but stiff (unverified as player usage) |
| AFK / noob / OP | AFK / noob / OP | "AFK ka", "Ang OP!" |
| VIP / Premium | VIP / Premium | never translate |
| trade | trade, mag-trade, makipag-trade | "palitan" (exchange) is understood but rarer in games (unverified) |
| inventory / backpack | inventory, backpack, bag | Minecraft's Filipino "Imbentaryo" reads like a textbook |
| daily reward | Daily Reward, reward | "gantimpala" sounds like a contest prize |
| codes | code | "Ilagay ang code", "i-redeem ang code" |
| group | community | Roblox's English UI says "Communities" since Nov 2024, so that is the page players land on. Many kids may still say "group" (unverified); use "group" only if the game's other UI does |
| like / favorite | i-like / i-favorite | "I-like ang game" |
| server | server | "sa server mo", "lumipat ng server" |
| friends / connections | kaibigan | Roblox renamed Friends to Connections, then back to Friends in April 2026; never "connections". In game text use "kaibigan" ("kalaro" = playmate) |
| shop / buy / sell | Shop / Bilhin, bumili / Ibenta, magbenta | "Tindahan" (everyday, not stiff) also correct; pick one per game |
| free | libre, libreng | never "malaya" (free as in freedom) |
| event / lag / grind | event / lag / mag-grind | "kaganapan" is formal |

## Grammar traps in UI strings
- Plurals: nouns do not inflect; "mga" marks a plural: "mga pet". With "mga", English nouns stay singular (Microsoft: "Mga file"). Never "mga" before a number: "mga 5 coins" means "about 5 coins".
- Numbers and linkers: CLDR's one/other split exists because a spoken number takes "-ng" or "na" before a noun ("tatlong araw", "apat na araw"). One string cannot pick, so keep a Filipino noun out of the slot after {count}: "Coins: {count}", "Kulang pa ng {amount} ang coins mo!". An English noun after a digit is accepted Taglish ("50 coins") but fails at 1.
- Names take personal markers: "si" (subject), "ni" (actor or owner), "kay" (to or with). "Sumali si {player} sa laro", "Inaaya ka ni {player} na mag-trade", "Nakipag-trade ka kay {player}". Never drop them, never "ang {player}".
- No gender: "siya" covers everyone, and verbs never agree, so any {player} works.
- Linkers after placeholders: never glue "-ng" to a placeholder ("{rarity}ng {pet}"). English names need none ("Legendary Dragon"); a Filipino adjective would ("Bihirang Dragon"), so keep rarity words English when they are inserted.
- "rin/din", "raw/daw": "rin" after a vowel, "din" after a consonant. Do not put them right after a placeholder; move them: "Sumali rin si {player}".
- Word order: verb first, short particles ("ka", "mo", "na", "pa") second. "Nag-level up ka!", not the English-shaped "Ikaw ay nag-level up!"; "Puno na ang backpack mo!".
- "ng" vs "nang": "ng" marks objects and owners ("Bumili ng pet"); "nang" means "when", "so that" or marks manner ("Bumalik nang mabilis").
- Aspect on English roots repeats the root's first consonant and vowel sound, hyphenated: "Nagte-trade", "Magre-rebirth", "Naglo-load" (Microsoft: "Nagda-download").
- Focus: "Ibenta" / "Bilhin" act on a specific thing ("Ibenta ang pet na ito"); "Magbenta" / "Bumili" are general ("Magbenta ng pet").
- Capitalization (Microsoft): capitalize the first word when the source does; in titles skip short markers ("ang", "ng", "sa", "na") after the first word; hyphenated forms capitalize only the first part: "Mag-rebirth", "I-claim".

## Typography and formatting
- Punctuation follows English (Microsoft): no space before ! ? : ;, English quotation marks. Microsoft prefers commas or parentheses to em dashes in Filipino.
- Numbers match en-us (CLDR fil: comma groups, period decimal, "#,##0%"): "1,250 Coins", "1.5x boost", "10%". The Microsoft PDF's punctuation page shows one stray "1.526"; its numbers section says Filipino uses the comma ("1,526", "$ 1,526.75"), as does CLDR. Percent takes no space.
- Durations: {time} comes from game code. Default to the compact "3h 20m" / "2d 5h": it fits every length limit, and CLDR's own narrow minute and second are "m" and "s" (player preference unverified). Spelled out, CLDR short units give "3 oras, 20 min." (comma, not "at"), and numbers ending in 4, 6 or 9 take "na" ("4 na oras"), so the formatter must choose per count. Do not mix styles in one game.
- Clock and dates (Microsoft): "3:00 PM", "Enero 1, 2026". Ordinals take "ika-" with a hyphen: "ika-2", "ika-10"; ranks are simpler as "#1" or "Top 1".
- Ellipsis: three periods, no space: "Naglo-load...".
- Hyphens change meaning: "i-ban" vs "iban" (Microsoft's example); write "i-like", "mag-hatch", "naka-hatch", never "ilike", "maghatch".
- Keys stay English (Microsoft keeps Enter, Shift, Spacebar): "Buksan gamit ang E". For touch, "I-tap" (unverified as Roblox wording).

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, XP, GG, noob, obby, tycoon, simulator, Rebirth, game pass.
- The game title "Pet Hatch Tycoon", display names, usernames, promo codes ("FREEPETS"), keybinds.
- Rarity names (Common, Rare, Epic, Legendary, Mythic): players know the English tiers from other games (unverified), and English words need no linker.
- Item names stay English by default ("Lucky Potion") so players can trade and look them up; localize them only when the developer wants it ("Potion ng Swerte").
- Never respell English game words in Filipino spelling ("koyns", "rebert", "imbentori"). Long-nativized words keep their Filipino spelling: espada, dragon, musika, libre.
- Bare "On"/"Off" stay English in toggles: "Bukas" also means "tomorrow", and Minecraft's "SIGE"/"HUWAG" reads as "okay"/"don't".

## Rendering on Roblox
- Filipino needs basic Latin plus Ñ/ñ. A cmap check of the 75 fonts in the Roblox build of 2026-11 found Ñ, ñ and the accented vowels in every Latin font (Builder Sans, Source Sans Pro, Montserrat, Roboto, Fredoka One, Luckiest Guy and the rest); only the non-Latin Noto UI fonts and emoji fonts lack them.
- The peso sign (U+20B1) is missing from 27 of the Latin font files (Fredoka One, Luckiest Guy, Press Start 2P, Permanent Marker, Creepster, Titillium Web, Ubuntu). Prices are Robux anyway; don't put pesos in game text.
- Players cannot choose Filipino as their Roblox account language. Roblox's locale API (2026-11-08) marks `fil_ph` enabled for in-game content only, not for the app or sign-up, and its 18 account languages leave it out; roblox.com/fil/ returns 404 and the client's CoreScript translations have no fil column. So `Player.LocaleId` is almost never `fil-ph`: players reach this column through the in-game Settings "Experience Language" dropdown, which Roblox's docs say lists the languages the game has enabled (enable Filipino in the game's localization settings; not tested in a live client), or through the game's own language picker.
- Length is the real risk. Measured in Studio 2026-11-08 (TextService:GetTextBoundsAsync, Builder Sans): TextWrapped breaks only at spaces, never at a hyphen, so "mag-rebirth" moves down whole; a single word wider than the box is cut at any letter. Long words ("makakakuha", "permanenteng", "pagkalipas") need AutomaticSize or slack rather than TextScaled shrinking.
- Test in Studio with a `fil-ph` test locale: rebirth.confirm at phone width, "Naglo-load..." in its 14-character label, and the trade popup with a 20-character display name.

## Mistakes machine translation makes here
1. "experience" -> "karanasan" (life experience): "Sumali sa karanasan" -> "Sumali sa game".
2. "free" -> "malaya" (free as in liberty): "Malayang reward" -> "Libreng reward".
3. Formal register: "Kayo po ay may bagong gantimpala" -> "May bagong reward ka!"; "Pakilagay po ang code" -> "Ilagay ang code".
4. English word order with "ay": "Ikaw ay nag-level up!" -> "Nag-level up ka!".
5. Purist calques: "Muling Pagsilang" -> "Rebirth"; "Pang-isahang-laro" style compounds -> plain Taglish; "SIGE" for On -> "On".
6. Dropped personal marker: "{player} sumali sa laro" -> "Sumali si {player} sa laro".
7. Wrong verb for hatch: "Pinisa mo ang itlog" (reads as "you crushed the egg") -> "Naka-hatch ka ng {pet}!".
8. "mga" misuse: "mga 5 coins" (about 5) -> "5 coins"; "mga pets" -> "mga pet".
9. "ng"/"nang" swapped: "Bumili nang pet" -> "Bumili ng pet"; "Bumalik ka ng mabilis" -> "Bumalik ka nang mabilis".
10. Tense flip: "Tapos na ang event" means it is already over -> "Matatapos ang event sa {time}" or "Event: {time} na lang".
11. Price button read as buying Robux: "Bumili ng {price} Robux" -> "Bilhin sa {price} Robux".
12. Wrong "we": "Sumali sa group natin" (implies the player is already in it) -> "Sumali sa community namin".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Maglaro | mag- infinitive; Minecraft's Filipino uses it too |
| shop.title | Shop | kept as players say it; "Tindahan" also correct |
| shop.buy | Bilhin | object focus: buy this item |
| reward.claim | Kunin | "I-claim" equally natural |
| rebirth.button | Rebirth | kept English as the game term; "Mag-rebirth" is 11 of 10 |
| rebirth.confirm | Mag-rebirth na? Mawawala ang coins mo, pero makakakuha ka ng permanenteng {multiplier}x boost. | |
| coins.need_more | Kulang pa ng {amount} ang coins mo! | number placed where no noun follows; works for 1 |
| coins.count | Coins: {count} | avoids "1 Coins" and the linker |
| egg.hatched | Naka-hatch ka ng {rarity} {pet}! | "naka-" = got to, as in "nakakuha"; English names, so no linker; 34 with "Legendary Dragon" |
| rarity.legendary | Legendary | "Maalamat" is bookish and needs a linker |
| pet.name.dragon | Dragon | same word in Tagalog |
| chat.player_joined | Sumali si {player} sa laro | "si" before the name |
| trade.request | Inaaya ka ni {player} na mag-trade | "inaaya" = is inviting; 46 with a 20-character name |
| prompt.open_shop | Buksan gamit ang E | "open using E"; "gamit ang" as in Microsoft's samples. "Pindutin ang E para buksan" is 26 |
| pass.buy_price | Bilhin sa {price} Robux | "sa" marks the price; 22 of 22 at "10,000", so a 6-digit price overflows |
| pass.coins2x | 2x Coins | |
| pass.vip | VIP | |
| reward.daily_title | Daily Reward | "Araw-araw na Reward" is 19 |
| reward.come_back | Balik ka pagkalipas ng {time} para sa susunod na reward! | 57 with "12h 30m"; a spelled-out {time} overflows 60 |
| codes.placeholder | Ilagay ang code | Microsoft's verb for entering a key |
| codes.invalid | Mali o expired na ang code na ito. | "expired na" is everyday Taglish |
| social.like_reward | I-like ang game para sa libreng <b>Lucky Potion</b>! | item name kept English |
| social.group_reward | Sumali sa community namin para sa libreng reward! | Roblox's rename; "unlock" folded into "para sa" |
| afk.warning | AFK ka. Gumalaw para patuloy kang kumita! | period kept from the source |
| leaderboard.title | Top Players | kept as players say it; "Mga Nangunguna" (14) fits but reads formal |
| level.up | Level up! Level {level} ka na. | "Level up!" kept as a game shout; period kept from the source |
| tutorial.sell | Pumasok sa umiilaw na bilog para ibenta ang mga pet mo. | |
| inventory.full | Puno na ang backpack mo! Magbenta ng pet para lumuwag. | "lumuwag" = free up room |
| settings.music | Musika | |
| settings.on | On | "Bukas" also means tomorrow; "Naka-on" is 7 |
| loading | Naglo-load... | 13 of 14 |
| event.ends_in | Event: {time} na lang | "Matatapos ang event sa {time}" overflows 28 |
| item.op | Ang OP ng espadang ito! | exclamative "Ang ... ng ...!" |
| friends.boost | +{percent}% boost sa bawat kaibigan sa server mo | |

## Sources
1. Microsoft Localization Style Guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
2. Microsoft Filipino Localization Style Guide (ka/iyo, no po/opo, "paki-" samples, loanword hyphens, capitalization, numbers, punctuation, keys): https://download.microsoft.com/download/25b05cb0-c8ad-41f0-be2e-30335c6ceb6a/fil-fil-StyleGuide.pdf
3. Unicode CLDR language plural rules chart (fil): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR JSON, Filipino units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/fil/units.json
5. CLDR JSON, Filipino numbers: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/fil/numbers.json
6. Roblox language codes (Filipino, fil, fil-ph): https://create.roblox.com/docs/production/localization/language-codes
7. roblox.com in Filipino, 404 on 2026-11-08: https://www.roblox.com/fil/games/920587237/Adopt-Me
8. Roblox client CoreScript translations, header has no fil column (ExtraContent/translations/CoreScriptLocalization.csv, build version-f0ea5da9412f4e35): local file from the Roblox install
9. Roblox bundled fonts, cmap check for Ñ, accented vowels and U+20B1 (content/fonts, same build): local files from the Roblox install
10. Tagalog Wikipedia, Roblox ("laro", "manlalaro", Robux, developer, server kept): https://tl.wikipedia.org/wiki/Roblox
11. Wikipedia, Taglish (affixes on English roots, register): https://en.wikipedia.org/wiki/Taglish
12. Minecraft Java Edition fil_ph language file (purist examples "Pang-isahang-laro", "SIGE"/"HUWAG", "Naglo-load", "Si %s ay sumali sa laro"): local asset index 29
13. Google Play in Filipino ("Mga Laro", "Mga App"): https://play.google.com/store/apps/details?id=com.roblox.client&hl=fil
14. Roblox locale API (`fil_ph`: in-game content on, full experience and sign-up off; checked 2026-11-08): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
15. Roblox locale API, the 18 account languages (no fil): https://locale.roblox.com/v1/locales/supported-locales
16. Roblox Creator Hub, Localize with scripting (players switch language in the in-game Settings menu): https://create.roblox.com/docs/production/localization/localize-with-scripting
17. Roblox DevForum, in-experience language switcher lists the languages a game enables: https://devforum.roblox.com/t/localization-api-update-for-upcoming-in-experience-language-switcher/1974795
18. Roblox DevForum, Friends Are Back (2026-04-02): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
19. Wiktionary, Tagalog "itlog", "pisa", "astig", "bano" (senses and slang labels): https://en.wiktionary.org/wiki/itlog, https://en.wiktionary.org/wiki/pisa, https://en.wiktionary.org/wiki/astig, https://en.wiktionary.org/wiki/bano
20. Studio test 2026-11-08, TextService:GetTextBoundsAsync with Builder Sans on "Naglo-load", "Mag-rebirth" and phrases (wrap at spaces only): local measurement
