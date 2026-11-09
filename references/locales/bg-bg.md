# Bulgarian (bg-bg) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `bg-bg` (bare `bg` also fine: Roblox lists only one Bulgarian locale) |
| Script, direction | Cyrillic (Bulgarian alphabet, 30 letters), LTR |
| Address the player as | informal singular "ти" everywhere; never "вие" or capitalized "Вие" |
| Text expansion vs English | about +15-30% for sentences (unverified rule of thumb); short buttons +40-75% ("Shop" -> "Магазин", "Rebirth" -> "Прераждане") |
| Plural categories (CLDR) | cardinal: one, other; ordinal: one, two, few, other |
| Model confidence | medium: standard Bulgarian is well covered, but models leak Russian words and get the definite article wrong; gamer slang is thinly documented |
| Native review before shipping | strongly recommended |

## Audience and register
- Roblox's own app is not in Bulgarian: the Roblox locale API (checked 2026-11-08) enables `bg_bg` for in-game content only, not for the app UI or sign-up. Bulgarian kids read Roblox itself in English and meet platform words (Robux, Premium, Friends) in English first.
- Reach is unverified: Roblox's docs do not say how `Player.LocaleId` is chosen, and with `bg_bg` off for the app UI it is likely missing from the account language menu, so a real Bulgarian player may never get `bg-bg` (perhaps only via a Bulgarian device language). The Player Emulator only proves the column renders; test with a real account before promising Bulgarian support.
- Roblox does not auto-translate Bulgarian: without a `bg-bg` column, players see the source text.
- Use "ти" in every string: singular imperative ("Купи", "Натисни", "Влез") and 2nd person singular verbs ("Ще получиш"). Bulgarian adults say ти to children and teens say it to each other; вие to a 9-16 player reads like a notice for parents. Counter-evidence: Microsoft's guide uses вие for software (ти only for Copilot prompts); Minecraft's Bulgarian file is mostly вие (about 144 strings vs 9), yet its death screen says "Ти умря!"; Roblox's Play listing used вие. Pick ти and never mix.
- Bulgarian has no infinitive. Buttons use the short singular imperative: "Играй", "Купи", "Вземи". Panel titles and feature labels use nouns: "Магазин", "Прераждане", "Настройки". Avoid verbal nouns ("Купуване") and the 1st-person command style of Microsoft menus ("Премествам надолу") on game buttons; both read like office software.
- Hype is short and natural: "Ура!", "Супер!", "Ново ниво!", "Не го пропускай!". Stiff or adult: "осъществявам", "в случай че", "уважаеми играчо", "данни", "съгласно".
- Microsoft's Bulgarian guide warns against archaic, bookish words and stacked possessives ("вашия"): write "Раницата е пълна", not "Твоята раница е пълна".
- Don't blame the player in errors: "Кодът е невалиден", not "Въведе грешен код".
- Kid-safe slang is fine in flavor text ("имба", "AFK"). No insults, no crude words; the street-slang dictionary BGJargon is not a kid-safe source.

