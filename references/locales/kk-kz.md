# Kazakh (kk-kz) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `kk-kz` (the only Kazakh locale Roblox lists, so no bare `kk` column is needed; Roblox labels it "Қазақ Тілі" in Cyrillic) |
| Script, direction | Cyrillic (Russian letters plus Ә Ғ Қ Ң Ө Ұ Ү Һ І), LTR. Never the Latin or Arabic Kazakh alphabets in game text |
| Address the player as | informal singular "сен" (verbs in -сың/-сің, bare imperative stem); never "сіз", never -ыңыз/-іңіз forms |
| Text expansion vs English | measured on the reference set: sentences -10% to +35% (about +10% overall), titles up to +40% ("Daily Reward" -> "Күнделікті сыйлық"); some buttons shrink ("Claim" -> "Алу"). The real risk is long agglutinated words ("айырбастасқысы") |
| Plural categories (CLDR) | cardinal: one, other; ordinal: many, other. Irrelevant in UI: nouns after a number stay singular |
| Model confidence | medium: lower-resource language; models slip into Russian words, Russian letters instead of Kazakh ones, and wrong vowel-harmony suffixes |
| Native review before shipping | strongly recommended |

## Audience and register
- Script decision: write Cyrillic. Kazakhstan adopted a Latin alphabet in 2021 with a phase-in planned for 2023-2031, but Cyrillic is what kids read at school and on screens today (classroom status in 2026 unverified), and Roblox itself labels the language in Cyrillic. Latin Kazakh ("Qazaq tili") would look like a different language to most 9-16 year olds.
- Kazakhstan is bilingual: Russian is also official and dominant in many cities, so many kids play Roblox in Russian or English. A player who gets the kk-kz column wants real Kazakh. Never fall back to Russian words when a common Kazakh one exists: "дүкен", not "магазин"; "сыйлық", not "награда"; "айдаһар", not "дракон".
- Platform status (Roblox locale API, checked 2026-11-08): kk_kz is enabled for in-experience text only, not for the Roblox app, site or sign-up. Kazakh players see Roblox's own UI in Russian or English, so there are no official Roblox Kazakh platform terms; follow the table below. A player can get `LocaleId` = `kk-kz` only by picking Kazakh in the in-experience menu (Roblox icon > Settings > language), and that list shows only languages the creator enabled in the experience's localization settings (DevForum, 2022), so enable Kazakh there. Not tested live for kk-kz; check with Studio's Player Emulator. Roblox does not auto-translate Kazakh: every empty key shows the source text.
- Use "сен" everywhere. The Kazakh Minecraft translation is mixed: its system, server and account messages use сіз ("басыңыз"), but everything about play (advancements, tutorial hints, the death screen) uses сен ("Мақсатыңа жеттің!", "Инвентарыңды аш", "Өліп қалдың!"). A game's UI is all play text. Microsoft's guide uses сіз, but that is adult software. Never mix: "E-ні басыңыз, сыйлық аласың" -> "E-ні бас, сыйлық аласың".
- Buttons, tabs and toggles: infinitive in -у/-ю or a noun, the Kazakh software norm (Microsoft: "Сақтау"; Minecraft: "Жалғастыру", "Бірге ойнау"): "Ойнау", "Алу", "Дүкен". Sentences and tips: сен-imperative: "Жануарларыңды сат", "Шеңберге кір".
- Hype that sounds natural: "Жаңа деңгей!", "Керемет!", "Тамаша!", "Жарайсың!", "Жаңа жетістік!". Stiff or adult: "өтінеміз" (please; Microsoft says never use it), "қажет" in instructions (sounds rude per Microsoft), "жүзеге асыру", "аталмыш".
- Errors stay neutral, no blame: "Код қате" rather than "Сен қате код енгіздің".
- Translate "your" only when ownership matters (Microsoft rule): "Сөмке толы!", not "Сенің сөмкең толы!".
- Kid-safe slang only; no insults or crude words, even in jokes.

