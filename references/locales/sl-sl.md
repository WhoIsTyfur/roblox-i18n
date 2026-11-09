# Slovenian (sl-sl) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `sl-sl` (Roblox's id, not the standard `sl-si`; the only Slovenian locale, so a bare `sl` column adds nothing and whether Roblox reads `sl-si` is unverified). Never confuse with Slovak `sk-sk` |
| Script, direction | Latin with č š ž (Č Š Ž), LTR. No ć, đ or accented vowels |
| Address the player as | informal singular "ti" everywhere; never "vi"/"Vi" |
| Text expansion vs English | +12% over the reference set; sentences -12% to +41%; short labels up to double ("Shop" -> "Trgovina", "On" -> "Vklop") |
| Plural categories (CLDR) | one, two, few, other -- Slovenian has a living dual (dvojina) |
| Model confidence | medium -- LLMs slip in Croatian or Slovak words, miss the dual and write gendered past and future forms for "you" |
| Native review before shipping | strongly recommended |

## Audience and register
- Roblox itself is not in Slovenian. The locale API (checked 2026-11-08) lists `sl_sl` (native name "Slovenski") for in-game content only, not for the site and app; roblox.com/sl/ redirected to the English site, and the Google Play and Xbox sl-SI store pages show Slovenian store chrome around an English Roblox description. Players read Roblox in English and know the English gaming words; your game may be the only Slovenian they see there.
- A Roblox search for "slovenija" and "slovenski" (2026-11-08) found no Slovenian-language games, so player slang below is marked (unverified) unless a dictionary backs it.
- Use "ti" in every string. Microsoft's guide uses "vi" for adult software, but Minecraft's Slovenian, the closest kid-game model, uses ti ("Odpri svoj inventar", "Pritisni %s"). Never mix: "Pritisni E in prevzemi nagrado", not "Pritisnite E in prevzemi".
- Buttons: 2nd-person singular imperative, as in Microsoft's and Minecraft's buttons ("Prekliči", "Nazaj"): "Igraj", "Kupi", "Prevzemi". Never the infinitive ("Kupiti") or plural ("Kupite"). Titles and tabs: nouns ("Trgovina", "Nastavitve"). Ongoing process: verbal noun ("Nalaganje ...").
- Prefer the present tense, as Microsoft advises: "Dobiš trajen bonus", not "Dobil boš". It is shorter and, with ti, gender-free (see Grammar traps).
- Hype is short exclamations: "Bravo!", "Super!", "Odlično!", "Juhu!", "Srečno!". Microsoft warns that most English "!" in error messages should become a period: "Koda ni veljavna.", not "Koda ni veljavna!".
- Drop English possessives: "Nahrbtnik je poln!", not "Tvoj nahrbtnik je poln!" (Microsoft: "Vklopite računalnik", never "vaš računalnik"). If one is needed, use reflexive "svoj".
- Write standard Slovenian. Colloquial "ful", "fajn", "kul" read as adult imitation of teen talk; no dialect. Kid-safe: no insults ("butec", "kreten"); "noob" only in a friendly joke.

