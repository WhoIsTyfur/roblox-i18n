# Latvian (lv-lv) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `lv-lv` (Roblox lists one Latvian locale only, so a bare `lv` column adds nothing) |
| Script, direction | Latin plus ā č ē ģ ī ķ ļ ņ š ū ž, LTR |
| Address the player as | informal singular "tu" ("Spied E", "Nāc atpakaļ"); never "jūs" ("Spiediet") |
| Text expansion vs English | about +15-30% for sentences (this file's reference set averages about +20%); short labels often double ("Pet" -> "Mīlulis", "On" -> "Ieslēgts") |
| Plural categories (CLDR) | zero, one, other (zero = 0, 10-20, 30, 40...; one = 1, 21, 31... but not 11) |
| Model confidence | medium -- low-resource language; models copy Microsoft's formal "jūs", drop the comma before "lai" and lose long marks |
| Native review before shipping | strongly recommended |

## Audience and register
- Roblox's locale service flags `lv_lv` for in-experience content only (not full app, not signup). Latvian kids read Roblox's own menus in English (or Russian) and know platform words in English. How a player ends up with LocaleId `lv-lv` (device language or an in-experience language choice) is unverified; Roblox's docs don't say. Test with Studio's Player Emulator, and expect fewer lv-lv players than Latvian speakers.
- Latvia has a large Russian-speaking minority who mostly play in Russian. Write standard Latvian; never mix in Russian words or slang.
- Use "tu" in every string. Microsoft's Latvian guide prescribes polite "jūs" for adult software; for 9-16 year olds that reads like a bank letter. Minecraft's Latvian translation mostly talks to the player with "tu" ("Tevi izmeta operators"), though a few strings slip into "jūs" ("Nospiediet Enter"): never mix the two.
- Buttons and menu commands: infinitive, the Latvian software norm (Microsoft "Atcelt"; Minecraft "Iziet", "Lēkt", "Atdzimt"): "Spēlēt", "Pirkt", "Saņemt", "Atvērt". The infinitive also sidesteps tu/jūs.
- Sentences, hints, tutorials: tu-imperative: "Spied E", "Nāc atpakaļ", "Pārdod mīluļus", "Pievienojies". Never the jūs forms in -iet ("Spiediet", "Ievadiet", "Pievienojieties").
- Titles and tabs: nouns ("Veikals", "Dienas balva"). Progress text: a verb, not a "-šana" noun chain (Microsoft): "Ielādē...", not "Notiek ielāde...".
- Hype that sounds natural: "Super!", "Forši!", "Lieliski!", "Malacis!", "Oho!", "Jauns līmenis!". Stiff or adult: "Lūdzu, ievadiet...", "Jūs esat veiksmīgi...", "Darbība ir izpildīta". Microsoft avoids "!" entirely; a game may use one per string, never "!!!".
- Drop the possessives English needs (Microsoft rule): "Pārdod mīluļus", not "Pārdod savus mīluļus".
- Kid-safe: "nūbs" in a joke is fine; no insults ("muļķis") and no swearing.

## Roblox and gaming vocabulary
| English | Latvian | note |
|---|---|---|
| Robux | Robux | Capital R, no Latvian endings after a number: "{price} Robux". Chat forms like "robuksi" (unverified) never go in UI. |
| Premium | Premium | "Premium abonements" in prose (lv.wikipedia). |
| game pass | spēles caurlaide; in the shop just the pass name | lv.wikipedia: "spēļu caurlaides"; players say "gamepass" (unverified). |
| developer product | (name the item) | players never see the term. |
| experience / game | spēle | never "pieredze" (= know-how, XP). Roblox shows "experience" in English only. |
| obby | obby; "šķēršļu josla" in descriptions | (unverified which kids prefer) |
| tycoon | tycoon | no native genre word (unverified); keep in titles. |
| simulator | simulators | Latvian ending -s: "Mīluļu simulators". |
| rebirth | pārdzimšana; button "Pārdzimt" | Minecraft's Latvian uses "Atdzimt" for Respawn, so "atdzimt" would read as respawn. Tezaurs tags "pārdzimt" poetic, but its sense "be born again" is transparent (pār- + dzimt) and fits the mechanic. Chat may say "rebirth" (unverified); UI keeps "Pārdzimt". |
| pet | mīlulis, pl. mīluļi, acc. pl. mīluļus | Tezaurs: a loved animal; its corpus writes "mājas mīluļi" for house pets. "mājdzīvnieks" is long and also covers farm animals (Tezaurs). English "pets" is chat only (unverified). |
| egg / hatch | ola / izšķilties (past "izšķīlās"); button "Atvērt olu" | Minecraft: "Ola". |
| coins | monētas (sg. monēta) | |
| gems | dimanti (sg. dimants) / dārgakmeņi | match the art; Minecraft "Dimants". |
| boost | bonuss | "pastiprinājums" is correct but long; chat "būsts" (unverified). |
| multiplier | reizinātājs; write "2x" | the sign beats the noun on buttons. |
| XP | XP | "+50 XP"; "pieredze" only in longer prose. |
| level / level up | līmenis / "Jauns līmenis!" | ordinal: "5. līmenis". |
| quest | uzdevums; misija | |
| leaderboard | līderu tabula; board title "Līderi" | |
| AFK | AFK | "Tu esi AFK". |
| noob | iesācējs (UI); "nūbs" (jokes) | Tezaurs lists "nūbs" as jargon from "newbie". |
| OP | neticami spēcīgs | "nereāli spēcīgs" is youth slang not in Tezaurs (unverified for kids); "pārāk spēcīgs" sounds like a complaint; "OP" understood by gamers (unverified). |
| VIP | VIP | "VIP serveris". |
| trade | maiņa; verb "mainīties" | Minecraft's villager trading uses "tirgoties"/"Darījumi"; for swapping pets "mainīties" is plainer. |
| inventory / backpack | inventārs / mugursoma | Minecraft: "Inventārs". |
| daily reward | dienas balva | "ikdienas" also reads "everyday, ordinary". |
| codes | kodi; "Ievadi kodu"; redeem = "Aktivizēt" | |
| group | kopiena; "grupa" still understood | Roblox renamed Groups to Communities (21 Nov 2024), so the English UI kids read says Communities. "grupai" only if the developer's other text says group. |
| like / favorite | "novērtē spēli" / "Pievienot izlasei" | Roblox shows a thumbs-up icon, not a word. lv.wikipedia calls Facebook's button "Man patīk"; Facebook's current label "Patīk" is unverified. |
| server | serveris; "serverī" | Minecraft: "Servera nosaukums". |
| friends | draugi | Roblox renamed Connections back to Friends in April 2026. Never "savienojumi" or "kontakti". |

## Grammar traps in UI strings
- Plurals (CLDR): one = 1, 21, 31 ("1 monēta", "21 monēta"); other = 2-9, 22-29... ("2 monētas"); zero = 0, 10-20, 30... (CLDR's own patterns use the genitive plural: "10 monētu", "11 dienu"; the nominative "10 monētas" is also common and not an error -- unverified against a grammar authority). The real errors are "1 monētas", "21 monētas", "2 monēta". One string per key, so never put {count} straight before a countable noun.
  - Bad: "{count} monētas" -> "1 monētas", "21 monētas". Good: "Monētas: {count}", "Vajag vēl {amount}" (number without a noun).
  - Safe after a number: undeclined units: "{price} Robux", "{percent}%", "{multiplier}x", "+{n} XP".
- Simple past and future do not mark gender; the perfect and predicate adjectives do. Microsoft: use simple past instead of the perfect.
  - "{player} pievienojās spēlei" (any gender), not "{player} ir pievienojies/pievienojusies".
  - For "you": "Tu ieguvi", "Tu sasniedzi", "Tu zaudēsi"; never "Tu esi ieguvis(-usi)" or "Tu esi gatavs/gatava".
- Adjectives agree: leģendārs pūķis (m), leģendāra pele (f), definite "leģendārais pūķis". Rarity tags go masculine (implied "mīlulis"); never write "{rarity} {pet}": use "{pet} ({rarity})". A feminine pet with a masculine tag ("Pele (Leģendārs)") may look like an agreement slip (unverified), so where Latvian offers a choice, name pets with masculine nouns: "Kaķis", "Suns", "Zaķis" (bunny), "Vienradzis", "Pūķis".
- Seven cases. Inserted {pet} or {item} arrive in the nominative: keep them as subject or after a colon. "Tu nopirki {item}" needs the accusative ("zobenu") -> "Pirkums: {item}". Usernames take no endings: let a noun carry the case: "Maiņa ar spēlētāju {player}", "Dāvana no spēlētāja {player}".
- Yes/no questions start with "Vai" (Microsoft calls omitting it a grammar error): "Vai pārdzimt tagad?", not "Pārdzimt tagad?".
- A comma always opens a subordinate clause, before "lai", "ja", "kad", "kas": "Spied E, lai atvērtu". Minecraft's Latvian file drops it ("Guli gultā lai mainītu..."): don't copy that.
- If-clauses match the main clause's tense (Microsoft): "Ja pārdzimsi, saņemsi bonusu", not "Ja pārdzimsti, saņemsi...".
- No articles: "a Rare Dragon" -> "rets pūķis". Use indefinite endings for new things: "saņem bezmaksas dziru".
- English noun stacks become genitive phrases: "Coin Boost" -> "monētu bonuss", "Pet Storage" -> "mīluļu glabātava". A compound can mean something else than the phrase (Microsoft: "lietotājvārds" vs "lietotāja vārds").
- Ordinals take a period: "{level}. līmenis", "1. vieta".
- Sentence case for titles, buttons and item names ("Dienas balva", "Veiksmes dzira"); never English Title Case. "tu", "tev", day and month names lowercase. Don't start a sentence with "Un" or "Bet" (Microsoft).

## Typography and formatting
- No space before ! ? : ; and one space after (Microsoft): "Super! Jauns līmenis!"
- Quotes: “...”, inner ‘...’ (CLDR; Microsoft for software text). Latvian print often uses „...” instead (unverified); never mix styles in one game. Avoid quoting UI names unless the sentence is unclear without it.
- Dashes: en dash with spaces for asides ("Pasākums – tikai šonedēļ!"); en dash without spaces for ranges ("1–5"); hyphen for compounds ("e-pasts"). Microsoft prefers the en dash over the em dash in UI.
- Ellipsis: three periods, no space before: "Ielādē...". Microsoft writes "…", Minecraft "..."; keep the three periods the source uses.
- Numbers: decimal comma "1,5"; group with a non-breaking space from five digits: "1250", "12 500", "1 000 000" (CLDR minimum grouping 2; Microsoft the same). A Latvian kid reads "1,250" as one and a quarter: ask the developer to format numbers per locale; never edit digits inside a string.
- Percent: no space: "25%", "+{percent}%" (Microsoft; CLDR "#,##0%").
- Durations (CLDR): short "2 d. 5 st.", "3 st. 20 min", "30 sek." (no period after "min"); narrow "2 d. 5 h", "3 h 20 min", "30 s". Default to the short Latvian abbreviations; narrow only where a timer is too tight (which kids prefer is unverified). Pick one style per game; code formats the duration, so tell the developer. A clock "03:20:15" is language-neutral. 24-hour time.
- Symbols: no "&" (write "un") and no "#" for "number" (Microsoft). "x" is fine: "2x monētas".
- Keys: keep letter keys: "Spied E". Enter, Shift, Esc stay English; Space = "atstarpes taustiņš" ("Spied atstarpes taustiņu"); arrows "kreisā/labā bultiņa" (Microsoft).

## Do not translate / keep as is
- Keep: Roblox, Robux, Premium, VIP, AFK, XP, usernames and display names, promo codes ("FREEPETS"), keybinds, the game title "Pet Hatch Tycoon" unless the developer ships a localized title.
- No Latvian endings on brand names (Microsoft: no genitive ending on product names; lv.wikipedia writes "Roblox platformā", "Roblox kontus"). Put a Latvian noun next to the brand: "Roblox spēle", "Robux valūta", "Premium abonements".
- Translate item, pet and rarity names: "Veiksmes dzira" (Minecraft already uses it for Potion of Luck), "Pūķis", "Leģendārs".
- Never respell English game words in Latvian letters in UI ("rebērts", "būsts", "nūbs" outside jokes); never strip diacritics ("Monetas" is chat typing, not UI).

## Rendering on Roblox
- Latvian needs ā č ē ģ ī ķ ļ ņ š ū ž and Ā Č Ē Ģ Ī Ķ Ļ Ņ Š Ū Ž (Latin Extended-A). Use the precomposed code points (ā U+0101, ģ U+0123, ķ U+0137, ļ U+013C, ņ U+0146), never a letter plus combining mark. Unicode names ķ ļ ņ "with cedilla", but fonts draw a comma below; lowercase ģ has its mark on top.
- Checked in the font files of the 2026-11-05 client: all 22 letters plus – “ ” „ are in Builder Sans (default), Builder Extended/Mono, Source Sans Pro, Roboto (+Condensed, Mono), Arimo, Montserrat, Nunito, Oswald, Bangers, Luckiest Guy, Titillium Web, Ubuntu, Press Start 2P, Merriweather, Josefin Sans, Amatic SC, Jura, Kalam, Patrick Hand, Michroma, Sarpanch, Special Elite, Fondamento, Grenze Gotisch, Guru and Zekton.
- Missing letters: **Fredoka One** (no ā ē ī ū č ģ ķ ļ ņ or their capitals -- a simulator UI staple), Comic Neue Angular and Inconsolata (no ā ē ī ū ģ ķ ļ ņ; Inconsolata also no –), Creepster, Permanent Marker, Balthazar, Accanthis ADF Std, Highway Gothic (no ā ē ī ū č ģ ķ ļ ņ), Roman Antique (also no ž), Denk One (no ā č ē ģ ī ļ ņ š ū ž), Indie Flower (no Ī). Rechecked on the same client build 2026-11-08. Tell the developer to swap them for lv (Luckiest Guy or Bangers keep the cartoon look). Whether Roblox falls back per glyph or draws boxes is unverified; either way "Mūzika" would not match its label.
- Gotham is a cloud asset, not in the local fonts folder, so it was not checked (unverified).
- Luau `string.upper` changes ASCII only: "mūzika" -> "MūZIKA". Write capitals directly in the table ("MŪZIKA").
- Macrons on capitals (Ā Ē Ī Ū) and commas under Ķ Ļ Ņ Ģ need extra line height; check clipping in tight TextScaled labels (unverified).
- Long words don't wrap ("Pievienojies", "pastāvīgu"); with TextScaled the whole label shrinks. Give labels AutomaticSize or slack.
- Verify in Studio: Player Emulator locale `lv-lv`; paste "ĀČĒĢĪĶĻŅŠŪŽ āčēģīķļņšūž Leģendārs pūķis, Ķēniņš, Mūzika" into every FontFace the game uses; open the longest strings (inventory.full 56/60, social.group_reward 52/55) and the smallest (settings.on 5/5).

## Mistakes machine translation makes here
| Mistake | Bad | Good |
|---|---|---|
| Microsoft's formal "jūs" | Ievadiet kodu; Pievienojieties grupai | Ievadi kodu; Pievienojies kopienai |
| Missing comma before "lai" | Spied E lai atvērtu | Spied E, lai atvērtu |
| Yes/no question without "Vai" | Pārdzimt tagad? | Vai pārdzimt tagad? |
| English Title Case | Dienas Balva | Dienas balva |
| Gendered perfect for you/{player} | Tu esi izperējis leģendāru pūķi | Jauns mīlulis: Pūķis (Leģendārs)! |
| Count before a noun | {count} monētas -> "1 monētas" | Monētas: {count} |
| Rebirth as respawn or literal birth | Atdzimt; Atkārtota dzimšana | Pārdzimt |
| claim as "request" | Pieprasīt | Saņemt |
| experience as "pieredze" | Pievienojies pieredzei | Pievienojies spēlei |
| trade as commerce | Tirdzniecības pieprasījums | {player} grib ar tevi mainīties |
| Latvian endings on brands | Pirkt par 100 Robuksiem | Pirkt par 100 Robux |
| Stripped or wrong marks | Monetas, Muzika, Leğendārs | Monētas, Mūzika, Leģendārs |

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Spēlēt | infinitive, as on Latvian buttons |
| shop.title | Veikals | |
| shop.buy | Pirkt | |
| reward.claim | Saņemt | not "Pieprasīt" (= request) |
| rebirth.button | Pārdzimt | "Atdzimt" is Minecraft's Respawn |
| rebirth.confirm | Vai pārdzimt tagad? Tu zaudēsi monētas, bet iegūsi pastāvīgu {multiplier}x bonusu. | "Vai" question; future tense avoids gender; code should print "1,5" |
| coins.need_more | Nepietiek monētu! Vajag vēl {amount}. | number without a noun avoids plural forms |
| coins.count | Monētas: {count} | 15/16 with "12 500" |
| egg.hatched | Jauns mīlulis: {pet} ({rarity})! | no {rarity} before {pet}; to keep "hatched": "Izšķīlās {pet} ({rarity})!" (verb first, {pet} as subject; 39/40 worst case) |
| rarity.legendary | Leģendārs | masculine, agrees with "mīlulis" |
| pet.name.dragon | Pūķis | |
| chat.player_joined | {player} pievienojās spēlei | Minecraft's exact wording; past tense is gender-neutral |
| trade.request | {player} grib ar tevi mainīties | |
| prompt.open_shop | Spied E, lai atvērtu | 20/22 |
| pass.buy_price | Pirkt par {price} Robux | Robux undeclined |
| pass.coins2x | 2x monētas | |
| pass.vip | VIP | |
| reward.daily_title | Dienas balva | |
| reward.come_back | Nāc atpakaļ pēc {time}, lai saņemtu nākamo balvu! | |
| codes.placeholder | Ievadi kodu | |
| codes.invalid | Kods ir nederīgs vai tam beidzies termiņš. | 42/45 |
| social.like_reward | Novērtē spēli un saņem bezmaksas <b>Veiksmes dziru</b>! | 48 without tags; item name in accusative. "novērtēt" = rate (as in app stores, unverified); Roblox's like is a thumbs-up icon with no label, so a quoted “Patīk” names a word kids never see there; "Ieliec “Patīk” ..." (49) only if the game's own button says it |
| social.group_reward | Pievienojies mūsu kopienai un saņem bezmaksas balvu! | 52/55; "grupai" if the developer prefers the old word |
| afk.warning | Tu esi AFK. Kusties, lai turpinātu pelnīt! | 42/45 |
| leaderboard.title | Līderi | "Labākie spēlētāji" is 17/16; "Labākie" (7) is closest to "Top"; "Līderu tabula" is a calque of "leaderboard", fine in prose but not as the board's title (natives' pick unverified) |
| level.up | Jauns līmenis! Tu sasniedzi {level}. līmeni. | simple past, gender-neutral; ordinal period |
| tutorial.sell | Ieej mirdzošajā aplī, lai pārdotu mīluļus. | no possessive (Microsoft) |
| inventory.full | Mugursoma ir pilna! Pārdod mīluļus, lai atbrīvotu vietu. | 56/60 |
| settings.music | Mūzika | Minecraft: "Mūzika" |
| settings.on | Iesl. | 5/5; pair with "Izsl.". Ask the developer for 8 characters to fit "Ieslēgts" (Minecraft's word). "Jā"/"Nē" answer a question, not a toggle state: last resort |
| loading | Ielādē... | verb form, as Microsoft prescribes for progress |
| event.ends_in | Pasākums: vēl {time} | "Pasākums beidzas pēc {time}" is 31/28 with "2 d. 5 st." (29 even with narrow "2 d. 5 h"); this fits "12 d. 23 st." (27) |
| item.op | Šis zobens ir neticami spēcīgs! | "unbelievably strong": hype without slang risk. "nereāli spēcīgs" is youth slang, not in Tezaurs; "Šis zobens ir OP!" if the game's tone is gamer slang (both unverified for kids) |
| friends.boost | +{percent}% bonuss par katru draugu serverī | no space before %; generic masculine "draugu" |

## Sources
1. Roblox language codes (Latvian (Latviešu), `lv-lv`): https://create.roblox.com/docs/production/localization/language-codes
2. Roblox locale service (`lv_lv`: in-game content only; 18 full-app locales): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
3. Microsoft localization style guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
4. Microsoft Latvian style guide PDF: https://download.microsoft.com/download/c/9/c/c9c901d9-8d73-4a07-bda2-e9177cc0e965/lav-lva-StyleGuide.pdf
5. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
6. CLDR Latvian number symbols: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/lv/numbers.json
7. CLDR Latvian duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/lv/units.json
8. CLDR Latvian quotation marks: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-misc-full/main/lv/delimiters.json
9. Minecraft Java 1.21.4 Latvian language file (register, "Atdzimt", "Veiksmes dzira", "pievienojās spēlei"): https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21.4/assets/minecraft/lang/lv_lv.json
10. Latvian Wikipedia, Roblox ("spēļu caurlaides", "Premium abonements", undeclined "Roblox"): https://lv.wikipedia.org/wiki/Roblox
11. Tezaurs, "pārdzimt" (poetic tone; be reborn, change for the better): https://tezaurs.lv/pārdzimt
12. Tezaurs, "mīlulis" (beloved animal; corpus "mājas mīluļi"): https://tezaurs.lv/mīlulis
13. Tezaurs, "nūbs" (jargon, from "newbie"): https://tezaurs.lv/nūbs
14. DevForum, "Friends Are Back!" (Connections -> Friends, April 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
15. DevForum, "Introducing Roblox Communities" (Groups -> Communities, Nov 2024): https://devforum.roblox.com/t/introducing-roblox-communities/3268307
16. Font coverage: cmap check of every font in the Roblox client's content/fonts folder (version-f0ea5da9412f4e35, 2026-11-05), run 2026-11-08.
17. Tezaurs, "mājdzīvnieki" (animals kept for farm or decorative use): https://tezaurs.lv/mājdzīvnieki
18. Tezaurs, "izšķilties" (hatch; past "izšķīlās"): https://tezaurs.lv/izšķilties
19. Tezaurs, "nereāls" (unrealistic, unreal; no intensifier sense): https://tezaurs.lv/nereāli
20. Latvian Wikipedia, Facebook ("Man patīk" button): https://lv.wikipedia.org/wiki/Facebook
