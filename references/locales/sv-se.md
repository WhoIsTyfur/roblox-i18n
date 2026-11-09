# Swedish (sv-se) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `sv-se`. It is Roblox's only Swedish locale, so no bare `sv` column is needed; Swedish speakers in Finland who pick Swedish read this column too |
| Script, direction | Latin, LTR; extra letters å ä ö Å Ä Ö (é in a few loans: "idé", "armé") |
| Address the player as | informal singular "du" (dig, din/ditt/dina); never "Ni", never generic "man" |
| Text expansion vs English | about +9% over the reference set below (measured); short buttons often shrink ("Buy" -> "Köp"), but compounds grow ("Settings" -> "Inställningar") and cannot wrap |
| Plural categories (CLDR) | cardinal one, other (one = exactly 1: "1 diamant", "0 diamanter", "1,5 diamanter"); ordinal one (1:a, 2:a, 21:a, 22:a) and other (3:e, 11:e, 12:e) |
| Model confidence | high -- well-resourced language; the risks are Norwegian/Danish leaks, split compounds, English Title Case, stiff office words and unverified player slang |
| Native review before shipping | recommended |

## Audience and register
- Roblox is big with Swedish kids: a 2022 Swedish survey cited by Swedish Wikipedia found that just over 6 in 10 internet users born in the 2010s had used it in the past year, and nearly 3 in 10 daily. Write for a 10-year-old reader.
- Roblox has no Swedish app UI: its locale API enables `sv_se` for in-experience content only, and Roblox does not auto-translate Swedish. Every Swedish word a player sees in your game comes from your table. Platform words come from Roblox's Swedish store listing and legal terms ("spel", "vänner", "grupp", "Robux").
- Use "du". Microsoft's Swedish guide talks to the user directly and in everyday words. Avoid office words: "erhålla" -> "få", "ha möjlighet att" -> "kan", "Vänligen ange koden" -> "Ange kod".
- Buttons and instructions use the imperative. For -a verbs it equals the infinitive ("Spela", "Hämta", "Öppna", "Samla"); for -er verbs drop the final -a: "köpa" -> "Köp", "sälja" -> "Sälj", "trycka" -> "Tryck", "byta" -> "Byt", "kläcka" -> "Kläck", "välja" -> "Välj". "Köpa"/"Sälja" on a button is wrong.
- Put the imperative first. Microsoft marks a fronted "För att ..." or "Om ..." clause before an imperative as wrong: "För att sälja, gå in i cirkeln" -> "Gå in i cirkeln för att sälja".
- Questions that ask for a decision are full sentences, not fragments (Microsoft): "Rebirth nu?" -> "Vill du göra en rebirth nu?".
- Microsoft trims possessives Swedish does not need ("Give your PC a name" -> "Ge datorn ett namn"): "Ryggsäcken är full" reads more natural than "Din ryggsäck är full". Keep "dina" where it marks ownership ("Sälj dina husdjur"). Use "vi" sparingly.
- Hype is short and plain: "Ny nivå!", "Grattis!", "Snyggt!", "Grymt!", "Wow!". Avoid "Vänligen", stacked "!!!", and slang parents dislike ("fett", "skit-" prefixes). Gamer loans kids use are fine in flavor text ("OP", "AFK", "noob").
- Write standard Sweden Swedish. Finland-Swedish players understand it; no Finland-Swedish forms and no regional slang.

