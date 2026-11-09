# Hungarian (hu-hu) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `hu-hu` (the only Hungarian locale Roblox lists, so it serves Hungary and the Hungarian minorities in Romania, Slovakia, Serbia and Ukraine alike; a bare `hu` column adds nothing and whether Roblox reads one is unverified) |
| Script, direction | Latin plus á é í ó ö ő ú ü ű, LTR |
| Address the player as | informal singular "te" (tegezés): "Írd be", "Lépj be"; never "Ön"/"maga" forms ("Adja meg", "Kérjük") |
| Text expansion vs English | about +20-35% for sentences (unverified rule of thumb); this guide's reference set came out +11% while fitted to budgets; fewer but much longer words ("kisállataidat" = "your pets" as object) |
| Plural categories (CLDR) | cardinal: one, other (a noun after a number is always singular, so one string fits every count); ordinal: one (1, 5), other (that split only approximates the "az"/"a" article ("az 5.", "a 2."; but also "az 50.", "az 1000."), not a word change) |
| Model confidence | medium: grammar is well documented, but models glue suffixes to {params}, pick the wrong a/az, mix definite and indefinite verbs, and Roblox has no Hungarian UI to anchor terms |
| Native review before shipping | strongly recommended |

## Audience and register
- Roblox's own app and site are not in Hungarian: the Roblox locale API flags `hu_hu` for in-game content only (not full experience, not signup), checked 2026-11-08, and the Hungarian App Store listing names 15 app languages without Hungarian. Kids see Robux, Premium, Friends and Groups in English. Roblox does not auto-translate Hungarian either, so every empty key shows English.
- Reach: `Player.LocaleId` is the account's locale (Roblox API docs), which Hungarian kids likely cannot set. The documented route is the in-game Settings menu language switcher, which lists the languages the game itself supports, so add Hungarian under Supported Languages in the Creator Dashboard. Whether that switcher offers Hungarian is unverified (needs a real account); the Player Emulator only previews the column.
- Write neutral standard Hungarian for readers in Hungary and the neighboring minorities: no forint prices, no Hungary-only holidays or town names.
- Address one player with "te" in every string. Microsoft's Hungarian guide uses "Ön" for software (while asking for a playful tone in games); Minecraft's Hungarian UI, which these kids know, uses "te": "Nyisd meg az eszköztárad", "Add meg a csatlakozási kódot". Never mix: "Írd be a kódot, és kapsz egy jutalmat!", not "Írja be a kódot, és kapsz...".
- One-word buttons, tabs, toggles: a verbal noun, as Microsoft ("Mentés") and Minecraft Bedrock do ("Játék" for Play, "Vásárlás", "Begyűjtés", "Beváltás", "Feloldás"). Sentences and calls to action, including buttons that carry an object or price: te-imperative, as Bedrock's "Játssz most" and "Vásárolj Minecraft-érméket": "Lájkold a játékot!", "Vedd meg 100 Robuxért". One style per element type.
- Plain, everyday words (Microsoft): "ha" not "amennyiben", "megpróbál" not "megkísérel", "szeretne" not "kíván". A suffix beats a heavy phrase: "a csoportunkkal" not "a csoportunk segítségével".
- Natural hype: "Szuper!", "Király!", "Hűha!", "Gratulálunk!", "Ne hagyd ki!". Microsoft notes "Oops" is too informal for Hungarian product text; in a kids' game "Hoppá!" is fine (Minecraft Bedrock: "Hoppá, hiba történt.").
- Stiff or adult: "Kérjük", "Tisztelt", "végrehajtásra kerül", "igénybe vesz". Don't blame the player: "Ez a kód nem működik", not "Rossz kódot írtál be".
- Kid-safe slang only in flavor text ("tök jó", "brutál erős", "OP"); no insults ("hülye", "béna", "lúzer") and no pressure lines ("Vedd meg most, különben lemaradsz!").

