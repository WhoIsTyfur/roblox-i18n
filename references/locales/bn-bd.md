# Bengali (bn-bd) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `bn-bd` (the only Bengali locale Roblox lists; Roblox's locale API calls it `bn_bd`, language `bn`) |
| Script, direction | Bengali (Beng), LTR, words separated by spaces |
| Address the player as | `তুমি` with `-ও` imperatives (`খেলো`, `করো`, `এসো`); never `তুই`, and never mix in `আপনি`/`-উন` |
| Text expansion vs English | about +17% in code points with sample values, +7% as the repo lint counts; one-word buttons can double (`Buy` -> `কিনে নাও`) |
| Plural categories (CLDR) | cardinal: one (`i = 0 or n = 1`), other; ordinal: one, two, few, many, other |
| Model confidence | medium: models drift to West Bengal words, bookish সাধু forms, the formal `আপনি` and literal calques |
| Native review before shipping | strongly recommended (a Bangladeshi reviewer, not a West Bengal one) |

## Audience and register
- Roblox does not offer its platform UI in Bengali: in Roblox's locale API `bn_bd` has in-game content enabled but full experience off. Bangladeshi kids see Roblox's menus in English and only your game in Bengali, so platform words should match the English UI they know.
- Many players are Bangla-medium students who read English game words fine but struggle with English sentences. Translate sentences fully; keep short gaming words (`লেভেল`, `বুস্ট`, `OP`) as loanwords.
- Microsoft's Bangladesh guide (formal pronoun only) and Mozilla's bn-BD guide both use `আপনি` with `-উন` imperatives (`করুন`), the house style of adult software. Roblox has no Bengali UI to set a precedent. For a 9-16 audience use `তুমি`, the familiar form adults and teachers use with kids, like tu/du in other guides: `তোমার ব্যাগ ভরে গেছে!` This is the guide's choice, not a checked norm for Bangladeshi games (unverified). If a studio insists on `আপনি`, convert the whole game, never single strings.
- `তুমি` imperatives always end in `ো`/`ও`: `করো`, `খেলো`, `দেখো`, `যাও`, `এসো`. Without it (`কর`, `দেখ`) it reads as the rude or intimate `তুই` form.
- Register map if you must switch: `খেলো`/`খেলুন`, `কিনে নাও`/`কিনুন`, `নিয়ে নাও`/`নিন`, `এসো`/`আসুন`.
- Write চলিত (standard colloquial) only. Never সাধু ভাষা verb forms such as `করিতেছে`, `হইয়াছে`; Mozilla's bn-BD guide rules them out as bookish.
- Third person for players is the ordinary form, not honorific: `{player} যোগ দিয়েছে`, not `যোগ দিয়েছেন`.
- Hype: short exclamations work (`লেভেল আপ!`, `দারুণ!`, `অসাধারণ!`). One `!`, never `!!!`. No street slang or insults, even mild ones like `গাধা`.
- Bangladesh, not India: use Bangladeshi vocabulary (`পানি`, `ভাইয়া`, `চাচা`, `দাওয়াত` for a meal invitation) where West Bengal says `জল`, `দাদা`, `কাকু`; in Bangladesh `দাদা` usually means grandfather. In-game invites are `আমন্ত্রণ` in both (unverified).
- Avoid religious words for game mechanics: `পুনর্জন্ম` (reincarnation) for Rebirth, `আশীর্বাদ` or `দোয়া` for Blessing. Use `রিবার্থ`, `বোনাস`, `বুস্ট`.