## Roblox and gaming vocabulary
| English | Kazakh | note |
|---|---|---|
| Robux | Robux | Latin; case endings after a hyphen by pronunciation ("Робакс"): "Robux-қа", "Robux-ты". Kazakh Wikipedia writes "Roblox-тағы". |
| Premium | Premium | Latin, as on Kazakh Wikipedia ("Premium жазылымы"). |
| game pass | геймпасс (chat, unverified) | in the shop just show the pass name. |
| developer product | name the item | players never see the term. |
| experience / game | ойын | never "тәжірибе" (= experience as XP or life experience). |
| obby | обби (unverified) | "паркур" in descriptions. |
| tycoon / simulator | тайкун (unverified) / симулятор | |
| rebirth | қайта туу; "Қайта туасың ба?" | button "Қайта туу" (9). Russian chat slang "ребёрт": not in UI. |
| pet | жануар, жануарлар | "үй жануары" is the dictionary word but long; never Russian "питомец". "пет" in chat (unverified). |
| egg / hatch | жұмыртқа (Minecraft); "жұмыртқадан шықты" | button "Ашу". |
| coins | монета | singular after numbers: "50 монета". |
| gems | асыл тас; алмас if the art shows diamonds (Minecraft "Алмас") | "гем" is chat slang. |
| boost | бонус (noun, both reference strings); күшейту (verb) | Minecraft uses "Күшейтер" for strength; "буст" is Russian-sphere chat slang. |
| multiplier | көбейткіш; "x2" | Latin x. |
| XP | тәжірибе ұпайы (Minecraft), XP | "+50 XP" in tight HUDs; pick one per game. |
| level / level up | деңгей; "Жаңа деңгей!", "Деңгей көтерілді!" | |
| quest | тапсырма | |
| leaderboard | көшбасшылар тақтасы; title "Үздік ойыншылар" | |
| AFK | AFK | Latin, no suffix glued on: "AFK күйдесің". |
| noob | жаңадан бастаушы (UI); нуб (jokes, unverified) | |
| OP | тым күшті | "имба" in chat (unverified for Kazakh speakers). |
| VIP | VIP | "VIP-сервер". |
| trade | айырбас; verb айырбастасу | Minecraft's "саудаласу" means buying from a trader, not swapping. |
| inventory / backpack | инвентарь (Minecraft) / сөмке | keep whichever the source means. |
| daily reward | күнделікті сыйлық | |
| codes | код, промокод; "Кодты енгіз" | |
| group | топ; "Топқа қосыл" | Roblox's English UI calls groups "Communities" since 2024-11; "топ" is clearer and shorter than "қауымдастық". |
| like / favorite | лайк, "лайк бас" / таңдаулылар, "Таңдаулыларға қос" | Roblox has no Kazakh UI to copy; "ұнату" is the formal verb. |
| server | сервер (Minecraft) | |
| friends | дос, достар | Roblox renamed Connections back to Friends in April 2026. Never "байланыстар". |
| shop / buy | дүкен / сатып алу, short "алу" | |

