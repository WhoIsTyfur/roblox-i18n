# Dutch (nl-nl) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `nl-nl` (no bare `nl` column: Dutch has one Roblox locale, so Flemish nl-be players who choose Nederlands also read `nl-nl`) |
| Script, direction | Latin, LTR; accents é ë ï ö ü è; the digraph ij is two letters (capital IJ) |
| Address the player as | informal "je" (stressed "jij"/"jouw" only for emphasis); never "u"/"uw", never Flemish "ge"/"gij" |
| Text expansion vs English | +20-30% for sentences (Microsoft's Dutch average), short labels up to +50% ("Claim" -> "Ophalen") |
| Plural categories (CLDR) | one, other (one = exactly integer 1: "1 munt", "2 munten", "1,5 munten") |
| Model confidence | high -- high-resource language; the risks are u vs je, loanword spelling, adjective endings around placeholders, NL vs BE word choice |
| Native review before shipping | recommended -- Roblox does not auto-translate games into Dutch, so this column is all players get; ideally one reviewer from NL and one from Flanders |

## Audience and register
- Players are mostly 9-16, in the Netherlands and Flanders. Roblox's Dutch app and help talk to them with "je" ("Zo markeer je een plek als favoriet", "kun je ruilen"). Its legal and policy pages still say "u"; that is legal register, not the model.
- Microsoft's Dutch guide still defaults to "u" for adult software, but notes the shift toward "je", says the choice depends on product and audience, and allows a playful tone for games. For kids use "je" and never mix: "Koop nu uw pas" -> "Koop nu je pas".
- Unstressed "je" is the default subject and possessive: "Je hebt een nieuw level!", "je rugzak". Use "jij"/"jouw" only for contrast: "Jij bent aan de beurt!".
- Buttons, tabs, menu items: infinitive ("Spelen", "Kopen", "Ophalen", "Code invoeren"), as in Microsoft's "Updates zoeken...". Instructions and tutorials: imperative, which is the bare stem ("Druk op E", "Verkoop je pets", "Kom terug"). Never the -t form ("Koopt nu", "Drukt u op E"): it sounds old or formal.
- Hype is short and warm: "Gefeliciteerd!", "Top!", "Super!", "Goed gedaan!". One exclamation mark, no stacking. Nothing crude or adult.
- Dutch creators mix English loans in freely; a Dutch Roblox roleplay game writes "Join onze community voor de nieuwste codes, updates...". Keep the loans players use (pets, codes, boost, rebirth, VIP) but keep the grammar and the rest of the sentence Dutch.
- Flemish players read the same column, so avoid words that mark one side. NL-only: "gaaf", "lekker" (meaning nice), "doei", "hartstikke". BE-only: "plezant", "amai", "proficiat", "goesting". Neutral: "leuk", "tof", "cool", "Gefeliciteerd!". Spelling is one Taalunie standard for both.
- Stiff markers (Microsoft's avoid list) read like a letter from school: "tevens", "betreffende", "met ingang van", and "wordt"-passives: "Uw beloning wordt toegevoegd" -> "Je beloning is binnen!".

## Roblox and gaming vocabulary
| English | Dutch in game UI | Note |
|---|---|---|
| Robux | Robux | Invariant: "1 Robux", "100 Robux". Roblox help calls it Roblox's "virtuele betaalmiddel". |
| game pass | pas, plural passen ("VIP-pas") | Roblox help calls them "passen" ("Ervaringspassen"); one help article writes "game passes". Players say "gamepass" (unverified). |
| developer product | (name the item) | Roblox help: "ontwikkelaarsproducten". Players never see the word. |
| experience / game | game, plural games ("de game") | Roblox's platform UI says "ervaring"; in a game that sounds stiff. nl.wikipedia also writes "games" for Roblox games. |
| obby / tycoon / simulator | obby / tycoon / simulator | Plural "obby's" (nl.wikipedia), "tycoons", "simulators" (also "simulatoren"). |
| rebirth | rebirth, plural rebirths | "Een rebirth doen". "Wedergeboorte" is long and religious. Slang verb "rebirthen" exists (unverified); keep it out of UI. |
| pet | pet, plural pets | "Huisdier" means a real cat at home. Careful: Dutch "pet" also means cap; context (eggs, pet cards) makes it clear. |
| egg / hatch | ei, plural eieren / uitbroeden | The player "broedt een ei uit"; the pet "komt uit": "Je pet is uit het ei gekomen!". "Hatchen" is player slang (unverified). |
| coins / gems | munten / edelstenen | "Coins" is also understood. "Diamanten" fits a diamond-shaped icon (unverified as the common game word); pick one per game. |
| boost / multiplier | boost / (write "2x") | "de boost", plural "boosts". "Vermenigvuldiger" is a math-class word; use "2x". |
| XP / level up | XP / Nieuw level! | "het level", plural "levels" (nl.wiktionary). "Level omhoog!" is a calque. |
| quest | opdracht or quest | "Opdracht" is clearest for young players; "missie" also works. Don't mix them in one game. |
| leaderboard | klassement / Topspelers | Roblox's Dutch UI calls the in-game player list "Klassement". For a lobby board title, "Topspelers" or "Ranglijst". |
| AFK / noob / OP / VIP | AFK / noob / OP / VIP | Kept. Plurals "noobs", "VIP's". "Dit zwaard is OP!" |
| trade | ruilen, ruilverzoek | Roblox's Dutch UI: "Ruilen", "Items ruilen", "Bod doen", "Accepteren", "Afwijzen". Players also say "traden" (unverified); UI says "ruilen". Never "handelen". |
| inventory / backpack | inventaris / rugzak | Roblox help: "de inventaris van je account". |
| daily reward | dagelijkse beloning / dagelijkse bonus | "Dagelijkse beloning" is 19 characters; use "Dagelijkse bonus" in tight titles. |
| codes | codes; "Code invoeren", "Code verzilveren" | Roblox help uses "verzilveren" for redeeming codes ("Retailcodes"). |
| group | community, plural community's | Roblox renamed groups; Dutch help: "Een community vinden en er lid van worden", button "Lid worden van community". "Groep" still appears in old pages. |
| like / favorite | duim omhoog, liken / favoriet | Roblox help: "een duim omhoog of omlaag geven aan ervaringen", "als favoriet markeren". Kids say "liken" ("Like de game!"). |
| server | server, privéserver | "op de server", "op je server". Roblox help: "privéservers". |
| friends | vrienden | Roblox's Dutch help uses "vrienden", "vriendschapsverzoek", "vertrouwde vrienden" (Trusted Friends). "Verbindingen" appears only once ("verbindingslijst"); don't use it. |
| Premium | Premium | "Premium-lidmaatschap", "Premium-leden" (Roblox help). |
| shop | winkel | Default "Winkel". "Shop" is also Dutch; use it only if the game's art already says Shop. Roblox's avatar shop is "Marktplaats". |

## Grammar traps in UI strings
- **Plurals with {count}.** Roblox has no plural selection and "1 munten" is wrong. Safe patterns:
  - label + colon: "Munten: {count}"
  - put the noun first so the number stands alone: "Niet genoeg munten! Nog {amount} nodig."
  - words that never change after a number: "{price} Robux", "{hours} uur", "{n} keer" ("3 uur", "1 uur" are both right)

  Never "munt(en)". Bad: "Je hebt {count} munten" -> good: "Munten: {count}".
- **de/het and demonstratives change with the noun.** "de draak" but "het paard", "deze draak" but "dit paard". Never put de/het/deze/dit/die/dat before {pet} or {item}. "een" and "je/jouw" never change: "je {pet}", "een {pet}".
- **Adjective endings.** An adjective after "een" gets -e for de-words but not het-words: "een legendarische draak", "een legendarisch paard". {rarity} arrives as a bare label ("Legendarisch"), so "een {rarity} {pet}" is wrong half the time. Use "Uitgebroed: {pet} ({rarity})!". Fixed adjectives on fixed nouns do inflect: "een blijvende boost". "Gratis" never inflects: "een gratis beloning".
- **{player} has unknown gender.** Verbs don't mark gender, but pronouns do: "{player} heeft gewonnen! Hij..." -> repeat {player} or switch to "je". For possession use "van": "de pet van {player}", not "{player}'s pet" (the genitive spelling depends on the name's last letter: Anna's, Pieters, Max').
- **Word order.** Verb second in main clauses, last in subclauses and after "om ... te"; separable verbs split: "terugkomen" -> "Kom over {time} terug", "lid worden" -> "Word lid van onze community". Reorder freely; placeholders are named.
- **Time prepositions.** Future "in 3 hours" is "over 3 uur", not "in 3 uur": "Kom over {time} terug", "Event eindigt over {time}".
- **No comma needed before "om ... te"** in short sentences (unlike German): "Loop naar de cirkel om je pets te verkopen."
- **Compound nouns are one word:** "geluksdrankje", "muntboost", "topspelers", "dagbeloning". Hyphenate with a digit, acronym or single letter: "2x-boost", "VIP-pas", "XP-boost", "Premium-leden" (Roblox's spelling). Hyphenate a vowel clash (a-e, e-e, o-e, etc.): "mega-ei", "zee-egel"; but "drakenei" (n-e is no clash). A space inside a compound is the classic error: "VIP pas" -> "VIP-pas".
- **Plurals with an apostrophe.** Words ending in a single a, i, o, u or y take 's: "obby's", "community's", "lobby's", "emoji's"; acronyms too: "VIP's". Consonant endings take plain -s: "pets", "codes", "noobs", "boosts", "levels", "games" (never "pet's").
- **English verbs** take Dutch endings and past participles: "liken -> geliket", "updaten -> geüpdatet", "resetten -> gereset" (nl.wiktionary, following the Woordenlijst). Prefer a Dutch verb in UI when one fits: "ruilen", not "traden".
- **Capitalization.** Sentence case for titles and buttons: "Dagelijkse bonus", not "Dagelijkse Bonus". IJ is capitalized as a pair: "IJsdraak", "IJzeren zwaard", never "Ijsdraak". Lowercase after a colon when one sentence follows: "Let op: je rugzak is vol." Days and months are lowercase ("maandag", "juli").

## Typography and formatting
- No space before ! ? : ; and no inverted marks: "Nieuw level!", "Nu een rebirth doen?".
- Quotes: CLDR's Dutch default is single ‘...’, and Microsoft uses single quotes ('Winkel') and drops quotes around names and variables. In game UI use '...' or "..."; the low „...” style exists in Dutch print but is rare on screens (unverified) and looks German.
- Numbers: 1.250 for thousands, 1,5 for decimals (CLDR nl), same in NL and BE. Game code fills {count} and {multiplier}; flag English-formatted values ("1,250", "1.5x") for the developer to format by the player's LocaleId.
- Percent: no space, "+10%" (CLDR nl pattern and Microsoft's "12%"). This differs from German and French.
- Durations: CLDR short forms are "3 uur 20 min", "2 dagen 5 uur", "45 sec"; narrow forms are "3 u 20 m", "2 d 5 u", "45 s". Use short forms where they fit, narrow in tight HUDs; the unspaced "3u 20m" is also common in games (unverified). "u" for uur is standard in NL and BE. English "3h 20m" is understood but looks untranslated.
- Ellipsis: three periods, no space: "Laden...". Microsoft pattern for progress text: infinitive plus dots ("Updates zoeken...").
- Dashes: Microsoft Dutch uses no en or em dash. Replace with a comma, colon, parentheses or a new sentence.
- Keys: capital letter, no quotes: "Druk op E". Combinations with plus: "Shift+E". Belgian players often type on AZERTY. Roblox KeyCodes are QWERTY positions, so E is safe (same spot), but "Druk op Q" or "WASD" points at the wrong keys for them. Let code fill a {key} from UserInputService:GetStringForKeyCode, which returns the layout's real key.
- Multipliers: "2x", "x2", "1,5x". Keep ASCII "x".

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, noob, obby, tycoon, simulator, rebirth, XP, boost.
- Game titles stay English: "Pet Hatch Tycoon". Dutch creators also keep English titles and words ("Albert Heijn Roleplay", "Redeem codes").
- Promo codes and examples (FREEPETS), usernames, display names, {player}, keybinds, emoji from the source.
- Translate in-game item, pet and rarity names, and keep each one identical everywhere: "Lucky Potion" -> "Geluksdrankje", "Dragon" -> "Draak". A diminutive (-je, -tje) often sounds friendlier for small items: "drankje", "eitje".
- Suggested rarity ladder (unverified as community standard): Gewoon, Ongewoon, Zeldzaam, Episch, Legendarisch, Mythisch.
- Script: Latin only. Write ij as the two letters i + j, never the ligature character ĳ/Ĳ (U+0133/U+0132): it breaks search and may be missing from fonts.

## Rendering on Roblox
- Dutch needs only Latin-1 letters (é ë ï ö ü è á). Glyph check (2026-11-08) of the 66 Latin font files in the local Roblox client (`content/fonts`), from Builder Sans, Montserrat and Source Sans to Fredoka One, Luckiest Guy and Press Start 2P: every one has é ë ï ö ü è á and É Ë Ï Ö Ü. Uploaded custom fonts are unverified: check ë, ï and é in each.
- Luau `string.upper` only changes ASCII letters, so "ideeën" becomes "IDEEëN". Write uppercase text directly in the table ("IDEEËN") or use a UTF-8-aware helper. Keep the accents on capitals (Microsoft: "BELGIË", "GEÏNTEGREERD").
- TextWrapped prefers spaces, but a word wider than the box is split mid-word with no hyphen (Roblox docs), so "geluksdrankje" can show as "geluksdrank / je"; with TextScaled the whole label shrinks instead. Choose shorter words in narrow buttons (max 8-10).
- Diaeresis dots on capitals (Ë, Ï) sit high; in tight TextScaled frames check they aren't clipped (unverified, rare in UI).
- Verify in Studio: set the test locale to nl-nl, open every panel, check the longest strings (rebirth confirm, tutorial, inventory full) and the shortest buttons; "Druk op E om te openen" fills the prompt's 22 exactly.

## Mistakes machine translation makes here
- Formal register: "Voert u de code in" -> "Code invoeren"; "Koop nu uw VIP-pas" -> "Koop nu je VIP-pas".
- Stressed pronouns everywhere: "Jij hebt jouw munten verloren" -> "Je bent je munten kwijt".
- Wrong verb for Claim: "Opeisen" / "Beweren" -> "Ophalen".
- "Free" read as unoccupied: "Vrije beloning" -> "Gratis beloning".
- Trade as commerce: "Handelen met {player}" -> "Ruilen met {player}".
- English "in" for future time: "Kom terug in {time}" -> "Kom over {time} terug".
- Over-translated gaming words: "Wedergeboorte" -> "Rebirth"; "huisdieren" -> "pets"; "vermenigvuldiger" -> "2x"; in-game "ervaring" -> "game".
- Adjective before an inserted noun: "Je hebt een Legendarisch Draak uitgebroed!" -> "Uitgebroed: {pet} ({rarity})!".
- Split compounds and wrong hyphens: "VIP pas", "Munt Boost", "Top Spelers" -> "VIP-pas", "muntboost", "Topspelers".
- English Title Case: "Dagelijkse Beloning Ophalen" -> "Dagelijkse beloning ophalen".
- Wrong plurals: "obbys", "pet's", "code's" -> "obby's", "pets", "codes".
- Calques and false friends: "Level omhoog!" -> "Nieuw level!"; "eventueel" means possibly, not eventually ("uiteindelijk"); "actueel" means current, not actual ("echt").
- Regional words: "Proficiat!" or "Gaaf!" -> "Gefeliciteerd!" / "Top!".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Spelen | Infinitive button. |
| shop.title | Winkel | Settled default; "Shop" only if the game's art already says Shop. |
| shop.buy | Kopen | |
| reward.claim | Ophalen | Plain Dutch every kid reads; not "Opeisen". "Claimen" is spoken slang, keep it out of buttons. |
| rebirth.button | Rebirth | Kept English. |
| rebirth.confirm | Nu een rebirth doen? Je verliest je munten, maar krijgt een blijvende {multiplier}x-boost. | Hyphen joins digit and noun; game code should send "1,5", not "1.5". |
| coins.need_more | Niet genoeg munten! Nog {amount} nodig. | Rebuilt so {amount} = 1 stays correct. |
| coins.count | Munten: {count} | Label pattern avoids "1 munten"; count formatted "1.250". |
| egg.hatched | Uitgebroed: {pet} ({rarity})! | Avoids de/het and the adjective ending; params reordered. |
| rarity.legendary | Legendarisch | 12/12. Bare form for tags. |
| pet.name.dragon | Draak | de-word ("de draak"); never insert after de/het. |
| chat.player_joined | {player} speelt nu mee | Natural "joined", no gender, no article. Minecraft's Dutch uses "kwam het spel binnen"; "{player} is de game binnengekomen" is the longer alternative. |
| trade.request | {player} wil met je ruilen | "ruilen" as in Roblox's Dutch UI. |
| prompt.open_shop | Druk op E om te openen | 22/22. E kept; same key on AZERTY. |
| pass.buy_price | Kopen voor {price} Robux | 22 at price "1.000"; for 5-digit prices use "Kopen: {price} Robux" (19). |
| pass.coins2x | 2x munten | Sentence case. |
| pass.vip | VIP | Kept. |
| reward.daily_title | Dagelijkse bonus | "Dagelijkse beloning" is 19, over the max of 18; "bonus" is a natural game word, so the max can stay. |
| reward.come_back | Kom over {time} terug voor je volgende beloning! | "over", not "in"; time like "3 uur 20 min" or "3 u 20 m". |
| codes.placeholder | Code invoeren | |
| codes.invalid | Deze code is ongeldig of verlopen. | |
| social.like_reward | Like de game voor een gratis <b>Geluksdrankje</b>! | 43. Kept: "liken" is how players say it. Roblox's own "duim omhoog" version, "Geef een duim omhoog voor een gratis <b>Geluksdrankje</b>!" (51), also fits. |
| social.group_reward | Word lid van onze community voor een gratis beloning! | "community" per Roblox's rename of groups; 53/55. |
| afk.warning | Je bent AFK. Beweeg om te blijven verdienen! | 44/45. |
| leaderboard.title | Topspelers | One word; gender-neutral generic "spelers". |
| level.up | Nieuw level! Je bent nu level {level}. | Not "Level omhoog!". |
| tutorial.sell | Stap in de lichtgevende cirkel om je pets te verkopen. | "Stap in" keeps "into" ("Loop naar" is only "to"). "lichtgevend", not "gloeiend" (red-hot). No comma before "om". |
| inventory.full | Je rugzak is vol! Verkoop pets om ruimte te maken. | |
| settings.music | Muziek | |
| settings.on | Aan | Pair with "Uit". |
| loading | Laden... | Microsoft progress pattern. |
| event.ends_in | Event eindigt over {time} | "het event" (nl.wiktionary); 26 with "2 d 5 u". |
| item.op | Dit zwaard is OP! | "het zwaard" -> "dit". |
| friends.boost | +{percent}% boost voor elke vriend op je server | No space before %; "op je server". Generic "vriend" covers girls too, like Roblox's "vrienden". |

## Sources
1. Microsoft Dutch localization style guide (nld-nld, PDF): https://aka.ms/dutch-styleguide
2. CLDR plural rules, Dutch: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON, nl numbers (separators, percent pattern): https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-numbers-full/main/nl/numbers.json
4. CLDR JSON, nl units (duration short and narrow forms): https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-units-full/main/nl/units.json
5. Roblox locale API (nl_nl enabled for the full Roblox experience): https://locale.roblox.com/v1/locales
6. Roblox Help (nl), auto-translation language list without Dutch: https://en.help.roblox.com/hc/nl/articles/40269095851284
7. Roblox Help (nl), "Manieren om Robux te krijgen": https://en.help.roblox.com/hc/nl/articles/203313200
8. Roblox Help (nl), "Ruilen op Roblox" (trade UI labels): https://en.help.roblox.com/hc/nl/articles/203313310
9. Roblox Help (nl), "Klassementen en meldingen binnen een ervaring": https://en.help.roblox.com/hc/nl/articles/204343250
10. Roblox Help (nl), "Een community vinden en er lid van worden": https://en.help.roblox.com/hc/nl/articles/203313490
11. Roblox Help (nl), "Vrienden maken" and trusted friends: https://en.help.roblox.com/hc/nl/articles/203313580
12. Roblox Help (nl), "Ervaringspassen": https://en.help.roblox.com/hc/nl/articles/203314040
13. Roblox Help (nl), favorites and thumbs-up wording: https://en.help.roblox.com/hc/nl/articles/203313670 and https://en.help.roblox.com/hc/nl/articles/45600166055188
14. Roblox Help (nl), "Retailcodes" (verzilveren): https://en.help.roblox.com/hc/nl/articles/49188142080788
15. Dutch Wikipedia, Roblox (games, obby's): https://nl.wikipedia.org/wiki/Roblox
16. Roblox games API, Dutch creator description of "Albert Heijn RP": https://games.roblox.com/v1/games?universeIds=7024648158
17. Roblox Creator docs, UserInputService:GetStringForKeyCode (AZERTY): https://create.roblox.com/docs/reference/engine/classes/UserInputService
18. Roblox client chat localization (no Dutch strings): https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/scripts/CoreScripts/Modules/Server/ServerChat/DefaultChatLocalization.lua
19. Roblox Creator docs, TextLabel.TextWrapped (long words split mid-word): https://create.roblox.com/docs/reference/engine/classes/TextLabel
20. CLDR JSON, nl delimiters (quotation marks): https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-misc-full/main/nl/delimiters.json
21. nl.wiktionary, "level", "event", "liken", "updaten", "resetten", "community" (gender, plurals, verb forms): https://nl.wiktionary.org/wiki/level
22. Minecraft Java nl_nl language file (join message wording): https://github.com/InventivetalentDev/minecraft-assets/blob/1.21.4/assets/minecraft/lang/nl_nl.json
