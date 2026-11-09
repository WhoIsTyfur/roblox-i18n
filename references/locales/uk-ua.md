# Ukrainian (uk-ua) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `uk-ua` (Ukrainian has one Roblox locale, so a bare `uk` column also works; fill one, never both) |
| Script, direction | Cyrillic, Ukrainian alphabet (і, ї, є, ґ, apostrophe; no ы, э, ъ, ё), LTR |
| Address the player as | informal singular "ти" everywhere; never "ви", never capitalized "Ви" |
| Text expansion vs English | sentences +5-30% (the reference set below measures +6%, written tight on purpose); short labels +20% on average, single words up to +75% ("Shop" -> "Магазин", "Rebirth" -> "Переродження") |
| Plural categories (CLDR) | one, few, many, other |
| Model confidence | medium: grammar is well covered, but models leak Russian words, letters and calques into Ukrainian, and kid gaming slang is thinly documented |
| Native review before shipping | strongly recommended |

## Audience and register
- Roblox's own app and site are not offered in Ukrainian: Roblox's locale API (checked 2026-11-08) marks `uk_ua` as enabled for in-game content only, not for the full platform UI or sign-up, and the Ukrainian App Store listing names 15 languages without Ukrainian. Ukrainian kids read Roblox's menus and purchase prompts in another language (most likely English); your game may be the only Ukrainian they see on Roblox.
- Ukrainian cannot be an account language, so a player reaches the `uk-ua` column only by picking Ukrainian in the in-experience Settings language menu, which lists only the languages the creator added in the experience's localization settings (Roblox docs; DevForum, 2022). Tell the developer to add Ukrainian there. Roblox docs describe `Player.LocaleId` as the account locale; the switcher changes the locale of the Translator from `GetTranslatorForPlayerAsync`, so code should read that, not `Player.LocaleId` (not tested live; Studio's Player Emulator only proves the column renders).
- Write standard modern Ukrainian (2019 orthography). A Russian word or spelling reads as careless machine output. Never build the `uk-ua` column by adapting the Russian one; an empty key falling back to English is better than Russian.
- Use "ти" in every string, with singular imperatives: "Натисни", "Продай", "Зайди", "Повертайся". Microsoft's Ukrainian guide uses "ви", but that is adult software; with 9-16 year olds "ви" reads like a school notice. Never mix: "Натисни E — отримаєш нагороду", not "Натисніть E — отримаєш".
- Buttons, tabs, toggles: infinitive or noun, the Ukrainian UI norm (Microsoft: "Створити", "Зберегти"): "Грати", "Купити", "Забрати", "Магазин". Sentences, tips and tutorials: ти-imperative.
- Natural hype: "Ура!", "Новий рівень!", "Круто!", "Супер!", "Не проґав!". Stiff or adult: "здійснити покупку" (Microsoft: avoid здійснити/виконати + noun) -> "купити"; "з метою" -> "щоб"; repeated "будь ласка".
- Prefer verbs to verbal nouns and drop needless possessives (both Microsoft rules): "Щоб продати улюбленців..." not "Для здійснення продажу..."; "Рюкзак повний!" not "Твій рюкзак повний!".
- Don't blame the player in errors: "Такого коду немає" rather than "Ти ввів неправильний код" (also gendered, see below).
- Kid-safe slang is fine ("імба", "буст", "нуб" in a joke). No insults, no crude words, no surzhyk "for flavor".