## Roblox and gaming vocabulary
| English | Swedish in game UI | Note |
|---|---|---|
| Robux | Robux | Invariant: "1 Robux", "100 Robux". Roblox's Swedish terms: "dina Robux", "Robux-bonusbelopp", and "Roblox spelvaluta" (no genitive s after x). |
| game pass | spelpass (ett spelpass, spelpasset, spelpass, spelpassen) | Roblox's Swedish terms say "spelpass". Players may write "gamepass" (unverified). |
| developer product | (name the item) | Roblox's terms say "utvecklarprodukter"; creator jargon players never need. |
| experience / game | spel (ett spel, spelet, spel, spelen) | Roblox's Swedish terms and store listing say "spel"; the listing mixes in "upplevelser", but "spel" dominates. Use "spel". |
| obby / tycoon / simulator | obby / tycoon / simulator | Genre names stay ("en obby, obbyn"). Roblox's listing says "simulatorer" and "magnatspel" for tycoons; players say "tycoon" (unverified). |
| rebirth | Rebirth (button), "rebirth" in text | Kept as a genre mechanic (unverified that Swedish players say it). "Återfödelse" is 11 characters and stiff. Use noun phrases: "Gör en rebirth", not a verb "rebirtha". |
| pet | husdjur (ett husdjur, husdjuret, husdjur, husdjuren) | Invariant plural: "1 husdjur", "5 husdjur". Players also say "pets" (unverified). |
| egg / hatch | ägg (invariant plural) / kläcka | Minecraft's Swedish: "Sköldpaddsägg kläcks". Button "Kläck", toast "Ägget kläcks...". |
| coins / gems | mynt (ett mynt, invariant plural) / diamanter or ädelstenar | "mynt" never changes: "1 mynt", "1 250 mynt". Pick one gem word per game (unverified which kids prefer). |
| boost / multiplier | boost (en boost, boosten) / "2x" | Swedish Wiktionary lists "boosta" as gaming slang. Keep "boost" for multipliers and save "bonus" for one-off extras, so the two never blur. Show multipliers as "2x", never "multiplikator". |
| XP / level up | XP / "Ny nivå!", "nivå 5" | Minecraft's Swedish: "erfarenhetsnivå", "erfarenhetspoäng". Kids say "levla" (Wiktionary: gaming slang); fine in chatty flavor text, not system UI. |
| grind | grinda / grindning | Swedish Wikipedia's article is "Grindning". |
| quest | uppdrag (ett uppdrag, invariant plural) | |
| leaderboard | topplista / Toppspelare | One closed word each. |
| AFK / noob / OP | AFK / noob / OP | Wiktionary has "noob" (plural "noobs"). "Du är AFK", "Svärdet är OP". |
| VIP | VIP | "VIP-pass", "VIP-området". |
| trade | byta (verb), byte (noun), byteshandel | Roblox's terms and Minecraft's Swedish use "byteshandel", "Byteshandla". Button "Byt". "handla" alone means to shop. |
| inventory / backpack | ryggsäck / förråd | Minecraft's Swedish inventory is "Förråd". "inventarier" means fixtures and furniture. |
| daily reward | daglig belöning | Two words, lowercase "b". |
| codes | koder (en kod, koden) / "Ange kod", "Lös in" | Roblox's gift card terms say credits "lösas in". |
| group | grupp (gruppen, grupper) | Roblox's Swedish listing says "Gå med i en grupp"; its terms write "grupp/community". The English UI's "Communities" is not needed. |
| like / favorite | gilla / favorit, "Lägg till i favoriter" | "Gilla" is the standard Swedish social-media verb (unverified for Roblox, which has no Swedish UI). |
| server | server (servern, servrar) | Plural "servrar", not "servers". Minecraft: "Ansluter till servern...". |
| friends | vänner (en vän, vännen, vänner, vännerna) | Roblox's Swedish listing says "vänner"; Minecraft has "vänlista", "vänförfrågan". Roblox renamed Connections back to Friends on 2026-04-02. Never "anslutningar" or "kontakter". |
| Premium / Roblox Plus | Premium / Roblox Plus | Brand names, never translated. Roblox Plus replaced new Premium sign-ups from April 30, 2026 (Roblox newsroom); the Swedish listing advertises "Roblox Plus", while the gift card terms still say "premiumabonnemang". |
| potion | brygd (en brygd, brygder) | Roblox's terms list "brygder" as a developer product; Minecraft's Potion of Luck is "Turbrygd". |
| shop / chat | butik (butiken) / chatt, chatta | Roblox's listing: "Chatta". |

