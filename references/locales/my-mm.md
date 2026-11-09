# Burmese (my-mm) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `my-mm` (Roblox lists one Burmese locale; a bare `my` column is optional and would carry the same text) |
| Script, direction | Myanmar script, Unicode only (never Zawgyi), LTR; Latin for kept terms and all digits |
| Address the player as | no pronoun; သင် / သင့် only when a sentence breaks without it; never မင်း, နင်, ခင်ဗျား or ရှင် |
| Text expansion vs English | lint width about 1.0x English (max 1.5x); rendered width median about 1.15x, short buttons and titles up to 2x (Play -> ကစားရန်); ink height about 1.2x Latin (font metrics, unshaped estimate) |
| Plural categories (CLDR) | other (one form, cardinal and ordinal) |
| Model confidence | low -- low-resource language, web text mixes Zawgyi with Unicode, and Roblox has no Burmese UI to copy platform terms from |
| Native review before shipping | strongly recommended |

## Audience and register
Roblox has no Burmese UI: its locale API marks my_mm as usable for in-game content but not as a Roblox UI or sign-up language (checked 2026-11-08). Myanmar kids therefore run Roblox in English and meet Robux, Friends, Community and Premium in English. Burmese gamers code-mix freely: Burmese Wikipedia's Mobile Legends article writes Hero, Item, Gold, Level and Rank in Latin inside Burmese sentences, often with a Burmese gloss such as အဆင့် (Level). Write the way a friendly local game would talk to them:
- Use colloquial written Burmese (the spoken style): endings တယ်, မယ်, ပြီ; connectors ရဲ့, နဲ့, ကို. Microsoft's Burmese voice asks for everyday conversational wording, and its samples end in ပါတယ် / ပါမယ်. Literary forms (သည်, မည်, ၏, နှင့်, သို့) are the voice of Android's Burmese system text and of notices; in a kids' game they read stiff. Never mix the two styles in one sentence.
- Buttons: verb + ရန် (ဝယ်ရန်, ရယူရန်, ကစားရန်), the standard Burmese command form: Android's Burmese buttons (ကူးရန်, ဖျက်ရန်, မျှဝေရန်, ကျော်ရန်) and Microsoft's command names (ပယ်ဖျက်ရန်) use it. It is the one literary form a casual game keeps; a connector on the same button stays literary too (ဖြင့်, not နဲ့). ကစားမယ် ("let's play") is a livelier Play label (unverified). Titles and labels: bare nouns (ဆိုင်, ဂီတ).
- Requests and tutorials: verb + ပါ, polite and neutral: Pet တွေ ရောင်းပါ။ Add နော် for a warm "okay?" (ပြန်လာခဲ့နော်!) and -လိုက် for a quick friendly push (ယူလိုက်!).
- Hype: perfective ပြီ + "!": ရပြီ! / အဆင့်တက်ပြီ! "Let's" is verb + ကြရအောင်: ကစားကြရအောင်!
- Drop "you" and "your"; Burmese omits the subject (Microsoft guide). "Your backpack is full" -> ကျောပိုးအိတ် ပြည့်နေပြီ! If unavoidable, use သင် (Microsoft's neutral polite form).
- Never end with ခင်ဗျာ or ရှင့်: they mark the speaker as male or female. Never use ကျွန်တော် / ကျွန်မ (gendered "I"); for "we" rephrase, or use the neutral but formal ကျွန်ုပ်တို့.
- Kid-safe: hatching is not gambling. Avoid ကံစမ်းမဲ (lottery) and လောင်း (bet); say ဥဖောက် (hatch).

## Roblox and gaming vocabulary
| English | Use in my-mm | Note |
|---|---|---|
| Robux | Robux | Latin, as everywhere on Roblox; never ရော့ဘတ်စ် |
| Premium | Premium | Roblox subscription name, Latin |
| game pass | Game Pass | Roblox's English store word; in a shop just name the perk (ဒင်္ဂါး 2 ဆ) |
| developer product | the item's name | players never see the term |
| experience / game | ဂိမ်း | Burmese Wikipedia's word; never အတွေ့အကြုံ (life experience) |
| obby | Obby | Latin; explain as အတားအဆီး ပြေးပွဲ in a tutorial if needed (unverified) |
| tycoon / simulator | Tycoon / Simulator | Latin, as in the game titles players search |
| rebirth | Rebirth | Latin + လုပ်: Rebirth လုပ်မလား။ ပြန်လည်မွေးဖွားခြင်း is long and is the Buddhist word for rebirth; ပြန်မွေး is a short option (unverified) |
| pet | Pet | Latin, counted with ကောင်; အိမ်မွေးတိရစ္ဆာန် is textbook-long (native check) |
| egg / hatch | ဥ / ဥဖောက် | ဥထဲက နဂါး ထွက်လာပြီ! ဥ is U+1025, not the letter ဉ |
| coins | ဒင်္ဂါး | classifier ပြား: ဒင်္ဂါး 50 ပြား |
| gems | ကျောက်မျက် | or Gem in Latin; one choice per game |
| boost | Boost | Latin: Boost ရမယ် |
| multiplier | ဆ | 2 ဆ = 2x (နှစ်ဆ = double); "2x" is fine on art and badges |
| XP | XP | never အတွေ့အကြုံ |
| level up | အဆင့်တက် | အဆင့် {level} on labels; Burmese Wikipedia glosses Level as အဆင့်. Gamers also say Level တက်, but Level twice in a line fails the lint |
| quest | မစ်ရှင် | Burmese spelling of "mission"; Quest in Latin also seen (unverified) |
| leaderboard | ထိပ်တန်းစာရင်း | "top list"; on the board itself ထိပ်တန်းကစားသမား |
| AFK | AFK | AFK ဖြစ်နေပြီ |
| noob | noob | keep; never aim it at the player |
| OP | OP | used like an adjective verb: OP တယ် (unverified) |
| VIP | VIP | |
| trade | လဲလှယ် | Trade in Latin is understood too |
| inventory / backpack | ကျောပိုးအိတ် | a storage screen title can be ပစ္စည်းများ |
| daily reward | နေ့စဉ်ဆုလာဘ် | ဆုလာဘ် = reward; ဆု alone = prize, award |
| codes | ကုဒ် | the code itself stays Latin |
| group | Community | Roblox's English UI name since Nov 2024; အဖွဲ့ if the game's other UI says group |
| like / favorite | Like / Favorite | the English Roblox buttons players press: Like ပေးပါ |
| server | ဆာဗာ | Server in Latin is also common |
| friends | သူငယ်ချင်း | Roblox's English UI says Friends again since April 2026; never "connections" (ချိတ်ဆက်မှု) |

## Grammar traps in UI strings
- Plurals with {count}: no plural agreement exists. Counted nouns take noun + number + classifier, correct for 0, 1 and 1,250: ဒင်္ဂါး {amount} ပြား (coins), Pet {count} ကောင် (animals), ကစားသမား {count} ယောက် (people), {count} ခု (things). Never add များ / တွေ next to a number. On tight HUD labels drop the classifier: ဒင်္ဂါး {count}.
- Gender: verbs and adjectives never agree with {player}; the only gender traps are the speaker particles and pronouns above.
- Particles follow placeholders: Burmese is SOV with postpositions. Subject က, object ကို, "with" နဲ့, "of" ရဲ့ go after the name, with a space after a Latin name or placeholder (house rule; it gives a wrap point): {player} က သင်နဲ့ လဲလှယ်ချင်တယ်
- The verb goes last, so English tails move left: "Buy for {price} Robux" -> {price} Robux ဖြင့် ဝယ်ရန်; "Come back in {time}" -> {time} ကြာရင် ... ပြန်လာခဲ့နော်!
- Modifiers: a noun-like modifier precedes its head, so keep {rarity} before {pet}: ဒဏ္ဍာရီ နဂါး.
- Questions need a final particle, လား (yes/no) or လဲ (wh-): Rebirth လုပ်မလား။ / ဘယ် Pet လဲ။ A "?" on a statement does not make a question.
- Negation wraps the verb: မ + verb + ဘူး (colloquial) or မ + verb + ပါ (polite): မရဘူး / မမှန်ပါ.
- Compounds: an English spaced or hyphenated compound becomes one closed word (Microsoft guide): နေ့စဉ်ဆုလာဘ်, not နေ့စဉ် ဆုလာဘ်.
- Myanmar script has no capitals; kept English words keep theirs (Rebirth, Boost, VIP).

## Typography and formatting
- Sentence end ။ (U+104B), pause ၊ (U+104A). Never "." or "," in Burmese text; digits keep ASCII (1,250 / 1.5).
- No ။ on buttons, titles, labels or placeholders (Microsoft guide: no period on titles).
- Hype toasts end with "!" instead of ။, never both (ရပြီ!။ is wrong).
- Questions: particle + ။, never "?" (house style). Microsoft ends Burmese questions with ။ and allows "?" only when context needs it; Android's Burmese strings end most questions with ။.
- Colon: Microsoft puts a space before it: ဆုလာဘ် :
- Ellipsis: three ASCII periods, at the end only: တင်နေ...
- Digits: Latin 0-9. CLDR's default for my is Burmese digits (၀-၉), but {count}, {amount} and {price} arrive from game code in Latin digits, and mixed systems look broken: 2 ဆ, not ၂ ဆ.
- Look-alikes that pass a glance but break search and lint: ၀ (zero) vs ဝ (wa), ၄ (four) vs ၎, ၇ (seven) vs ရ, ဥ (U+1025, egg) vs ဉ (U+1009, as in နေ့စဉ်).
- Percent: no space: +{percent}% (CLDR #,##0%).
- Durations: game code fills {time} (sample "3h 20m"), so the translation must read right with that; 3h 20m is understood. CLDR's units are "{0} ရက်", "{0} နာရီ", "{0} မိနစ်", "{0} စက္ကန့်": in the string's note, ask the developer to format {time} as 3 နာရီ 20 မိနစ် for this locale. Either way {time} goes before ကြာရင် or ကျန်တယ်.
- Spaces: none between words; a space marks a phrase break. House rule: one space between Burmese and Latin or digits: AFK ဖြစ်နေပြီ / ဒင်္ဂါး {count}.
- Keyboard keys stay Latin: ဖွင့်ရန် E နှိပ်ပါ
- Quotation marks follow the English source: "..." (Microsoft guide).

## Do not translate / keep as is
- Latin, byte-identical: Roblox, Robux, Premium, the game title, VIP, AFK, OP, XP, noob, promo codes (FREEPETS), keys (E), display names. Never transliterate Robux or Roblox into Myanmar script.
- Latin by this guide's choice (see table): Rebirth, Boost, Event, Pet, Obby, Tycoon, Simulator -- gamer loans whose Burmese is long or misleading (pipeline.md lets a locale guide override translate -> keep). Where a short everyday word exists, translate: Level -> အဆင့်.
- Lint: a string that is all Latin (Rebirth, VIP) needs keep:true. The script check counts only Burmese consonants and independent vowels as letters (vowel signs and medials do not count), so a line needs at least as many of those as Latin letters: restructure a Latin-heavy line instead of marking it keep.
- Language picker label: မြန်မာဘာသာ, as in data/locales.json; it matches CLDR's မြန်မာ and Burmese Wikipedia's မြန်မာဘာသာစကား. Roblox's docs and locale API name it ဗမာစာ, which no other source here uses (native check).
- Translate ordinary item, pet and rarity words: Dragon -> နဂါး, Lucky Potion -> ကံကောင်းဆေးရည်, Legendary -> ဒဏ္ဍာရီ.
- Encoding: Unicode only, never Zawgyi. Myanmar switched officially to Unicode on 1 October 2019 ("U-Day"), but Zawgyi still fills old sites, social posts and model training data, so pasted or remembered Burmese may be Zawgyi. Red flags:
  - Code points U+1060-U+1097 (ၾ, ၿ, ႏ, ၤ) or ဳ ဴ (U+1033, U+1034) in Burmese text; Zawgyi uses them for ra medial and stacked letters. The repo lint rejects them.
  - ေ, ြ or ျ first in a word or right after a space. Unicode stores ေ after its consonant and medials: ကြော့ is U+1000 U+103C U+1031 U+102C U+1037; the Zawgyi version of that word shows as ေၾကာ့ in a Unicode font.
  - A word-final killer typed as U+1039 instead of U+103A (asat). In Unicode, U+1039 only stacks consonants (ဒဏ္ဍာရီ) or builds kinzi (ဒင်္ဂါး = U+1012 U+1004 U+103A U+1039 U+1002 U+102B U+1038).
  - Dotted circles, or vowels on the wrong side, in Studio.
- When unsure, score the text with Google's myanmar-tools detector (near 1.0 = Zawgyi) and convert with ICU's "Zawgyi-my" transform rather than hand-fixing. Hand-written regex detectors misflag Shan and Mon Unicode text (Unicode FAQ).

## Rendering on Roblox
- Roblox ships a Unicode Burmese fallback font. Every installed Windows player and Studio build contains content/fonts/NotoSansMyanmarUI-Regular.ttf (Noto 2.000, 2017), the player executable names it beside its other Noto fallbacks and contains HarfBuzz code, and the font carries OpenType Myanmar ('mym2') reordering and mark-positioning tables (local inspection 2026-11-08; Roblox docs do not document this). Burmese shows in Noto Sans Myanmar UI whatever Font the label uses; stylized faces (Fredoka One, Luckiest Guy) have no Myanmar glyphs, so Latin words in the same line keep the stylized look.
- Because the font is Unicode, Zawgyi text renders scrambled for every player. There is no player-side fix.
- Shaping: ေ must draw left of its consonant, ြ around it, kinzi above the next letter, stacked letters below. Font and shaper suggest this works (unverified); dotted circles (U+25CC, in the font) mean a broken sequence. In Studio, set the test locale to my-mm and check: ကြော့, ဒင်္ဂါး, ဒဏ္ဍာရီ, လျှောက်ဝင်ပါ, နေ့စဉ်ဆုလာဘ်.
- Only a Regular weight ships, so <b> may not look bold (unverified). Keep the tags; never rely on bold for meaning.
- Height: marks stack above (ိ ီ ံ, kinzi) and below (ု ူ ျ ှ, stacked consonants). The UI variant is squeezed to fit: its line box is about 1.08x Builder Sans's and its ink reaches 1.05 em above the baseline and 0.27 em below (Builder Sans: 0.91 / 0.20), so allow about 1.2x the Latin height or AutomaticSize Y. Check that tall marks are not clipped on tight or TextScaled labels at phone size.
- Wrapping: with no spaces between words, TextWrapped can likely break only at phrase spaces (unverified). Keep a space between phrases or a long line overflows or splits mid-syllable. Do not insert U+200B: the font has the glyph, but whether Roblox breaks lines there is unverified, and it is invisible to reviewers.

## Mistakes machine translation makes here
- Zawgyi or mixed encoding: ေၾကာ့ -> ကြော့ (see the red flags above).
- Literary register in toasts: သင်သည် အဆင့် 5 သို့ ရောက်ရှိပါသည်။ -> အဆင့် 5 ရောက်ပြီ!
- "You" in every line: သင်၏ ကျောပိုးအိတ် ပြည့်နေပါသည်။ -> ကျောပိုးအိတ် ပြည့်နေပြီ!
- Gendered politeness: ဝယ်ပါခင်ဗျာ -> ဝယ်ရန်
- "Experience" and "XP" as life experience: ဒီအတွေ့အကြုံကို Like ပေးပါ -> ဂိမ်းကို Like ပေးပါ; အတွေ့အကြုံ 50 -> XP 50
- Rebirth as religious rebirth: ပြန်လည်မွေးဖွားခြင်း -> Rebirth
- Plural marker beside a number: ဒင်္ဂါးများ 5 -> ဒင်္ဂါး 5 ပြား
- English full stop, or ။ on a button: ဆိုင်ကိုဖွင့်ပါ. -> ဆိုင်ကိုဖွင့်ပါ။ and ဝယ်ရန်။ -> ဝယ်ရန်
- Burmese digits beside Latin params, or the letter ဝ typed as zero: ၂ ဆ -> 2 ဆ
- Claim as "demand": တောင်းဆိုရန် -> ရယူရန်
- Friends as "connections": ချိတ်ဆက်မှုများ -> သူငယ်ချင်း
- Hatching as a lottery, or Robux transliterated: ကံစမ်းမဲ -> ဥဖောက်; ရော့ဘတ်စ် -> Robux

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | ကစားရန် | verb + ရန် like every button; ကစားမယ် ("let's play") is livelier (unverified) |
| shop.title | ဆိုင် | |
| shop.buy | ဝယ်ရန် | |
| reward.claim | ရယူရန် | "receive"; never တောင်းဆို |
| rebirth.button | Rebirth | kept Latin, needs keep:true; ပြန်မွေး is a Burmese option (unverified) |
| rebirth.confirm | အခု Rebirth လုပ်မလား။ ဒင်္ဂါးတွေ ပျောက်သွားမယ်၊ ဒါပေမယ့် အမြဲတမ်း {multiplier} ဆ Boost ရမယ်။ | ဆ works for 2 and 1.5; ဒါပေမယ့် is Microsoft's spoken "but" |
| coins.need_more | ဒင်္ဂါး {amount} ပြား ထပ်လိုသေးတယ်! | ပြား classifier; fine for 1 |
| coins.count | ဒင်္ဂါး {count} | classifier dropped to fit the HUD |
| egg.hatched | ဥထဲက {rarity} {pet} ထွက်လာပြီ! | "came out of the egg"; no "you" |
| rarity.legendary | ဒဏ္ဍာရီ | "legend"; also a stacked-letter render test |
| pet.name.dragon | နဂါး | |
| chat.player_joined | {player} ဂိမ်းထဲ ဝင်လာပြီ | no gender to agree |
| trade.request | {player} က သင်နဲ့ လဲလှယ်ချင်တယ် | the set's only သင်; needed for "with you" |
| prompt.open_shop | ဖွင့်ရန် E နှိပ်ပါ | E stays Latin |
| pass.buy_price | {price} Robux ဖြင့် ဝယ်ရန် | ဖြင့် matches the literary button verb |
| pass.coins2x | ဒင်္ဂါး 2 ဆ | Burmese order: thing + times |
| pass.vip | VIP | keep:true |
| reward.daily_title | နေ့စဉ်ဆုလာဘ် | closed compound |
| reward.come_back | {time} ကြာရင် နောက်ဆုလာဘ် ယူဖို့ ပြန်လာခဲ့နော်! | နော် = friendly "okay?" |
| codes.placeholder | ကုဒ် ထည့်ပါ | |
| codes.invalid | ဒီကုဒ် မမှန်ပါ ဒါမှမဟုတ် သက်တမ်းကုန်ပြီ။ | ဒါမှမဟုတ် = colloquial "or" |
| social.like_reward | ဂိမ်းကို Like ပေးပြီး <b>ကံကောင်းဆေးရည်</b> အခမဲ့ ရယူပါ! | Like matches Roblox's English button |
| social.group_reward | Community ထဲ ဝင်ပြီး အခမဲ့ ဆုလာဘ် ရယူပါ! | "our" dropped; အဖွဲ့ if the game says group |
| afk.warning | AFK ဖြစ်နေပြီ! ဒင်္ဂါး ဆက်ရဖို့ လှုပ်ရှားပါ! | "earning" named as coins; bare ဆက်ရဖို့ lacks an object |
| leaderboard.title | ထိပ်တန်းကစားသမား | plural marker dropped to fit 16 |
| level.up | အဆင့်တက်ပြီ! အခု အဆင့် {level} ရောက်ပြီ။ | the Latin Level version fails the lint script check |
| tutorial.sell | Pet တွေ ရောင်းဖို့ လင်းနေတဲ့ စက်ဝိုင်းထဲ လျှောက်ဝင်ပါ။ | Pet kept Latin, see table |
| inventory.full | ကျောပိုးအိတ် ပြည့်နေပြီ! နေရာလွတ်ဖို့ Pet တွေ ရောင်းပါ။ | |
| settings.music | ဂီတ | |
| settings.on | ဖွင့် | Off = ပိတ် |
| loading | တင်နေ... | Android's Burmese "Loading"; ခဏစောင့်ပါ... ("please wait") also fits |
| event.ends_in | Event ပြီးဖို့ {time} ကျန်တယ် | "{time} left until the Event ends"; label form Event ကျန်ချိန် {time} fails the lint |
| item.op | ဒီဓား အရမ်း OP တယ်! | အရမ်းအစွမ်းထက်တယ် for non-gamers |
| friends.boost | ဆာဗာထဲက သူငယ်ချင်း တစ်ယောက်စီအတွက် Boost +{percent}% | |

## Sources
1. Microsoft Burmese Localization Style Guide -- https://aka.ms/burmese-styleguide (mya-MMR-StyleGuide.pdf)
2. Unicode CLDR, Language Plural Rules -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON, my numbers (default digits, percent) -- https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-numbers-full/main/my/numbers.json
4. CLDR JSON, my units (duration units) -- https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-units-full/main/my/units.json
5. Roblox locale API (my_mm not a full-UI locale) -- https://locale.roblox.com/v1/locales
6. Roblox Creator Docs, Language codes -- https://create.roblox.com/docs/production/localization/language-codes
7. Unicode, Myanmar Scripts and Languages FAQ (Zawgyi) -- https://www.unicode.org/faq/myanmar.html
8. Wikipedia, Zawgyi font (U-Day, ကြော့ example) -- https://en.wikipedia.org/wiki/Zawgyi_font
9. Google myanmar-tools (Zawgyi detector and converter) -- https://github.com/google/myanmar-tools
10. Burmese Wikipedia, Mobile Legends: Bang Bang (gaming code-mixing) -- https://my.wikipedia.org/wiki/မိုဘိုင်းလက်ဂျန့်စ်:ဘန်းဘန်း
11. Wikipedia langlinks in Burmese (video game, coin, Burmese language) -- https://en.wikipedia.org/w/api.php?action=query&titles=Video_game|Coin|Burmese_language&prop=langlinks&lllang=my
12. Roblox Windows client and Studio install (content/fonts, RobloxPlayerBeta.exe strings; font tables and metrics read with fontTools against BuilderSans-Regular.otf), inspected 2026-11-08
13. Roblox DevForum, Friends Are Back (April 2026) -- https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
14. Roblox DevForum, Introducing Roblox Communities (Nov 2024) -- https://devforum.roblox.com/t/introducing-roblox-communities/3268307
15. Android (AOSP) framework strings in Burmese (button forms, "Loading", question marks, register) -- https://android.googlesource.com/platform/frameworks/base/+/refs/heads/main/core/res/res/values-my/strings.xml
16. CLDR JSON, my language names (မြန်မာ) -- https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-localenames-full/main/my/languages.json
