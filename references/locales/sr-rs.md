# Serbian (sr-rs) translation guide

**Script decision: write Cyrillic (ћирилица) in every string, with Latin only for the tokens listed under "Do not translate".** Roblox labels the locale "српски", and Roblox's own Serbian Google Play listing is in Cyrillic, with Roblox and Robux left in Latin. CLDR expands `sr` to `sr-Cyrl-RS` (Latin is the default only for `sr-ME`), Cyrillic is Serbia's constitutional script, and schools teach both scripts (Cyrillic first, unverified), so every Serbian kid reads it. Kids do chat in Latin, and Latin dominates online, but Google Play's Serbian UI is Cyrillic and Minecraft's Latin "Srpski" file has the same keys as its Cyrillic "Српски" and is mostly a transliteration of it (about 80% of strings letter for letter). Cyrillic -> Latin transliteration is one-to-one, so a developer who wants Latin can convert this column mechanically; the reverse is ambiguous ("konjunkcija", "nadživeti"). The repo's locale row (`"script": "Cyrl"`) and lint expect Cyrillic. The cost: most Roblox display fonts have no Cyrillic (see Rendering).

## At a glance
| | |
|---|---|
| Roblox locale / column | `sr-rs` (Roblox lists one Serbian locale only, so a bare `sr` column adds nothing) |
| Script, direction | Cyrillic (Serbian alphabet, 30 letters incl. ђ ј љ њ ћ џ), LTR; ekavian standard |
| Address the player as | informal singular "ти" ("Играј", "Купи"); never "ви"/"Ви" |
| Text expansion vs English | sentences about 0-30% (this guide's reference set: +5% on average, -33% to +57% per string); one-word labels up to +150% ("Shop" -> "Продавница") |
| Plural categories (CLDR) | one, few, other |
| Model confidence | medium: models leak Russian letters and words, Latin look-alike letters and Croatian/Bosnian forms into Serbian Cyrillic; kid slang unverified |
| Native review before shipping | strongly recommended |

## Audience and register
- Readers: kids in Serbia, plus Serbs in Republika Srpska (BiH), Montenegro and the diaspora. Bosnian and Croatian players have their own Latin columns.
- Roblox has no Serbian app UI: its locale service enables `sr_rs` for in-experience content only, not the full app or signup. Players see Roblox menus in English (or another language) and know platform terms from there. How a player ends up with LocaleId `sr-rs` is unverified; test with Studio's Player Emulator.
- Use "ти" everywhere. Microsoft's Serbian guide prescribes lowercase "ви" for adults, and Roblox's store listing uses ви imperatives ("Откријте", "Придружите се"); Minecraft's Serbian buttons use ти ("Играј", "Изађи из игре", "Направи нови свет"), though its tooltips slip into ви ("Пријатељи могу видети шта играте"); do not copy that mix. Never mix in one game: "Притисни E и покупи награду", not "Притисните E и покупи награду".
- Buttons: 2nd-person singular imperative ("Играј", "Купи", "Покупи", "Отвори"). Titles and tabs: nouns ("Продавница", "Дневна награда"). Ongoing processes: verbal noun, as Microsoft prescribes ("Учитавање…", not "Учитава").
- After modal verbs prefer "да + present", the form Microsoft uses ("морате да обновите", "Желите ли да наставите?"): "Мораш да продаш љубимце". The infinitive is correct but reads more Croatian.
- Hype that sounds natural: "Супер!", "Браво!", "Свака част!", "Лудило!", "Легенда си!", "Нови ниво!". Stiff or adult: "Извршите куповину", "Успешно сте...", "Обавештавамо вас", anything with "од стране" (Microsoft bans it as a calque). Microsoft's plain-word pairs apply: "пронаћи" not "лоцирати", "следеће" not "наредно", "проверити" not "уверити се".
- Drop the possessives English needs (Microsoft rule): "Продај љубимце", not "Продај твоје љубимце". When one is needed, use reflexive "свој": "Покажи своје љубимце".
- Ekavian Serbian standard: "време", "следећи", "место", "свет", "светлећи", "помери се". Serbian words: "хиљада", "музика", "ниво", "куповина", "недеља" (week).
- Kid-safe: light slang is fine ("лудило", "свака част", "нуб" in a joke); no insults ("будала", "глуп си") and no swearing.

## Roblox and gaming vocabulary
| English | Serbian | note |
|---|---|---|
| Robux | Robux | Latin, as in Roblox's Serbian listing ("бесплатним Robux трансферима"). After a number, undeclined like a currency code: "{price} Robux". Declined: "Robux-а". sr.wikipedia writes "Робукс"; not in UI. |
| Premium | Premium / Roblox Plus | Latin, undeclined. The Play listing (English and Serbian, checked 2026-11-08) sells the subscription as "Roblox Plus", while Creator Hub docs still say "Premium"; a rename on every surface is unverified. Use the name the game's English source uses. |
| game pass | пропусница; in the shop just the pass name | sr.wikipedia writes "гејм-пес"; chat "gejmpas" (unverified). |
| developer product | (name the item) | players never see the term. |
| experience / game | игра | the Play listing uses "искуства" for experiences; in a game's own UI say "игра". |
| obby | стаза с препрекама; "оби" in titles (unverified) | sr.wikipedia: "игре са препрекама". |
| tycoon | тајкун | Play listing: "у тајкунима". |
| simulator | симулатор | Play listing: "симулаторе". |
| rebirth | препород; verb "препородити се" | 8 letters, fits buttons; chat "rebirth" (unverified). |
| pet | љубимац, pl. љубимци, acc. pl. љубимце | "пет" in chat (unverified). |
| egg / hatch | јаје / излећи се; button "Отвори јаје" | past "излегао се" agrees with "љубимац". |
| coins | новчићи (sg. новчић) | "кованице" sounds like real money. |
| gems | драгуљи | "дијаманти" if the art shows diamonds. |
| boost | појачање | "буст" in chat (unverified); "бонус" is fine for % bonuses. |
| multiplier | "2x", "{multiplier}x" | write the sign; noun "множилац" rarely needed. |
| XP | XP; искуство | "+50 XP"; Minecraft says "ниво искуства". Pick one per game. |
| level / level up | ниво / "Нови ниво!" | Minecraft: "Ниво унапређен". |
| quest | задатак; мисија | Play listing: "епске задатке". |
| leaderboard | Најбољи играчи; ранг-листа | |
| AFK | AFK | Latin capitals in UI; Vukajlija lists "afk" as Serbian gamer slang. |
| noob | почетник (UI); "нуб" (jokes) | Vukajlija lists "noob" and "nubiša" in Latin. |
| OP | прејак | "OP" understood by gamers (unverified). |
| VIP | VIP | "VIP сервер", gen. "VIP-а". |
| trade | размена; "мењати се" | Minecraft: "Размене". Not "трговина" (= commerce). |
| inventory / backpack | инвентар / ранац | Minecraft: "Инвентар". |
| daily reward | дневна награда | |
| codes | кодови; "Унеси код"; redeem = "Искористи" | |
| group | група | "Придружи се групи". |
| like / favorite | лајк, "Лајкуј игру" / "Додај у омиљене" | verb "лајковати", imperative "лајкуј"; kid preference vs "Дај лајк" unverified. |
| server | сервер; приватни сервер | Play listing: "приватне сервере". "на серверу", not "у серверу". |
| friends | пријатељи | Play listing: "са пријатељима". Roblox renamed Connections back to Friends in April 2026; never "конекције" or "везе". |
| avatar / chat | аватар / чет | Play listing "аватар", "гласовно ћаскање"; Minecraft "чет". |

## Grammar traps in UI strings
- Plurals: one (1, 21, 31; not 11), few (2-4, 22-24; not 12-14), other (0, 5-20, 25...). "1 новчић, 2 новчића, 5 новчића, 21 новчић"; feminine nouns have three forms: "1 награда, 2 награде, 5 награда". One string per key, so never put {count} straight before a countable noun.
  - Bad: "{count} новчића" -> "1 новчића", "21 новчића". Good: "Новчићи: {count}", "Фали још {amount}".
  - Safe after a number: undeclined units "{price} Robux", "{percent}%", "{multiplier}x", "{n} ком.".
- Past tense carries gender: "ушао" (m) / "ушла" (f). Minecraft's "%s је ушао у игру" is wrong for every girl. {player} can be anyone, so:
  - use present or a state: "{player} је сада у игри", "{player} ти нуди размену";
  - or a fixed head noun: "Играч {player} је напустио игру" (agrees with "играч");
  - or a colon: "Победник: {player}", "Аутор: {player}".
- The player as "you" has gender too: "Добио си" / "Добила си", and the conditional "да би зарађивао". Use future, present or a noun: "Добићеш...", "Сада си на нивоу 5", "Твоја награда: ...". Never "Добио/ла си".
- Adjectives agree: легендарни змај, легендарна мачка, легендарно јаје. Translate rarity tags in the masculine (agreeing with an implied "љубимац") and never write "{rarity} {pet}"; use "Нови љубимац: {pet} ({rarity})!". A lone adjective in a menu with no noun goes neuter (Microsoft: "Ново", "Непознато").
- Seven cases. An inserted {pet} or item arrives in the nominative; keep it as subject or after a colon: "Купио си {item}" -> "Купљено: {item}". Usernames are never declined; carry the case on a noun: "Играј са играчем {player}", "Поклон од играча {player}".
- Latin tokens decline with a hyphen and a Cyrillic ending (Microsoft: "XML-у", "ID-ом"; Roblox's listing: "на Roblox-у"): "Robux-а", "VIP-у". The ending must be Cyrillic а/у, not Latin a/u.
- Future is one word: "изгубићеш", "добићеш" (not Croatian/Bosnian "добит ћеш"). Questions: "Желиш ли да наставиш?" or "Да ли желиш да наставиш?".
- No articles: drop a/the ("a Rare Dragon" -> "редак змај"). Indefinite adjective for new things: "добиј бесплатан напитак", not "бесплатни".
- English noun stacks become genitive, adjective + noun, or a preposition (Microsoft): "Coin Boost" -> "појачање новчића", "Pet Storage" -> "простор за љубимце".
- No comma before a trailing "да" clause (Microsoft): "Притисни E да отвориш", not "Притисни E, да отвориш".
- Capitalization: sentence case for titles, buttons and item names ("Дневна награда", "Напитак среће"); days, months and language names lowercase ("субота", "мај", "српски").

## Typography and formatting
- No space before ! ? : ; and one space after (Microsoft). "Браво! Нови ниво!"
- Quotes: Serbian „...“ (U+201E, U+201C) for UI references, ’...’ (U+2019 on both sides) inside them (Microsoft): Кликни „Купи“. Never English “...”.
- Dashes: no em dash in Serbian (Microsoft). Spaced en dash for asides: "Купи одмах – бесплатно!"; unspaced en dash in ranges: "10–20". Hyphen for compounds and endings: "ранг-листа", "VIP-а".
- Ellipsis: one "…" character (U+2026), no space before (Microsoft): "Учитавање…".
- Numbers: decimal comma, period for thousands (CLDR): "1,5", "1.250". Game code that outputs "1,250" reads to a Serbian kid as one point twenty-five, so ask the developer to format numbers per locale; do not "fix" numbers inside the string.
- Percent: no space (CLDR pattern `#,##0%`): "50%", "+{percent}%". Ordinals take a period: "5. ниво", "1. место".
- Durations: CLDR narrow units "д ч м с", Microsoft "ч", "мин", "с" without a period: "3 ч 20 мин", "2 д 5 ч". If the game's formatter prints "3h 20m", the line mixes scripts. LocalizationTables only substitute {params}, so the fix is a LocaleId-aware formatter in game code (flag it to the developer); never rewrite the value inside the string. Clock: 24-hour, "14:30".
- Keys: keep the Latin key letter: "Притисни E". Microsoft: Enter, Shift, Esc stay English; Space = "размакница" (Minecraft: "Размак"); arrows "стрелица нагоре/надоле".
- Multiplier: Latin "x" or "×", never Cyrillic "х" (U+0445), which looks the same but is a letter.

## Do not translate / keep as is
- Keep in Latin: Roblox, Robux, Premium/Roblox Plus, VIP, AFK, XP, usernames and display names, promo codes ("FREEPETS"), keybinds, the game title "Pet Hatch Tycoon" unless the developer ships a localized title. Roblox's Serbian listing keeps Roblox, Roblox Studio, Marketplace, RPG and game titles in Latin; Microsoft keeps product names untranslated and unquoted.
- Do not transliterate those ("Роблокс", "Робукс" are Wikipedia and news style, not UI), and add no other Latin words.
- Translate in-game item, pet and rarity names ("Напитак среће", "Змај", "Легендарни").
- Every other word is Serbian Cyrillic. Never Russian я ю ё й ы э щ ъ ь, Ukrainian і ї є or Macedonian ѓ ќ ѕ.
- If the developer insists on Latin, transliterate this finished column letter by letter (љ -> lj, њ -> nj, џ -> dž, ђ -> đ, ћ -> ć, ј -> j), keep the Latin tokens, and change the locale row to `Latn` so lint passes; never retranslate. Fredoka One lacks Č Ć Đ č ć đ, so Latin breaks there too.

## Rendering on Roblox
- Glyph check run locally 2026-11-08 (fontTools cmap on the Roblox client's `content/fonts`): no Cyrillic at all in Builder Sans, Builder Extended, Builder Mono, Fredoka One, Luckiest Guy, Bangers, Denk One, Titillium Web, Sarpanch, Permanent Marker, Comic Neue Angular, Creepster, Michroma, Patrick Hand, Kalam, Indie Flower, Josefin Sans, Special Elite or Source Sans Pro Italic.
- Full Serbian Cyrillic (incl. Ђ Ј Љ Њ Ћ Џ) plus „ “ – …: Arimo, Source Sans Pro (Regular, Light, Semibold, Bold), Roboto, Roboto Condensed, Roboto Mono, Montserrat, Merriweather, Nunito, Oswald, Ubuntu, Press Start 2P, Amatic SC, Jura, Zekton.
- A Latin-only font falls back to another font for Cyrillic. Which one is unverified: the client ships Noto fallbacks for other scripts but none for Cyrillic, plus LegacyArial and Arimo families, which fits a 2019 DevForum report of an Arial fallback that rendered larger and left an empty line under TextScaled.
- Recommendation: for sr-rs set a Cyrillic font instead of relying on fallback (Nunito or Montserrat for a rounded, friendly look; Roboto for plain UI; Press Start 2P for pixel style), so one label never mixes "2x" in the display font with Serbian in a fallback. Only the bundled faces were checked (Nunito ships Regular only); other weights stream as assets, so test bold faces too.
- Serbian italic б г д п т differ from Russian ones (Russian italic т looks like m). Arimo, Merriweather, Montserrat, Source Sans Pro and Ubuntu carry Serbian (SRB) OpenType forms; whether Roblox applies them is unverified, so avoid italic Serbian text. Upright Russian shapes read fine.
- Luau `string.upper` changes ASCII only, so "новчићи" stays lowercase. Write capitals in the table ("НОВЧИЋИ").
- Verify in Studio: Player Emulator locale `sr-rs`; paste "ЂЈЉЊЋЏ ђјљњћџ Љубичасти џемпер, ђак, ћуп, „Купи“ 1.250 – 50%…" into every FontFace the game uses; open the longest strings (social.group_reward at 53/55) and full buttons (shop.title at 10/10).

## Mistakes machine translation makes here
| Mistake | Bad | Good |
|---|---|---|
| Latin output in the Cyrillic column | Kupi, Igraj | Купи, Играј |
| Latin look-alike letters inside Cyrillic words (Roblox's own locale list has "Cрпски" with Latin C; Minecraft's Serbian file has 61 such strings) | Cрпски, Откриjте | Српски, Откријте |
| Russian words or letters | Загрузка..., Магазин, Уровень | Учитавање…, Продавница, Ниво |
| Ijekavian (Bosnian/Montenegrin) forms | Сљедећа награда, вријеме | Следећа награда, време |
| Croatian vocabulary | разина, глазба, тисућа, купња | ниво, музика, хиљада, куповина |
| Adult "ви" register | Притисните E да отворите | Притисни E да отвориш |
| Transliterated brands | 100 Робукса, Роблокс | 100 Robux, Roblox |
| Latin ending on a Latin token | Robux-a, Robuxa | Robux-а (Cyrillic а) |
| Gendered past for {player} or you | {player} је ушао у игру; Излегао си змаја | {player} је сада у игри; Нови љубимац: Змај |
| Count before a noun | {count} новчића -> "1 новчића" | Новчићи: {count} |
| claim as "затражи" (= request) or "преузми" (= download) | Затражи | Покупи |
| English Title Case (Minecraft has "Ниво Искуства") | Дневна Награда | Дневна награда |
| "од стране" passive calque | Направљено од стране {player} | Аутор: {player} |

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Играј | |
| shop.title | Продавница | 10/10; "Радња" (5) if space is tight |
| shop.buy | Купи | |
| reward.claim | Покупи | not "Затражи"; "Преузми" reads as Download |
| rebirth.button | Препород | |
| rebirth.confirm | Препород сада? Изгубићеш новчиће, али добићеш трајно појачање {multiplier}x. | future tense avoids gender |
| coins.need_more | Немаш довољно новчића! Фали још {amount}. | number without a noun avoids plural forms; "Недостаје" is the formal verb |
| coins.count | Новчићи: {count} | label pattern; 14/16 with "1.250" |
| egg.hatched | Нови љубимац: {pet} ({rarity})! | no past tense, no {rarity} before {pet} |
| rarity.legendary | Легендарни | masculine, agrees with "љубимац" |
| pet.name.dragon | Змај | |
| chat.player_joined | {player} је сада у игри | "is now in the game"; gender-neutral. If a "joined" verb is wanted: "Играч {player} се придружио игри" (verb agrees with "играч") |
| trade.request | {player} ти нуди размену | |
| prompt.open_shop | Притисни E да отвориш | 21/22; E stays Latin |
| pass.buy_price | Купи за {price} Robux | Robux undeclined after a number |
| pass.coins2x | 2x новчићи | "Дупли новчићи" (13) also natural |
| pass.vip | VIP | kept: Latin abbreviation Serbian players use as is ("VIP сервер") |
| reward.daily_title | Дневна награда | |
| reward.come_back | Врати се за {time} по следећу награду! | |
| codes.placeholder | Унеси код | |
| codes.invalid | Код није исправан или је истекао. | |
| social.like_reward | Лајкуј игру и добиј бесплатан <b>Напитак среће</b>! | "Напитак среће" is Minecraft's Serbian name for the luck potion |
| social.group_reward | Придружи се нашој групи и откључај бесплатну награду! | 53/55; shorter: "Уђи у нашу групу за бесплатну награду!" |
| afk.warning | AFK си! Помери се и настави да зарађујеш. | "настави да" keeps it gender-neutral |
| leaderboard.title | Најбољи играчи | masculine generic |
| level.up | Нови ниво! Сада си на нивоу {level}. | gender-neutral |
| tutorial.sell | Уђи у светлећи круг да продаш љубимце. | no possessive (Microsoft rule) |
| inventory.full | Ранац је пун! Продај љубимце да ослободиш место. | |
| settings.music | Музика | |
| settings.on | Укљ. | 4/5; Off = "Искљ." (5) also fits, unlike Latin "Isklj." (6). Minecraft's Serbian toggles use "ДА"/"НЕ" instead |
| loading | Учитавање… | single ellipsis character |
| event.ends_in | Догађај траје још {time} | "lasts {time} more"; 25/28 with "2 д 5 ч", 28/28 with "3 ч 20 мин"; "се завршава за" overflows |
| item.op | Овај мач је прејак! | keeping "OP" would also be understood (unverified) |
| friends.boost | +{percent}% појачања за сваког пријатеља на серверу | genitive after %, as in "20% попуста" |

## Sources
1. Roblox language codes (Serbian shown as "српски", `sr` / `sr-rs`, no Latin variant): https://create.roblox.com/docs/production/localization/language-codes
2. Roblox locale API (`sr_rs`: in-game content only; native name "Cрпски" with a Latin C): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
3. Microsoft localization style guides index (Serbian Cyrillic and Latin guides): https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
4. Microsoft Serbian (Cyrillic) style guide PDF: https://download.microsoft.com/download/eac5bda0-b3f6-45dd-add8-449f6d47a4c6/scc-scg-StyleGuide.pdf
5. Microsoft Serbian (Latin) style guide PDF (same rules, Latin endings): https://download.microsoft.com/download/7/3/1/7312fa5f-ac47-438b-906b-3f141421aa59/srp-scg-StyleGuide.pdf
6. CLDR plural rules (sr, bs, hr identical): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-core/supplemental/plurals.json
7. CLDR likely subtags (`sr` -> `sr-Cyrl-RS`, `sr-ME` -> `sr-Latn-ME`): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-core/supplemental/likelySubtags.json
8. CLDR Serbian numbers and units (separators, percent pattern, duration abbreviations): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/sr/numbers.json and https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/sr/units.json
9. Wikipedia, Serbian Cyrillic alphabet (official status, script polls, Latin online, italic forms): https://en.wikipedia.org/wiki/Serbian_Cyrillic_alphabet
10. Roblox on Google Play, Serbian and English listings (Cyrillic; Roblox-у, Robux, тајкуни, пријатељи, приватни сервери; "ROBLOX PLUS" in both): https://play.google.com/store/apps/details?id=com.roblox.client&hl=sr&gl=RS and https://play.google.com/store/apps/details?id=com.roblox.client&hl=en&gl=US
11. Serbian Wikipedia, Roblox (Роблокс, Робукс, гејм-пес, игре са препрекама): https://sr.wikipedia.org/wiki/Roblox
12. Minecraft Java Edition Serbian language files `minecraft/lang/sr_sp.json` and `sr_cs.json` (assets index 29, read from a local install): Играј, Инвентар, Размене, Напитак среће, "%s је ушао у игру", mixed-script strings.
13. Roblox client font files (`content/fonts` and `content/fonts/families`, client version-f0ea5da9412f4e35), cmap and GSUB check run locally 2026-11-08 and repeated by the reviewer.
14. DevForum, "Russian Text Scaling Issues" (Cyrillic falls back to Arial, 2019): https://devforum.roblox.com/t/russian-text-scaling-issues/232672
15. DevForum, "Friends Are Back!" (Connections -> Friends, April 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
16. Vukajlija slang dictionary, "nub" and "afk" entries (Latin-script gamer slang): https://vukajlija.com/nub and https://vukajlija.com/afk
17. Creator Hub, Engagement-based payouts (still says "Premium", checked 2026-11-08): https://create.roblox.com/docs/production/monetization/engagement-based-payouts