## Roblox and gaming vocabulary
| English | Hungarian | note |
|---|---|---|
| Robux | Robux | Latin, capital R; suffixes attach directly, as Wikipedia ("Robuxokat") and the press ("a Robloxot") write: "Robuxért", "Robuxból". After a number it stays singular: "100 Robux". |
| Premium | Premium | Roblox's product name; "prémium tagság" for the membership in prose (Hungarian Wikipedia). |
| game pass | gamepass | players' word (unverified); Hungarian Wikipedia's calque is "játékbérlet". In the shop show the pass's own name instead of either. |
| developer product | fejlesztői termék | Hungarian Wikipedia's term; players never see it, name the item. |
| experience / game | játék | Hungarian Wikipedia notes Roblox calls games "élmények"; nobody else does. Never "tapasztalat" (know-how, and the XP word). |
| obby | obby; akadálypálya | "akadálypálya" in descriptions (unverified which kids prefer). |
| tycoon | tycoon | kept in English in titles (unverified); "tycoon játék" if it needs a noun. |
| simulator | szimulátor | ordinary Hungarian word. |
| rebirth | rebirth; újjászületés | "Újjászületés" is 12 chars, too long for most buttons; if you keep "rebirth", don't suffix it (see grammar traps). |
| pet | kisállat; pet | "kisállat" (one word) is the shop and vet word for pets; "háziállat" covers farm animals too. Chat says "pet", "petek" (unverified). |
| egg / hatch | tojás; kikel (intransitive) | "Kikelt egy Sárkány!" keeps the pet in the nominative; "kikeltet" (transitive) forces an object suffix. |
| coins | érme | "250 érme", "érméid"; Bedrock calls Minecoins "Minecraft-érme". "coin" in chat (unverified). |
| gems | drágakő; gyémánt | "gyémánt" only if the icon is a diamond. |
| boost | bónusz; boost | "boost" in chat (unverified). |
| multiplier | szorzó; "2x" | "2x érme"; "állandó szorzó" (permanent; "végleges" means final). |
| XP | XP; tapasztalati pont | Minecraft's Hungarian says "tapasztalati pont/szint"; "+50 XP" in HUDs. Article "az XP" (iksz). |
| level up | szintet lép; szintlépés | Minecraft: "Játékos szintet lép"; toast "Szintet léptél!". |
| quest | küldetés | |
| leaderboard | ranglista | "toplista" also natural. |
| AFK | AFK | "AFK vagy"; article "az AFK". |
| noob | noob; kezdő | "noob" only in friendly jokes. |
| OP | OP; túl erős | "nagyon OP" in flavor text (unverified how widespread). |
| VIP | VIP | compounds with a hyphen: "VIP-szerver", "VIP-terem". |
| trade | csere; cserél | "trade" in chat (unverified). Never "kereskedelem" (commerce). |
| inventory / backpack | eszköztár / hátizsák | Minecraft's Hungarian inventory is "Eszköztár"; keep whichever the source means. |
| daily reward | napi jutalom | |
| codes | kódok; beváltás | redeem button "Beváltás"; placeholder "Írd be a kódot". |
| group | csoport | "Lépj be a csoportunkba". |
| like / favorite | lájk, lájkol / kedvenc | "Lájkold a játékot!"; "Add hozzá a kedvenceidhez!". |
| server | szerver | Minecraft Java: "Csatlakozás a szerverhez..."; "kiszolgáló" (Microsoft, Bedrock) reads as IT-speak in a kids' game. |
| friends | barátok | Roblox's English UI says Friends; never "kapcsolatok" (sounds like LinkedIn). |
| event | esemény | "event" in chat (unverified). |
| item | tárgy | Minecraft's word; "cucc" only in jokes. |