## Grammar traps in UI strings
- **Plurals with {count}.** One = exactly 1. Safe patterns:
  - invariant nouns: mynt, husdjur, ägg, svärd, uppdrag, spelpass, poäng, Robux. "{count} mynt" is right for 0, 1 and 1 250.
  - label + colon for other nouns: "Diamanter: {count}" (not "{count} diamanter", which breaks at 1).
  - no adjective before a counted noun: "{count} nya husdjur" gives "1 nya husdjur" (needs "1 nytt husdjur"). Write "Nya husdjur: {count}".
- **en/ett gender.** The noun's gender picks the article and adjective form: "en ny drake" but "ett nytt ägg"; "legendarisk drake" but "legendariskt ägg"; "din drake", "ditt ägg", "dina husdjur". "varje" never changes: "varje vän", "varje ägg".
- **Inserted nouns.** Never put an article or adjective before {pet} or {item}: "en {pet}" fails for neuter pets ("ett lejon"), and "{rarity} {pet}" cannot agree. Never glue an ending to a placeholder ("{pet}en"). Use a colon or parentheses: "Nytt husdjur: {pet} ({rarity})!".
- **{player} has unknown gender.** Verbs don't change; never refer back with "han" or "hon". Microsoft notes "hen" is accepted, but repeating {player} or switching to "du" is safer for kids: "{player} vill byta med dig".
- **Genitive.** No English apostrophe (Microsoft). Names add -s ("Annas husdjur"), but names ending in s, x or z add nothing ("Roblox spelvaluta"), so "{player}s" fails for "Lucas". Rephrase: "{player} har en drake", "Draken tillhör {player}".
- **Acronyms and digits in compounds** take a hyphen (Microsoft): "VIP-pass", "XP-boost", "Robux-pris", "Roblox-konto", "2x-boost". Inflected acronyms take a colon: "VIP:en", "XP:n"; rephrase when it looks odd.
- **Ordinals:** colon + a/e per CLDR: "1:a plats", "2:a", "3:e", "11:e", "21:a". For {rank} use "Plats {rank}", which needs no suffix.
- **Verb second.** A fronted word pushes the subject behind the verb: "Nu är du på nivå 5", not "Nu du är". In subclauses "inte" goes before the verb: "om du inte rör dig"; in main clauses after it: "du rör dig inte".
- **Double definiteness.** Adjective + definite noun takes den/det/de and the suffix: "den lysande cirkeln", "det nya ägget", not "den lysande cirkel" (Danish).
- **"fler" vs "mer".** Countable nouns take "fler": "fler mynt", "fler husdjur"; "mer" only for mass nouns ("mer plats", "mer XP"). "mer mynt" is a typical error.
- **Time prepositions.** "om" for a point ahead ("om 3 tim"), "i" for a span ("i 3 timmar"): "Eventet slutar om {time}", never "i {time}".
- **Compounds are closed.** Splitting them (särskrivning) is the most visible Swedish error: "topp spelare" -> "toppspelare", "husdjurs butik" -> "husdjursbutik". Watch the linking -s: "husdjursbutik", "uppdragslista".
- **Capitalization.** Microsoft: lowercase everything but names and the first word; never copy English Title Case. "Daglig belöning", not "Daglig Belöning". Weekdays, months and languages are lowercase ("måndag", "svenska"). Item and pet names: first letter only ("Turbrygd", "Gyllene drake").
- **Commas.** No serial (Oxford) comma: "mynt, diamanter och husdjur". Microsoft puts a comma between main clauses unless they are very short: "Du förlorar dina mynt, men du får en boost."

