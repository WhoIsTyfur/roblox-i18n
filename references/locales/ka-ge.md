# Georgian (ka-ge) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `ka-ge` (the only Georgian locale Roblox lists; no bare `ka` column needed) |
| Script, direction | Georgian Mkhedruli (U+10D0-U+10FA), LTR, no upper/lower case; never Mtavruli capitals (U+1C90-U+1CBF) |
| Address the player as | informal singular "შენ" (2nd singular verbs: "იყიდე", "გახსენი", "დაბრუნდი"); never mix in formal "თქვენ" ("გსურთ", "სცადეთ") |
| Text expansion vs English | +12% in characters on this guide's reference set (sentences +8%, buttons/labels/titles +19%, single words up to +50%: "Play" -> "თამაში"); rendered width unverified, measure in Studio |
| Plural categories (CLDR) | cardinal: one, other; ordinal: one, many, other. Nouns after numerals stay singular, so one string fits every count |
| Model confidence | low: low-resource language with complex verb agreement; no Roblox Georgian UI to anchor terms; slang is unverified |
| Native review before shipping | strongly recommended |

## Audience and register
- Players in Georgia and the diaspora share one column. Write standard literary Georgian (the Tbilisi norm), no lari prices, no Russian-flavored words.
- Roblox's own app is not in Georgian: the locale API flags `ka_ge` for in-game content only (not full experience, not signup), checked 2026-11-08, and the client's CoreScript translations have no Georgian column. Georgian kids pick Georgian from Roblox's experience-language list and otherwise see Roblox menus in English. Platform words (Robux, Premium, Friends, Communities) reach them in English. Roblox does not auto-translate Georgian, so every empty key shows English.
- Microsoft's Georgian guide and Minecraft's Georgian translation both use formal "თქვენ" ("თქვენ მოკვდით!", "ისევ სცადეთ"). To a 9-16 year old that sounds like school or a bank. A game talks to one kid: "შენ", 2nd singular, as this repo's Russian, Ukrainian and Turkish guides do. That is a judgment, not a sourced Georgian game norm: native review should confirm it reads naturally. Pick it once and never mix: not "იყიდე" in one string and "გსურთ" in the next.
- Gaming loanwords (რებირთი, პეტი, ქოინი, ბუსტი, ლეველი, ტრეიდი, გეიმპასი, ლაიქი) could not be confirmed as common kid usage. Keep them out of UI strings and use the standard word from the table; only "ივენთი" and "ტოპ" are used, both everyday loans.
- Buttons: verbal noun (masdar), the pattern of Microsoft and Minecraft Georgian ("გაუქმება", "გაგრძელება", "შესვლა"). It is register-free and short: "თამაში", "ყიდვა", "მიღება", "გახსნა". Sentences and tips: 2nd singular imperative: "გახსენი", "გაყიდე", "შედი", "დაბრუნდი".
- Titles and labels: a noun phrase without a verb ("ყოველდღიური ჯილდო", "მაღაზია"). A full sentence needs a verb (Microsoft): "კოდი არასწორია.", not "არასწორი კოდი."
- Ongoing states: present passive on "-ება": "იტვირთება...", "ინახება...". Simple tenses; avoid the future where the present works.
- Drop "შენი" when the owner is obvious (Microsoft drops "თქვენი" the same way): "გაყიდე ცხოველები", not "გაყიდე შენი ცხოველები".
- Natural hype: "ყოჩაღ!", "მაგარია!", "ვაუ!", "გილოცავ!", "სუპერ!". Stiff or adult: "გთხოვთ", "გთავაზობთ", "აღნიშნული", "გაითვალისწინეთ", "წარმატებით განხორციელდა".
- Errors state the fact, not blame (Microsoft's "ვერ ..." pattern): "შენახვა ვერ მოხერხდა", "კოდი არასწორია". Kid-safe: "ნუბი" only in friendly jokes; no insults, no "იყიდე ახლავე, თორემ ინანებ!".

## Roblox and gaming vocabulary
| English | Georgian | note |
|---|---|---|
| Robux | Robux | Latin, as Georgian Wikipedia writes it. Case endings after a hyphen: "Robux-ით", "Robux-ად"; no nominative "-ი" (Microsoft). |
| Premium | Premium | "Roblox Premium"; Wikipedia's prose form is "პრემიუმ წევრობა". |
| game pass | (pass name) | no settled Georgian word (unverified); show the pass name. "გეიმპასი" in kids' chat (unverified). |
| developer product | შესყიდვა | players never see the term; name the item. |
| experience / game | თამაში (pl. თამაშები) | never "გამოცდილება": that is XP (Minecraft's Georgian uses it so). |
| obby | obby | (unverified); in descriptions "დაბრკოლებების ზოლი" (obstacle course). |
| tycoon | Tycoon | Latin, as in Wikipedia's "Tycoon თამაშები". |
| simulator | სიმულატორი | Wikipedia lists "სიმულატორები" as a genre. |
| rebirth | აღორძინება | 10 letters, "revival/rebirth"; the confirm dialog explains the reset. Verb "აღორძინდი". Slang "რებირთი" (unverified): not in UI. |
| pet | ცხოველი (pl. ცხოველები) | "შინაური ცხოველი" is the dictionary word but long; "პეტი" in chat (unverified). |
| egg / hatch | კვერცხი / გამოჩეკვა | command "გამოჩეკე დრაკონი!"; result "გამოიჩეკა დრაკონი!" (a dragon hatched); egg button "გახსნა". |
| coins | მონეტა (pl. მონეტები) | not "ფული" (money). "ქოინი" in chat (unverified). |
| gems | ალმასი (diamond art), კრისტალი | never "გემი": it means ship. |
| boost | ბონუსი | everyday loanword; "ბუსტი" among gamers (unverified); "გაძლიერება" is stiff. |
| multiplier | "2x", "x2"; მამრავლი | keep the game's one format everywhere. |
| XP | XP; გამოცდილება in long text | "+50 XP". |
| level / level up | დონე / "ახალი დონე!" | Minecraft uses "დონე". "ლეველი" is slang (unverified). |
| quest | მისია | "დავალება" also means homework. |
| leaderboard | რეიტინგი; title "ტოპ მოთამაშეები" | "ლიდერების დაფა" when space allows. |
| AFK | AFK | Latin caps: "AFK ხარ". |
| noob | დამწყები (UI), ნუბი (jokes) | "ნუბი" (unverified as common). |
| OP | სუპერძლიერი | Latin "OP" in chat (unverified). |
| VIP | VIP | "VIP ზონა", "VIP სერვერი". |
| trade | გაცვლა; verb "გაცვალე" | "ვაჭრობა" is commerce (Minecraft's villager trading); "ტრეიდი" slang (unverified). |
| inventory / backpack | ინვენტარი / ზურგჩანთა | "ინვენტარი" is Minecraft's word; keep whichever the source means. |
| daily reward | ყოველდღიური ჯილდო | |
| codes | კოდები; redeem = "გააქტიურება" | placeholder "შეიყვანე კოდი" (Microsoft: Enter = "შეყვანა"). |
| group | ჯგუფი | Roblox's English UI renamed Groups to Communities (2024-11); "ჯგუფი" is clearer than "საზოგადოება" (society). |
| like / favorite | "მოიწონე" / "რჩეულებში დამატება" | "ლაიქი" is the spoken form (unverified); the Roblox buttons are a thumbs-up and a star. |
| server | სერვერი | "სერვერზე" (on a server), "სერვერთან დაკავშირება" (Minecraft). |
| friends | მეგობრები | Roblox's English UI went from Connections back to Friends (2026-04-02); never "კავშირები". |
| chat / avatar | ჩატი / ავატარი | both on Georgian Wikipedia's Roblox page. |

## Grammar traps in UI strings
- Plurals: a noun after any numeral stays singular, and so does its verb: "1 მონეტა", "5 მონეტა", "0 მონეტა"; "დარჩა 5 მონეტა". So "{count} მონეტა" is correct for every value. The plural "-ებ-" appears only without a number: "მონეტები", "2x მონეტები". Never "{count} მონეტები".
- No grammatical gender: "{player} შემოუერთდა თამაშს" fits any player, and "ის" covers he/she. Plural "they" for one person -> singular "ის", "მისი" (Microsoft).
- Subject case changes with tense. Present/future transitive and intransitive verbs take a plain nominative: "{player} გთავაზობს გაცვლას". Past transitive (aorist) needs ergative "-მა": "{player}-მა გამოჩეკა დრაკონი". Verbs of wanting and having need dative "-ს": "{player}-ს სურს გაცვლა". Prefer the nominative form; it needs no suffix on a name.
- Suffixes on placeholders, Latin words and numbers go after a hyphen: genitive "{player}-ის", dative "E-ს", "-ში" (in), "-ზე" (on), "-თან" (with), adverbial "{price} Robux-ად" (for). Microsoft: "%s-ის". Genitive "-ის" and dative "-ს" are safe on any name; avoid ergative "-მა", whose form shifts after vowel-final names.
- 2nd singular imperative and past ("you did") are the same form: "გამოჩეკე დრაკონი!" is both "Hatch a dragon!" and "You hatched a dragon!". For results, use the intransitive or add "შენ": "გამოიჩეკა {rarity} {pet}!", "შენ მიიღე ...".
- Adjective + noun: a consonant-stem adjective drops its "-ი" before a dative noun and "-ში"/"-ზე" ("მუდმივ ბონუსს", "მანათობელ წრეში"), keeps it before a genitive ("შემდეგი ჯილდოსთვის") and takes "-მა" in the ergative. An inserted {rarity} cannot change form, so use {rarity} {pet} only where the phrase is nominative: "გამოიჩეკა {rarity} {pet}!" Elsewhere use a colon: "ახალი ცხოველი: {rarity} {pet}".
- Word order is free and the verb often comes last. Reorder instead of copying English: "გასახსნელად დააჭირე E-ს", "ცხოველების გასაყიდად შედი წრეში".
- Ordinals are irregular ("1-ლი", "მე-2", "მე-21"); with {level} avoid them: "შენი დონეა {level}", "დონე: {level}".
- Durations take "-ში" (in) or "-მდე" (until): "{time}-ში" works but glues a suffix to "20 წთ". Safer: a colon, "დარჩა: {time}".
- Compounds: hyphen or genitive + noun ("ინტერნეტ-ანგარიშები" in Microsoft's guide, "იღბლის ელექსირი"); never an English-style noun pile like "იღბალი ელექსირი".
- Capitalization: Georgian has none. Titles and buttons are written like any word: "ყოველდღიური ჯილდო". Latin names keep their case: VIP, AFK, Robux.
- Commas (Microsoft): before "რომ" clauses ("იმოძრავე, რომ შოვნა გააგრძელო"), after "გთხოვთ", never before "და", before "ან" only between two clauses.

## Typography and formatting
- No space before ! ? : ; (same as English): "AFK ხარ!", "დარჩა: {time}".
- Quotes: „ “ (U+201E open, U+201C close): „იღბლის ელექსირი“. Straight quotes only inside code or markup.
- Numbers (CLDR, Microsoft): decimal comma, no-break-space grouping: "1 250", "1,5x". English "1,250" reads as one and a quarter to a Georgian player, and "1.5" looks wrong. Flag it to the developer: game code must format {count}, {amount}, {multiplier} and {price} per locale (or pass plain "1250"); the translation cannot fix it. Short forms: "1,2 ათ." (thousand), "3 მლნ." (million); "1.2K" style in games is unverified.
- Percent: no space, "+10%" (CLDR "#,##0%").
- Durations (CLDR short): "3 სთ 20 წთ", "45 წმ", "2 დღე 5 სთ"; tight HUDs may drop the space ("3სთ 20წთ", CLDR narrow). "დღე" has no shorter form. No period after სთ/წთ/წმ.
- Ellipsis: "..." right after the word, as Microsoft writes it: "იტვირთება...".
- Dashes (Microsoft): hyphen inside compounds and before case suffixes; unspaced en dash or hyphen in ranges ("50-100"). Between phrases in UI prefer a colon over a dash.
- Keyboard keys stay Latin with a hyphenated suffix: "დააჭირე E-ს", "Shift-ით".

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, XP, game and studio names ("Pet Hatch Tycoon"), usernames, promo codes (FREEPETS), keybinds (E, Shift, Space).
- Never add nominative "-ი" to a kept Latin word ("VIP", not "VIP-ი"); other case endings go after a hyphen (Microsoft).
- Do not transliterate brand names into Georgian letters ("რობლოქსი" appears in casual text, but keep "Roblox" in UI).
- Script: Mkhedruli only. Never Mtavruli capitals (ᲛᲐᲦᲐᲖᲘᲐ) for loud titles, never the church scripts Asomtavruli or Nuskhuri, and never Latin "translit" (gamarjoba) that some players type in chat.
- Translate descriptive item names: "Lucky Potion" -> "იღბლის ელექსირი". Keep invented proper names in Latin unless the game localizes them.

## Rendering on Roblox
- Checked in the installed Windows client (version-f0ea5da9412f4e35, 2026-11-08): content/fonts ships NotoSansGeorgian-Regular.ttf. Its cmap covers all 43 Mkhedruli letters (U+10D0-U+10FA) plus Asomtavruli and Nuskhuri, but no Mtavruli (U+1C90-U+1CBF), no Latin and no digits.
- None of the other 74 font files (Builder Sans, Fredoka One, Luckiest Guy, Montserrat, Roboto, Source Sans Pro, Arimo, Bangers...) has a single Georgian glyph. The client binary maps locale `ka_GE` to that Noto file, so it is the Georgian fallback; that every TextLabel font falls back to it is still unverified in Studio. Expect plain Noto Georgian beside the game's stylized Latin and digits ("2x მონეტები", "AFK ხარ!"); check that sizes and baselines line up.
- Mtavruli has no glyph in any shipped font, so all-caps Georgian should show as boxes (unverified in the engine; inferred from the cmap). Luau `string.upper` only changes ASCII, but Python `str.upper()` and JS `toUpperCase()` turn Mkhedruli into Mtavruli ("მაღაზია" -> "ᲛᲐᲦᲐᲖᲘᲐ"): never uppercase Georgian in build tools, and keep RichText `<uc>`/`<uppercase>` off Georgian strings (engine behavior unverified).
- Only the Regular weight ships. The binary also names a NotoSansGeorgian-VF.ttf (variable font) that is not in the install folder; whether it downloads and gives `<b>` a real bold is unverified. Keep the tags, check "<b>იღბლის ელექსირი</b>" stands out, and add a color if not.
- Mkhedruli is a four-line script: letters rise above (ბ, ლ, ძ, ხ) and drop below (ფ, ქ, ყ, ჟ) the x-height. With TextScaled or tight label heights, check that tops and tails are not clipped (unverified).
- Long words cannot break: "გაათავისუფლე", "ყოველდღიური", "აღორძინება" (10/10). Check TextWrapped labels at phone size.
- Verify in Studio with a `ka-ge` test player: the rebirth dialog (86/110), inventory.full (58/60), event.ends_in (28/28) and the 22-character buttons.

## Mistakes machine translation makes here
- Register mixing: "იყიდე VIP! გსურთ გაგრძელება?" -> "იყიდე VIP! გინდა გაგრძელება?"
- Plural after a number: "გჭირდება 5 მონეტები" -> "გჭირდება 5 მონეტა".
- Wrong subject case: "{player} გამოჩეკა დრაკონი" -> "{player}-მა გამოჩეკა დრაკონი", or better a present-tense verb.
- Experience as XP: "ახალი გამოცდილება Roblox-ზე" -> "ახალი თამაში Roblox-ზე".
- False friend: "გემები" for gems (ships) -> "ალმასები" or "კრისტალები".
- Calqued hype: "დონე ზემოთ!" -> "ახალი დონე!"; "ეს ხმალი ზედმეტად ძალაუფლებიანია" -> "ეს ხმალი სუპერძლიერია!".
- Wrong trade word: "ვაჭრობა {player}-თან" (commerce) for swapping pets -> "{player} გთავაზობს გაცვლას".
- Connections calque: "+5% თითო კავშირზე" -> "+5% ბონუსი ყოველი მეგობრისთვის".
- Mtavruli for emphasis: "ᲧᲝᲕᲔᲚᲓᲦᲘᲣᲠᲘ ᲯᲘᲚᲓᲝ" (boxes in Roblox) -> "ყოველდღიური ჯილდო".
- Chemistry potion: "იღბლის ხსნარი" (a chemical solution, Minecraft's word) -> "იღბლის ელექსირი" (dictionary spelling, not "ელიქსირი").
- Translated keys: "დააჭირე ე-ს" -> "დააჭირე E-ს".
- Office tone: "გთხოვთ, დაელოდოთ, მიმდინარეობს ჩატვირთვა" -> "იტვირთება...".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | თამაში | masdar, as in Minecraft's "თამაში არჩეულ სამყაროში" |
| shop.title | მაღაზია | |
| shop.buy | ყიდვა | |
| reward.claim | მიღება | "აიღე!" if an imperative fits the art |
| rebirth.button | აღორძინება | exactly 10/10; slang "რებირთი" unverified, not used |
| rebirth.confirm | ახლავე გინდა აღორძინება? მონეტებს დაკარგავ, მაგრამ მიიღებ მუდმივ {multiplier}x ბონუსს. | game should pass "1,5", not "1.5" |
| coins.need_more | გჭირდება კიდევ {amount} მონეტა! | singular after numeral fits 1 and up |
| coins.count | {count} მონეტა | same for 0, 1, 1 250 |
| egg.hatched | გამოიჩეკა {rarity} {pet}! | "a ... hatched": nominative subject keeps inserted words in base form; "გამოჩეკე" would also read as a command |
| rarity.legendary | ლეგენდარული | |
| pet.name.dragon | დრაკონი | "გველეშაპი" is the folk-tale dragon; kids say "დრაკონი" |
| chat.player_joined | {player} შემოუერთდა თამაშს | Minecraft's wording; no gender, no suffix |
| trade.request | {player} გთავაზობს გაცვლას | "offers you a trade"; avoids dative "{player}-ს სურს" |
| prompt.open_shop | დააჭირე E-ს და გახსენი | 22/22, "press E and open (it)", natural with the object dropped; if the game allows 23, "დააჭირე E-ს გასახსნელად" (Minecraft's order) |
| pass.buy_price | ყიდვა {price} Robux-ად | adverbial "-ად" = "for"; 22/22 |
| pass.coins2x | 2x მონეტები | plural: a multiplier, not a count |
| pass.vip | VIP | |
| reward.daily_title | ყოველდღიური ჯილდო | |
| reward.come_back | დაბრუნდი შემდეგი ჯილდოსთვის! დარჩა: {time} | colon avoids a suffix on "3 სთ 20 წთ" |
| codes.placeholder | შეიყვანე კოდი | |
| codes.invalid | ეს კოდი არასწორი ან ვადაგასულია. | |
| social.like_reward | მოიწონე თამაში და მიიღე უფასო <b>იღბლის ელექსირი</b>! | 53/55 with tags; "მოიწონე" is the everyday verb for a Like |
| social.group_reward | შემოგვიერთდი ჯგუფში და გახსენი უფასო ჯილდო! | "join us in the group" carries "our" |
| afk.warning | AFK ხარ! იმოძრავე, რომ შოვნა გააგრძელო. | comma before "რომ" |
| leaderboard.title | ტოპ მოთამაშეები | "ლიდერები" if a shorter title is needed |
| level.up | ახალი დონე! ახლა შენი დონეა {level}. | avoids ordinals |
| tutorial.sell | ცხოველების გასაყიდად შედი მანათობელ წრეში. | |
| inventory.full | ზურგჩანთა სავსეა! გაყიდე ცხოველები და გაათავისუფლე ადგილი. | 58/60 |
| settings.music | მუსიკა | |
| settings.on | კი | Minecraft's Georgian options.on (Off = "არა"); "ჩართული" (7) is over budget; "ჩართ." fits but is an ad-hoc abbreviation (unverified) |
| loading | იტვირთება... | |
| event.ends_in | ივენთის დასრულებამდე: {time} | 28/28; "ივენთი" is the everyday loan, "ღონისძიება" reads official |
| item.op | ეს ხმალი სუპერძლიერია! | adapted; "ეს ხმალი OP-ია!" if the game leans on gamer slang |
| friends.boost | +{percent}% ბონუსი შენს სერვერზე ყოველი მეგობრისთვის | genitive + "-თვის" = "for each friend" |

## Sources
1. Microsoft Georgian localization style guide (PDF via https://aka.ms/georgian-styleguide): https://download.microsoft.com/download/f/0/1/f01a1fc2-bf79-4f80-98d1-2fc5920c3400/kat-geo-StyleGuide.pdf
2. Microsoft localization style guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. CLDR language plural rules (ka cardinal and ordinal): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR JSON, ka number symbols, percent and short formats: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/ka/numbers.json
5. CLDR JSON, ka quotation marks: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-misc-full/main/ka/delimiters.json
6. CLDR JSON, ka duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/ka/units.json
7. Roblox locale API (ka_ge flags: in-game only), checked 2026-11-08: https://locale.roblox.com/v1/locales?displayValueLocale=en_us
8. DevForum, "Cloud Localization Support Extended to 45 Languages" (Georgian listed; platform UI stays English): https://devforum.roblox.com/t/cloud-localization-support-extended-to-45-languages/337149
9. DevForum, "Friends Are Back!" (Connections -> Friends, 2026-04-02): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
10. DevForum, "Introducing Roblox Communities" (Groups -> Communities, 2024-11-21): https://devforum.roblox.com/t/introducing-roblox-communities/3268307
11. Installed Roblox Windows client, version-f0ea5da9412f4e35: content/fonts cmaps (NotoSansGeorgian-Regular.ttf and every other face), the ka_GE -> NotoSansGeorgian-Regular.ttf locale-font table in RobloxPlayerBeta.exe, and ExtraContent/translations/CoreScriptLocalization.csv columns (no ka), inspected 2026-11-08.
12. Minecraft Java 26.3 Georgian language file minecraft/lang/ka_ge.json (Mojang asset index): https://piston-meta.mojang.com/mc/game/version_manifest_v2.json
13. Georgian Wikipedia, Roblox (Robux and Roblox in Latin with hyphenated cases; სიმულატორები, Tycoon თამაშები, ავატარი, ჩატი): https://ka.wikipedia.org/wiki/Roblox
14. Wikipedia, Georgian grammar (singular after numerals, cases, postpositions): https://en.wikipedia.org/wiki/Georgian_grammar
15. Wikipedia, Mtavruli (capitals used only for all-caps titles and emphasis): https://en.wikipedia.org/wiki/Mtavruli
16. Glosbe, English-Georgian "hatch" (გამოჩეკვა, იჩეკება): https://glosbe.com/en/ka/hatch
17. Wiktionary "elixir" and Glosbe "elixir" (Georgian ელექსირი): https://en.wiktionary.org/wiki/elixir , https://glosbe.com/en/ka/elixir