## Grammar traps in UI strings
- Vowel harmony: most suffixes come in back (a o u) and front (e ö ü) forms chosen by the word's vowels: "játékban"/"szerverben", "ranglistához"/"szerverhez"/"szörnyhöz". Accusative "-t" changes too: "kardot", "érmét", "tojást", "drágakövet". "-val/-vel" also copies the last consonant: "Annával", "Péterrel", "Tommal".
- A {param}'s value is unknown, so no suffix can be chosen. "{player}-val" fits Anna, not Péter or Tom. Restructure so the placeholder needs no ending:
  - as the subject: "{player} csatlakozott a játékhoz", "{player} cserélni szeretne veled" (the suffix sits on "veled");
  - after a colon: "Győztes: {player}", "Új kisállat: {rarity} {pet}";
  - behind a fixed noun that takes the suffix (Minecraft's own trick): "{player} játékossal cserélsz", "{pet} nevű kisállatot";
  - with a postposition, a separate word: "{time} múlva", "{player} után", "{amount} érme helyett".
  - Never "{player}-t", "{pet}-ot", "{player}-val/-vel" in player-facing text; Minecraft's Hungarian does this and it reads machine-made.
- Article a/az: "az" before a vowel sound, "a" before a consonant: "az Égi Sárkány", "a Sárkány", "az XP", "a VIP". Before an unknown {param} use "egy" (invariant) or no article; Minecraft's "a(z) %s" is a fallback, not polish.
- Numbers: suffixes need a hyphen and follow the spoken number: "2-t", "3-at", "5-öt", "10-et", "100-at" (AkH 265). Never suffix {amount} or {count}; suffix the noun: "Még {amount} érme kell" or "Még {amount} érmére van szükséged".
- Ordinals: digit plus period, "{level}. szint". The article depends on the number ("az 1.", "az 5.", "a 2.", "az 50."), so drop it: "Már {level}. szintű vagy", not "Elérted a(z) {level}. szintet".
- Percent is safe: the suffix follows the spoken "százalék", so "{percent}%-os", "{percent}%-kal" are right for any number (AkH: "80%-os", "6%-kal"). Multipliers are not: "2x-es" (kétszeres) but "3x-os" (háromszoros), so write "{multiplier}x bónusz" with no suffix.
- Plurals: the noun after a number stays singular, and so does the verb: "1 érme", "250 érme", "3 játékos csatlakozott". Bad: "{count} érmék".
- No grammatical gender: "ő" and "csatlakozott" fit any {player}; adjectives never agree.
- Definite vs indefinite verb: an object with "a/az", a possessive or a name takes the definite form ("Lájkold a játékot", "Elveszíted az érméidet"); with "egy" or no article, the indefinite ("Vegyél egy kardot", "Kapsz egy jutalmat"). Bad: "Vedd meg egy kardot".
- "Your" becomes a possessive suffix: "Tele a hátizsákod!", not "A te hátizsákod tele van!".
- Loanwords and names take suffixes by pronunciation, attached directly when spelled as said: "a Robloxon", "a Robloxban" (press), "Robuxokat" (Wikipedia), "petek". A name ending in a silent letter takes a hyphen (AkH 217: "Rousseau-val"); a foreign word ending in x assimilates without one (AkH 216 b: "fixszel", "Félixszel"), so the correct form is "Robuxszal", not Wikipedia's "Robux-szal". It still looks odd: prefer "Robuxért", "Robuxból".
- Don't suffix English words whose pronunciation kids disagree on ("rebirth"): "Jöhet a rebirth?" needs no ending.
- Compounds: one word for Hungarian parts ("kisállatbolt", "szerencsebájital", "tojásnyitás"); a hyphen after a name or acronym ("Roblox-fiók", "Robux-csomag", "XP-bónusz").
- Capitalization: only the first word of titles, buttons and labels is capitalized; English Title Case is an error (Microsoft): "Napi jutalom", "Legjobb játékosok". Brand names keep theirs: "Roblox Premium". Item and rarity names: capitalize the first word only ("Arany kard"), consistently. Labels inserted mid-sentence keep that capital ("Kikelt egy Legendás Sárkány!"), as Minecraft inserts its item names; accept it as item-name style rather than lowercasing the label keys.

## Typography and formatting
- No space before ! ? : ; and one after.
- Quotation marks: „...” (low opening, high closing), »...« inside (Microsoft, AkH). Never English "..." pairs or a mix.
- Numbers (CLDR): comma for decimals, a no-break space for thousands: "1,5", "1 250". A {count} preformatted as "1,250" reads as 1.25, and a multiplier "1.5" should be "1,5". Flag both to the developer.
- Percent (CLDR, AkH): no space: "25%", "+25%"; suffix with a hyphen: "25%-os".
- Dashes (Microsoft): never an em dash. Ranges take an unspaced en dash: "3–5"; minus is a spaced en dash. In short UI text prefer a colon or a new sentence to a parenthetical dash.
- Ellipsis: three periods, no space before (Microsoft): "Betöltés...".
- Periods end full sentences; fragments get none (Microsoft). Hungarian grammar wants "!" after imperatives, but Microsoft keeps plain instructions on a period: hype gets "!", tutorial steps may end in ".".
- Durations, CLDR short forms: nap, óra "ó", perc "p", másodperc "mp": "2 nap 5 ó", "3 ó 20 p", "45 mp". Minecraft Bedrock uses the same spaced "%s ó", "%s p" (and "%s n" for days). The unspaced "3ó 20p" has no source behind it; use no-break spaces instead so the pair never wraps apart. Clock time "10:35".
- Roblox has no localized duration formatter: {time} comes from the developer's own code, so code that outputs "3h 20m" shows letters that mean nothing in Hungarian. Flag it and give the developer the forms above.
- Keys stay Latin capitals, but article and suffix follow the letter's name: "az E-t" (é), "az F-et" (ef), "a Q-t" (kú). Safest is key plus verbal noun, as Bedrock's interact hints pair the key icon with "Kinyitás": "E: megnyitás" works for any key.
- Never drop accents ("Vasarlas" for "Vásárlás") and never swap ő ű for õ û or ô (old Latin-1 fonts did this): "Kőtojás", not "Kõtojás".
- Agglutination builds long words ("Szerencsebájitalért", "kisállataidat"); Roblox doesn't hyphenate, so enable TextWrapped and test the longest strings.

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, Roblox Studio: Latin as written, with Hungarian suffixes attached and the definite article Microsoft requires before product names: "a Robloxon", "a Robux".
- Game titles ("Pet Hatch Tycoon"): keep in English; players search the English title. With an article and suffix by pronunciation: "a Pet Hatch Tycoonban".
- Usernames and display names: never translate, transliterate or suffix.
- Promo codes ("FREEPETS"): exactly as given, same case; translate only the text around them.
- Key names (E, Q, Shift) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Szerencsebájital", after Minecraft's "bájital"); they are fixed text, so inflect them freely ("Szerencsebájitalért").
- Keep established gamer acronyms (OP, AFK, XP, VIP, noob); don't respell them Hungarian-style ("nub", "ápé") in UI.

## Rendering on Roblox
- Hungarian needs á é í ó ö ú ü (Latin-1) plus ő ű Ő Ű (U+0151 U+0171 U+0150 U+0170, Latin Extended-A). The double-acute letters are the ones decorative fonts lack.
- Font files in a local Studio install (content/fonts, cmap check, 2026-11-08): FredokaOne, Creepster, DenkOne, PermanentMarker, Balthazar, RomanAntique (Antique), AccanthisADF (Fantasy) and HWYGOTH (Highway) have no ő ű Ő Ű. Builder Sans/Extended/Mono, Luckiest Guy, Bangers, Montserrat, Nunito, Press Start 2P, Source Sans Pro, Roboto, Oswald, Arimo and Ubuntu cover every Hungarian letter.
- Rendered in Studio 2026-11-08: Roblox draws the missing ő ű from a fallback sans in a thin regular weight (never a box), so "Kőtojás" in Fredoka One shows a mismatched letter mid-word. Fredoka One is a favorite simulator font, so this is the main Hungarian risk: switch Hungarian text to a covering font such as Luckiest Guy or Builder Sans.
- Accents on capitals (Á É Ő Ű) may clip at the top of tight TextScaled labels (unverified).
- Luau's string.upper/lower are byte-wise ASCII (checked in Studio 2026-11-08): string.upper("érme őr") gives "éRME őR". Store all-caps text as written; never auto-case Hungarian.
- Verify in Studio: Player Emulator set to Hungarian; paste the test phrase "Árvíztűrő tükörfúrógép" and "ÁRVÍZTŰRŐ TÜKÖRFÚRÓGÉP" into every font face used; open the panels with the longest strings.

## Mistakes machine translation makes here
- Suffix on a placeholder: "{player}-val cseréltél" -> "{player} játékossal cseréltél".
- Article on a placeholder: "Kikeltetted a(z) {pet}-ot!" -> "Kikelt egy {rarity} {pet}!".
- Title Case: "Napi Jutalom", "Legjobb Játékosok" -> "Napi jutalom", "Legjobb játékosok".
- Formal or mixed register: "Kérjük, adja meg a kódot" -> "Írd be a kódot"; "Mozogjon, és gyűjts tovább!" -> "Mozogj, és gyűjts tovább!".
- Plural after a count: "{count} érmék" -> "{count} érme".
- Definite/indefinite clash: "Vedd meg egy kardot" -> "Vegyél egy kardot".
- Calqued "a/an": "Ez egy legendás kard, ami egy nagyon erős fegyver" -> "Ez a legendás kard nagyon erős" (Microsoft flags the "egy" habit).
- Missing article before names: "Roblox a legjobb" -> "A Roblox a legjobb".
- "Claim" as "Igénylés" (an application form) -> "Begyűjtés" or "Átvétel".
- "Experience" as "élmény" or "tapasztalat" -> "játék"; "pet" as "háziállat" (farm animals too) -> "kisállat"; "trade" as "kereskedelem" -> "csere".
- "Unlock" calqued: "Lépj be a csoportba egy jutalom feloldásához" -> "Lépj be a csoportunkba egy ingyenes jutalomért!".
- English number formats: "1,250 érme", "1.5x", "% 10" -> "1 250 érme", "1,5x", "10%".
- Wrong accents: "Kõtojás", "Vasarlas" -> "Kőtojás", "Vásárlás".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Játék | Minecraft Bedrock's own Play button |
| shop.title | Bolt | |
| shop.buy | Vásárlás | 8/8; Bedrock's buy button |
| reward.claim | Begyűjtés | 9/10; Bedrock's word for collect; never "Igénylés" |
| rebirth.button | Rebirth | "Újjászületés" is 12 > max 10; players' word (unverified) |
| rebirth.confirm | Jöhet a rebirth? Elveszíted az érméidet, de kapsz egy állandó {multiplier}x bónuszt. | no suffix on "rebirth" or after "x"; "állandó" = permanent ("végleges" means final); multiplier must arrive as "1,5" |
| coins.need_more | Még {amount} érme kell! | singular noun works for 1; no suffix on the number |
| coins.count | {count} érme | lowercase noun; "1,250" must be "1 250" (code issue) |
| egg.hatched | Kikelt egy {rarity} {pet}! | intransitive verb keeps both params nominative; "egy" avoids a/az; the labels' capitals ("Legendás Sárkány") are accepted item style |
| rarity.legendary | Legendás | |
| pet.name.dragon | Sárkány | |
| chat.player_joined | {player} csatlakozott a játékhoz | Minecraft's exact pattern; no gender, no suffix |
| trade.request | {player} cserélni szeretne veled | suffix sits on "veled" |
| prompt.open_shop | E: megnyitás | key plus verbal noun, like Bedrock's interact hints; survives a key change. Sentence form "Nyisd meg az E-vel" (18) fits E only ("az F-fel", "a Q-val") |
| pass.buy_price | Vedd meg {price} Robuxért | 22/22 at a 4-digit price; fallback "{price} Robuxért" |
| pass.coins2x | 2x érme | "Dupla érme" (10) also natural |
| pass.vip | VIP | |
| reward.daily_title | Napi jutalom | sentence case |
| reward.come_back | Gyere vissza {time} múlva a következő jutalomért! | postposition "múlva", no suffix; needs "3 ó 20 p", not "3h 20m" |
| codes.placeholder | Írd be a kódot | 14/16 |
| codes.invalid | Ez a kód érvénytelen vagy lejárt. | |
| social.like_reward | Lájkold a játékot egy ingyenes <b>Szerencsebájitalért</b>! | 51/55 visible; suffix inside the tag is fine, the item name is fixed |
| social.group_reward | Lépj be a csoportunkba egy ingyenes jutalomért! | "unlock" dropped, not calqued |
| afk.warning | AFK vagy! Mozogj, hogy tovább gyűjthess! | |
| leaderboard.title | Ranglista | "Legjobb játékosok" is 17 > max 16 |
| level.up | Szintet léptél! Már {level}. szintű vagy. | ordinal period, no article before the number |
| tutorial.sell | Lépj be a világító körbe, hogy eladd a kisállataidat. | |
| inventory.full | Tele a hátizsákod! Adj el kisállatokat, hogy legyen hely. | 57/60; "your" is the suffix -d |
| settings.music | Zene | Minecraft's word |
| settings.on | Be | pair "Ki" (Minecraft: BE/KI) |
| loading | Betöltés... | no space before the periods |
| event.ends_in | Vége {time} múlva | the banner's title and art name the event; "Esemény vége {time} múlva" is exactly 28 with "2 nap 5 ó" but 30 with "12 nap 23 ó"; "Esemény: még {time}" (22) keeps the word |
| item.op | Ez a kard nagyon OP! | "brutál erős" if OP feels too English |
| friends.boost | +{percent}% bónusz minden barátodért a szerveren | no space before %; "%-os" would also be safe |

## Sources
1. Microsoft Hungarian localization style guide (PDF, via https://aka.ms/hungarian-styleguide): https://download.microsoft.com/download/d/3/b/d3b023b0-ddf3-4692-b19f-72aff669e8a0/hun-hun-StyleGuide.pdf
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR Hungarian number symbols: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/hu/numbers.json
4. CLDR Hungarian unit names (duration abbreviations): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/hu/units.json
5. A magyar helyesírás szabályai, 12th ed. (AkH rules 216-217, 265, 275, 292): https://helyesiras.mta.hu/helyesiras/default/akh12
6. Roblox locale API (hu_hu: in-game content only, no app UI): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
7. Roblox language codes page (Hungarian = hu-hu): https://create.roblox.com/docs/production/localization/language-codes
8. Roblox on the Hungarian App Store (15 app languages, no Hungarian): https://apps.apple.com/hu/app/roblox/id431946152
9. Hungarian Wikipedia, Roblox (Robuxokat, Robloxban, élmények, fejlesztői termék, játékbérlet): https://hu.wikipedia.org/wiki/Roblox
10. HVG, Roblox tag page (press suffix usage: a Robloxon, a Robloxot): https://hvg.hu/cimke/roblox
11. Minecraft Java 1.21.4 Hungarian language file (te-register, placeholder patterns, game terms): https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21.4/assets/minecraft/lang/hu_hu.json
12. Roblox Studio install, content/fonts (cmap check of bundled fonts) and a Studio render of ő ű in each font, 2026-11-08: local check, no URL
13. Google Fonts source, Fredoka (cmap checked: no ő ű): https://github.com/google/fonts/tree/main/ofl/fredoka
14. Minecraft Bedrock Hungarian language file (Play, buy, collect, redeem, duration abbreviations, "Hoppá"): https://raw.githubusercontent.com/Mojang/bedrock-samples/main/resource_pack/texts/hu_HU.lang
15. Roblox API reference, Player.LocaleId (the account's locale): https://create.roblox.com/docs/reference/engine/classes/Player#LocaleId
16. Roblox docs, Localize with scripting (in-game Settings language switcher lists the game's languages): https://create.roblox.com/docs/production/localization/localize-with-scripting