## Roblox and gaming vocabulary
| English | Bulgarian | note |
|---|---|---|
| Robux | Robux | Latin, undeclined, as in Bulgarian Wikipedia and Roblox's Play listing: "100 Robux", "за 50 Robux". |
| Premium | Premium | Latin brand. The writer's fetch of the Play listing (2026-11-08) showed "Roblox Plus"; a rename is unverified, so use whatever the current English UI shows. |
| game pass | пропуск; геймпас (chat) | Roblox UI is English here; in the shop just show the pass name. Both words unverified for Bulgarian players. |
| developer product | покупка | players never see the term; name the item. |
| experience / game | игра | never "опит" (= XP). Roblox's listing says "преживявания" in marketing; players say "игра". |
| obby | паркур; оби (chat, unverified) | |
| tycoon | Tycoon (titles); тайкун (unverified) | Roblox's Bulgarian listing keeps "Tycoons" in Latin. |
| simulator | симулатор | as in the Play listing. |
| rebirth | прераждане; verb "преродя се" | Minecraft uses "Прераждане" for respawn, so pick another word for respawn ("Възкръсни") if the game has both. "Ребърт" slang unverified. |
| pet | любимец, любимци | masculine. "Питомец" also correct; "пет/петове" chat slang (unverified). |
| egg / hatch | яйце / излюпвам | button "Отвори"; "Излюпи дракон!" |
| coins | монети | feminine: "1 монета", "2 монети". |
| gems | диаманти | "кристали" if the art shows crystals. |
| boost | бонус | "буст" is gamer talk, but BGJargon's only sense is a drug/alcohol high; keep it out of UI. Speed boost: "ускорение". |
| multiplier | множител; "x2" | Latin x. |
| XP | опит, XP | Minecraft: "Ниво на опита". Pick one per game. |
| level up | ново ниво | "Ново ниво!"; never "левъл ъп". |
| quest | мисия, задача | Play listing also says "куестове". |
| leaderboard | класация; "Топ играчи" | |
| AFK | AFK | Latin in UI, like other acronyms (Microsoft: don't localize acronyms). "АФК" is used in chat, but BGJargon also records it as a "spaced-out" taunt. |
| noob | новак (UI); нуб (jokes, unverified) | |
| OP | имба | BGJargon: "unbeatable, top-tier", from "imbalanced"; how widely Roblox kids use it is unverified. Never Cyrillic "ОП" (BGJargon: a chat operator); "супер силен" is the plain fallback. |
| VIP | VIP | "VIP сървър", no hyphen after an acronym (Microsoft). |
| trade | размяна; разменям | "трейд" chat only (unverified). |
| inventory / backpack | инвентар / раница | Minecraft: "Инвентар". |
| daily reward | ежедневна награда | "Дневна награда" when short. |
| codes | кодове | redeem = "Активирай"; placeholder "Въведи код". |
| group | група | "Присъедини се към групата ни" (listing: "Присъединете се към група"). |
| like / favorite | Харесай; "Дай лайк" (casual) / любими, "Добави в любими" | |
| server | сървър; частен сървър | listing: "частни сървъри"; "на сървъра" and "в сървъра" are both heard; pick one per game. |
| friends | приятели | Roblox renamed Connections back to Friends in April 2026; Roblox's Bulgarian listing says "приятели". Never "връзки" or "контакти". |

## Grammar traps in UI strings
- Plurals: CLDR has only one and other, but masculine non-person nouns take a count form after numbers: "1 дракон", "2 дракона", "5 любимеца"; feminine just pluralizes: "1 монета", "2 монети". One string per key, so "{count} монети" breaks at 1 ("1 монети").
  - Bad: "Имаш {count} монети". Good: "Монети: {count}", "Трябват ти още монети: {amount}!".
  - Undeclinable units are safe: "{price} Robux", "{percent}%", "x{multiplier}".
- Gender: the simple past (aorist) and present are gender-neutral; the l-participle and adjectives are not.
  - Good: "{player} се присъедини към играта", "{player} спечели!" (aorist). Bad: "{player} е спечелил" (masculine).
  - The player has gender too: "Готов ли си?" excludes girls -> "Започваме ли?"; "Неактивен си" -> "AFK си".
- Inserted item names: adjectives agree with the noun: легендарен дракон, легендарна котка, легендарно зайче. Write standalone rarity tags in the masculine: it agrees with an implied "любимец" or "предмет" (both masculine), so one tag set serves pets and items. Use "{rarity} любимец: {pet}!", never "{rarity} {pet}". If code puts {rarity} right before a feminine or neuter noun ("{rarity} отвара"), ask for separate keys per gender.
- Nouns have no case, so {pet} and {player} need no declension, but the definite article is a suffix and cannot attach to a placeholder. Put inserted nouns where Bulgarian needs no article: after a colon or as a bare indefinite noun. Bad: "Купи {pet}-а". Good: "Нов любимец: {pet}".
- Masculine full vs short article: the subject takes -ът/-ят, everything else -а/-я. "Кодът е невалиден" (subject) vs "Въведи кода" (object); "в светещия кръг" (after a preposition).
- Clitics (ти, ми, се, го) never start a sentence: "Трябват ти още монети", never "Ти трябват още монети" (ungrammatical: a clitic cannot open a sentence).
- Questions take the particle ли after the stressed word: "Искаш ли да се преродиш сега?", "Сигурен ли си?" (gendered; prefer "Продължаваме ли?").
- Ordinals change suffix by number (CLDR ordinal one/two/few/other: 1-ви, 2-ри, 3-ти, 5-и). Avoid "{level}-то ниво"; write "ниво {level}".
- No articles from English: drop "a/the" ("a Rare Dragon" -> "рядък дракон").
- English noun stacks become "на"/"за" phrases or adjectives: "Coin Boost" -> "бонус за монети", "Pet Storage" -> "хранилище за любимци". Compounds with an acronym stay two words: "VIP сървър", "XP бонус".
- Comparatives and superlatives always take a hyphen: "по-бързо", "най-добрият". "Най добри" is a spelling error.
- Capitalization: sentence case for titles and buttons ("Ежедневна награда", "Топ играчи"); Microsoft calls English title case an error in Bulgarian.

## Typography and formatting
- No space before ! ? : ; and one space after: "Ура! Ново ниво!".
- Quotes: „…“ (U+201E opening, U+201C closing): „Отвара на късмета“. Never the English pair that opens with U+201C, and never «».
- Dashes: en dash with spaces " – " for asides ("Нова награда – само днес!"); Microsoft says the em dash is not used in Bulgarian. Hyphen without spaces in words ("по-добре").
- Numbers (CLDR): decimal comma ("1,5"), thousands separator a non-breaking space, and 4-digit numbers stay ungrouped: "1250", "12 500". The canonical {count} arrives as "1,250", which a Bulgarian reads as 1.25; flag it to the developer. Same for "1.5" multipliers.
- Percent: no space ("25%"), per both Microsoft and CLDR. Other units take a non-breaking space ("45 км/ч").
- Multiplier: Latin x, before the number: "x2", "Монети x2". Never Cyrillic "х2".
- Durations (CLDR short forms, no periods): "2 д 5 ч", "3 ч 20 мин", "45 сек". If game code outputs "3h 20m", flag it.
- Ellipsis: the single character …, no space before: "Зареждане…".
- Abbreviations: only established ones ("Вкл."/"Изкл.", "мин", "ч", "напр."); don't invent short forms like "ур." for "ниво".
- Exclamation marks: Microsoft avoids them in software; in a game, one per string at most, and code or system errors end with a period.
- Keys stay Latin: "Натисни E". Mouse: "ляв бутон", "десен бутон" (Minecraft: "Десен бутон").
- Words are long ("Прераждане", "Присъедини") and Roblox does not hyphenate: enable TextWrapped, never insert manual hyphens.

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, Roblox Studio, Marketplace: Latin, undeclined, no article ("в Roblox", never "Roblox-а"). Microsoft treats untranslated brand names the same way.
- Game titles ("Pet Hatch Tycoon"): keep English; players search for the English title.
- Usernames and display names: never translate, transliterate or add an article.
- Promo codes ("FREEPETS"): exactly as given, Latin, same case; translate only the text around them.
- Key names (E, Q, Shift, Space) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Отвара на късмета", Minecraft's name for the luck potion); keep invented brand-like names Latin only if the game treats them as brands.
- Script: always Cyrillic. Teens often chat in Latin-letter Bulgarian ("шльокавица"), never in UI. No Russian letters (ы, э, ё) and no Russian words.
- Transliterate only established gamer loanwords (имба); acronyms stay Latin (AFK, VIP, XP); don't invent new ones ("лъки поушън").

## Rendering on Roblox
- Glyph check (2026-11-08) of the font files in the local Roblox client, `content/fonts`: Builder Sans, Builder Extended, Builder Mono, Fredoka One, Luckiest Guy, Bangers, Denk One, Titillium Web, Permanent Marker, Comic Neue Angular, Creepster, Michroma, Patrick Hand, Kalam and Source Sans Pro Italic have no Cyrillic at all.
- Full Bulgarian alphabet plus „“ – …: Arimo, Source Sans Pro (Regular, Light, Semibold, Bold), Roboto, Roboto Condensed, Roboto Mono, Montserrat, Merriweather, Nunito, Oswald, Ubuntu, Press Start 2P, Amatic SC. Jura and Zekton cover the alphabet but lack ѝ or №.
- A Latin-only font falls back to another font for Cyrillic. Which one is unverified: the client ships Noto fallbacks for other scripts but none for Cyrillic, plus Arimo and LegacyArial families, which fits a 2019 DevForum report of an Arial fallback that rendered larger and left an empty line under TextScaled (no fix was ever posted).
- Recommendation: for the bg locale, set a Cyrillic font (Montserrat, Nunito or Roboto for a cartoon look) instead of relying on fallback, so one label never mixes two fonts ("x2" in the display font, Bulgarian in the fallback).
- Montserrat, Merriweather and Ubuntu contain Bulgarian letterforms (OpenType locl BGR); whether Roblox applies them is unverified. Russian-style shapes are what most software shows and read fine.
- ѝ (U+045D, the pronoun "her") is in every Cyrillic font above except Jura (Zekton lacks only №); the reference strings avoid it anyway.
- Verify in Studio: Player Emulator set to Bulgarian; open every panel with the longest strings; check й, ъ, щ, ю, „ “ and numbers in each font face; watch tight TextScaled buttons ("Прераждане" is 10/10).

## Mistakes machine translation makes here
- Russian leaking in: "Загрузка…", "Ежедневная награда" -> "Зареждане…", "Ежедневна награда".
- Russian-style infinitive buttons or stray forms: "Играть", "Да купиш" -> "Играй", "Купи".
- Wrong full/short article: "Въведи кодът", "Магазина е затворен" -> "Въведи кода", "Магазинът е затворен".
- "experience" as опит (= XP): "Най-добрият опит в Roblox" -> "Най-добрата игра в Roblox".
- "Claim" as претендирай or изискай: "Изискай" -> "Вземи".
- "redeem" as откупи: "Откупи код" -> "Активирай код".
- Register drift: "Натиснете E и ще получиш" -> "Натисни E и ще получиш".
- Gendered participle with a username: "{player} е спечелил" -> "{player} спечели".
- Number + noun: "Имаш {count} монети" -> "Монети: {count}".
- English title case: "Ежедневна Награда" -> "Ежедневна награда".
- Em dash and missing hyphen: "Меч — имба", "Най добри" -> "Меч – имба", "Най-добри".
- Literal slang: "Този меч е ОП" / "свръхмощен" -> "Този меч е имба!".
- Cyrillic look-alikes in keys and codes: "Натисни Е" (Cyrillic Е) -> "Натисни E" (Latin); "х2" -> "x2".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Играй | singular imperative on buttons |
| shop.title | Магазин | |
| shop.buy | Купи | |
| reward.claim | Вземи | "Получи" (6) also fine |
| rebirth.button | Прераждане | 10/10; feature noun. "Прероди се" (10) if a verb is preferred |
| rebirth.confirm | Искаш ли да се преродиш сега? Ще загубиш монетите си, но ще получиш постоянен бонус x{multiplier}. | "Искаш ли" is the natural ти question; multiplier moved after x; "1.5" should arrive as "1,5" |
| coins.need_more | Трябват ти още монети: {amount}! | colon avoids "1 монети" |
| coins.count | Монети: {count} | "1,250" should be "1250" for Bulgarian (code issue) |
| egg.hatched | {rarity} любимец: {pet}! | rarity masculine; no article, no agreement with {pet} |
| rarity.legendary | Легендарен | masculine, agrees with "любимец" |
| pet.name.dragon | Дракон | |
| chat.player_joined | {player} се присъедини към играта | aorist is gender-neutral; Minecraft's wording |
| trade.request | {player} ти предлага размяна | present tense, neutral |
| prompt.open_shop | Натисни E за отваряне | Latin E; 21/22 |
| pass.buy_price | Купи за {price} Robux | Robux undeclined |
| pass.coins2x | Монети x2 | "2x монети" also seen |
| pass.vip | VIP | |
| reward.daily_title | Ежедневна награда | 17/18; fallback "Дневна награда" |
| reward.come_back | Ела пак след {time} за следващата награда! | time should be "3 ч 20 мин" |
| codes.placeholder | Въведи код | |
| codes.invalid | Кодът е невалиден или е изтекъл. | full article on the subject |
| social.like_reward | Харесай играта за безплатна <b>Отвара на късмета</b>! | 46/55 (`scripts/i18n.py` counts visible text: no tags, no {params}); "безплатна" agrees with feminine "отвара" |
| social.group_reward | Присъедини се към групата ни за безплатна награда! | "unlock" dropped to fit and flow |
| afk.warning | AFK си. Движи се, за да продължиш да печелиш! | 45/45; Latin AFK, one "!" as in the source; fallback "AFK си. Движи се, за да печелиш!" |
| leaderboard.title | Топ играчи | "Класация" also fine; "Най-добри играчи" is 16/16 |
| level.up | Ново ниво! Вече си на ниво {level}. | avoids ordinal suffixes |
| tutorial.sell | Влез в светещия кръг, за да продадеш любимците си. | short article after a preposition |
| inventory.full | Раницата е пълна! Продай любимци, за да освободиш място. | "your" dropped |
| settings.music | Музика | |
| settings.on | Вкл. | pair with "Изкл." (Microsoft, Minecraft) |
| loading | Зареждане… | single ellipsis character |
| event.ends_in | Събитие: край след {time} | 26/28 rendered with "2 д 5 ч". "Събитието свършва след {time}" is more natural and passes the linter (23 visible) but renders 30; use it if the banner can grow. "Край след {time}" if the event name is on the banner |
| item.op | Този меч е имба! | "супер силен" for a non-gamer tone |
| friends.boost | +{percent}% бонус за всеки приятел на сървъра | "бонус", not "буст" |

## Sources
1. Microsoft Bulgarian localization style guide (PDF, via https://aka.ms/bulgarian-styleguide): https://download.microsoft.com/download/6/6/8/66825d50-e7e0-404e-981e-ca9b6da7db19/bul-bgr-StyleGuide.pdf
2. CLDR language plural rules (bg cardinal and ordinal): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON, Bulgarian number symbols and minimum grouping: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/bg/numbers.json
4. CLDR JSON, Bulgarian duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/bg/units.json
5. Roblox locale API (bg_bg: in-game content only, no app UI): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
6. Roblox language codes (bg / bg-bg): https://create.roblox.com/docs/production/localization/language-codes
7. DevForum, "Friends Are Back!" (Connections -> Friends, April 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
8. Roblox on Google Play, Bulgarian listing (Robux, приятели, група, частни сървъри, вие register; writer's 2026-11-08 fetch, the reviewer's re-fetch came back truncated): https://play.google.com/store/apps/details?id=com.roblox.client&hl=bg&gl=BG
9. Bulgarian Wikipedia, Roblox (Robux and Roblox Studio kept in Latin): https://bg.wikipedia.org/wiki/Roblox
10. Minecraft Java Edition Bulgarian language file `minecraft/lang/bg_bg.json` (assets index 32, read from a local install, re-checked 2026-11-08): Инвентар, Вкл./Изкл., Прераждане (respawn), "се присъедини към играта", "Отвара на късмета", "Ти умря!", mostly вие elsewhere.
11. BGJargon slang dictionary entries АФК, имба, оп, буст (нуб, трейд, лвл have no entry): https://www.bgjargon.com/word/meaning/имба (same pattern for the others)
12. Roblox client font files (`content/fonts`, client version-f0ea5da9412f4e35), cmap and GSUB glyph check run locally 2026-11-08.
13. DevForum, "Russian Text Scaling Issues" (Cyrillic falls back to Arial, breaks TextScaled, 2019): https://devforum.roblox.com/t/russian-text-scaling-issues/232672
