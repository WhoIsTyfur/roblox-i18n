# Slovak (sk-sk) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `sk-sk` (the only Slovak locale; no bare `sk` column needed) |
| Script, direction | Latin with diacritics (á ä č ď é í ĺ ľ ň ó ô ŕ š ť ú ý ž), LTR |
| Address the player as | informal singular "ty" (tykanie) everywhere; never "vy" or capitalized "Vy" |
| Text expansion vs English | about +5% overall on this guide's references; sentences -20% to +30%; short buttons +50-100% ("Buy" -> "Kúpiť", "On" -> "Zap.") |
| Plural categories (CLDR) | one, few, many, other |
| Model confidence | medium -- grammar is well documented and Slovak Minecraft shows real kids'-game wording, but Roblox has no Slovak UI to copy platform terms from, and Slovak kid gamer slang is barely documented online |
| Native review before shipping | strongly recommended (six cases, gender agreement on every adjective, constant risk of Czech bleed) |

## Audience and register
- Players are in Slovakia. Most Slovak kids read Czech easily and see a lot of Czech content, so MT and LLMs drift into Czech. Write standard Slovak only (see mistakes).
- Roblox's own website and app are not offered in Slovak: the Roblox locale API (checked 2026-11-08) has `sk_sk` off for the full experience and sign-up, on only for in-game content. Kids run Roblox in another language (likely English) and meet Slovak only inside games. Roblox's docs say players switch language in the in-game Settings menu, which lists the languages the game supports: add Slovak to the game's supported languages or players cannot pick it. Whether a Slovak device language selects `sk-sk` by itself is unverified; test with Studio's Player Emulator.
- Use "ty" in every string. Microsoft's Slovak guide uses "vy" for adult software ("Skontrolujte ho a zadajte ho znova") but asks for an informal tone in Copilot prompts; for a kids' game "Zadajte kód" reads like a school form. House choice: "Zadaj kód", "Vráť sa zajtra". Never mix both in one game.
- Buttons, tabs, toggles: infinitive or noun, as Microsoft does for menu items: "Hrať", "Kúpiť", "Získať", "Obchod". No final punctuation on buttons. Tips and tutorials: ty-imperative: "Vojdi do kruhu", "Predaj zvieratká".
- Natural hype: "Super!", "Paráda!", "Hurá!", "Nová úroveň!", "Nenechaj si to ujsť!".
- Microsoft's "modern voice" list, applied: "cez" not "prostredníctvom", "tento" not "nasledovný", "Načítava sa…" not "Prebieha načítavanie…". For "do X to get Y" avoid "pre"/"na" + verbal noun: Microsoft marks "Pre/Na získanie Pomocníka stlačte kláves F1" as wrong. Use a clause or the instrumental: "Ak chceš pokračovať, klikni sem", "Otvor stlačením E".
- Don't blame the player in errors: "Kód je neplatný", not "Zadal si zlý kód" (also gendered, see below).
- Kid-safe slang is fine in flavor text ("totálne OP", "noob" in a joke). No insults, no swearing.

