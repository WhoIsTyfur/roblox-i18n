# Russian (ru-ru) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `ru-ru` (a bare `ru` column is optional: Roblox lists one Russian locale, so players in other regions fall back to `ru-ru` anyway) |
| Script, direction | Cyrillic, LTR |
| Address the player as | informal singular "ты" everywhere, as Roblox's own Russian UI does; never "вы", never capitalized "Вы" |
| Text expansion vs English | measured on the reference set below: sentences -13% to +26% (+11% overall, helped by colon rewrites); short buttons and labels +20-100% ("Buy" -> "Купить", "Daily Reward" -> "Ежедневная награда"). Budget +30% for free text |
| Plural categories (CLDR) | one, few, many, other |
| Model confidence | high: well-resourced language, and Roblox's own Russian UI confirms the register; the real risks are gender and plural agreement around placeholders and gamer slang |
| Native review before shipping | recommended |

## Audience and register
- Russian is read across Russia, Belarus, Kazakhstan, Kyrgyzstan and the diaspora. Write neutral standard Russian: no rubles, Russia-only holidays or region names.
- Platform status, 2025-2026: Roblox was blocked in Russia in December 2025 (press reports, unverified) and Roblox confirmed restored access on 2026-06-11. A July 2026 DevForum bug report says Russian is not officially offered in the app: the app showed Russian for a few days, then reverted to English; no staff reply. The client still ships Russian core UI strings (1,585 of 1,605 CoreScript strings have a `ru` translation, client build of 2026-11-05). Whether real Russian players get `Player.LocaleId` = `ru-ru` is unverified; Studio's Player Emulator only proves the table works, not what live players receive.
- Use "ты" in every string. Roblox's own Russian UI does ("Повтори попытку позже", "Проверь подключение"; 136 ты-forms to 4 вы-forms in the client strings), and so do games and YouTubers for 9-16 year olds; "вы" reads like a bank or a school notice. Microsoft's Russian guide uses вы, but that is adult software register. Never mix: "Нажми E — получишь награду", not "Нажмите E — получишь награду".
- Buttons, tabs and toggles: infinitive or noun, the Russian UI norm (Roblox: "Купить", "Выйти"): "Играть", "Купить", "Забрать", "Магазин". When neither fits the box, a short ты-imperative is fine ("Переродись"). Sentences, tips and tutorials: ты-imperative: "Продай питомцев", "Зайди в круг".
- Hype sounds natural as short exclamations: "Ура!", "Новый уровень!", "Круто!", "Не упусти!". Too adult or stiff: "данный", "осуществить покупку", "в целях", "уникальное предложение".
- Prefer verbs to verbal nouns (Microsoft guide): "Чтобы продать питомцев..." not "Для осуществления продажи питомцев...".
- Don't blame the player in errors: "Код не подошёл" rather than "Ты ввёл неверный код" (which is also gendered, see below).
- Write the letter ё consistently ("ещё", "твоё", "зелёный"). It helps young readers and matches Roblox's own Russian UI ("ещё" 13 times, "еще" never); Microsoft omits it. Never mix both spellings in one game.
- Kid-safe slang is fine ("имба", "буст", "нуб" in a joke). No insults ("лох", "дурак"), no crude words.

## Roblox and gaming vocabulary
| English | Russian | note |
|---|---|---|
| Robux | Robux | Latin, never declined, as in Roblox's UI ("Купить Robux", "Недостаточно Robux"): "за 50 Robux". Players write "робуксы"/"робаксы" in chat; not in UI. |
| Premium | Premium | Latin; Roblox writes "подписка Premium", "Только для подписчиков Premium". |
| game pass | геймпасс | what Russian players and press say; "пропуск" as plain synonym. In the shop just show the pass name. Roblox's own Russian label unverified. |
| developer product | покупка, товар | players never see the term; name the item itself. |
| experience / game | игра; Roblox UI: плейс | your own game is "игра". Roblox's Russian UI calls an experience "плейс" ("Этот плейс отключён"). Never "опыт" (= XP) or "впечатление". |
| obby | обби | "паркур" in descriptions. |
| tycoon | тайкун | |
| simulator | симулятор | |
| rebirth | перерождение; verb переродиться | short button: "Переродись" (10). Never the slang ребёрт / ребирт / ребитх in UI: players spell it several ways, so any pick looks wrong to some. |
| pet | питомец, питомцы | "пет", "петы" are chat slang; UI says питомец. |
| egg / hatch | яйцо; открыть яйцо; вылупиться | button "Открыть"; "Из яйца вылупился дракон". |
| coins | монеты | |
| gems | кристаллы | "гемы" is slang; "алмазы" if the art shows diamonds. |
| boost | буст | standard gamer word; "усиление" in longer text. |
| multiplier | множитель; "x2" | |
| XP | опыт, XP | "+50 опыта" or "+50 XP"; pick one per game. |
| level up | новый уровень; уровень повышен | not "левел ап". |
| quest | задание | "квест" also understood. |
| leaderboard | таблица лидеров; лучшие игроки; топ | |
| AFK | АФК | Cyrillic in UI; Latin AFK also seen in chat. |
| noob | новичок (UI); нуб (jokes) | |
| OP | имба | teen slang from "imbalanced". |
| VIP | VIP | Latin; "VIP-сервер", "VIP-статус". |
| trade | обмен; обменяться | "трейд" in chat only. |
| inventory / backpack | инвентарь / рюкзак | keep whichever the source means. |
| daily reward | ежедневная награда | |
| codes | коды, промокоды | redeem = "активировать"; placeholder "Введи код". |
| group | группа | "Вступи в группу". |
| like / favorite | лайк, "Поставь лайк" / избранное, "Добавь в избранное" | Roblox's Russian UI: "Избранное", "Хочешь добавить в избранное...?". |
| server | сервер; частный сервер | Roblox's UI says "частный сервер"; players also say "приватный сервер". |
| friends | друзья | Roblox renamed Connections back to Friends in April 2026; its Russian UI shows "Друзья", "Добавить друга" (a few leftover strings still say "контакт"). Game text: друзья; never "связи" or "контакты". |