## Roblox and gaming vocabulary
| English | Slovenian | note |
|---|---|---|
| Robux | Robux | Latin, undeclined after a number in UI, like a currency code ("100 EUR"): "Kupi za 100 Robux". In prose players likely decline it ("robuxov", unverified). |
| Premium | Premium | brand; "naročnina Premium" if a noun is needed. |
| game pass | game pass; prepustnica | players keep the English (unverified); in the shop just show the pass name. |
| developer product | izdelek; paket | players never see the term; name the item. |
| experience / game | igra | never "izkušnja" (that is the XP word: Minecraft "točke izkušenj"). |
| obby | obby; parkur | "parkur" in descriptions (unverified which players prefer). |
| tycoon | tycoon | keep English in titles. |
| simulator | simulator | |
| rebirth | prerod; verb preroditi se | SSKJ² and Pravopis prefer "prerod"; "preporod" is marked bookish (knjiž., neobč.). "Ponovno rojstvo" is 15 chars; players likely say "rebirth" (unverified). |
| pet | ljubljenček, pl. ljubljenčki | Slovenian, not Croatian "ljubimac"; "pet" in chat (unverified). |
| egg / hatch | jajce (pl. jajca) / izvaliti se | Minecraft "Jajce". "Izvalil se je zmaj"; button "Odpri". |
| coins | kovanci (kovanec, m.) | never Croatian "novčići". |
| gems | dragulji (dragulj, m.) | "diamanti" if the art shows diamonds (Minecraft "Diamant"). |
| boost | bonus; okrepitev | "boost" in chat (unverified). |
| multiplier | množitelj; "x2" | |
| XP | XP; točke izkušenj | Minecraft wording. Pick one per game. |
| level up | nova stopnja; stopnja | Minecraft "stopnja izkušenj". SSKJ marks "nivo" as journalistic; "level" in chat (unverified). |
| quest | naloga; misija | |
| leaderboard | lestvica | "Najboljši igralci" if space allows. |
| AFK | AFK | Latin. |
| noob | začetnik (UI); noob (jokes) | |
| OP | noro močan; nepremagljiv | Pravopis marks "noro" (= zelo) emphatic, not colloquial; "premočan" reads as a complaint. "OP" also kept by gamers (unverified). |
| VIP | VIP | |
| trade | menjava; menjati | "Ponudi menjavo", "Sprejmi". |
| inventory / backpack | inventar / nahrbtnik | inventar as in Minecraft; never Croatian "ruksak". |
| daily reward | dnevna nagrada | weekly: "tedenska nagrada". |
| codes | kode (koda, f.); "Vnesi kodo" | redeem = "unovči kodo". |
| group | skupina | Microsoft's word; "Pridruži se naši skupini". |
| like / favorite | všečkati, "Všečkaj igro" / priljubljene, "Dodaj med priljubljene" | SSKJ² lists "všečkati" unmarked; "lajkati" is colloquial (Sprotni slovar). "Priljubljene" is Microsoft's Favorites. |
| server | strežnik | Microsoft and Minecraft ("Pridruži se strežniku"); kids say "server" (unverified). |
| friends | prijatelji | Roblox's UI is English, so players see "Friends"/"Connections"; in game always "prijatelji", never "povezave" or "stiki". |

## Grammar traps in UI strings
- Plurals (CLDR, by the last two digits): one = 1, 101, 201 (21 is NOT one); two = 2, 102; few = 3-4, 103-104 and all decimals; other = 0, 5-20, 21, 100. Nouns: "1 kovanec, 2 kovanca, 3 kovanci, 5 kovancev"; "1 nagrada, 2 nagradi, 3 nagrade, 5 nagrad"; "1 jajce, 2 jajci, 3 jajca, 5 jajc". One string per key, so never put {count} before a countable noun.
  - Bad: "{amount} kovancev" -> "1 kovancev", "2 kovancev", "3 kovancev". Good: "Kovanci: {count}", "Manjka še: {amount}".
  - Safe after a number: undeclined units "{price} Robux", "{percent} %", "x{count}", and ordinals "{level}. stopnja".