## Roblox and gaming vocabulary
| English | Slovak | note |
|---|---|---|
| Robux | Robux | Latin. This guide keeps it invariant after a number, like a unit ("100 Robux", compare "100 XP"). Roblox's own Polish UI inflects Robux, so a native reviewer may prefer "za 100 Robuxov" (right for every price from 5 up, wrong for 1-4). Players' "robuxy/robuxov" in chat is unverified. |
| Premium | Premium | brand; "prémiové členstvo" in prose (unverified, no Slovak Roblox UI). |
| game pass | game pass / gamepass | in the shop show the pass name; players' spelling unverified. |
| developer product | name the item itself | players never see the term. |
| experience / game | hra | never "zážitok" or "skúsenosť" (skúsenosti = XP). Slovak Wikipedia says "hry", "hráči". |
| obby | obby | "prekážková dráha" in descriptions (unverified for Roblox players). |
| tycoon / simulator | tycoon / simulátor | |
| rebirth | rebirth (button); znovuzrodenie (formal) | "Znovuzrodenie" is 13 chars, too long for buttons; gamers keep "rebirth" (unverified). Never "Oživiť": Slovak Minecraft uses it for respawn. |
| pet | zvieratko, pl. zvieratká, gen. pl. zvieratiek | kid-friendly and neuter (easy agreement). "Maznáčik" (masc.) also works but turns every rarity label masculine ("Legendárny"); avoid "miláčik", mainly "darling". "pet/pety" in chat (unverified). |
| egg / hatch | vajce, pl. vajcia / vyliahnuť sa | "Z vajca sa vyliahol drak"; button "Otvoriť". |
| coins / gems | mince / drahokamy | "diamanty" if the art shows diamonds. |
| boost / multiplier | bonus / násobič, "2×" | "boost" is gamer talk (unverified); "bonus" is plain Slovak. |
| XP / level up | XP, skúsenosti / nová úroveň | Slovak Minecraft's UI writes both "úroveň skúseností" and "%s levelov skúsenosti", so "level" is real Slovak game wording; pick level or úroveň per game and keep it. |
| quest | úloha | "quest" among gamers (unverified). |
| leaderboard | rebríček; "Najlepší hráči" | |
| AFK | AFK | Latin capitals. |
| noob | nováčik (UI); noob (jokes) | |
| OP | OP; "neskutočne silný" | gamer use of OP in Slovak unverified. |
| VIP | VIP | "VIP server", "VIP výhody". |
| trade | výmena; vymeniť si | "trejdovať" in chat only (unverified). |
| inventory / backpack | inventár / batoh | Slovak Minecraft wording uses "inventár". |
| daily reward | denná odmena | |
| codes | kódy; "Zadaj kód"; redeem = "uplatniť" | never "vykúpiť". |
| group | skupina; "Pridaj sa do skupiny" | |
| like / favorite | like, "Daj hre like" / obľúbené, "Pridaj do obľúbených" | no Slovak Roblox labels exist to copy. |
| server | server, "na serveri"; súkromný server | |
| friends | priatelia (list labels); kamarát in sentences | English Roblox now says "connections"; no Slovak UI shows either. "priateľ" alone often means "boyfriend": "za každého kamaráta", not "za každého priateľa". |
| event | event; udalosť (formal) | "event" is common gamer Slovak (unverified). |

## Grammar traps in UI strings
- Plurals (CLDR): one = 1 ("1 minca"), few = 2-4 ("2 mince"), many = decimals ("1,5 mince"), other = 0 and 5+ ("5 mincí"). 22-24 fall in "other" ("22 mincí"). One string per key, so never put {count} right before a countable noun.
  - Bad: "{amount} mincí" -> "2 mincí". Good: "Mince: {count}", "Potrebuješ ešte {amount}." The verb must agree with "ty", not the number: "Chýba ti {amount}" breaks at 2-4 ("chýbajú ti 2").
  - Numbers drive verb agreement too: "2 hráči čakajú" but "5 hráčov čaká". Use "Čakajúci hráči: {count}".
  - Safe after a number: "{price} Robux", "{percent} %", "{multiplier}×", "{n} XP", "3 h 20 min".
- Gender: the past tense and the conditional agree with the subject, and {player} can be any gender. Use present tense: "{player} vstupuje do hry", "{player} ti ponúka výmenu". Microsoft's slash form "{player} sa pripojil/-a" is correct but clunky in a game.
- The player as "ty" is gendered too: "Získal si", "aby si zarábal", "Si pripravený?" all need -a for girls. Use present, future or imperative: "Získaš", "Zarábaj ďalej", "Môžeme začať?".
- Every adjective agrees, unlike Czech's invariant "-í" adjectives: legendárny drak, legendárna mačka, legendárne zvieratko. Translate rarity labels in the gender of one head noun (here neuter, for "zvieratko") and write "{rarity} zvieratko: {pet}!", never "{rarity} {pet}".
- Case: Slovak has six cases and a translated {pet} arrives in the nominative. Keep placeholders as subjects, after a colon or in parentheses; "Získal si {pet}" would need the accusative. Let a head noun carry the case: "Výmena s hráčom {player}". Never add endings to usernames.
- Vocalized prepositions (s/so, z/zo, v/vo, k/ku) depend on the next word: "so Zuzkou", "zo zvieratka", "ku kruhu". The word after a placeholder is unknown, so never write "s {player}"; put a head noun in between.
- "In {time}" is "o" + accusative: "Vráť sa o {time}"; Slovak Minecraft writes "obnovený bude o %s" the same way. "Za" + duration is the Czech pattern and in Slovak means how long something takes ("urobil to za hodinu"; norm not rechecked at JÚĽŠ). Time-of-day also uses "o" ("o 15:00"), so for countdowns a colon is clearest: "Do konca eventu: {time}".
- Rhythmic shortening: two long syllables can't follow each other in endings: "vzácny" (not "vzácný"), "legendárny", "krásne". Czech-looking "-ý" after a long syllable is a red flag.
- No articles: drop "a/the". Drop most "your": "Batoh je plný!" not "Tvoj batoh je plný!". When the possessive refers to the subject, use svoj: "Predaj svoje zvieratká", never "tvoje".
- Noun stacks become adjective + noun or a genitive: "Egg Shop" -> "Obchod s vajcami", "Pet Storage" -> "Úložisko zvieratiek". Digit + word compounds take a hyphen (Microsoft: "3-slovné"): "2-násobný bonus", "10-percentná zľava" (Czech writes these solid).
- Ordinals take a period: "5. úroveň"; "úroveň {level}" sidesteps it.
- Capitalization: sentence case for titles, buttons and item names: "Denná odmena", "Najlepší hráči", "Elixír šťastia".