## Roblox and gaming vocabulary
| English | Use in bn-bd | Note |
|---|---|---|
| Robux | `Robux` | Latin, as the English Roblox UI shows it. Bengali Wikipedia's `রবাক্স` is not an official form; don't use it in UI. |
| Premium | `Premium` | Product name, Latin. |
| experience / game | `গেম` | Never `অভিজ্ঞতা` (life experience). |
| game pass | `গেম পাস` | |
| developer product | `ডেভেলপার পণ্য` (Bengali Wikipedia) | Players never see it; show the item's own name. |
| obby | `অবি` | Players' word (unverified); `বাধার কোর্স` if you must explain. |
| tycoon / simulator | `টাইকুন` / `সিমুলেটর` | |
| rebirth | `রিবার্থ` | Not `পুনর্জন্ম` (see register). Player usage unverified. |
| pet | `পোষা প্রাণী` | Never bare `পেট`: written, it reads as belly, whatever players say aloud (unverified). Short labels: the pet's own name. |
| egg / hatch | `ডিম` / `ডিম ফোটানো` | `ডিম ফুটে বের হলো...` for the result. |
| coins | `কয়েন` | Not `মুদ্রা` (currency, formal). |
| gems | `জেম` | `ডায়মন্ড` if the game calls them diamonds; Free Fire made that word familiar (unverified). |
| boost / multiplier | `বুস্ট` / `2x`, `{n} গুণ` | `দ্বিগুণ` = double. |
| XP / level up | `XP` / `লেভেল আপ` | Latin XP; `লেভেল` for level. |
| quest | `মিশন` | An everyday Bengali loanword; `কোয়েস্ট` is rarer (unverified). One term per game. |
| leaderboard | `লিডারবোর্ড`; title `সেরা খেলোয়াড়` | |
| AFK / noob / OP | `AFK` / `নুব` / `OP` | Latin for AFK and OP (unverified player usage). |
| VIP | `VIP` | |
| trade | `ট্রেড` | `বিনিময়` is correct but formal (unverified preference). |
| inventory / backpack | `ব্যাগ`; `ইনভেন্টরি` for a full inventory screen | |
| daily reward | `দৈনিক পুরস্কার` | |
| codes | `কোড` | Promo codes stay as typed. |
| group | `গ্রুপ` | Not `দল`, which means team. |
| like / favorite | `লাইক দাও` / `ফেভারিট` | Facebook-style `লাইক`. `প্রিয়` is the native option for favorite (unverified preference). |
| server | `সার্ভার` | Microsoft and Bengali Wikipedia spelling. |
| friends / connections | `বন্ধু` | Roblox's English UI now says Connections; no Bengali platform term exists. In game text say `বন্ধু`. |

