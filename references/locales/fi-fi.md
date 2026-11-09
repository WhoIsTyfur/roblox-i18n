# Finnish (fi-fi) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `fi-fi` (Roblox lists one Finnish locale, so a bare `fi` column adds nothing) |
| Script, direction | Latin with ä ö (å only in Swedish names), LTR |
| Address the player as | singular "sinä", shown by verb endings ("Osta", "Sait", "Olet"); never plural "te" |
| Text expansion vs English | about +10-20% for sentences (measured on the reference set below); short labels +25-70% ("Legendary" -> "Legendaarinen", "Top Players" -> "Parhaat pelaajat"); long compounds have no space to break at |
| Plural categories (CLDR) | one, other (ordinals: other only) |
| Model confidence | medium: grammar is well documented, but models glue endings onto placeholders, calque "to do X" and miss how Finnish kids talk |
| Native review before shipping | strongly recommended |

## Audience and register
- Readers: kids in Finland. Roblox enables `fi_fi` for in-game content only, not for the app, so players use Roblox's own menus in English and know platform terms in English. Swedish-speaking Finns pick `sv-se`; never put Swedish in this column.
- Finnish is not one of Roblox's 18 auto-translated languages: every Finnish string comes from the table.
- Talk to one player, informally (Microsoft's "sinuttelu"). Leave "sinä/sinun" out; endings carry the person: "Reppusi on täynnä", not "Sinun reppusi on täynnä". Never plural/formal "Painakaa", "Ostakaa".
- Buttons: 2nd person singular imperative: "Pelaa", "Osta", "Lunasta", "Avaa". Titles and tabs: nouns ("Kauppa", "Päivän palkinto"). Progress: passive ("Ladataan...", "Yhdistetään...").
- "Do X to get Y" -> imperative + ", niin" + present: "Liiku, niin jatkat tienaamista". Or "-malla": "Avaa painamalla E". Microsoft calls the "-aksesi" form ("Paina E avataksesi") stiff.
- Avoid officialese (Microsoft's "kapulakieli"): "jos" not "mikäli", "heti" not "välittömästi", "pitää tehdä" not "tulee tehdä".
- Hype that sounds natural: "Mahtavaa!", "Siistiä!", "Jee!", "Taso nousi!", "Onnea!". At most one "!" per string; Microsoft warns against overusing them and prefers stronger words.
- Stiff or adult: "Onnittelut, olet saavuttanut...", "Suorita ostotapahtuma", "Toiminto epäonnistui". Kid-safe: no swearing, not even mild everyday words like "perkele".
- Finnish has no grammatical gender and one pronoun "hän", so any past tense works for any {player}: "{player} liittyi peliin". Use neutral nouns ("pelaaja", never "-mies" compounds).

## Roblox and gaming vocabulary
| English | Finnish | note |
|---|---|---|
| Robux | Robux | Capital R, as fi.wikipedia writes it. Inflects with -i-: "Robuxin", "450 Robuxia", "Robuxilla", plural "Robuxeja". Never "Robux:ia". |
| Premium / Roblox Plus | Premium / Roblox Plus | Brands; Roblox Plus replaced new Premium sign-ups on April 30, 2026. Compound with hyphen: "Premium-jäsen". |
| game pass | pelipassi; in the shop just the pass name | "gamepass" in chat (unverified) |
| developer product | (name the item) | players never see the term |
| experience / game | peli | fi.wikipedia says "pelit"; never "kokemus" |
| obby | obby; "esterata" in descriptions | (unverified which kids prefer) |
| tycoon | tycoon | no Finnish genre word; keep in titles |
| simulator | simulaattori | |
| rebirth | rebirth ("rebirthin", "rebirthit") | native "uusi alku" if the game prefers Finnish (unverified usage) |
| pet | lemmikki, pl. lemmikit | |
| egg / hatch | muna / kuoriutua (pet hatches), kuoriuttaa (you hatch an egg) | "Kuoriuta muna" for a button |
| coins | kolikot | |
| gems | jalokivet; timantit if the art shows diamonds | |
| boost | tehostus | "boosti" in chat (unverified) |
| multiplier | kerroin; "2x" in names | "2-kertainen" is formal |
| XP | XP, kokemuspisteet | Minecraft: "kokemuspisteet", "kokemustaso" for XP level; "+50 XP" |
| level / level up | taso / "Taso nousi!" | "levu", "lvl" in chat (unverified) |
| quest | tehtävä | |
| leaderboard | tulostaulu; title "Parhaat pelaajat" | |
| AFK | AFK | "Olet AFK" |
| noob | aloittelija (UI); nuubi, nyyppä (jokes) | fi.wikipedia lists nuubi and nyyppä |
| OP | OP; ylivoimainen | "ihan OP" in chat (unverified) |
| VIP | VIP | "VIP-palvelin", "VIP:n" |
| trade | vaihtokauppa; verb vaihtaa | Minecraft: "Vaihtokaupat"; "treidata" in chat (unverified) |
| inventory / backpack | tavaraluettelo / reppu | Minecraft uses "Tavaraluettelo"; "inventaario" in chat (unverified) |
| daily reward | päivän palkinto | |
| codes | koodit; "Syötä koodi"; redeem = "Lunasta" | |
| group | ryhmä | fi.wikipedia "Ryhmät"; "yhteisö" if the game says Community |
| like / favorite | "Tykkää pelistä" / "Lisää suosikkeihin" | never "Pidä pelistä" (= enjoy it); "tykätä" is the social-media verb, but Roblox has no Finnish UI to confirm it (unverified) |
| server | palvelin, "palvelimella" | Minecraft "palvelimeen"; "serveri" in chat (unverified) |
| friends | kaverit | Roblox went back to Friends in April 2026; never "yhteydet". "ystävät" sounds formal. No Roblox Finnish UI to check (unverified) |

## Grammar traps in UI strings
- **Never suffix a placeholder.** An ending's shape depends on the word's last sound, vowel harmony and consonant gradation (Pupu -> Pupulle, Lohikäärme -> Lohikäärmeelle, Mikko -> Mikolle), and game code fills {player}, {pet} or {amount} with values you cannot see. "{player}lle", "{pet}n", "{item}:ä" break. Restructure so the placeholder stays in base form and a fixed word takes the ending:
  - Keep the placeholder as subject, in base form: "{player} liittyi peliin", "Kuoriutui {rarity} {pet}!", "{item} ostettu!"
  - Head noun (Microsoft's rule, Minecraft's practice): inflect a fixed noun beside it. "Lahja pelaajalta {player}", "Vaihda pelaajan {player} kanssa", "Tasolla {level}".
  - Colon label: "Voittaja: {player}", "Kolikot: {count}".
  - Space + hyphen compound when the value may hold spaces: "Ostit {item} -paketin", "Varusta {pet} -lemmikki" (Microsoft: "Windows Server 2022 -käyttöjärjestelmä").
- **Numbers.** CLDR one = 1 only. After 1 a subject noun is nominative ("1 kolikko"), after 2+ partitive singular ("5 kolikkoa"), so "{count} kolikkoa" shows "1 kolikkoa". Safe:
  - Label: "Kolikot: {count}"; number alone: "Puuttuu {amount}."
  - Any other case: noun stays singular and agrees for every number: "Osta {price} Robuxilla", "{amount} kolikon paketti", "{count} kolikolla".
- **Colon endings** go only on numbers, abbreviations and symbols ("VIP:n", "XP:tä", "50 %:n"); names written as pronounced take none ("Robloxissa"). Endings on a number follow its spoken form (1:tä, 2:ta, 3:a), so only genitive ":n" fits every {n}. "%" always reads "prosentti", so "{percent} %:n" is safe.
- **Adjectives agree** in case and number: "{rarity} {pet}" works only when both stay nominative singular. Give rarity tags as nominative adjectives ("Legendaarinen", "Harvinainen").
- **Possessive suffix, not pronoun:** "kolikkosi", "reppusi", "lemmikkisi".
- **Questions** take -ko/-kö: "Teetkö rebirthin nyt?", "Haluatko jatkaa?". Passive invitation: "Aloitetaanko?".
- **Objects in commands** stay in base form: "Lunasta palkinto", "Palaa hakemaan seuraava palkinto" (not "palkinnon").
- **No articles:** drop a/the; "a Rare Dragon" -> "harvinainen lohikäärme".
- **Compounds** are one word: "kolikkotehostus", "lemmikkikauppa", "Onnenjuoma". Two words ("kolikko tehostus") is a classic error. Avoid stacks of three or more parts; use a genitive ("lemmikkien säilytystila").
- **Capitalization:** sentence case everywhere ("Päivän palkinto", "Parhaat pelaajat"). Lowercase after a colon, and for days and months ("lauantai", "joulukuu").
- Capitalized inserted names ("Kuoriutui Legendaarinen Lohikäärme!") are accepted game style; lowercase forms read more natural if the developer can supply them.

## Typography and formatting
- No space before ! ? : ; and one space after. Don't copy English quote-heavy style.
- Quotes: Finnish uses the same mark on both sides, ”Osta” (U+201D twice), or straight "..."; never “...” or „...". UI references need none: "Valitse Osta".
- Dashes: no em dash. En dash with spaces as a pause ("Valmis – mennään!"), without spaces in ranges ("1–5"). Hyphen in compounds; space + hyphen after a multiword part or a placeholder.
- Numbers: decimal comma, space as thousands separator: "1,5", "1 250" (CLDR uses a no-break space). Game code that prints "1,250" reads as one point twenty-five; ask the developer to format per locale, don't edit numbers in strings.
- Percent: space before %: "50 %", "+{percent} %" (CLDR).
- Ordinals take a period: "5. sija". Clock: 24-hour with a period: "14.30" (CLDR "H.mm").
- Durations: have the formatter output CLDR short units with spaces: "2 pv 5 t", "3 t 20 min", "30 s". "h" (the SI symbol) is also understood, but pick one and never mix "t" and "h" in a game. Same form for 1 and many.
- Ellipsis: three periods, no space: "Ladataan...".
- Keys: keep the letter, "Paina E". Microsoft names: Enter, Esc stay; Space = "välilyönti", Shift = "vaihto" (Minecraft writes "Shift"); arrows "ylänuoli", "alanuoli". "Painaa" takes a partitive object for named keys: "Paina välilyöntiä", not "Paina välilyönti".

## Do not translate / keep as is
- Keep: Roblox, Robux, Premium, Roblox Plus, VIP, AFK, XP, OP, usernames and display names, promo codes ("FREEPETS"), keybinds, the game title "Pet Hatch Tycoon" unless the developer ships a Finnish title.
- Foreign names keep their spelling and inflect by pronunciation without a colon: "Robloxissa", "Robloxia", "Robuxilla". Acronyms take a colon: "VIP:n", "XP:tä".
- Translate in-game item, pet and rarity names ("Onnenjuoma", "Lohikäärme", "Legendaarinen") and keep each one identical everywhere.
- Never write "a"/"o" for ä/ö ("Paalla", "Lohikaarme"): it is chat typing, and some words change meaning (säästä = save, saasta = filth).

## Rendering on Roblox
- Finnish needs ä ö Ä Ö (Latin-1). German, a full Roblox app language, uses the same letters, so the default UI fonts render them (inferred, not tested). å, š, ž appear only in names.
- Cartoon display fonts: Google Fonts' "latin" subset covers Latin-1, so ä ö are likely present (unverified per font in Roblox). Paste "ÄÖ äö Päällä Lohikäärme Säästä" into every FontFace the game uses.
- Luau `string.upper` changes ASCII only: "päällä" -> "PääLLä". Write capitals in the table ("PÄÄLLÄ").
- TextWrapped prefers spaces, but Roblox's docs say a word wider than the label is split across lines, with no hyphen ("Legendaari / nen"). Long compounds hit this in narrow frames; TextScaled shrinks the whole label instead. Test the longest words ("Legendaarinen", "palvelimellasi") in the narrowest frames and shorten or rephrase rather than accept a split word.
- Dots on Ä Ö sit above cap height; check tight TextScaled labels for clipping (unverified).
- Verify in Studio with Player Emulator locale `fi-fi`; open rebirth.confirm, friends.boost (57/60), leaderboard.title (16/16) and rarity.legendary (13/12).

## Mistakes machine translation makes here
| Mistake | Bad | Good |
|---|---|---|
| Ending glued to a placeholder | {player}:lle lähetettiin lahja | Lahja lähetetty pelaajalle {player} |
| Partitive after a count | Tarvitset {amount} kolikkoa (-> "1 kolikkoa") | Kolikot eivät riitä! Puuttuu {amount}. |
| Plural formal "te" | Painakaa E avataksenne | Avaa painamalla E |
| Stiff "-aksesi" for "to do" (Microsoft lists it as overformal) | Paina E avataksesi | Avaa painamalla E |
| Pronoun where an ending is enough | Sinun reppusi on täynnä | Reppusi on täynnä |
| experience as "kokemus" | Liity kokemukseen | Liity peliin |
| claim as "vaadi" (= demand) | Vaadi palkinto | Lunasta palkinto |
| like as "pidä" (= enjoy) | Pidä pelistä | Tykkää pelistä |
| Split compound | kolikko tehostus | kolikkotehostus |
| English Title Case | Päivän Palkinto | Päivän palkinto |
| English number and % format | 1,250 kolikkoa, 50% | 1 250 kolikkoa, 50 % |
| Level up calqued | Tasoa ylös! | Taso nousi! |
| Officialese | Mikäli koodi on vanhentunut | Jos koodi on vanhentunut |

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Pelaa | |
| shop.title | Kauppa | |
| shop.buy | Osta | |
| reward.claim | Lunasta | |
| rebirth.button | Rebirth | kept English: a game mechanic name Finnish gaming talk usually borrows (like "levelata", "farmata"), and the confirm dialog explains it; unverified for Roblox kids. "Uusi alku" (9) if the game goes native, then use it in rebirth.confirm too |
| rebirth.confirm | Teetkö rebirthin nyt? Menetät kolikkosi, mutta saat pysyvän {multiplier}x-tehostuksen. | head noun "-tehostuksen" carries the case; "1,5x" if the game formats decimals |
| coins.need_more | Kolikot eivät riitä! Puuttuu {amount}. | number without a noun avoids 1 vs many |
| coins.count | Kolikot: {count} | 16/16 raw; 14 with "1 250" |
| egg.hatched | Kuoriutui {rarity} {pet}! | both stay nominative; 35 with "Legendaarinen Lohikäärme". Verb-first reads as a natural announcement of something new ("Tuli uusi viesti"); "Munasta kuoriutui..." reaches 43. Never "Sait {rarity} {pet}" (object needs -n) |
| rarity.legendary | Legendaarinen | 13/12: widen the tag by one character. It is the everyday word ("legendaarista!"); "Tarunomainen" (12) is literary, so use it only if the tag cannot grow, and then everywhere |
| pet.name.dragon | Lohikäärme | |
| chat.player_joined | {player} liittyi peliin | no gender in Finnish; same as Minecraft |
| trade.request | {player} haluaa vaihtaa kanssasi | |
| prompt.open_shop | Avaa painamalla E | 17/22 |
| pass.buy_price | Osta {price} Robuxilla | 22/22 raw; adessive is right for 1 and 1000 |
| pass.coins2x | 2x kolikot | "Tuplakolikot" (12) also natural |
| pass.vip | VIP | |
| reward.daily_title | Päivän palkinto | |
| reward.come_back | Palaa {time} päästä hakemaan seuraava palkinto! | "päästä" after a duration needs no ending on {time} |
| codes.placeholder | Syötä koodi | |
| codes.invalid | Koodi on virheellinen tai vanhentunut. | |
| social.like_reward | Tykkää pelistä, niin saat ilmaisen <b>Onnenjuoman</b>! | 47 without tags; item named in the string, so it may inflect |
| social.group_reward | Liity ryhmäämme, niin avaat ilmaisen palkinnon! | |
| afk.warning | Olet AFK. Liiku, niin jatkat tienaamista! | 41/45; one "!" as in the source; "ansaitsemista" is the neutral word |
| leaderboard.title | Parhaat pelaajat | 16/16 |
| level.up | Taso nousi! Olet nyt tasolla {level}. | head noun "tasolla" |
| tutorial.sell | Myy lemmikkisi kävelemällä hehkuvaan ympyrään. | Microsoft's "-malla" pattern |
| inventory.full | Reppusi on täynnä! Myy lemmikkejä, niin saat tilaa. | |
| settings.music | Musiikki | |
| settings.on | Kyllä | fits 5; the Off state must then be "Ei". "Päällä"/"Pois" (Minecraft's pair) is better if the toggle fits 6; never mix the pairs |
| loading | Ladataan... | |
| event.ends_in | Tapahtumaa jäljellä {time} | 26/28 raw; 28 with "2 pv 5 t" |
| item.op | Tämä miekka on ihan OP! | "ylivoimainen" if the game avoids slang |
| friends.boost | +{percent} % tehostus jokaisesta kaverista palvelimellasi | 57/60 |

## Sources
1. Microsoft localization style guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
2. Microsoft Finnish style guide (sinuttelu, kapulakieli, placeholders and head nouns, quotes, dashes, key names): https://download.microsoft.com/download/c/7/3/c7371dae-ae9d-4f9b-aa10-a131d432930f/fin-fin-StyleGuide.pdf
3. CLDR language plural rules (fi: one, other): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR Finnish numbers (decimal comma, no-break space grouping, "#,##0 %"): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/fi/numbers.json
5. CLDR Finnish units (pv, t, min, s): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/fi/units.json
6. CLDR Finnish Gregorian calendar (time "H.mm"): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-dates-full/main/fi/ca-gregorian.json
7. Roblox locale service (`fi_fi`: in-game content only, not the app): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
8. Finnish Wikipedia, Roblox ("pelit", "450 Robuxia", "Robuxeja", "Ryhmät", "Premium-jäsen"): https://fi.wikipedia.org/wiki/Roblox
9. Finnish Wikipedia, Kaksoispiste (colon before endings: "EU:n"): https://fi.wikipedia.org/wiki/Kaksoispiste
10. Finnish Wikipedia, Noob (nuubi, nyyppä): https://fi.wikipedia.org/wiki/Noob
11. Minecraft 1.21.10 Finnish strings (Tavaraluettelo, Vaihtokaupat, "%s liittyi peliin", "pelaajalle %s", Päällä/Pois, Kyllä/Ei, kokemuspisteet): https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21.10/assets/minecraft/lang/fi_fi.json
12. Roblox App Store listing, Finnish storefront (description in English, Roblox Plus): https://apps.apple.com/fi/app/roblox/id431946152?l=fi
13. Roblox Newsroom, "Introducing Roblox Plus" (April 2026): https://about.roblox.com/newsroom/2026/04/introducing-roblox-plus-subscription
14. DevForum, "Friends Are Back!" (April 2026), via the en-us guide: https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
15. Roblox engine docs, TextLabel.TextWrapped (breaks at spaces, splits a word wider than the label): https://create.roblox.com/docs/reference/engine/classes/TextLabel#TextWrapped