## Typography and formatting
- No space before ! ? : ; and one space after, as in English.
- Quotes: „takto“ (low-high), nested ‚takto‘. Microsoft says never English "..." in Slovak and quote much less than English does; don't quote item names.
- Dashes: en dash with spaces as a sentence dash ("Si AFK – pohni sa!") and in ranges ("2017 – 2021" per Microsoft); never the em dash; hyphen without spaces inside compounds ("2-násobný").
- Numbers: decimal comma ("1,5"), thousands separated by a no-break space ("1 250"). The canonical {count} arrives as "1,250", which a Slovak player reads as 1.25 -- flag it to the developer; same for a multiplier "1.5".
- Percent: a no-break space before % (Microsoft, CLDR "#,##0 %"): "Šanca: 10 %", "+10 % bonus". The space stays in adjectival use too ("15 % zľava", per STN 01 6910 as cited by Slovak Wikipedia); the word form "10-percentný" is also correct. Czech drops the space there, and so do one Slovak handbook and Slovak Minecraft, but spaced is the norm. In this guide these spaces are real U+00A0; reproduce them.
- Multiplier: "2×" (U+00D7) after the number, no space; players type a Latin "2x".
- Time: compact timers "3 h 20 min", "45 s", "2 d. 5 h". CLDR's narrow Slovak units are "h", "min", "s" without periods but "d." with one, and Slovak Minecraft also shows "d."; Microsoft and Minecraft use "hod." and "min." too. Never "m" for minutes: m is meters. If code outputs "3h 20m" or "2d 5h", flag it.
- Ellipsis: one "…" or exactly three dots, no space before: "Načítava sa…".
- Keys stay Latin capitals: "Stlač E", "Otvor stlačením E". The key is masculine "kláves" (Microsoft: "stlačte kláves F1", "stlačením klávesu F1"; Minecraft: "Tento kláves"). Space bar = "medzerník".
- Microsoft asks for a no-break space after one-letter prepositions and conjunctions (a, i, k, o, s, u, v, z) so they never end a line: "v obchode". In Studio U+00A0 renders as a normal space and holds when wrapping (measured for the French guide, 2026-11-08).

## Do not translate / keep as is
- Robux, Roblox, Premium, VIP, Roblox Studio: Latin. Robux stays invariant after numbers in this guide (see the vocabulary table). Roblox declines in sentences like a masculine noun: "hrať na Robloxe", "hry na Robloxe".
- Game titles ("Pet Hatch Tycoon"): keep in English; players search the English title.
- Usernames and display names: never translate, decline or add endings.
- Promo codes ("FREEPETS"): exactly as given, ASCII, same case; translate only the text around them.
- Key names (E, Q, Shift) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Elixír šťastia"); no hybrids like "Lucky elixír". "Elixír šťastia" is exactly Slovak Minecraft's Potion of Luck, and Minecraft calls every potion "elixír". "Lektvar" reads Czech (Wiktionary has only a Czech entry); "nápoj" is just a drink.
- Established gamer loanwords may stay: AFK, XP, VIP, obby, tycoon, event, rebirth, like. Don't invent new ones.
- Never strip diacritics. Kids often chat without mäkčene and dĺžne, but UI text without them ("Ziskaj odmenu") looks broken.