## Roblox and gaming vocabulary
| English | Ukrainian | note |
|---|---|---|
| Robux | Robux | Latin, never declined: "100 Robux", "за 50 Robux" (Ukrainian Wikipedia does the same). Chat form "робукси" (unverified); not in UI. |
| Premium | Premium | Latin: "підписка Roblox Premium". |
| game pass | геймпас | one "с", Ukrainian loanword spelling (players' usage unverified); in the shop just show the pass name. |
| developer product | покупка, товар | players never see the term; name the item itself. |
| experience / game | гра | never "досвід" (= XP) or "враження"; Ukrainian Wikipedia also uses "плейс". |
| obby | паркур; оббі | "паркур" in UI text; "оббі" spelling unverified. |
| tycoon | тайкун | |
| simulator | симулятор | |
| rebirth | переродження; verb переродитися | one term per game; 10-char button "Переродись" (colloquial -сь imperative); slang "ребірт" unverified, never in UI. |
| pet | улюбленець, улюбленці | masculine, which the egg.hatched and rarity patterns rely on; Ukrainian Wikipedia's Adopt Me! article says "домашні тварини" and "улюбленці". "вихованець" (also masculine) works too but doubles as "pupil", so default to улюбленець; "пет" is chat slang (unverified). |
| egg / hatch | яйце; вилупитися; відкрити яйце | "З яйця вилупився дракон"; button "Відкрити". |
| coins | монети | |
| gems | кристали | "алмази" if the art shows diamonds. |
| boost | буст | gamer word; "підсилення" in longer text. |
| multiplier | множник; "x2" | |
| XP | досвід, XP | "+50 досвіду" (Ukrainian Minecraft Wiki: "очки досвіду"); pick one per game. |
| level up | новий рівень | "рівень"; never "уровень" or "левел ап". |
| quest | завдання | "квест" also understood; not "задача" (a math problem). |
| leaderboard | таблиця лідерів; найкращі гравці; топ | |
| AFK | АФК or AFK | both seen; which one kids prefer is unverified. Pick one per game; never decline it. |
| noob | новачок (UI); нуб (jokes) | "нуб" has its own Ukrainian Wikipedia article. |
| OP | імба | Ukrainian spelling with і, never Russian "имба". |
| VIP | VIP | Latin; "VIP-сервер", "VIP-статус". |
| trade | обмін; обмінятися | "трейд" in chat only; "торгівля" is for NPC shops. |
| inventory / backpack | інвентар / рюкзак | keep whichever the source means. |
| daily reward | щоденна нагорода | |
| codes | коди, промокоди | redeem = "активувати", never "погасити"; placeholder "Введи код". |
| group | група | "Вступи до нашої групи". |
| like / favorite | лайк, "Постав лайк" / обране, "Додай в обране" | "вподобайка" is a popular Ukrainian word for a like (unverified for Roblox); there is no Ukrainian Roblox label to copy. |
| server | сервер; приватний сервер | "на сервері". |
| friends | друзі | Roblox announced Connections -> Friends again in April 2026; no Ukrainian Roblox UI exists, so never "зв’язки", "з’єднання" or "контакти". |
| event | подія; івент | "івент" with і, not "ивент". |

## Grammar traps in UI strings
- Plurals: four CLDR forms: one (1, 21, 101: монета), few (2-4, 22-24: монети), many (0, 5-20, 25, 100: монет), other (fractions: 1,5 монети). One string per key, so never put {count} right before a countable noun.
  - Bad: "{amount} монет" -> "1 монет", "2 монет". Good: "Монети: {count}", "Бракує монет: {amount}". Microsoft's guide uses the same colon trick ("...кількість користувачів: %d").
  - Undeclinable units are safe after a number: "{price} Robux", "{percent}%", "x{multiplier}", "{n} шт.".
- Gender: past-tense verbs and short adjectives agree with the subject. {player} can be any gender, so use present tense ("{player} приєднується до гри"), a fixed noun head ("Гравець {player} вийшов", agrees with "гравець") or a colon ("Переможець: {player}").
- The player as "you" has gender too (Microsoft: keep the user gender-neutral): "Ти отримав(ла)", "Ти готовий?" -> "Ти отримуєш...", "Отримано: ...", "Починаємо?".
- Adjectives agree with inserted nouns: легендарний дракон, легендарна кішка, легендарне яйце. Translate rarity labels in the masculine (agreeing with an implied "улюбленець") and write "{rarity} улюбленець: {pet}!", never "{rarity} {pet}".
- Case: seven cases, including the vocative. A translated {pet} arrives in the nominative; keep it as subject or after a colon. "У тебе немає {pet}" needs the genitive -> "Немає улюбленця: {pet}". Latin usernames never decline, so "з {player}" and "Привіт, {player}!" are safe.
- Euphony, a Ukrainian-only rule Microsoft follows: у between consonants, at a sentence start before a consonant, and always before в, ф or clusters like св, тв, хв ("Гравець у грі", "У рюкзаку немає місця", "Зайди у ворота"); в between vowels, after a vowel, and after a consonant before a vowel ("Зайди в коло", "Додай в обране"); і between consonants, й between vowels ("брат і сестра", "монети й кристали"); з / із / зі ("з гри", "зі скрині"). Never alternate when the letter changes the word: "удача" is luck, "вдача" is temperament.
- Ordinals: write "Рівень {level}" or "Рівень: {level}"; "{level}-й рівень" agrees only with masculine nouns.
- No articles: drop "a/the" ("a Rare Dragon" -> "рідкісний дракон").
- Noun stacks become genitive phrases: "Pet Storage" -> "сховище улюбленців", "Coin Boost" -> "буст монет". An English singular first noun often means plural (Microsoft: "Template wizard" -> "Майстер шаблонів"). Latin + Ukrainian compounds take a hyphen: "VIP-сервер".
- Capitalization: sentence case for titles and buttons ("Щоденна нагорода", "Найкращі гравці"); days, months and languages lowercase ("у суботу", "українська").

## Typography and formatting
- No space before ! ? : ; and one space after: "Ура! Новий рівень!".
- Dash between words with spaces: " — " ("Цей меч — імба!"); Microsoft uses the en dash " – " in software, so pick one per game. Hyphen without spaces in compounds ("VIP-сервер"); en dash without spaces in ranges ("10–20").
- Quotes: «ялинки» in game text, nested „лапки“; Microsoft uses straight "" in software UI. Never English curly quotes or single quotes.
- The apostrophe is part of the word: "м’яч", "п’ять", "зв’язок", "обов’язково". Use ’ (U+2019, Microsoft's choice) in every string. Every Roblox client font checked has U+2019; ʼ (U+02BC) is missing from Fredoka One, Luckiest Guy, Bangers, Press Start 2P and other display fonts, so avoid it. Straight ' renders too, but don't mix. Never drop it ("пять"), never Russian ъ ("объект" -> "об’єкт").
- Numbers (CLDR): thousands separator a no-break space U+00A0 ("1 250"), decimal comma ("1,5"). The canonical {count} arrives as "1,250", which a Ukrainian reader takes as 1.25; flag it to the developer; same for multiplier "1.5".
- Percent: keep "{percent}%" attached as in the source.
- Multiplier: Latin x before the number: "x2", "Монети x2", "буст x{multiplier}". Never Cyrillic "х2".
- Time: Microsoft's list has "год." (hour), "хв." (minute), "с" (second) for running text. Compact timers use CLDR's short forms, no period except days: "3 год 20 хв", "45 с", "2 дн. 5 год". Not "д" alone (CLDR narrow, too cryptic) and not Russian "ч", "мин". If game code outputs "3h 20m", flag it.
- Ellipsis: the single character … with no space before, as in Microsoft's examples: "Завантаження…".
- Keys stay Latin: "Натисни E", "клавіша E". ЛКМ / ПКМ (ліва / права кнопка миші) for mouse buttons.
- Words run long ("Переродження", "Налаштування") and Roblox does not hyphenate: enable TextWrapped, never insert manual hyphens.
- Accepted short forms: "год.", "хв.", "див." (Microsoft list); "тис.", "млн", "шт." (standard Ukrainian). Toggles "Увімк." / "Вимк." are the usual Ukrainian UI form (unverified); never cut a word without a period ("Увімк").

## Do not translate / keep as is
- Robux, Roblox, Premium, VIP, Roblox Studio: Latin, undeclined.
- Game titles ("Pet Hatch Tycoon"): keep in English; players search for the English title.
- Usernames and display names: never translate, transliterate or decline.
- Promo codes ("FREEPETS"): exactly as given, Latin, same case; translate only the text around them.
- Key names (E, Q, Shift, Space) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Зілля удачі"); invented brand-like names stay Latin only if the game treats them as brands.
- Loanwords take Ukrainian spelling, not Russian: "імба", "чітер" (Ukrainian Wikipedia's spelling), "івент", "геймпас". English G becomes г ("геймер", "гайд"); ґ belongs to native words ("ґудзик", "проґавити"). "Ґрати" means "bars", "Грати" means "Play".
- Language picker: write "Українська" yourself; Roblox's locale API returns a misspelled native name for `uk_ua` ("Yкраїньска").

## Rendering on Roblox
- Glyph check (2026-11-08) of the font files in the local Roblox client, `content/fonts`:
  - No Cyrillic at all: Builder Sans (Roblox's default UI font), Builder Extended and Mono, Fredoka One, Luckiest Guy, Bangers, Denk One, Titillium Web, Comic Neue Angular, Creepster, Patrick Hand, Permanent Marker, Kalam, Michroma, Sarpanch, Source Sans Pro Italic and most other bundled display fonts. Ukrainian text in these falls back to another font.
  - Cyrillic but no Ґ ґ: Press Start 2P and Zekton, so "проґавити" would switch font mid-word.
  - Every Ukrainian letter plus ’ and ʼ: Arimo, Amatic SC, Jura, Merriweather, Montserrat, Nunito, Oswald, Roboto (and Condensed, Mono), Source Sans Pro (not Italic), Ubuntu.
- Which fallback face current builds use is unverified. A 2019 DevForum report found Arial, rendered larger, which broke TextScaled sizing and left an empty line.
- Risks: one label mixing two fonts ("x2" in the display font, Ukrainian in the fallback); Ї and Й marks clipped in tight TextScaled boxes; long words overflowing buttons.
- Verify in Studio: Player Emulator set to Ukrainian; open every panel with the longest strings; paste "Чуєш їх, доцю, га? Кумедна ж ти, прощайся без ґольфів!" plus "м’яч" and «» into each font face used.
- Recommend the developer set a full-coverage font for the uk locale (Nunito or Montserrat Bold for a cartoon look) instead of relying on fallback.

## Mistakes machine translation makes here
- Russian words in Ukrainian dress: "Получи нагороду" -> "Отримай нагороду"; "Нажми E" -> "Натисни E"; "Уровень" -> "Рівень"; "Загрузка" -> "Завантаження".
- Surzhyk calques: "Не хватає монет" -> "Бракує монет"; "Самий кращий гравець" -> "Найкращий гравець"; "Приймати участь" -> "Брати участь"; "Співпадає" -> "Збігається"; "На протязі години" -> "Протягом години" (last three from Microsoft's list).
- "вірний" for "correct" (Microsoft: it means "faithful"): "Невірний код" -> "Неправильний код" or "Такого коду немає".
- Russian-style active participles (Microsoft avoids present participles): "Світяще коло" -> "Сяйливе коло"; "Мигаюча кнопка" -> "Кнопка, що блимає". Set terms stay ("спливаюче вікно"; Microsoft rejects "спливне").
- Russian letters and spellings: "Твоё", "ещё", "объект", "имба" -> "Твоє", "ще", "об’єкт", "імба".
- Lookalike characters: Latin i inside a word ("вiдкрити") or Cyrillic Е / х in keys and multipliers ("Натисни Е", "х2") -> Cyrillic і in words, Latin E and x in keys and multipliers.
- "experience" as досвід (= XP): "Найкращий досвід у Roblox" -> "Найкраща гра в Roblox".
- "Claim" as вимагати or заявити -> "Забрати"; "redeem" as погасити -> "Активувати".
- Russian toggles: "Вкл." / "Викл." -> "Увімк." / "Вимк.".
- Register drift: "Натисніть E, ти отримаєш" -> "Натисни E — отримаєш".
- Gendered past with a username: "{player} приєднався до гри" -> "{player} приєднується до гри".
- Number + noun: "У тебе {count} монет" -> "Монети: {count}".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Грати | infinitive on buttons |
| shop.title | Магазин | |
| shop.buy | Купити | |
| reward.claim | Забрати | "Отримати" (8) also fine |
| rebirth.button | Переродись | 10/10; imperative only because "Переродження" and "Переродитися" (12) don't fit; use "Переродження" if the button allows 12; no slang "ребірт" |
| rebirth.confirm | Переродитися зараз? Ти втратиш монети, але отримаєш постійний буст x{multiplier}. | multiplier moved before the number |
| coins.need_more | Бракує монет: {amount}! | colon avoids plural forms; not "не хватає" |
| coins.count | Монети: {count} | "1,250" should be "1 250" (code issue) |
| egg.hatched | {rarity} улюбленець: {pet}! | 31/40 with Легендарний + Дракон; "You hatched" dropped: "У тебе вилупився..." runs 48 |
| rarity.legendary | Легендарний | masculine, agrees with "улюбленець" |
| pet.name.dragon | Дракон | |
| chat.player_joined | {player} приєднується до гри | present tense avoids gender |
| trade.request | {player} пропонує тобі обмін | present tense avoids gender |
| prompt.open_shop | Тисни E, щоб відкрити | Latin E; 21/22 ("Натисни E, щоб відкрити" is 23) |
| pass.buy_price | Купити за {price} Robux | Robux undeclined; 20/22 with a 4-digit price |
| pass.coins2x | Монети x2 | Latin x |
| pass.vip | VIP | |
| reward.daily_title | Щоденна нагорода | |
| reward.come_back | Повертайся через {time} по нову нагороду! | по + accusative of purpose is normative ("піти по воду"); 46/60 with "3 год 20 хв". "Наступна нагорода через {time}" if space is tight |
| codes.placeholder | Введи код | |
| codes.invalid | Такого коду немає або він уже не діє. | avoids calque "невірний"; "уже" after a consonant |
| social.like_reward | Постав лайк і отримай <b>Зілля удачі</b> безкоштовно! | |
| social.group_reward | Вступи до нашої групи й отримай безкоштовну нагороду! | 53/55; "й" between vowels; "отримай" reads more natural here than "розблокуй" |
| afk.warning | Ти АФК! Рухайся, щоб і далі заробляти! | "АФК" avoids gendered "неактивний"; Latin "AFK" if the game uses it elsewhere |
| leaderboard.title | Найкращі гравці | "Топ гравців" also fine |
| level.up | Новий рівень! Твій рівень: {level}. | colon avoids ordinal agreement |
| tutorial.sell | Зайди в сяйливе коло, щоб продати улюбленців. | "в" after a vowel; not "світяще" |
| inventory.full | Рюкзак повний! Продай улюбленців, щоб звільнити місце. | "your" dropped |
| settings.music | Музика | |
| settings.on | Так | pair with "Ні"; the usual toggle "Увімк." is 6 > 5, so ask the developer to widen the box to 6 and use "Увімк." / "Вимк." |
| loading | Завантаження… | single ellipsis character |
| event.ends_in | До кінця події: {time} | 27/28 with "2 дн. 5 год"; players also say "івент" |
| item.op | Цей меч — імба! | |
| friends.boost | Буст +{percent}% за кожного друга на сервері | |

## Sources
1. Microsoft Ukrainian localization style guide (PDF, via https://aka.ms/ukrainian-styleguide): https://download.microsoft.com/download/bdeb8a55-e64c-4844-ab0c-b5a26e0ac772/ukr-ukr-StyleGuide.pdf
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox language codes (`uk`, `uk-ua`): https://create.roblox.com/docs/production/localization/language-codes
4. Roblox locale API (`uk_ua`: in-game content yes, full platform UI no): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
5. Roblox on the Ukrainian App Store (language list without Ukrainian): https://apps.apple.com/ua/app/roblox/id431946152?l=uk
6. DevForum, "Friends Are Back!" (Connections -> Friends, April 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
7. DevForum, "Russian Text Scaling Issues" (Cyrillic fallback to Arial, 2019): https://devforum.roblox.com/t/russian-text-scaling-issues/232672
8. Ukrainian Wikipedia, Roblox (Robux, Premium, плейси, групи): https://uk.wikipedia.org/wiki/Roblox
9. Ukrainian Wikipedia, Adopt Me! (домашні тварини, улюбленці, вилуплюються з яєць, легендарні): https://uk.wikipedia.org/wiki/Adopt_Me!
10. Ukrainian Wikipedia, Нуб: https://uk.wikipedia.org/wiki/Нуб
11. Ukrainian Wikipedia, Комп'ютерний сленг (чітер, лаг, English origin of gamer slang): https://uk.wikipedia.org/wiki/Комп'ютерний_сленг
12. Ukrainian Minecraft Wiki, Досвід (досвід, рівень, інвентар, торгівля): https://uk.minecraft.wiki/w/Досвід
13. CLDR Ukrainian unit and number data (short duration forms "год", "хв", "с", "дн."; group separator U+00A0): https://github.com/unicode-org/cldr-json/tree/main/cldr-json/cldr-units-full/main/uk
14. Roblox Creator Docs, Localize with scripting (in-experience language switcher) and Player.LocaleId: https://create.roblox.com/docs/production/localization/localize-with-scripting, https://create.roblox.com/docs/reference/engine/classes/Player
15. DevForum, in-experience language switcher (2022; lists the languages the experience enables): https://devforum.roblox.com/t/localization-api-update-for-upcoming-in-experience-language-switcher/1974795
16. Font glyph check: cmap tables of the font files in the local Roblox client's `content/fonts`, 2026-11-08 (fontTools).