## Grammar traps in UI strings
- Plurals: four CLDR forms: one (1, 21: монета), few (2-4, 22-24: монеты), many (0, 5-20, 11-14, 25: монет), other (1,5: монеты). One string per key, so never put {count} right before a countable noun.
  - Bad: "{amount} монет" -> "1 монет", "2 монет". Good: "Монеты: {count}", "Нужно ещё монет: {amount}" (Roblox itself writes "Ещё Robux: {robux}").
  - Undeclinable units are safe after a number: "{price} Robux", "{percent}%", "x{multiplier}", "{n} шт.".
- Gender: past-tense verbs and short adjectives agree with the subject. {player} can be any gender, so:
  - use present tense, as Roblox's own Russian UI does ("{RBX_NAME} получает награду", "...присоединяется к плейсу"): "{player} заходит в игру", "{player} предлагает тебе обмен";
  - or a fixed noun head: "Игрок {player} вышел" (agrees with "игрок");
  - or a colon: "Победитель: {player}".
- The player as "you" has gender too: "Ты получил(а)" is ugly. Use future, present or a noun: "Ты получишь...", "Твоя награда: ...", "Получено: ...".
- Inserted item names: adjectives agree with the noun's gender: легендарный дракон, легендарная кошка, легендарное яйцо. Translate rarity labels in the masculine (agreeing with an implied "питомец") and write "{rarity} питомец: {pet}!", never "{rarity} {pet}".
- Case: a translated {pet} arrives in the nominative. Keep it as subject or after a colon; "у тебя нет {pet}" would need the genitive -> rewrite "Нет питомца: {pet}". Usernames are Latin and never declined.
- Durations after "через" are safe because abbreviations don't decline: "через 3 ч 20 мин".
- Ordinals: "уровень {level}" or "Уровень: {level}" is safest; "{level}-й уровень" works but adds a suffix rule.
- No articles: drop "a/the" entirely ("a Rare Dragon" -> "редкий дракон").
- English noun stacks become genitive or adjective phrases: "Pet Storage" -> "хранилище питомцев", "Coin Boost" -> "буст монет". Latin + Russian compounds take a hyphen: "VIP-сервер".
- Capitalization: sentence case for titles and buttons ("Ежедневная награда", "Лучшие игроки"); no capital after a colon mid-sentence.

## Typography and formatting
- No space before ! ? : ; and one space after them: "Ура! Новый уровень!".
- Dash: em dash with spaces " — " ("Этот меч — имба!"); hyphen without spaces in compounds ("VIP-сервер"); en dash without spaces in ranges ("10–20").
- Quotes: «ёлочки», nested „лапки“, as Roblox's own Russian UI does ("нажми на клавишу «/»"; 26 «» pairs to one straight pair). Never English curly quotes (U+201C, U+201D). Microsoft prescribes straight quotes for software UI; ignore that here.
- Numbers: thousands separator is a space ("1 250"), decimal separator a comma ("1,5"). The canonical {count} arrives preformatted as "1,250", which a Russian reader takes for 1.25, and a multiplier "1.5" shows a decimal point. Translators can't fix values filled by code: keep {count} as is and tell the developer to format numbers per locale in code (space for thousands, comma for decimals).
- Percent: keep "{percent}%" attached as in the source; documentation style puts a non-breaking space ("10 %"), not needed in compact UI.
- Multiplier: Latin x before the number: "x2", "Монеты x2", "буст x{multiplier}". Never Cyrillic "х2".
- Time: ч, мин, с without a period; compact timers "2 д 5 ч", "3 ч 20 мин" (Microsoft lists "дн." for days in running text). If game code outputs "3h 20m", flag it.
- Ellipsis: the single character … with no space before: "Загрузка…" (Microsoft). Roblox's own Russian UI types three periods; also acceptable, but pick one per game. Every Cyrillic Roblox font below has the … glyph.
- Keys stay Latin: "Нажми E", or "Нажми клавишу E". Mouse buttons: ЛКМ / ПКМ are standard gamer abbreviations.
- Words are long ("Перерождение", "Достижения") and Roblox does not hyphenate: enable TextWrapped, never insert manual hyphens.
- Accepted short forms only: "ур." (уровень), "шт.", "мин", "Вкл." / "Выкл.".