- The dual (dvojina) also changes verbs, adjectives and pronouns: "1 igralec čaka, 2 igralca čakata, 3 igralci čakajo, 5 igralcev čaka"; "2 nova ljubljenčka"; two keys = "tipki" (Microsoft: "pritisnete tipki SHIFT+F5"); you two = "vidva". Never write the plural for two: "2 kovanci", "Ostali so 2 dni" -> "2 kovanca", "Ostala sta 2 dneva". Avoid spelled-out units in {time} (dneva/dni/dni); use CLDR abbreviations, which never change.
- Gender of {player}: past tense uses the l-participle, which agrees ("pridružil se je" m., "pridružila se je" f.). Use the present ("{player} je zdaj v igri", "{player} ti ponuja menjavo") or a colon ("Zmaga: {player}!"). No slashes: Minecraft's "Rad/a bi jih prijavil/a" is what not to copy.
- Gender of "you": past, future and conditional are all gendered with ti: "Izvalil si", "Dobil boš", "Bi rad kupil?". Use the present ("Dobiš ..."), "želiš" ("Želiš kupiti?") or a noun. Minecraft's "Umrl si!" assumes a boy.
- Adjectives agree in gender, number and case: legendarni zmaj (m.), legendarna mačka (f.), legendarno jajce (n.). Translate rarity labels in the masculine, agreeing with an implied "ljubljenček", and write "{rarity} ljubljenček ... {pet}", never "{rarity} {pet}".
- Definite vs indefinite adjective (Microsoft; visible only in masc. nom./acc.): English "a" -> indefinite ("brezplačen napoj", "trajen bonus", "neveljaven parameter"); "the", or a fixed type name -> definite ("svetleči krog", "trdi disk"). After "ta", "svoj", "ves" always definite ("ta legendarni zmaj"); after "vsak" indefinite ("vsak nov igralec").
- Case: names cannot be declined. Keep {player} and {pet} in the nominative (subject or after a colon), or let a head noun take the case: "Menjava z igralcem {player}", not "Menjava s {player}om".
- Never put s/z or k/h straight before a placeholder: the choice depends on the next sound ("s Petrom" but "z Ano"; "k Ani" but "h Kristini"). Rewrite: "z igralcem {player}", "k igralcu {player}".
- Clitics (je, se, si, ti, mi, bo) go in second position: "Nahrbtnik je poln!", "{player} ti ponuja menjavo", "Izvalil se je zmaj".
- English noun stacks become noun + genitive or adjective: "Pet Storage" -> "shramba ljubljenčkov", "Coin Boost" -> "bonus za kovance", "Daily Reward" -> "Dnevna nagrada".
- Capitalization: sentence case for titles and buttons ("Dnevna nagrada"); item names capitalize only the first word ("Napoj sreče"); days and months lowercase ("sobota", "december"); non-sentence text in parentheses lowercase ("(priporočeno)", Microsoft).
- No articles; never add "en"/"ena" for English "a": "a free reward" -> "brezplačno nagrado", not "eno brezplačno nagrado".

## Typography and formatting
- No space before ! ? : ; and one space after: "Bravo! Nova stopnja!".
- Quotation marks »...« (Microsoft, all software text); never "...", '...' or „...“. Don't quote button names in short game text.
- Ellipsis takes a space before it (Microsoft): "Nalaganje ...", "Povezovanje ...". Minecraft's "Povezovanje na strežnik..." breaks this rule.
- Dash: en dash with spaces " – " for a break ("Ta meč – noro močan!"); en dash without spaces in ranges ("8–21"); Slovenian has no em dash (Microsoft).
- Numbers: group separator period, decimal comma (Microsoft, CLDR): "1.250", "1,5". A {count} preformatted as "1,250" reads as one and a quarter, and multiplier "1.5" as fifteen hundred -- flag both to the developer.
- Percent: no-break space (U+00A0) before % (CLDR "#,##0 %"): "+10 %". Roblox's bundled Fredoka One, Balthazar and Roman Antique have no U+00A0 glyph; with those fonts use a normal space.
- Multiplier: Latin x: "x2", "Kovanci x2". Never Cyrillic "х".
- Durations (CLDR short): "3 h 20 min", "2 d", "45 sek." (narrow form "45 s"). Developer-formatted "3h 20m" is readable, but "m" is the metre symbol -- ask for "min".
- Ordinal = numeral + period: "5. stopnja", "1. mesto". Abbreviations take a period ("npr.", "št.", "itd."); acronyms don't ("XP", "VIP").
- Keys stay Latin; key = "tipka": "Pritisni E", "Odpri s tipko E". Space bar = "preslednica", left mouse button = "levi gumb" (Minecraft). "Shift", "Ctrl" unchanged.
- Words run long ("ljubljenčkov", "Nalaganje"); enable TextWrapped, never hand-hyphenate.

