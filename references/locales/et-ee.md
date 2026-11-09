# Estonian (et-ee) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `et-ee` (the only Estonian locale; no bare `et` column needed) |
| Script, direction | Latin with õ ä ö ü (and š ž in loanwords), LTR |
| Address the player as | informal singular "sina", usually dropped into the verb ("Oled AFK", "Osta", "Tule tagasi"); never plural/formal "teie" |
| Text expansion vs English | about +5-15% on sentences (measured on the reference set); short buttons and titles +40-100% ("Claim" -> "Võta vastu", "On" -> "Sees") |
| Plural categories (CLDR) | one (i = 1 and v = 0: "1 münt"), other ("0 münti", "2 münti", "1,5 münti"); ordinals: other only, written "5." |
| Model confidence | medium -- short strings come out fluent, but models break numeral agreement, split compounds and slip into the formal "teie" register |
| Native review before shipping | strongly recommended |

## Audience and register
Estonian is spoken mainly in Estonia; the country also has a large Russian-speaking minority who will usually pick the `ru` column. Roblox's own site and app are not offered in Estonian: Roblox's locale API marks `et_ee` as enabled for in-experience content only, not for the full site or signup. So Estonian kids read Roblox itself in English (or Russian) and meet Estonian only inside your game. Since Estonian cannot be an account language, the route to `et-ee` is presumably an in-experience language choice, but how players pick it is (unverified); expect a small share of Estonian players on this column.
- Use "sina" forms and drop the pronoun: "Oled AFK", "Kas oled kindel?" -- Minecraft's Estonian text talks to players the same way ("Sa olid liiga kaua eemal!"). Microsoft's running text uses plural "teie" ("Sulgege need rakendused", "valige"), which reads like a bank or a tax form to a 12-year-old. If a pronoun is needed, write it lowercase (Microsoft's rule): "sina/sinu", or reflexive "oma".
- Buttons: second person singular imperative, as Microsoft and Minecraft do ("Loobu", "Proovi uuesti", "Välju", "Mängi"): "Osta", "Liitu", "Sulge". Never the dictionary ma-infinitive ("Ostma").
- Titles: nouns ("Pood", "Seaded", "Edetabel"). Progress labels: -mine nouns ("Laadimine...").
- Yes/no questions open with "Kas": "Kas soovid jätkata?"; a casual "Oled valmis?" is fine in toasts.
- Hype that sounds native: "Super!", "Vau!", "Äge!", "Lahe!", "Tubli!", "Jess!", "Palju õnne!". One exclamation mark at most.
- Reads stiff or adult: "antud mäng" (for "this game") -> "see mäng"; "teostama" -> "tegema"; "läbi" for "via" -> "kaudu"; heavy -mine chains ("Müümise teostamiseks...") -> a verb ("Müümiseks kõnni..."); Microsoft's avoid list: "protsess" -> "toiming", "navigeerima" -> "liikuma", "-eeri-" verbs ("modifitseerima") -> plain verbs ("muutma").
- Say "we" for the game only in warm marketing lines; system messages go impersonal (Microsoft): "Koodi ei leitud.", not "Me ei leidnud koodi".
- Kids mix English game words into speech; in UI keep only the established ones (AFK, OP, XP, VIP) and put slang like "nuub" in flavor text only. Kid-safe: Wiktionary notes "noob" can sting.

## Roblox and gaming vocabulary
| English | et-EE | Note |
|---|---|---|
| Robux | Robux; gen./part. Robuxi | "Osta 100 Robuxi eest". EKI puts an apostrophe only where the written and spoken ending disagree ("Skype'i") and declines known names plainly ("Facebookist"); x is spoken, so "Robuxi" like "Robloxi". Wikipedia's "Robux'i" is off-norm |
| Premium | Premium; Premiumi | Wikipedia: subscription "Premium" |
| game pass | mängupass | Estonian Wikipedia's word; players may say "gamepass" (unverified); in the shop just name the pass |
| developer product | (item name) | No player-facing term; Creator docs are not in Estonian |
| experience / game | mäng | Microsoft warns against literal "kogemus"; Wikipedia says "Robloxi mäng" |
| obby / tycoon / simulator | obby / tycoon / simulaator | "takistusrada" if you translate obby; game titles stay English |
| rebirth | taassünd; verb taassündima | Minecraft's Respawn button is the imperative "Taassünni"; kids may say "rebirth" in chat (unverified), but UI uses one Estonian term |
| pet | lemmikloom (pl. lemmikloomad) | Never bare "lemmik": it means "favorite". Chat slang "pet/petid" is (unverified); keep it out of UI |
| egg / hatch | muna / munast koorus... | "kooruma" = to hatch (Minecraft: "Nuuskijamuna koorub"); "koorima" = to peel. Button: "Ava muna" |
| coins / gems | mündid (münt, mündi, münti) / kalliskivid | "teemandid" if the art shows diamonds; players may say "gemid" (unverified) |
| boost | boonus | "2x boonus"; players also say "boost" (unverified) |
| multiplier | kordaja | Prefer showing "2x"; "kordaja" in descriptions |
| XP | XP (XP-d, XP-boonus) | Minecraft: "kogemuspunktid", "kogemustase" -- too long for a HUD |
| level / level up | tase / "Tase tõusis!" | "tasemel 12"; slang "level" in chat only |
| quest | ülesanne | "Igapäevased ülesanded"; "missioon" for story quests |
| leaderboard | edetabel | Board title "Tippmängijad" |
| AFK, noob, OP, GG | AFK, nuub/noob, OP, GG | Wiktionary glosses noob as "kollanokk" (greenhorn) |
| VIP | VIP (VIP-i, VIP-server) | Hyphen before endings and in compounds |
| trade | vahetus / vahetama | Estonian Wikipedia describes Adopt Me pet trading with "vahetada"; Minecraft's "kauplema" is for villager trades |
| inventory / backpack | seljakott | Minecraft's word for Inventory; matches Roblox's Backpack |
| daily reward | igapäevane auhind | Claim button "Võta vastu" |
| codes | koodid | "Sisesta kood", redeem button "Lunasta" |
| group | kogukond | Roblox's English UI now says "Community"; players still say "grupp" (unverified) |
| like / favorite | pöial püsti / lemmikutesse | "Pane mängule pöial püsti", "Lisa lemmikutesse" |
| server | server | "serveris", "Server on täis!" (Minecraft) |
| friends / connections | sõbrad | Roblox's English UI says "Connections"; never "ühendused" |

## Grammar traps in UI strings
- **Plurals with {count}.** "1 münt", but every other number takes the partitive singular: "0 münti", "2 münti", "1,5 münti". Nominative plural after a number ("5 mündid") is always wrong. So "{count} münti" breaks only at 1. Safe patterns: a label ("Mündid: {count}"), or a construction where the number stands in another case, because there the noun is singular and agrees for every value: "{price} Robuxi eest" (genitive), "Sul jääb {amount} mündist puudu" (elative), "{n} sõbraga" (comitative).
- **No grammatical gender.** "tema" is he and she, and verbs do not change: "{player} liitus mänguga" fits every player. Do not invent gender workarounds.
- **Case endings around placeholders.** Estonian puts the case on the noun, and a username or translated item name cannot be declined safely. Keep {player}, {pet}, {item} in the nominative: as subject ("{player} tahab sinuga vahetada"), after a colon ("Võitja: {player}"), or after a declined head noun, as Microsoft prescribes and Minecraft does ("Mängijal %s on..."): "Vaheta mängijaga {player}". Never "{player}iga"; Minecraft's "%2$s-ga" is readable but clumsy.
- **Object case.** After an imperative the total object stays nominative, so names survive: "Osta {item}!", "Saa tasuta {item}!". In statements it turns genitive: "Said {pet}" would need "Said draakoni". Rephrase with the name as subject: "Munast koorus {pet}!", "Uus lemmikloom: {pet}!".
- **Rarity agreement.** Adjectives agree in case and number: "legendaarne draakon", "legendaarset draakonit", "legendaarse draakoniga". {rarity} is translated in the nominative singular, so put it only in front of a nominative singular {pet}.
- **Word order.** Microsoft puts the purpose before the action in instructions ("Avamiseks vajuta E"); short prompts may follow Minecraft's "Vajuta E, et avada"; time phrases take the postposition after the value: "{time} pärast".
- **Compounds.** Write them as one word: "seljakott", "lemmikloom", "õnnejook", "tippmängijad". Hyphen after abbreviations, digits and letters: "VIP-server", "XP-boonus", "E-klahv".
- **Capitalization.** Sentence case for titles, buttons and item names ("Igapäevane auhind", "Õnnejook"); lowercase after a colon, and for months, weekdays and language names ("eesti keel").

## Typography and formatting
- No space before ! ? : ;. Microsoft ends error messages with a period and keeps "!" for exceptional cases: "See kood on vale või aegunud." In a game, one "!" on rewards and hype is fine.
- Quotation marks: „...“ (U+201E, U+201C), inner ‚...‘ (CLDR; Microsoft allows straight quotes if used consistently).
- Numbers: decimal comma ("1,5x"); thousands separator is a non-breaking space, and CLDR does not group four-digit numbers: "1250", "12 500". English "1,250" from game code reads as one and a quarter -- flag it to the developer instead of patching the string.
- Percent: no space -- EKI, CLDR and Minecraft agree ("+10%", "3,5%", range "5–15%" with the sign once). EKI adds case endings only from the illative on, with a hyphen and no stem vowel ("10%-st", "10%-le"); never "10%-i".
- Durations (CLDR narrow, EKI "1 t 25 min"): "3 t 20 min", "2 p 5 t", "45 s"; "t" = tund, "p" = päev (Microsoft notes "h" in SI contexts). "m" is metres. The {time} format comes from game code.
- Ordinals are a number plus period: "1. koht", "5. tase" -- never "1st". Avoid ending a sentence on a bare number where "5." could read as "5th": "Uus tase: {level}".
- Ellipsis without a space: "Laadimine..." (Microsoft). Dashes: spaced en dash in sentences ("Pood – ainult täna!"), unspaced in ranges ("1–3"); no em dash. "&" -> "ja".
- Dates: "08.11.2026" or "8. november". Clock time: EKI writes "kell 14.30"; the EVS 8 standard and CLDR use "14:30". Both are correct; keep one per game.
- Keys: letters stay ("Vajuta E", Minecraft "Vajuta %s"); Space is "tühik" (Minecraft) or "tühikuklahv" (Microsoft); "Enter", "Shift" stay. PC "Klõpsa", touch "Puuduta".

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, XP, GG and the "x" in "2x".
- Do decline brand names with a plain ending, as EKI prescribes and Microsoft does ("Microsofti kontoga"): "Robloxis", "Robloxi mäng", "Premiumiga", "Robuxi eest". No apostrophe: "Robux'i" and "Roblox'is" are wrong.
- The game title ("Pet Hatch Tycoon") and promo codes (FREEPETS), same case; usernames and display names.
- Translate pet, item, egg and area names once and reuse them ("Draakon", "Õnnejook").
- Never drop or swap diacritics: "Mängi" not "Mangi", "Õnnejook" not "Onnejook" or "Önnejook" -- õ and ö are different letters.
- Latin script only. Russian belongs in the `ru` column; never mix Russian words into `et-ee`.

## Rendering on Roblox
- Checked the cmaps of every Latin font shipped with the Roblox client (content/fonts, 2026-11-08): Builder Sans, Source Sans Pro, Montserrat and the display fonts alike contain õ ä ö ü š ž, their capitals, „ “ and –, with three exceptions below.
- Missing: **Denk One** lacks š Š ž Ž; **Roman Antique** lacks ž Ž; **Inconsolata** (the Code font) lacks the en dash –. š/ž are rare ("šokolaad", "garaaž"), but avoid them in item names in those fonts, and use a hyphen in Code-font text. What Roblox draws instead (fallback font or a box) is (unverified): check in Studio.
- Luau `string.upper` changes only ASCII letters: "õnnejook" becomes "õNNEJOOK". Write uppercase text directly in the table ("ÕNNEJOOK", Minecraft's "SEES").
- Õ Ä Ö Ü marks sit above cap height; check for clipping in tight TextScaled labels (unverified).
- Long compounds have no break point ("kogukonnaga", "helendavasse", "lemmikloomad"); Roblox does not hyphenate, so TextScaled shrinks the whole label. Give labels AutomaticSize or slack.
- Verify in Studio: set the test locale to et-ee, paste the pangram "Põdur Zagrebi tšellomängija-följetonist Ciqo külmetas kehvas garaažis" into every font the game uses at its smallest TextSize, then open the longest strings (rebirth.confirm, reward.come_back) and the tightest (reward.claim, event.ends_in, settings.on).

## Mistakes machine translation makes here
1. Formal plural register: "Proovige uuesti", "Kas soovite jätkata?" -> "Proovi uuesti", "Kas soovid jätkata?".
2. Dictionary form on buttons: "Mängima", "Ostma" -> "Mängi", "Osta".
3. Wrong verb sense: "Play" as "Esita" (media) -> "Mängi"; "Claim" as "Nõua" (demand) -> "Võta vastu"; "Hatch" as "Koori" (peel) -> "Ava muna".
4. Numeral agreement: "5 mündid", "1 münti" -> "5 münti", "Mündid: 1".
5. Platform words translated literally: "experience" -> "kogemus" -> "mäng"; "connections" -> "ühendused" -> "sõbrad".
6. Split compounds: "selja kott", "õnne jook", "lemmik loom" -> "seljakott", "õnnejook", "lemmikloom".
7. English Title Case: "Igapäevane Auhind", "Tipp Mängijad" -> "Igapäevane auhind", "Tippmängijad".
8. "poolt" passive calque: "Sind kutsuti mängija {player} poolt" -> "{player} kutsus sind".
9. Suffix glued to a placeholder: "Vaheta {player}iga" -> "{player} tahab sinuga vahetada".
10. English number format: "1,250 münti", "1.5x" -> "1250 münti", "1,5x".
11. System "we": "Me ei leidnud seda koodi" -> "Koodi ei leitud."
12. "pet" as "lemmik" (= favorite): "Uus lemmik!" -> "Uus lemmikloom!".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Mängi | Minecraft's Play button |
| shop.title | Pood | |
| shop.buy | Osta | |
| reward.claim | Võta vastu | Exactly 10, within the limit; if the font runs wide, "Võta" (same verb). Never "Nõua" |
| rebirth.button | Taassünd | Noun as a feature label, like "Pood"; Minecraft's imperative "Taassünni" also fits. Same root as rebirth.confirm |
| rebirth.confirm | Kas soovid kohe taassündida? Kaotad oma mündid, kuid saad püsiva {multiplier}x boonuse. | Decimals need a comma ("1,5x") |
| coins.need_more | Sul jääb {amount} mündist puudu! | Elative keeps "mündist" right for 1 and for 5 |
| coins.count | Mündid: {count} | Label form avoids "1 münti"; expects "1250" or "12 500", not "1,250" |
| egg.hatched | Munast koorus {rarity} {pet}! | Name as subject stays nominative; rarity agrees with any pet. Accept the capitals ("Munast koorus Legendaarne Draakon!"): they read as item tags, and lowercase would need extra keys |
| rarity.legendary | Legendaarne | 11 of 12 |
| pet.name.dragon | Draakon | |
| chat.player_joined | {player} liitus mänguga | Minecraft's own wording; no gender |
| trade.request | {player} tahab sinuga vahetada | Casual "tahab" fits a popup; "kaubelda" sounds like buying and selling |
| prompt.open_shop | Vajuta E, et avada | Minecraft pattern "Vajuta %s" |
| pass.buy_price | Osta {price} Robuxi eest | Genitive after "eest" works for every price; 21 of 22 at 4 digits |
| pass.coins2x | 2x mündid | "Topeltmündid" (12) as a native alternative |
| pass.vip | VIP | |
| reward.daily_title | Igapäevane auhind | 17 of 18 |
| reward.come_back | Tule {time} pärast tagasi järgmise auhinna järele! | 54 of 60 with "3 t 20 min" |
| codes.placeholder | Sisesta kood | |
| codes.invalid | See kood on vale või aegunud. | Error message ends with a period (Microsoft) |
| social.like_reward | Pane mängule pöial püsti ja saa tasuta <b>Õnnejook</b>! | Standard thumbs-up idiom, matching Roblox's thumb icon; slang like "laigi" or "anna like" is (unverified). Imperative keeps the item nominative; 48 visible. Minecraft's luck potion is "Õnne võlujook" |
| social.group_reward | Liitu meie kogukonnaga ja saa tasuta auhind! | "kogukond" matches Roblox's Community button; "grupiga" also understood |
| afk.warning | Oled AFK. Liigu, et edasi teenida! | |
| leaderboard.title | Tippmängijad | One compound; "Parimad mängijad" is exactly 16 |
| level.up | Tase tõusis! Uus tase: {level} | Avoids a sentence-final "{level}." that reads as an ordinal |
| tutorial.sell | Kõnni helendavasse ringi, et lemmikloomad maha müüa. | |
| inventory.full | Seljakott on täis! Müü lemmikloomi, et ruumi teha. | Possessive dropped |
| settings.music | Muusika | |
| settings.on | Sees | Minecraft's toggle word (shown there as "SEES") |
| loading | Laadimine... | |
| event.ends_in | Üritus lõpeb {time} pärast | 27 of 28 with "2 p 5 t"; "Lõpuni {time}" if space runs short |
| item.op | See mõõk on OP! | |
| friends.boost | +{percent}% boonust iga sõbra eest sinu serveris | Partitive "boonust" after a percent |

## Sources
1. Microsoft Estonian Localization Style Guide -- https://download.microsoft.com/download/7/7/3/7734c896-d576-44f6-bf00-66350cb24be9/est-est-StyleGuide.pdf
2. Unicode CLDR language plural rules chart -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON for et: units, numbers, delimiters -- https://github.com/unicode-org/cldr-json/tree/main/cldr-json (cldr-units-full, cldr-numbers-full, cldr-misc-full, main/et)
4. Roblox locale API (et_ee: in-experience content only, not full site or signup) -- https://locale.roblox.com/v1/locales
5. Roblox Creator docs, language codes -- https://create.roblox.com/docs/production/localization/language-codes
6. Roblox Creator docs, localization overview -- https://create.roblox.com/docs/production/localization
7. Roblox client CoreScriptLocalization.csv (no Estonian column) and bundled fonts in content/fonts, cmap checked on 2026-11-08 -- local files from the Roblox install
8. Minecraft Java 1.21.4 Estonian strings (et_ee.json) -- https://assets.mcasset.cloud/1.21.4/assets/minecraft/lang/et_ee.json
9. Estonian Wikipedia, Roblox ("mängupass", "Premium", "vahetada" for Adopt Me trading) -- https://et.wikipedia.org/wiki/Roblox
10. Estonian Wiktionary, "noob" and "afk" -- https://et.wiktionary.org/wiki/noob, https://et.wiktionary.org/wiki/afk
11. EKI teatmik, apostrophe in declined foreign names -- https://teatmik.eki.ee/teatmik/ulakoma/
12. EKI teatmik, percent sign (no space, case endings) -- https://teatmik.eki.ee/teatmik/muid-marke/
13. EKI teatmik, spaces (clock "9.00", EVS 8 colon, "1 t 25 min") -- https://teatmik.eki.ee/teatmik/tuhikud/