## Grammar traps in UI strings
- Plurals: after a numeral the noun stays singular, so "{count} монета" is correct for 0, 1 and 1 250. Never add -лар/-лер after a number: "5 монеталар" is wrong. CLDR's one/other split never shows in UI text.
- Gender: Kazakh has none. Verbs and adjectives never agree with {player}: "{player} ойынға қосылды" works for anyone (Minecraft uses exactly this).
- Vowel harmony: case suffixes change with the last vowel and consonant of the word (Асан -> Асанға, Ерке -> Еркеге). Never glue a suffix to {player}, {pet}, {count} or {time}. Keep placeholders in the nominative, or let a following noun carry the suffix: "{player} деген ойыншыға" (Minecraft pattern), "E пернесін".
- "after {time}": "кейін" needs the ablative ("3 сағаттан кейін"), which breaks on a placeholder. Use "{time} өткен соң" or a colon: "Іс-шара бітуіне: {time}".
- Ordinals: number + hyphen is the written ordinal ("5-деңгей" = fifth level), and further suffixes go on the noun: "{level}-деңгейдесің". Safe for every integer.
- Word order is subject-object-verb, verb last; postpositions follow the noun: "Buy for {price} Robux" -> "{price} Robux-қа алу"; "for each friend" -> "әр дос үшін".
- Adjectives never change form: "{rarity} {pet}" -> "Легендарлы айдаһар". Translate rarity labels in their base form.
- Latin names take suffixes after a hyphen, chosen by pronunciation: "Roblox-та", "Robux-қа", "VIP-ке" (unverified for VIP). Kazakh Wikipedia does this ("Roblox-та", "Windows-ке", "Robux-ты", once wrongly "Robux-ті"). Microsoft adds no endings to acronyms: when unsure, add a noun ("VIP мәртебесі").
- Possessive "your" is a suffix (-ың/-ің/-ң): "монеталарың". Never mix with сіз forms (-ыңыз).
- Question particles ма/ме/ба/бе/па/пе are written separately: "Қайта туасың ба?".
- Capitalization: sentence case, first word only (Microsoft): "Күнделікті сыйлық", not "Күнделікті Сыйлық". No capital after a colon mid-sentence.

## Typography and formatting
- No space before ! ? : ; and one space after.
- Dash: em dash with spaces " — " ("Достық — дертке сеп!", Minecraft); hyphen without spaces in compounds ("іс-шара", "VIP-сервер"); en dash without spaces in ranges ("10–20").
- Quotes: «» with nested “” (CLDR). Microsoft uses straight quotes in software UI; in game text «» read as native.
- Numbers: thousands separator is a non-breaking space ("1 250"), decimal separator a comma ("1,5") (CLDR). The canonical {count} arrives as "1,250", which reads as 1.25, so flag it to the developer. Same for multiplier "1.5".
- Percent: no space, "25%" (CLDR pattern).
- Multiplier: Latin x: "x2", "Монета x2". Never Cyrillic "х2".
- Durations (CLDR short units): "2 күн", "3 сағ", "20 мин", "5 с"; no periods (Microsoft lists "сек" for seconds; pick one per game). Timers: "2 күн 5 сағ", "3 сағ 20 мин". If game code outputs "3h 20m", flag it.
- Progress text uses the -уде/-уда form plus an ellipsis (Microsoft): "Жүктелуде...". Use "..." or "…" consistently.
- Keys stay Latin. Microsoft always adds the noun "перне" (key): "E пернесін бас"; when space is tight, "E-ні бас" (unverified with players).
- Agglutination makes long words ("Жануарларыңды", "айырбастасқысы"). Roblox does not hyphenate: enable TextWrapped, never insert manual hyphens.

## Do not translate / keep as is
- Robux, Roblox, Premium, VIP, Roblox Studio: Latin; suffixes only after a hyphen.
- Game titles ("Pet Hatch Tycoon"): keep in English.
- Usernames and display names: never translate, transliterate or put a suffix on them.
- Promo codes ("FREEPETS"): exactly as given, same case.
- Key names (E, Q, Shift) stay Latin.
- Descriptive item names translate, using Minecraft's Kazakh words kids already know: "Lucky Potion" -> "Сәтті ішірткі" (Minecraft's own name for its Potion of Luck; "ішірткі" = potion).
- Script: Cyrillic only. Never output the 2021 Latin alphabet (Ä, Ğ, Q, Ñ...) or the Arabic-script Kazakh used in China, and never mix scripts in one string.
- Don't import Russian gamer slang into UI (ребёрт, имба, буст, питомец). International words Kazakh already uses are fine: сервер, монета, бонус, лайк, инвентарь.