## Do not translate / keep as is
- Robux, Roblox, Premium, VIP, Roblox Studio: Latin, undeclined.
- Game titles ("Pet Hatch Tycoon"): keep in English; players search for the English title.
- Usernames and display names: never translate, transliterate or decline.
- Promo codes ("FREEPETS"): exactly as given, Latin, same case; translate only the text around them.
- Key names (E, Q, Shift, Space) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Зелье удачи"); invented brand-like names stay Latin only if the game treats them as brands.
- Transliterate only established gamer loanwords (буст, тайкун, обби, имба); don't invent new ones ("лакки потион").

## Rendering on Roblox
- Checked 2026-11-08 by reading the character maps of the fonts bundled with the Roblox client (build of 2026-11-05, `content/fonts`) for А-я, Ёё, « », …, —:
  - Full Russian: Arimo, Montserrat (Regular to Black), Nunito, Oswald, Roboto (incl. Condensed, Mono), Source Sans Pro (Light to Bold; the 2020 report that Regular lacked Cyrillic is outdated), Ubuntu, Merriweather, Amatic SC, Jura, Press Start 2P, Zekton (no №).
  - No Cyrillic at all: Builder Sans (Roblox's default UI font), Builder Extended and Mono, Fredoka One, Luckiest Guy, Bangers, Denk One, Titillium Web, Comic Neue Angular, Creepster, Patrick Hand, Permanent Marker, Kalam, Michroma, Sarpanch, Source Sans Pro Italic. Russian text in these falls back to another font.
  - Gotham and the cloud-only Builder Sans weights (Thin, Light, Semi Bold) were not checked.
- Which fallback face current builds use is unverified. A 2019 DevForum report found Arial, rendered larger, which broke TextScaled sizing and left an empty line.
- Recommendation: the game's code should swap FontFace for Russian players (a LocalizationTable can't): Montserrat Bold/Black or Nunito for cartoon headers and buttons, Source Sans Pro or Roboto for body text.
- Risks: one label mixing two fonts ("x2" in the display font, Russian in the fallback); Ё and Й marks clipped in tight TextScaled boxes; long words overflowing buttons.
- Verify in Studio: Player Emulator set to Russian; open every panel with the longest strings; paste "Съешь же ещё этих мягких французских булок, да выпей чаю" into each font face used; check ё, й, щ, ъ, « » and numbers.