## Grammar traps in UI strings
- **Plurals.** Bengali nouns do not change after a number, so one string covers 0, 1 and 1,250: `{count} কয়েন`. Never add `গুলো`/`রা` after a number: `{count} কয়েনগুলো` is wrong.
- **Classifiers.** Currency and units take none: `আরও {amount} কয়েন`, `{price} Robux`. Countable things normally take `টি` after a number, and it never changes with the number, so it is safe on a placeholder: `{count}টি ডিম`.
- **Plural suffix choice.** Use `গুলো` (Bangladeshi usage) and avoid `গুলি` in action games: `গুলি` also means bullet. Microsoft's `-সমূহ` is too formal for games.
- **No gender.** Pronouns and verbs ignore gender (Microsoft's Bangladesh guide confirms), so `{player}` never needs agreement. Only honorific level agrees: keep players ordinary (`চায়`, `দিয়েছে`).
- **Case endings after placeholders.** Genitive is `-এর` after a consonant, `-র` after a vowel, and code can't choose. Rephrase so the placeholder needs no ending: `{player} তোমার সাথে ট্রেড করতে চায়`. If unavoidable, attach `-এর`, `-কে`, `-এ` with a hyphen, as Microsoft's Bangladesh guide does after Latin words (`PC-এর`, `Microsoft-এ`): `{player}-এর ড্রাগন`.
- **Word order is SOV.** Verbs move last, postpositions follow nouns: "Buy for {price} Robux" -> `{price} Robux-এ কিনে নাও`; "Come back in {time}" -> `{time} পরে আবার এসো`.
- **Adjectives before nouns, uninflected.** A translated rarity slots in as is: `{rarity} {pet}` -> `লেজেন্ডারি ড্রাগন`.
- **Indefinite objects take no `-কে`.** Animals and things as objects stay bare: `ড্রাগন পেয়েছ`, not `ড্রাগনকে পেয়েছ`.
- **Ordinals** change by number (`১ম`, `২য়`, `৩য়`, `৪র্থ`, `৬ষ্ঠ`) and break with a `{rank}` param. Use `#{rank}` or `{rank} নম্বর`.
- **Loan verbs.** English verbs take `করা`: `আনলক করো`, `ট্রেড করো`, `রিবার্থ করবে?` (Microsoft lists `ডাউনলোড করা` and similar).
- **Bangla Academy spelling for loanwords.** Only `ি`/`ু` (never `ী`/`ূ`) and no `ণ`/`ষ`: `লেজেন্ডারি`, `পোশন`, `মিশন`. Use `অ্যা` for the English a sound: `অ্যাকাউন্ট`, `ব্যাগ`. `কী` (what) vs `কি` (yes/no question).
- **Bangladesh spelling.** Bangla Academy writes `ং` where a sandhi `ম্` meets ক-গ (`সংগীত`, `অহংকার`); `সঙ্গীত` is the older spelling still common in West Bengal. Write `আরও`, not `আরো` (unverified).
- **No capitalization** in Bengali; Latin terms keep their case: `VIP`, `XP`, `AFK`.

## Typography and formatting
- Sentence end is the dari `।` (U+0964), with no space before it. Not `.`, not the pipe `|`, and not the look-alike `৷` (U+09F7, a currency sign), which Microsoft's PDF mixes in.
- `?` and `!` replace the dari and attach with no space: `এখনই রিবার্থ করবে?` Commas, colons and quotes follow English use: `“লাকি পোশন”`.
- Titles, labels and buttons take no dari: `দৈনিক পুরস্কার`.
- Ellipsis: `...` attached: `লোড হচ্ছে...`.
- Digits: CLDR's default for bn is Bengali digits (`০-৯`), as in Bangladeshi print and Bengali Wikipedia, but Roblox has no locale number formatting, so `{params}` arrive as Latin digits. Never mix systems in one string; use Latin digits in static text (`2x কয়েন`) unless the game converts every number in code. Every English-UI game these kids play shows Latin digits; that they prefer them is unverified.
- Grouping is lakh-style in both countries (`12,34,567`, CLDR). Code that prints `1,234,567` is readable. Prefer K/M as in English Roblox over CLDR's compact `হা`/`লা` (thousand/lakh) (unverified).
- Percent and `x` attach to the number: `+20%`, `2x`. Words for big numbers: `হাজার`, `লাখ`, `কোটি`.
- Durations: CLDR's short forms are the full words; ask code to format `{time}` as `3 ঘণ্টা 20 মিনিট`, `2 দিন 5 ঘণ্টা`, `45 সেকেন্ড`. CLDR's narrow `ঘঃ`, `মিঃ`, `সেঃ` are abbreviation style kids may not parse (unverified). When a line overflows, shorten the template first; for bare HUD timers use `02:15:30`, which needs no script.
- Keys: keep the Latin key and drop the word "key": `E চাপো`. Never `E কী চাপো`; `কী` also means "what".
- Case suffixes after Latin words, digits and placeholders take a hyphen: `Robux-এ`, `VIP-দের`, `{level}-এ`. The classifier `টি` attaches directly: `{count}টি`.
- Unicode: write `ো` (U+09CB) and `ৌ` (U+09CC) as single characters, not `ে` + `া` or `ে` + `ৗ`; `ৎ` is U+09CE. `য়`, `ড়`, `ঢ়` normalize (NFC) to letter + nukta, so keep one form or string matching fails. English "ra" + ya-phala needs ZWJ after `র`: `র‍্যাঙ্ক`; without it you get reph (`র্যাঙ্ক`).
- Lengths: the repo lint counts code points of visible text, skipping `{params}`, tags, and only the virama `্` and nukta `়` among Bengali marks; vowel signs count (`কিনে নাও` = 8). `ু`, `ূ`, `ৃ`, `ঁ` take no width, but Bengali glyphs run larger than Latin, so check strings within 10% of max in Studio.
- Text copied from PDFs often comes out with `ি`/`ে` misplaced (text extracted from the Microsoft guides does). Type Bengali; never paste from PDFs.
- Rich text: keep tags on word boundaries, never inside a conjunct: `<b>লাকি পোশন</b>`.

## Do not translate / keep as is
- `Roblox` and `Robux` in UI, Latin. In long prose (descriptions) `রবলক্স` is the Bengali Wikipedia spelling.
- `Premium`, `VIP`, game pass and product brand names, promo codes (`FREEPETS`), usernames and display names, keybinds (`E`, `Shift`).
- Game titles: keep the English title; Bangladeshi players search and talk about Roblox games by English names (unverified).
- Invented item names: transliterate (`লাকি পোশন`, `ড্রাগন`) rather than coin Sanskrit compounds.
- Gamer abbreviations `XP`, `AFK`, `OP` stay Latin.
- Script: Bengali script only. Kids chat in Romanized Bengali ("Banglish"), but UI text in it looks broken (unverified).

## Rendering on Roblox
- Roblox's release notes 406 (Oct 2019) added support for Bengali text, with Hindi, Thai and four other scripts. Before that, DevForum replies (Aug 2019) reported Hindi and Thai as boxes.
- The client ships one Bengali font, `content/fonts/NotoSansBengaliUI-Regular.ttf`, named in the player binary (checked in a local install, 2026-11-08). Roblox's font families seem to lack Bengali glyphs (a 2020 DevForum reply asked for some), so this is likely the fallback for every font (unverified).
- That file has OpenType shaping tables, ZWJ/ZWNJ, the dari and both digit sets, but no Latin letters and only a Regular weight. Expect mixed fonts: in `Robux-এ` or `2x কয়েন` the Latin part uses the game's font, the Bengali part Noto. Bold fonts and `<b>` may not embolden Bengali (unverified).
- Its line box is 1.36 em, against 1.26 for Builder Sans and 1.21 for Fredoka One, and Bengali stacks marks above the headstroke (`ি`, `ী`, `ৈ`, `ৌ`, `ঁ`, reph) and below (`ু`, `ূ`, `ৃ`, `্র`). Give labels sized for English about 15-20% more height and check TextScaled clipping (estimate).
- Verify in Studio with a bn-bd test player: conjuncts (`ক্ষ`, `স্ট`, `ন্ড`, `ঙ্ক`), reph in `রিবার্থ`, split vowels in `লোড`, `ি` drawn left of its consonant, the ZWJ form in `র‍্যাঙ্ক`, `<b>` on Bengali, and wrapping of the 60-70 character toasts. That Roblox applies the shaping tables correctly is unverified.
- A dotted circle or detached marks usually mean bad code-point order (text pasted from a PDF): retype the string. Changing FontFace likely won't change Bengali glyphs, since faces fall back to the same Noto file.

## Mistakes machine translation makes here
- সাধু verbs: `তোমার ব্যাগ পূর্ণ হইয়াছে` -> `তোমার ব্যাগ ভরে গেছে!`
- Formal software register: `কয়েন সংগ্রহ করুন` -> `কয়েন নিয়ে নাও`
- `তুই` imperative by dropping `ো`: `বিক্রি কর` -> `বিক্রি করো`
- Pet as belly: `পেট বিক্রি করো` -> `পোষা প্রাণী বিক্রি করো`
- Rebirth as reincarnation: `পুনর্জন্ম` -> `রিবার্থ`
- Claim as a legal claim: `দাবি করুন` -> `নিয়ে নাও`
- West Bengal forms: `জল`, `দাদা`, `সঙ্গীত`, `বেরোল` -> `পানি`, `ভাইয়া`, `সংগীত`, `বের হলো`
- Plural after a number: `{count}টি কয়েনগুলো` -> `{count} কয়েন`
- Like as "be fond of" (and formal): `গেমটি পছন্দ করুন` -> `গেমে লাইক দাও`
- Free as "liberated": `মুক্ত পুরস্কার` -> `ফ্রি পুরস্কার`
- Experience as life experience: `নতুন অভিজ্ঞতা খেলুন` -> `নতুন গেম খেলো`
- Wrong full stop: `কোডটি ভুল.` / `ভুল|` -> `কোডটি ভুল।`

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | খেলো | `খেলুন` in an `আপনি` game. |
| shop.title | দোকান | `শপ` is also understood. |
| shop.buy | কিনে নাও | 8 of 8. Not `কেনো`: it is widely misspelled for `কেন` (why). |
| reward.claim | নিয়ে নাও | |
| rebirth.button | রিবার্থ | |
| rebirth.confirm | এখনই রিবার্থ করবে? তোমার সব কয়েন চলে যাবে, কিন্তু স্থায়ী {multiplier}x বুস্ট পাবে। | `{multiplier} গুণ` also works for 2 and 1.5. |
| coins.need_more | তোমার আরও {amount} কয়েন লাগবে! | No classifier, fine for 1. |
| coins.count | {count} কয়েন | No plural form. |
| egg.hatched | ডিম ফুটে বের হলো {rarity} {pet}! | Rephrased ("out of the egg came..."); `পেলে` would read as "if you get". |
| rarity.legendary | লেজেন্ডারি | `কিংবদন্তি` is bookish and a noun. |
| pet.name.dragon | ড্রাগন | |
| chat.player_joined | {player} গেমে যোগ দিয়েছে | Ordinary third person. |
| trade.request | {player} তোমার সাথে ট্রেড করতে চায় | `সাথে` is the common Bangladeshi form of `সঙ্গে` (unverified). |
| prompt.open_shop | খুলতে E চাপো | Key kept Latin, no `কী`. |
| pass.buy_price | {price} Robux-এ কিনে নাও | Hyphen before the suffix. |
| pass.coins2x | 2x কয়েন | `দ্বিগুণ কয়েন` is the native option. |
| pass.vip | VIP | |
| reward.daily_title | দৈনিক পুরস্কার | |
| reward.come_back | পরের পুরস্কার পেতে {time} পরে আবার এসো! | Needs `{time}` like `3 ঘণ্টা 20 মিনিট`. |
| codes.placeholder | কোড লেখো | |
| codes.invalid | কোডটি ভুল অথবা মেয়াদ শেষ হয়ে গেছে। | |
| social.like_reward | গেমে লাইক দিয়ে ফ্রি <b>লাকি পোশন</b> নাও! | Item name transliterated. |
| social.group_reward | আমাদের গ্রুপে যোগ দিয়ে ফ্রি পুরস্কার আনলক করো! | |
| afk.warning | তুমি এখন AFK। আয় চালিয়ে যেতে নড়াচড়া করো! | 42 of 45 by the lint (44 code points in NFC); drop `এখন` if tight. |
| leaderboard.title | সেরা খেলোয়াড় | |
| level.up | লেভেল আপ! এখন তোমার লেভেল {level}। | Avoids a suffix after `{level}`. |
| tutorial.sell | তোমার পোষা প্রাণী বিক্রি করতে জ্বলজ্বলে বৃত্তের ভেতরে হেঁটে যাও। | |
| inventory.full | তোমার ব্যাগ ভরে গেছে! জায়গা করতে পোষা প্রাণী বিক্রি করো। | |
| settings.music | মিউজিক | `সংগীত` is the formal option. |
| settings.on | চালু | Off = `বন্ধ`. |
| loading | লোড হচ্ছে... | |
| event.ends_in | ইভেন্ট শেষ হতে বাকি {time} | With `2 দিন 5 ঘণ্টা` it is 33 code points (the lint skips `{time}`). If the banner overflows, drop `ইভেন্ট` (26) rather than use Latin units. |
| item.op | এই তলোয়ারটা একদম OP! | |
| friends.boost | তোমার সার্ভারে থাকা প্রতিটি বন্ধুর জন্য +{percent}% বুস্ট | `বন্ধু`, not Connections. |

## Sources
1. Microsoft Bangla (Bangladesh) Style Guide, 2017 (register, dari, pronouns, gender, loanwords, key names): https://download.microsoft.com/download/4/5/b/45b699fe-91a3-4405-ab3e-fdae2d196b32/ben-bgd-styleguide.pdf
2. Microsoft Bangla (India) Style Guide, for comparison: https://download.microsoft.com/download/3/a/c/3ac7e8b5-a15c-498e-a73e-c824a82b6347/ben-ind-StyleGuide.pdf
3. Microsoft Localization Style Guides index (lists only Bangla (India) today): https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
4. Mozilla bn-BD localization style guide (আপনি, -উন imperatives, digits, lakh grouping, loanwords): https://mozilla-l10n.github.io/styleguides/bn-BD
5. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
6. Roblox locale API (`bn_bd`: in-game content on, full experience off): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
7. DevForum, Cloud Localization extended to 45 languages (2019; platform UI vs game content, boxes for some scripts): https://devforum.roblox.com/t/cloud-localization-support-extended-to-45-languages/337149
8. DevForum, Release Notes for 406 (Bengali text support): https://devforum.roblox.com/t/release-notes-for-406/369825
9. DevForum, New fonts are live (reply 106, Oct 2020, asking for Bangla-capable fonts): https://devforum.roblox.com/t/new-fonts-are-live/821617
10. DevForum, Bangladeshi Roblox translator portfolio (register sample): https://devforum.roblox.com/t/open-0techy-first-ever-bengalibangla-translator/1035101
11. Bengali Wikipedia, Roblox (রবলক্স, রবাক্স, ডেভেলপার পণ্য, প্রিমিয়াম): https://bn.wikipedia.org/wiki/রবলক্স
12. Bengali Wikipedia, Garena Free Fire (loanword spellings `সার্ভার`, `ইভেন্ট`, `মোড`, `র‍্যাঙ্ক`): https://bn.wikipedia.org/wiki/গেরিনা_ফ্রি_ফায়ার
13. Bengali Wikipedia, Bangla Academy standard spelling rules: https://bn.wikipedia.org/wiki/প্রমিত_বাংলা_বানানের_নিয়ম
14. English Wikipedia, Bengali language (east/west and religious vocabulary pairs): https://en.wikipedia.org/wiki/Bengali_language
15. Kishor Alo, Bangladeshi teen magazine (Bengali digits in Bangladeshi media): https://www.kishoralo.com/
16. CLDR JSON, bn units and numbers (narrow `ঘঃ`/`মিঃ`/`সেঃ`, default Bengali digits, lakh pattern): https://github.com/unicode-org/cldr-json/tree/main/cldr-json/cldr-units-full/main/bn
17. Roblox client files, `content/fonts/NotoSansBengaliUI-Regular.ttf` and `BuilderSans-Regular.otf` (cmap, tables, line metrics read from a local install, 2026-11-08)