## Rendering on Roblox
- Checked 2026-11-08 by reading the character maps of the fonts bundled with the installed Roblox client (content/fonts) for the nine Kazakh letters Ә Ғ Қ Ң Ө Ұ Ү Һ І in both cases plus the Russian alphabet:
  - Full Kazakh coverage: Arimo, Montserrat (incl. Bold, Black), Nunito, Oswald, Roboto (incl. Condensed, Mono), Source Sans Pro (Light to Bold), Ubuntu, Merriweather.
  - Russian Cyrillic but only І/і of the Kazakh letters: Amatic SC, Jura, Press Start 2P, Zekton. The other eight letters fall back to a different font mid-word.
  - No Cyrillic at all: Builder Sans (Roblox's default UI font), Builder Extended and Mono, Fredoka One, Luckiest Guy, Bangers, Denk One, Titillium Web, Comic Neue Angular, Creepster, Patrick Hand, Permanent Marker. The whole string falls back.
  - Gotham is cloud-loaded and was not checked (unverified).
- Which fallback face Roblox uses, and whether it breaks TextScaled sizing, is unverified for current builds.
- Recommendation for the kk-kz column: Montserrat Bold/Black or Nunito for cartoon headers and buttons, Source Sans Pro or Roboto for body text.
- Risks: tails on Қ Ң Ғ Ұ clipped in tight TextScaled boxes; a label mixing two fonts; long words overflowing buttons.
- Verify in Studio: Player Emulator set to Kazakh, open every panel, and paste "Әә Ғғ Ққ Ңң Өө Ұұ Үү Һһ Іі" into each font face the game uses.

## Mistakes machine translation makes here
- "experience" as тәжірибе: "Roblox-тағы ең үздік тәжірибе" -> "Roblox-тағы ең үздік ойын".
- Russian words for existing Kazakh ones: "Магазин", "Награда", "питомец" -> "Дүкен", "Сыйлық", "жануар".
- Plural after a number: "5 монеталар" -> "5 монета".
- Register drift to сіз: "Ашу үшін E басыңыз" -> "Ашу үшін E-ні бас".
- Plain Russian letters for Kazakh ones (к/қ, н/ң, у/ұ/ү, о/ө, г/ғ): "Кунделікті сыйлык" -> "Күнделікті сыйлық".
- Latin Kazakh output: "Dükenge kir" -> "Дүкенге кір".
- Suffix glued to a placeholder: "{time}-тан кейін" -> "{time} өткен соң".
- "Claim" as талап ету (demand): "Талап ету" -> "Алу".
- "Unlock" calqued as құлпын ашу: "Тегін сыйлықтың құлпын аш" -> "Тегін сыйлық ал".
- "Please" as өтінеміз: "Өтінеміз, күтіңіз" -> "Жүктелуде...".
- Title Case: "Үздік Ойыншылар" -> "Үздік ойыншылар".
- Literal slang: "Бұл қылыш ОП!" -> "Бұл қылыш тым күшті!".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Ойнау | infinitive on buttons |
| shop.title | Дүкен | |
| shop.buy | Алу | "Сатып алу" is 9 > max 8; use it if the button allows 9. The price beside the button makes "Алу" read as buy; imperative "Сатып ал" would break the infinitive-button rule |
| reward.claim | Алу | same word as shop.buy is fine |
| rebirth.button | Қайта туу | 9/10 |
| rebirth.confirm | Қазір қайта туасың ба? Монеталарыңды жоғалтасың, бірақ мәңгілік x{multiplier} бонус аласың. | multiplier moved after Latin x; "1.5" should be "1,5" |
| coins.need_more | Тағы {amount} монета керек! | singular after a number, so every amount works |
| coins.count | {count} монета | "1,250" should be "1 250" (code issue) |
| egg.hatched | Жұмыртқадан {rarity} {pet} шықты! | no suffix on placeholders; a capitalized rarity mid-sentence is acceptable |
| rarity.legendary | Легендарлы | native "Аңыздық" (7) is shorter, unverified in games |
| pet.name.dragon | Айдаһар | not Russian "Дракон" |
| chat.player_joined | {player} ойынға қосылды | Minecraft's own wording |
| trade.request | {player} сенімен айырбастасқысы келеді | |
| prompt.open_shop | Ашу үшін E-ні бас | Latin E; Microsoft's form "Ашу үшін E пернесін бас" is 23 > max 22, use it if the prompt allows 23 |
| pass.buy_price | {price} Robux-қа алу | "сатып алу" fits only with prices up to 3 digits |
| pass.coins2x | Монета x2 | |
| pass.vip | VIP | |
| reward.daily_title | Күнделікті сыйлық | 17/18 |
| reward.come_back | Келесі сыйлық үшін {time} өткен соң қайта кел! | "өткен соң" avoids a suffix on {time} (Minecraft: "%s өткен соң"); units "3 сағ 20 мин" |
| codes.placeholder | Кодты енгіз | |
| codes.invalid | Код қате немесе мерзімі өтіп кеткен. | |
| social.like_reward | Ойынға лайк басып, тегін <b>Сәтті ішірткі</b> ал! | an indefinite object takes no accusative, so the item name keeps its shop form |
| social.group_reward | Біздің топқа қосылып, тегін сыйлық ал! | "unlock" rendered as "get" |
| afk.warning | AFK күйдесің! Монета жинай беру үшін қозғал! | 44/45; fallback "AFK күйдесің! Қозғал!" |
| leaderboard.title | Үздік ойыншылар | 15/16 |
| level.up | Жаңа деңгей! Енді сен {level}-деңгейдесің. | hyphen ordinal, suffix on the noun; same shape kids use for school grade ("5-сыныптамын") |
| tutorial.sell | Жануарларыңды сату үшін жарқыраған шеңберге кір. | |
| inventory.full | Сөмке толы! Орын босату үшін жануарларды сат. | "your" dropped |
| settings.music | Әуен | Minecraft's label; "Музыка" also understood |
| settings.on | Иә | Minecraft's own On/Off pair is Иә / Жоқ; "Қосулы" (6 > max 5) if the toggle allows 6 |
| loading | Жүктелуде... | Microsoft progress form |
| event.ends_in | Іс-шара бітуіне: {time} | 28/28 with "2 күн 5 сағ" |
| item.op | Бұл қылыш тым күшті! | |
| friends.boost | Серверіңдегі әр дос үшін +{percent}% бонус | |

## Sources
1. Microsoft Kazakh localization style guide (PDF, via https://aka.ms/kazakh-styleguide): https://download.microsoft.com/download/aa5b82ec-3bd1-43db-a393-b3a793ef0be1/kaz-kaz-StyleGuide.pdf
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON for kk (numbers, units, delimiters): https://github.com/unicode-org/cldr-json/tree/main/cldr-json
4. Roblox locale API (kk_kz flags, native name): https://locale.roblox.com/v1/locales
5. Roblox language codes: https://create.roblox.com/docs/production/localization/language-codes
6. Roblox localization overview: https://create.roblox.com/docs/production/localization
7. DevForum, "Friends Are Back!" (April 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217; "Introducing Roblox Communities" (2024-11): https://devforum.roblox.com/t/introducing-roblox-communities/3268307; in-experience language switcher (2022): https://devforum.roblox.com/t/localization-api-update-for-upcoming-in-experience-language-switcher/1974795
8. Minecraft Kazakh language file kk_kz.json, release 26.3, from Mojang's asset index: https://piston-meta.mojang.com/mc/game/version_manifest_v2.json
9. Kazakh Wikipedia, Roblox: https://kk.wikipedia.org/wiki/Roblox
10. Wikipedia, Kazakh alphabets (2021 Latin alphabet, 2023-2031 phase-in): https://en.wikipedia.org/wiki/Kazakh_alphabets
11. Wikipedia, Kazakh language (script, Latin transition delays): https://en.wikipedia.org/wiki/Kazakh_language
12. Wikipedia, Censorship of Roblox (no Kazakhstan block listed): https://en.wikipedia.org/wiki/Censorship_of_Roblox
13. Roblox client bundled fonts (content/fonts), glyph coverage read locally with fontTools on 2026-11-08 (no URL).