## Mistakes machine translation makes here
- "experience" as опыт (= XP): "Лучший опыт в Roblox" -> "Лучшая игра в Roblox".
- "redeem" as погасить (pay off a debt): "Погасить код" -> "Активировать код".
- "Claim" as требовать or заявить: "Требовать" -> "Забрать".
- Register drift: "Нажмите E, ты получишь" -> "Нажми E — получишь".
- Gendered past with a username: "{player} присоединился к игре" -> "{player} заходит в игру".
- Number + noun: "У тебя {count} монет" -> "Монеты: {count}".
- Cyrillic look-alikes in keys and codes: "Нажми Е" (Cyrillic Е) -> "Нажми E" (Latin); "х2" -> "x2".
- English Title Case: "Ежедневная Награда" -> "Ежедневная награда".
- Literal slang: "Этот меч сверхмощный" / "ОП" -> "Этот меч — имба!".
- Translating every "your": "Твой рюкзак полон" -> "Рюкзак полон!".
- Bureaucratic nouns: "Для продолжения заработка осуществите движение" -> "Двигайся, чтобы и дальше зарабатывать".
- Stacked calques: "Топ Игроки" -> "Лучшие игроки".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Играть | infinitive on buttons |
| shop.title | Магазин | |
| shop.buy | Купить | |
| reward.claim | Забрать | "Получить" (8) also fine |
| rebirth.button | Переродись | 10/10. Use "Перерождение" (12) if the button allows 12; imperative only because "Переродиться" (12) doesn't fit; no slang spellings |
| rebirth.confirm | Переродиться сейчас? Ты потеряешь монеты, но получишь буст x{multiplier} навсегда. | x before the number; "навсегда" for permanent ("вечный" sounds odd) |
| coins.need_more | Нужно ещё монет: {amount}! | colon avoids plural forms |
| coins.count | Монеты: {count} | "1,250" should be "1 250" for Russian (code issue, not the translator's) |
| egg.hatched | {rarity} питомец: {pet}! | rarity must be masculine and leads, so its capital fits; "You hatched" dropped to avoid a gendered verb, since the toast follows the egg opening |
| rarity.legendary | Легендарный | masculine, agrees with "питомец" |
| pet.name.dragon | Дракон | |
| chat.player_joined | {player} заходит в игру | present tense avoids gender |
| trade.request | {player} предлагает тебе обмен | present tense avoids gender |
| prompt.open_shop | Нажми E, чтобы открыть | Latin E; 22/22 fits, so keep it; "E — открыть" only for a smaller box |
| pass.buy_price | Купить за {price} Robux | Robux undeclined |
| pass.coins2x | Монеты x2 | |
| pass.vip | VIP | kept: Latin VIP is the standard Russian form ("VIP-статус") |
| reward.daily_title | Ежедневная награда | 18/18; fallback "Награда дня" |
| reward.come_back | Возвращайся через {time} за новой наградой! | time units should be "3 ч 20 мин" |
| codes.placeholder | Введи код | |
| codes.invalid | Код неверный или уже не действует. | |
| social.like_reward | Поставь лайк игре — получи <b>Зелье удачи</b> бесплатно! | "игре" keeps "the game"; Зелье is neuter, so accusative = nominative |
| social.group_reward | Вступи в нашу группу и получи бесплатную награду! | "получи", not calque "разблокируй" |
| afk.warning | Ты АФК! Двигайся, чтобы зарабатывать! | "чтобы и дальше зарабатывать" (keep earning) is 46 > 45 |
| leaderboard.title | Лучшие игроки | "Топ игроков" also fine |
| level.up | Уровень повышен! Твой уровень: {level}. | colon avoids ordinal agreement |
| tutorial.sell | Зайди в светящийся круг, чтобы продать питомцев. | |
| inventory.full | Рюкзак полон! Продай питомцев, чтобы освободить место. | "your" dropped |
| settings.music | Музыка | |
| settings.on | Вкл. | pair with "Выкл." |
| loading | Загрузка… | single ellipsis character |
| event.ends_in | До конца события: {time} | 25/28 with "2 д 5 ч", 28/28 with "3 ч 20 мин": keep as default; "Осталось: {time}" if durations run longer or the box is smaller |
| item.op | Этот меч — имба! | |
| friends.boost | Буст +{percent}% за каждого друга на сервере | |

## Sources
1. Microsoft Russian localization style guide (PDF, via https://aka.ms/russian-styleguide): https://download.microsoft.com/download/c/8/a/c8ab1532-a15d-4f94-96c2-9740bc230757/rus-rus-StyleGuide.pdf
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. DevForum, "Friends Are Back!" (Connections -> Friends, April 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
4. DevForum, Russian missing from the app language list (July 2026): https://devforum.roblox.com/t/russian-language-is-not-supported-although-localization-data-is-available/4732213
5. Roblox newsroom, access restored in Russia (2026-06-11): https://about.roblox.com/newsroom/2026/06/roblox-access-restored-in-russia
6. DevForum, "Russian Text Scaling Issues" (Arial fallback, 2019): https://devforum.roblox.com/t/russian-text-scaling-issues/232672
7. Roblox client files, `ExtraContent/translations/CoreScriptLocalization.csv`, `ru` column (Roblox's own Russian UI: ты, ё, «», плейс, Избранное, частный сервер, Robux undeclined), read 2026-11-08
8. Roblox client files, `content/fonts` character maps (Cyrillic coverage per font), read 2026-11-08
9. T-Journal, "Геймпасс в «Роблоксе»" (геймпасс, пропуск, робуксы, игра): https://t-j.ru/roblox-gamepass/
10. Russian Roblox dev community, simulator tutorial (монеты, питомцы, симулятор): https://m.vk.ru/@roblo_forum-kak-sozdat-svoi-pervyi-simulyator-v-roblox-studio-rukovodstv
11. ichip.ru, finding friends in Roblox ("Друзья" menu; search summary): https://ichip.ru/gejming/igry/kak-najti-druzej-v-roblokse-gajd-dlya-pk-i-mobilnogo-prilozheniya-922702
12. Mel, "имба" as teen slang (search summary): https://mel.fm/gramotnost/chto-eto-znachit/5632879-chto-takoye-ili-kto-takoy-imba-yeshche-odno-slovo-iz-podrostkovogo-slenga
13. Machine-translated Pet Simulator X codes page (example of MT errors such as "Погасить"): https://www.alucare.fr/ru/wiki/roblox/roblox-codes-pet-simulator-x/