## Rendering on Roblox
- Slovak needs Latin-1 (á ä é í ó ô ú ý) plus Latin Extended-A (č ď ĺ ľ ň ŕ š ť ž). Checked 2026-11-08 in the cmaps of the fonts bundled with the Roblox client (build of 2026-11-05): Builder Sans/Extended/Mono, Luckiest Guy, Bangers, Montserrat, Source Sans Pro, Roboto, Arimo, Nunito, Oswald, Press Start 2P, Titillium Web, Ubuntu and Comic Neue Angular have all 34 letters plus „ “ ‚ ‘ – … ×.
- Missing č ď ĺ ľ ň ŕ ť and capitals: **Fredoka One** (has š ž and the Latin-1 letters), Permanent Marker, Creepster, Highway Gothic, Accanthis ADF Std, Balthazar; Roman Antique also lacks ž, Denk One also š ž. In Fredoka One almost every Slovak string breaks ("Kúpiť", "Hrať", "Načítava sa"): switch sk-sk text to Builder Sans, Luckiest Guy or Bangers. Studio draws missing letters from a thin sans fallback, mixed into the word (measured for the Polish guide, 2026-11-08).
- Lowercase ď ť ľ and capital Ľ carry a caron shaped like an apostrophe; that is correct, not a bug. Rendered from the bundled files with FreeType (not Roblox's renderer): Builder Sans and Luckiest Guy keep it tight to the letter; Bangers draws Ľ with a detached tick that reads like "L'". Luckiest Guy and Bangers are caps-only. Capitals with marks (Č Ľ Š Ž Á Ô) are taller; check tight TextScaled labels for clipping (unverified).
- Luau string.upper changes only ASCII: "získaš" -> "ZíSKAš". Write uppercase text directly in the table or use a UTF-8-aware helper.
- Slovak letters are 2 bytes in UTF-8: string.sub and # can split "ľ" into a broken glyph; utf8.len and utf8.offset are safe.
- Verify in Studio: Player Emulator set to Slovak; a TextLabel with the pangram "Kŕdeľ šťastných ďatľov učí pri ústí Váhu mĺkveho koňa obhrýzať kôru a žrať čerstvé mäso." (every Slovak diacritic) and its uppercase form in every font the game uses; the longest strings (rebirth confirm, inventory full) at phone size.

## Mistakes machine translation makes here
- Czech bleed: "Koupit", "Hrát", "odměna", "zdarma", "dost" -> "Kúpiť", "Hrať", "odmena", "zadarmo", "dosť". Czech-only letters ř ě ů never appear in Slovak.
- Czech adjective forms: "Legendární drak" -> "Legendárny drak"; "Vzácný" -> "Vzácny".
- "experience" as zážitok: "Najlepší zážitok na Robloxe" -> "Najlepšia hra na Robloxe".
- "Claim" as nárokovať: "Nárokovať" -> "Získať"; "redeem" as vykúpiť: "Vykúpiť kód" -> "Uplatniť kód".
- Purpose with "pre"/"na" + verbal noun (Microsoft marks both wrong): "Stlač E pre otvorenie" -> "Otvor stlačením E".
- Register mixing: "Stlačte E a získaš odmenu" -> "Stlač E a získaš odmenu".
- Gendered past with a username: "{player} sa pripojil k hre" -> "{player} vstupuje do hry".
- Number + noun: "Máš {count} mincí" -> "Mince: {count}".
- Preposition before a placeholder: "Výmena s {player}" -> "Výmena s hráčom {player}".
- English Title Case: "Denná Odmena" -> "Denná odmena".
- Literal slang: "Tento meč je premožený" (= defeated) -> "Tento meč je totálne OP!".
- English number and percent format: "Získaj 1,250 mincí a 10% bonus" -> "Mince: 1 250", "+10 % bonus".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Hrať | infinitive on buttons |
| shop.title | Obchod | |
| shop.buy | Kúpiť | |
| reward.claim | Získať | "Vyzdvihnúť" is exactly 10 |
| rebirth.button | Rebirth | kept English: "Znovuzrodenie" is 13 > max 10 |
| rebirth.confirm | Urobiť rebirth teraz? Prídeš o mince, ale získaš trvalý bonus {multiplier}×. | future tense avoids gender; "1.5" should arrive as "1,5" |
| coins.need_more | Málo mincí! Potrebuješ ešte {amount}. | no noun after the number, and the verb agrees with "ty", so 1, 2 and 5 all work |
| coins.count | Mince: {count} | colon avoids plural forms; "1,250" should be "1 250" (code issue) |
| egg.hatched | {rarity} zvieratko: {pet}! | rarity in the neuter, agreeing with "zvieratko"; "hatched" is left to the toast's context, since "Vyliahlo sa ti {rarity} ..." runs over 40 and puts a capitalized {rarity} mid-sentence |
| rarity.legendary | Legendárne | neuter to match "zvieratko"; use "Legendárny" if the game's head noun is "predmet" |
| pet.name.dragon | Drak | |
| chat.player_joined | {player} vstupuje do hry | present tense avoids gender |
| trade.request | {player} ti ponúka výmenu | present tense avoids gender |
| prompt.open_shop | Otvor stlačením E | 17/22; Minecraft's pattern ("Skoč stlačením ..."); not "pre/na otvorenie" |
| pass.buy_price | Kúpiť za {price} Robux | Robux invariant; "Robuxov" if no price is under 5 (native call) |
| pass.coins2x | 2× viac mincí | 13/14; "×" is U+00D7 |
| pass.vip | VIP | |
| reward.daily_title | Denná odmena | |
| reward.come_back | Vráť sa o {time} po ďalšiu odmenu! | "o" + duration = "in", never "za"; time should be "3 h 20 min" |
| codes.placeholder | Zadaj kód | |
| codes.invalid | Kód je neplatný alebo už vypršal. | |
| social.like_reward | Daj hre like a získaš zadarmo <b>Elixír šťastia</b>! | "elixír" accusative = nominative, so the tag wraps the plain name |
| social.group_reward | Pridaj sa do našej skupiny a získaj odmenu zadarmo! | 51/55; "získaj", not the calque "odomkni" |
| afk.warning | Si AFK! Pohni sa a zarábaj ďalej! | imperatives avoid gendered "aby si zarábal" |
| leaderboard.title | Najlepší hráči | "Rebríček" also fine |
| level.up | Nová úroveň! Teraz si na úrovni {level}. | 40/45; "Level up! Teraz máš level {level}." if the game says level |
| tutorial.sell | Vojdi do svietiaceho kruhu a predaj zvieratká. | "your" dropped |
| inventory.full | Batoh je plný! Predaj zvieratká a uvoľni miesto. | |
| settings.music | Hudba | |
| settings.on | Zap. | pair with "Vyp."; Slovak Minecraft shows "ZAP"/"VYP"; "Zapnuté" (7) if space allows |
| loading | Načítava sa… | Microsoft's "-uje sa…" pattern; single ellipsis character |
| event.ends_in | Do konca eventu: {time} | 25/28 with "2 d. 5 h"; colon avoids "o" reading as a clock time |
| item.op | Tento meč je totálne OP! | gamer OP unverified; fallback "Tento meč je neskutočne silný!" |
| friends.boost | +{percent} % bonus za každého kamaráta na serveri | space before %; "kamaráta" avoids the boyfriend reading of "priateľa" |

## Sources
1. Microsoft Slovak localization style guide (PDF, via https://aka.ms/slovak-styleguide): https://download.microsoft.com/download/2/9/8/298bd25a-ac5b-4700-ab57-a86e0c268a78/slk-svk-StyleGuide.pdf
2. Microsoft localization style guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR Slovak number symbols and formats: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/sk/numbers.json
5. Roblox language codes (Slovak = `sk` / `sk-sk`): https://create.roblox.com/docs/production/localization/language-codes
6. Roblox locale API (sk_sk, cs_cz and pl_pl flags; checked 2026-11-08): https://locale.roblox.com/v1/locales
7. Roblox on the Slovak App Store (description English only, no Slovak listing): https://apps.apple.com/sk/app/roblox/id431946152
8. Slovak Wikipedia, "Roblox" (hry, hráči, Robux): https://sk.wikipedia.org/wiki/Roblox
9. Slovak Wikipedia, "Minecraft" (server, hráč, inventár, skúsenosti/XP): https://sk.wikipedia.org/wiki/Minecraft
10. English Wiktionary, "lektvar" (Czech entry only): https://en.wiktionary.org/wiki/lektvar
11. Font files bundled with the Roblox Windows client, cmap read with fontTools, 2026-11-08: `%LOCALAPPDATA%\Roblox\Versions\<version>\content\fonts`
12. Minecraft Java Slovak language file (elixír, level/úroveň, kláves, "o %s", ZAP/VYP, d./hod./min.): https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21.4/assets/minecraft/lang/sk_sk.json
13. Roblox docs, react to users switching languages (in-game Settings language menu): https://create.roblox.com/docs/production/localization/localize-with-scripting
14. Slovak Wikipedia, "Percento" (space before % also in adjectival use, STN 01 6910): https://sk.wikipedia.org/wiki/Percento
15. CLDR Slovak units (narrow "d.", "h", "min", "s"): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/sk/units.json