## Typography and formatting
- No space before ! ? : ; ("Ny nivå!", "Mynt: 1 250").
- Quotes are ”...” with the same closing mark (U+201D) on both sides (CLDR); inner ’...’. Microsoft also accepts straight "...". Never English “...” or „...“ or «...». Microsoft writes UI element names without quotes: "Tryck på Hämta".
- Numbers: space as thousands separator (CLDR uses U+00A0), decimal comma: "1 250", "1,5". Game code formats numbers, so flag English values ("1,250", "1.5x") for the developer to format by LocaleId. A plain space is fine if U+00A0 renders oddly (unverified per font).
- Percent: space before % (CLDR; Roblox's Swedish listing writes "20 % rabatt"): "+10 % boost".
- Minus: CLDR's Swedish minus is U+2212; in game text a hyphen "-5" is safer (unverified that every Roblox font has U+2212).
- Durations: CLDR short forms "2 d 5 tim", "3 tim 20 min", "45 s"; narrow "2d 5h", "3h 20m" (same as English). Long forms: "3 timmar", "20 minuter"; kids say "2 dagar" (CLDR's long "dygn" sounds formal).
- Time of day uses 24 hours: "18:00" (CLDR) or "kl. 18.00". Dates: "8 november 2026" or "2026-11-08".
- Abbreviations take periods ("t.ex.", "m.m.", "kl."); unit symbols don't ("min", "tim", "s").
- Ellipsis: three periods or "…". In UI Microsoft puts no space before it (the spaced "Vänta …" is for running documentation text); Minecraft's Swedish writes "Läser in vänlista..." the same way. Pick one character per game.
- Dashes: Microsoft says Swedish has no em dash. Use a spaced en dash " – " sparingly, unspaced in ranges ("1–10").
- Keys: keep the key as printed ("E", "Q", "F"). Minecraft writes "Tryck på %s"; "Tryck E" is the short spoken form for tight prompts. Space -> "Mellanslag" (Minecraft; Microsoft says "Blanksteg"), Enter -> "Retur", Shift -> "Skift", Tab -> "Tabb".
- Multipliers: ASCII "x" glued to the number: "2x mynt", "1,5x".

## Do not translate / keep as is
- Roblox, Robux, Premium, Roblox Plus, VIP, AFK, OP, noob, obby, tycoon.
- Game titles stay English ("Pet Hatch Tycoon"). Promo codes (FREEPETS), usernames, display names, {player}, keybinds and emoji too.
- Translate item, pet and rarity names, and use each the same way everywhere ("Lucky Potion" -> "Turbrygd", "Legendary" -> "Legendarisk").
- Never write å ä ö as aa, ae, oe or plain a/o: "här" = here but "har" = has; "får" = gets but "far" = father.
- Never use Norwegian or Danish letters: ø and æ are not Swedish ("Køb", "Kjøp" -> "Köp").

## Rendering on Roblox
- å ä ö Å Ä Ö é sit in Latin-1 Supplement, the same block as German ä ö ü, which Roblox renders in its own UI. Builder Sans, Montserrat (Gotham's replacement), Arimo (Arial's) and Source Sans should cover them, but Roblox publishes no glyph lists (unverified per font). Decorative and pixel fonts are the real risk.
- Luau `string.upper` and `string.lower` change only ASCII: "nivå" becomes "NIVå". Write capitals directly in the table ("NY NIVÅ!") or use a UTF-8-aware helper.
- Each of å ä ö is 2 bytes: truncating with `string.sub` or counting with `#` can split a letter into a broken glyph; use `utf8.len` and `utf8.offset`.
- TextWrapped breaks at spaces, so compounds ("husdjursbutiken", "erfarenhetspoäng") cannot wrap, and TextScaled shrinks the whole label instead. Whether Roblox splits a word wider than its label, or breaks after a hyphen, is unverified. Keep narrow buttons to short words.
- The ring on Å and the dots on Ä Ö reach above cap height: check for clipping in tight TextScaled frames (unverified).
- Verify in Studio: set the test locale to `sv-se`, put "ÅÄÖ åäö ”” – é 1 250 20 %" in a TextLabel in every font the game uses, then open the longest strings (rebirth confirm, tutorial, group banner) and the 8-10 character buttons at phone size.

## Mistakes machine translation makes here
- Norwegian or Danish bleed: "Kjøp" / "Køb" -> "Köp"; "Spill" (Swedish "spill" = spillage) -> "Spela"; "ikke" -> "inte"; "hvad" -> "vad".
- Infinitive buttons: "Köpa", "Sälja", "Kläcka" -> "Köp", "Sälj", "Kläck".
- Split compounds and Title Case: "Topp Spelare", "Daglig Belöning" -> "Toppspelare", "Daglig belöning".
- Stiff register: "Vänligen ange koden", "Du kan erhålla" -> "Ange kod", "Du kan få".
- Claim as "Kräv" or "Gör anspråk på" (a legal claim) -> "Hämta".
- Fronted purpose clause: "För att sälja, gå in i cirkeln" -> "Gå in i cirkeln för att sälja".
- "i" for a future point and "mer" with countables: "Kom tillbaka i 3 timmar", "mer mynt" -> "Kom tillbaka om 3 tim", "fler mynt".
- Calques: "Level upp!" -> "Ny nivå!"; "Tur dryck" -> "Turbrygd"; "Spelet tillåter dig att ..." -> "I spelet kan du ...".
- False friends: "eventuellt" means possibly, not eventually ("till slut"); "aktuell" means current, not actual; "inventarier" (fixtures) -> "ryggsäck"; "handla" (shop) for trade -> "byta".
- Gender and agreement slips: "en legendarisk ägg", "ett ny husdjur", "1 nya husdjur" -> "ett legendariskt ägg", "ett nytt husdjur", "Nya husdjur: 1".
- English genitive and number format: "{player}'s husdjur", "1,250 mynt", "1.5x" -> "{player} har ett husdjur", "1 250 mynt", "1,5x".
- Over-translated platform words: "upplevelse" for a game -> "spel"; "anslutningar" -> "vänner"; "överkraftig" -> "OP".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Spela | Imperative (= infinitive for -a verbs). |
| shop.title | Butik | |
| shop.buy | Köp | Imperative, not "Köpa". |
| reward.claim | Hämta | Not "Kräv". |
| rebirth.button | Rebirth | Genre term kept; "Återfödelse" (11) is over the limit and stiff. |
| rebirth.confirm | Vill du göra en rebirth nu? Du förlorar dina mynt, men du får en permanent {multiplier}x-boost. | Full question for a decision (Microsoft); hyphen after the number. 86/110 with "1,5". Code should send "1,5", not "1.5". |
| coins.need_more | Du behöver {amount} mynt till! | Invariant "mynt" keeps {amount} = 1 correct; "till" = more. 27/40 with "1 250". |
| coins.count | {count} mynt | Invariant noun, so no label pattern needed; lowercase. Count should arrive as "1 250". |
| egg.hatched | Nytt husdjur: {pet} ({rarity})! | Avoids article and adjective agreement; "Nytt" matches neuter "husdjur". 34/40 with Drake/Legendarisk. |
| rarity.legendary | Legendarisk | 11/12. Base form for a tag; "legendariskt" only before an ett-noun. |
| pet.name.dragon | Drake | Common gender (en drake, draken), as in Minecraft's "Enderdrake". |
| chat.player_joined | {player} gick med i spelet | Minecraft says "anslöt sig till spelet"; "gick med i" is friendlier and matches Roblox's "Gå med i". |
| trade.request | {player} vill byta med dig | |
| prompt.open_shop | Tryck E för att öppna | 21/22; the standard "Tryck på E för att öppna" is 24. |
| pass.buy_price | Köp för {price} Robux | 19/22 with "1 000". |
| pass.coins2x | 2x mynt | "Dubbla mynt" (11) also fits. |
| pass.vip | VIP | Kept. |
| reward.daily_title | Daglig belöning | 15/18, sentence case. |
| reward.come_back | Kom tillbaka om {time} för nästa belöning! | "om" for a time ahead; 48/60 with "3 tim 20 min". |
| codes.placeholder | Ange kod | Microsoft's verb for "Enter"; "Skriv in kod" (12) is the chattier option. |
| codes.invalid | Koden är ogiltig eller har gått ut. | |
| social.like_reward | Gilla spelet och få en gratis <b>Turbrygd</b>! | "Turbrygd" is Minecraft's Swedish Potion of Luck; common gender, so "en gratis". 39/55 without tags. |
| social.group_reward | Gå med i vår grupp och lås upp en gratis belöning! | 50/55. "grupp", as in Roblox's Swedish listing. |
| afk.warning | Du är AFK! Rör dig för att fortsätta tjäna! | 43/45. |
| leaderboard.title | Toppspelare | Closed compound; "Topplista" also works. |
| level.up | Ny nivå! Nu är du på nivå {level}. | Verb second after "Nu". |
| tutorial.sell | Gå in i den lysande cirkeln för att sälja dina husdjur. | Imperative first; double definiteness. 55/70. |
| inventory.full | Ryggsäcken är full! Sälj husdjur för att få plats. | Definite noun instead of "Din"; invariant "husdjur". 50/60. |
| settings.music | Musik | |
| settings.on | På | Pair with "Av" (Minecraft: PÅ/AV). |
| loading | Laddar... | The everyday word kids use; "Läser in..." (Minecraft's "Läser in terräng...") is correct but more formal. No space before "...". |
| event.ends_in | Eventet slutar om {time} | "event" (ett event) is common gamer Swedish; "evenemang" is formal. 27/28 with CLDR short "2 d 5 tim", 23 with narrow "2d 5h" (identical to English). Two-digit days ("12 d 23 tim") overflow; then use "Slutar om {time}". |
| item.op | Det här svärdet är OP! | "Det här" is the everyday form; "Detta svärd" reads formal. |
| friends.boost | +{percent} % boost för varje vän på servern | Space before %; "varje" has one form; "servern" without "din". 36/60. |

## Sources
1. Microsoft Swedish localization style guide (PDF): https://aka.ms/swedish-styleguide
2. Microsoft localization style guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. CLDR plural rules (sv, cardinal and ordinal): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR JSON, sv numbers, duration units and quotation delimiters: https://github.com/unicode-org/cldr-json/tree/main/cldr-json
5. Roblox locale API (sv_se enabled for in-experience content, not the full app): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
6. Roblox Creator Hub, Language codes (Swedish row, sv / sv-se): https://create.roblox.com/docs/production/localization/language-codes
7. Roblox Help Center locale list (sv, sv-se present): https://en.help.roblox.com/api/v2/help_center/locales.json
8. Roblox Help (sv), Terms of Use for the EEA, UK and Switzerland (spel, spelpass, utvecklarprodukter, brygder, grupp/community, byteshandel): https://en.help.roblox.com/hc/sv/articles/52986395990932
9. Roblox Help (sv), Swedish gift card and credit terms (Roblox spelvaluta, Robux-bonusbelopp, premiumabonnemang, lösas in): https://en.help.roblox.com/hc/sv/articles/17138427757204
10. Google Play Sweden, Roblox listing in Swedish (spel, upplevelser, vänner, grupp, simulatorer, magnatspel, Roblox Plus, "20 % rabatt"): https://play.google.com/store/apps/details?id=com.roblox.client&hl=sv&gl=SE
11. Swedish Wikipedia, Roblox (spel, spelskapare, 2022 survey of Swedish users): https://sv.wikipedia.org/wiki/Roblox
12. Minecraft Java Edition 26.3 lang file sv_se.json (anslöt sig till spelet, Förråd, Turbrygd, Byteshandla, PÅ/AV, Retur, Mellanslag), via Mojang's asset index: https://piston-meta.mojang.com/mc/game/version_manifest_v2.json
13. Swedish Wiktionary, "levla", "noob", "boosta": https://sv.wiktionary.org/wiki/levla
14. Swedish Wikipedia, Grindning: https://sv.wikipedia.org/wiki/Grindning
15. DevForum, Introducing Builder font (Gotham -> Montserrat, Arial -> Arimo; no glyph list): https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222
16. Roblox newsroom, Connections back to Friends (2026-04-02): https://about.roblox.com/newsroom/2026/04/expanding-trusted-friends
17. Roblox newsroom, Introducing Roblox Plus (new Premium sign-ups end from 2026-04-30): https://about.roblox.com/newsroom/2026/04/introducing-roblox-plus-subscription