## Do not translate / keep as is
- Robux, Roblox, Premium, VIP, Roblox Studio: Latin, undeclined after a number. In prose Roblox declines normally: "na Robloxu", "igre na Robloxu".
- Game titles ("Pet Hatch Tycoon"): keep English; players search the English title.
- Usernames and display names: never translate, transliterate or decline; give them a head noun when a case is needed ("igralcu {player}").
- Promo codes ("FREEPETS"): exactly as given, same case; translate only the text around them.
- Key names (E, Q, Shift) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Napoj sreče", Minecraft's Slovenian name for the Potion of Luck); brand-like invented names may stay English.
- Acronyms decline with a hyphen when needed (Microsoft: "PIN-a", "RAM-a"): "brez VIP-a", "z VIP-om".
- Script: Latin only, letters č š ž. Croatian ć đ, Slovak ä ľ ô ť ň and accented á é í ó ú are never correct in Slovenian UI text -- they mean the model drifted into another language.

## Rendering on Roblox
- Slovenian needs only Č č Š š Ž ž (U+010C-010D, U+0160-0161, U+017D-017E) plus » « – … and U+00A0. Š and Ž sit in Windows-1252; Č does not, so č is the letter that goes missing.
- Checked 2026-11-08 by reading the character maps of the font files bundled with the installed Roblox client: Builder Sans, Builder Extended, Source Sans Pro, Montserrat, Arimo, Roboto, Nunito, Oswald, Bangers, Luckiest Guy, Press Start 2P, Titillium Web, Ubuntu, Jura and Kalam have every glyph above.
- Missing č/Č in the bundled files (Enum.Font name from the client's family table in brackets): Fredoka One, Permanent Marker, Creepster, Highway Gothic (Highway), Accanthis ADF Std (Bodoni), Balthazar (Fantasy). Roman Antique (Antique) also lacks ž; Denk One lacks č, š and ž. Inconsolata (Code) lacks the en dash. Google's newer Fredoka has latin-ext, but Roblox ships the old Fredoka One.
- Fredoka One is common in simulator UIs: "Prevzemi" renders, but "Všečkaj", "ljubljenček" and "Napoj sreče" hit the missing č. Switch those labels to Builder Sans or Luckiest Guy for sl-sl. A Studio check with Polish letters (2026-11-08, see pl-pl) showed no boxes: the client draws a missing letter from a thin sans fallback, so "ljubljenček" in Fredoka One mixes two fonts in one word (not yet tested with č).
- Carons on capitals (Č Š Ž) add height and can clip in tight TextScaled labels or ALL-CAPS styles (unverified).
- Verify in Studio: Player Emulator set to sl-sl; open every panel with the longest strings; paste "Čez žgečkljivo šumečo goščavo – ČŠŽ čšž »« ..." into each font face used.

## Mistakes machine translation makes here
- Croatian words: "Novčići", "Glazba", "Postavke", "Učitavanje", "ljubimac", "razina", "ruksak", "igrač" -> "Kovanci", "Glasba", "Nastavitve", "Nalaganje", "ljubljenček", "stopnja", "nahrbtnik", "igralec".
- Slovak/Slovenian mix-up (sk vs sl): "Slovenčina", "Hrať", "Kúpiť" -> "Slovenščina", "Igraj", "Kupi".
- Plural for two: "2 kovanci", "2 igralci sta" -> "2 kovanca", "2 igralca sta".
- Number + noun: "Imaš {count} kovancev" -> "Kovanci: {count}".
- Gendered "you": "Izvalil si legendarnega zmaja!", "Dobil boš bonus" -> "{rarity} ljubljenček izvaljen: {pet}!", "Dobiš bonus".
- Gendered past with a username: "{player} se je pridružil igri" -> "{player} je zdaj v igri".
- "experience" as izkušnja: "Najboljša izkušnja na Robloxu" -> "Najboljša igra na Robloxu".
- "Claim" as zahtevati (= demand): "Zahtevaj" -> "Prevzemi"; "redeem" as odkupiti: "Odkupi kodo" -> "Unovči kodo".
- Formal register, infinitive buttons and possessives: "Pritisnite E", "Kupiti", "Vaš nahrbtnik je poln" -> "Pritisni E", "Kupi", "Nahrbtnik je poln!".
- Title Case: "Dnevna Nagrada", "Napoj Sreče" -> "Dnevna nagrada", "Napoj sreče".
- Punctuation: "Nalaganje...", "Koda je napačna!", straight-quoted 'Shrani' -> "Nalaganje ...", "Koda ni veljavna.", »Shrani«.
- Split "V redu" written as "Vredu" (even Minecraft's OK button has it) -> "V redu".

## Reference translations
Lengths: `scripts/i18n.py lint` counts visible text without <b> tags or {params}; where it matters, the length with a sample value follows.

| key | translation | note |
|---|---|---|
| menu.play | Igraj | 2sg imperative |
| shop.title | Trgovina | |
| shop.buy | Kupi | |
| reward.claim | Prevzemi | 8/10; not "Zahtevaj" |
| rebirth.button | Prerod | 6/10; the dictionaries' unmarked word ("Preporod" is bookish); "Ponovno rojstvo" is 15 |
| rebirth.confirm | Prerod zdaj? Izgubiš kovance, dobiš pa trajen bonus x{multiplier}. | present tense avoids gendered "izgubil boš"; indefinite "trajen" for "a permanent" (Microsoft); "1.5" must reach the player as "1,5" -- code issue |
| coins.need_more | Premalo kovancev! Manjka še: {amount} | colon avoids kovanec/kovanca/kovanci/kovancev; 34/40 with "1.250" |
| coins.count | Kovanci: {count} | "1,250" should be "1.250" -- code issue |
| egg.hatched | {rarity} ljubljenček izvaljen: {pet}! | participle and rarity agree with "ljubljenček", so the pet's gender doesn't matter; 38/40 with Legendarni + Zmaj. Headline participle like Minecraft's toasts ("Cilj dosežen!"); {rarity} stays first so its capital is right. "... se je izvalil: ..." is 43, too long |
| rarity.legendary | Legendarni | masculine definite, agrees with implied "ljubljenček" |
| pet.name.dragon | Zmaj | masculine |
| chat.player_joined | {player} je zdaj v igri | present avoids pridružil/pridružila (Minecraft's "%s se je pridružil igri" assumes a boy); "se pridružuje" would mean still joining |
| trade.request | {player} ti ponuja menjavo | |
| prompt.open_shop | Pritisni E, da odpreš | 21/22; Minecraft's "Pritisni ..., da odpreš" pattern; "Odpri s tipko E" (15) if tighter |
| pass.buy_price | Kupi za {price} Robux | Robux undeclined |
| pass.coins2x | Kovanci x2 | |
| pass.vip | VIP | acronym, kept as players know it |
| reward.daily_title | Dnevna nagrada | 14/18 |
| reward.come_back | Vrni se čez {time} po naslednjo nagrado! | best with "3 h 20 min" |
| codes.placeholder | Vnesi kodo | |
| codes.invalid | Koda ni veljavna ali je potekla. | period, not "!", per Microsoft |
| social.like_reward | Všečkaj igro in dobi brezplačen <b>Napoj sreče</b>! | 44/55 (51 with the tags); indefinite "brezplačen" for "a free"; č needs a font that has it |
| social.group_reward | Pridruži se naši skupini in odkleni brezplačno nagrado! | 55/55, no margin; "odkleni" keeps "unlock"; "dobi" (52) if the banner overflows |
| afk.warning | AFK si. Premakni se in služi naprej! | avoids gendered "neaktiven/neaktivna" |
| leaderboard.title | Lestvica | "Najboljši igralci" is 17 > 16; "Top igralci" (11) is colloquial anglicism |
| level.up | Nova stopnja! Zdaj si na stopnji {level}. | never "nivo" in UI |
| tutorial.sell | Stopi v svetleči krog in prodaj ljubljenčke. | definite "svetleči" for "the glowing circle" |
| inventory.full | Nahrbtnik je poln! Prodaj ljubljenčke in sprosti prostor. | 57/60; "your" dropped |
| settings.music | Glasba | never "Glazba" |
| settings.on | Vklop | 5/5; Off = "Izklop" (6): if Off has the same 5 limit, use Minecraft's "Da"/"Ne" pair for both |
| loading | Nalaganje ... | space before the ellipsis (Microsoft); 13/14 |
| event.ends_in | Konec dogodka čez {time} | 25/28 with "2 d 5 h" |
| item.op | Ta meč je noro močan! | "noro" = emphatic "zelo" (Pravopis), upbeat and kid-safe; "Ta meč je nepremagljiv!" if the game's tone is plainer; kept "OP" unverified |
| friends.boost | Bonus +{percent} % za vsakega prijatelja na strežniku | no-break space before %; generic masculine "prijatelja" is normal for "each friend" |

## Sources
1. Microsoft Localization Style Guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
2. Microsoft Slovenian localization style guide (PDF, via https://aka.ms/slovenian-styleguide): https://download.microsoft.com/download/0/d/7/0d705b3b-662f-4d88-b35e-3b166941c6ce/slv-svn-StyleGuide.pdf
3. CLDR JSON, plural rules (sl: one, two, few, other): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-core/supplemental/plurals.json
4. CLDR JSON, Slovenian number symbols and percent pattern: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/sl/numbers.json
5. CLDR JSON, Slovenian duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/sl/units.json
6. Roblox locale API (sl_sl "Slovenski": in-game content only, not full experience): https://locale.roblox.com/v1/locales
7. roblox.com/sl/charts redirected to the English site (2026-11-08): https://www.roblox.com/sl/charts
8. Google Play Roblox page in Slovenian (Slovenian store chrome, English description): https://play.google.com/store/apps/details?id=com.roblox.client&hl=sl
9. Xbox Store Roblox page, sl-SI (English description): https://www.xbox.com/sl-SI/games/store/roblox/BQ1TN1T79V9K
10. Roblox omni-search for "slovenija"/"slovenski" (no Slovenian-language games found): https://apis.roblox.com/search-api/omni-search?searchQuery=slovenija&sessionId=x&pageType=all
11. Minecraft Java 1.21.4 Slovenian language file (game UI conventions): https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21.4/assets/minecraft/lang/sl_si.json
12. Fran, "všečkati" (SSKJ², unmarked): https://fran.si/iskanje?View=1&Query=v%C5%A1e%C4%8Dkati
13. Fran, "lajkati" (Sprotni slovar, colloquial): https://fran.si/iskanje?View=1&Query=lajkati
14. Fran, "nivo" (SSKJ², journalistic; see raven, stopnja): https://fran.si/iskanje?View=1&Query=nivo
15. Google Fonts metadata (font subsets), e.g.: https://raw.githubusercontent.com/google/fonts/main/ofl/fredoka/METADATA.pb
16. Character maps of the font files in the installed Roblox client (content/fonts, read locally 2026-11-08); Enum.Font names from the client's content/fonts/families/*.json and the family order in RobloxPlayerBeta.exe.
17. Fran, "preporod" (SSKJ² knjiž.; Pravopis neobč. -> prerod): https://fran.si/iskanje?View=1&Query=preporod and "prerod" (unmarked): https://fran.si/iskanje?View=1&Query=prerod
18. Fran, "noro" (Pravopis: emphatic, = zelo): https://fran.si/iskanje?View=1&Query=noro
19. Polish guide's Studio check of missing-glyph fallback (2026-11-08): references/locales/pl-pl.md
