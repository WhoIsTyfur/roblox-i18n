# Khmer (km-kh) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `km-kh` (a bare `km` column is optional; Khmer has one variant, so it may carry the same text) |
| Script, direction | Khmer script (abugida with stacked subscript consonants), LTR; no spaces between words, a space marks a phrase or clause break; Arabic digits in UI |
| Address the player as | no pronoun when the sentence works without one; អ្នក when it needs one; never លោកអ្នក, ឯង or បង / ប្អូន |
| Text expansion vs English | about the same width overall (-1% across the reference set, measured in Studio against Source Sans); per string -50% to +45%, short buttons swing most (Claim +43%). Code-point counts run higher than width, because vowel signs and subscripts add code points but little width |
| Plural categories (CLDR) | other (only one form, cardinal and ordinal) |
| Model confidence | low: low-resource language: models misspell, write bookish Khmer, emit broken Unicode order, and real gamer usage could not be confirmed |
| Native review before shipping | strongly recommended |

## Audience and register
Khmer Roblox players are kids and young teens in Cambodia. Roblox itself has no Khmer interface: its core UI translation table has no Khmer column, and Roblox's locale API marks `km_kh` as enabled for in-game content only, not for the app or signup (checked 2026-11-08). So Khmer is not an account language; menus, chat system text and purchase dialogs stay in English. Players still reach this column: asked without a login from a Khmer browser, the API returns `km_kh` as the in-game locale, so the device language decides; a player can also pick ភាសាខ្មែរ in the in-experience language menu if the game enables Khmer. Whether an account saved on English still gets `km-kh` is unverified. Your game may be the only Khmer these players see on Roblox, and they already know the English genre words. Write short, everyday, upbeat Khmer: a friendly game host, not a ministry notice or a school textbook.
- Pronoun: Microsoft's Khmer guide uses អ្នក for "you" (gender-neutral); លោកអ្នក sounds adult and stiff. Drop អ្នក when the sentence is clear without it: អ្នកត្រូវការកាក់ 5 ទៀត -> ត្រូវការកាក់ 5 ទៀត!
- Never ឯង (rude to strangers) or បង / ប្អូន (they assign an age rank). For another player repeat {player} rather than គាត់ (Microsoft's neutral he/she, which sounds adult), and never វា ("it").
- Never the speaker particles បាទ (male) or ចាស (female) in UI or system text; they give the game a gender. Only a fixed-gender NPC may use them in dialogue.
- Microsoft says avoid over-polite សូម and សូមមេត្តា. In a kids' game drop them from buttons, toasts and tutorials: សូមចុចលេង -> លេង. Keep សូម for real errors about purchases or accounts: សូមព្យាយាមម្ដងទៀត
- Buttons and labels: bare verb or noun, no subject: លេង / ទិញ / ទទួលយក / ហាង
- Questions end in ទេ; skip the formal opener តើ in short UI: តើអ្នកចង់ទិញទេ? -> ចង់ទិញទេ?
- Hype: ! is natural, plus words like ឡូយណាស់ (so cool) or អស្ចារ្យ (amazing) in moderation (unverified how much kids use ឡូយ in writing). No chat slang, no romanized Khmer.
- Prefer short everyday words: បាន over ទទួលបាន in toasts, ចុច (press, Microsoft's word) over ប៉ះ for keys, ចប់ over បញ្ចប់.

## Roblox and gaming vocabulary
Roblox has no Khmer UI, so platform terms have no official Khmer form; keep them in Latin, as Khmer Wikipedia does for Robux. Translate actions and objects; keep a few genre words Latin. Community spellings below could not be checked (no Khmer gaming source was reachable) and are marked.

| English | Use in km-kh | Note |
|---|---|---|
| Robux | Robux | Latin, as on Khmer Wikipedia; never a Khmer-script spelling |
| game pass | the pass's name / Game Pass | Roblox shows players English "Passes"; ហ្គេមផាស in speech (unverified) |
| developer product | the item's name | never ផលិតផលអ្នកអភិវឌ្ឍន៍ |
| experience / game | ហ្គេម | Google Play's Khmer UI and Khmer Wikipedia use ហ្គេម; never បទពិសោធន៍; avoid bookish ល្បែង |
| obby / tycoon / simulator | Obby / Tycoon / Simulator | Latin inside titles (unverified whether kids transliterate) |
| rebirth | កើតជាថ្មី | "be born anew"; Rebirth in Latin if the game keeps genre words English (unverified which kids prefer) |
| pet | សត្វចិញ្ចឹម | counted with ក្បាល: សត្វចិញ្ចឹម 3 ក្បាល |
| egg / hatch | ពង / ញាស់ | ពង = egg that hatches; ស៊ុត is an egg for eating |
| coins / gems | កាក់ / ត្បូង | ពេជ្រ for diamonds, the word used for mobile-game top-up currency (unverified) |
| boost / multiplier | x2 on tags; {n} ដង in sentences | ដង = times: ច្រើន 2 ដង, also works for 1.5 ដង; Boost in Latin is acceptable |
| XP / level / level up | XP / កម្រិត / ឡើងកម្រិត | Lv. on tight tags; ឡេវែល is spoken (unverified) |
| quest | បេសកកម្ម | daily quest = បេសកកម្មប្រចាំថ្ងៃ |
| leaderboard | តារាងចំណាត់ថ្នាក់ | title "Top Players" = អ្នកលេងកំពូល |
| AFK / VIP / OP | AFK / VIP / ខ្លាំងពេក | AFK and VIP stay Latin; kids may write OP in chat (unverified), but ខ្លាំងពេក ("too strong") reads for every player |
| noob | អ្នកថ្មី | neutral "newcomer"; no mocking words in UI |
| trade | ដោះដូរ | ប្ដូរ on tight buttons |
| inventory / backpack | ឃ្លាំង / កាបូប | ឃ្លាំង = storage; កាបូប = bag, កាបូបស្ពាយ if a backpack must be explicit |
| daily reward | រង្វាន់ប្រចាំថ្ងៃ | modifier follows the noun |
| codes | កូដ | បញ្ចូលកូដ = enter code; never លេខសម្ងាត់ (password) |
| group | ក្រុម | ចូលរួមក្រុម = join the group; Roblox's English UI now says "Communities", so use សហគមន៍ when the game's own string says community |
| like / favorite | ចូលចិត្ត / ចំណូលចិត្ត | Like = ចុចចូលចិត្ត, favorite = ដាក់ក្នុងចំណូលចិត្ត; the two look alike, so keep them apart (Facebook-style Khmer, unverified on Roblox) |
| server | Server | Latin (unverified); ម៉ាស៊ីនមេ is the technical word and reads like IT jargon |
| friends | មិត្តភក្តិ / មិត្ត | Roblox's English UI label has switched between Friends and Connections; in Khmer just say friends |
| Premium | Premium | Latin |
| shop | ហាង | |
| free | ឥតគិតថ្លៃ | ហ្វ្រី is spoken (unverified) |

## Grammar traps in UI strings
- Plurals: none. "{count} Coins" -> {count} កាក់ works for 0, 1 and 1,250. Microsoft says plural words like ទាំងឡាយ or នានា are optional; in UI leave them out.
- Classifiers: Khmer counts noun + number + classifier: សត្វចិញ្ចឹម 3 ក្បាល / មិត្ត 2 នាក់. Currencies count themselves: {amount} កាក់, {price} Robux. "each friend" -> មិត្តម្នាក់ៗ. With a demonstrative, skip the classifier: ដាវនេះ (this sword).
- Gender: none, so {player} needs nothing around it. Repeat the name instead of a pronoun: {player} ចង់ដោះដូរជាមួយអ្នក
- Modifier after noun: Daily Reward -> រង្វាន់ប្រចាំថ្ងៃ; 2x Coins -> កាក់ x2; Top Players -> អ្នកលេងកំពូល; Lucky Potion -> ថ្នាំសំណាង.
- "{rarity} {pet}" -> {pet}ថ្នាក់{rarity}. House tier word: ថ្នាក់ (class, grade, rank) fits any rarity word (នាគថ្នាក់រឿងព្រេង) and leaves កម្រិត for player level only; never use កម្រិត for rarity.
- Hatching: ញាស់ is what the animal does (it leaves the egg), so make the pet the subject: នាគ ញាស់ចេញពីពងហើយ! ("a dragon hatched out of the egg"), not អ្នកញាស់... or ពងញាស់ចេញនាគ.
- Possessive: X របស់អ្នក; drop it when obvious: កាបូបរបស់អ្នកពេញហើយ -> កាបូបពេញហើយ!
- Aspect, not tense (Microsoft): បាន for done (បានចូលហ្គេម), កំពុង for in progress (កំពុងផ្ទុក...), នឹង for will (នឹងបាត់អស់), ហើយ for "now / already" (ពេញហើយ).
- "in {time}" -> ក្នុង {time} ទៀត ("{time} more"): ត្រឡប់មកវិញក្នុង {time} ទៀត
- Placeholders holding digits or Latin ({count}, {price}, {player}, {time}, {level}) get a space on both sides. Placeholders holding Khmer words ({pet}, {rarity}) attach to the words of their own phrase, with a space only at a phrase break: {pet}ថ្នាក់{rarity} ញាស់ចេញពីពងហើយ!
- No capitalization in Khmer. Latin words keep their case: VIP, Robux, AFK.

## Typography and formatting
- ។ (khan) is the full stop. House rule: put ។ where the English sentence ends in a period, whether toast, popup, dialog, tutorial or error (កូដនេះមិនត្រឹមត្រូវ ឬ ផុតកំណត់ហើយ។), unless you deliberately turn the line upbeat with !. No ។ where the English has no final period (chat system lines, trade popup), and never on buttons, titles, labels, or next to ! or ?. No space before ។ (Microsoft: a space lets it wrap alone): ផុតកំណត់ហើយ។ not ផុតកំណត់ហើយ ។
- ! and ? attach to the word, no space before; one space after when text follows: ឡើងកម្រិត! ឥឡូវ...
- Khmer uses a space where English has a comma between clauses: កាក់នឹងបាត់អស់ ប៉ុន្តែ... Microsoft: commas only between long independent clauses, never before និង or ឬ in a list, and put a space on both sides of និង and ឬ (មិនត្រឹមត្រូវ ឬ ផុតកំណត់).
- Colon: ៖ in Khmer text (រង្វាន់៖ 100 កាក់); ASCII : only in clock times.
- Quotes: « » or ""; pick one per game (« » is common in Khmer print, Microsoft examples use ""). Never quote promo codes; show them bare: FREEPETS
- ៗ (repeat mark) attaches to the word: ម្នាក់ៗ, ផ្សេងៗ. Avoid ។ល។ (etc.) in UI.
- Digits: Arabic. CLDR's default numbering for km is Latin digits with 1,250 and 1.5; percent attached: 50%. Khmer digits (០-៩) are valid but game code fills Arabic digits, so never mix ២ and 2 in one game.
- Space on both sides of digits and Latin words: ទិញដោយ 100 Robux / ចុច E ដើម្បីបើក
- Durations: ask game code to format {time} the CLDR way: 3 ម៉ោង 20 នាទី / 2 ថ្ងៃ 5 ម៉ោង / 45 វិនាទី (number, space, unit). CLDR keeps the full unit words even in its narrow form, and Khmer has no standard short time units (Microsoft), so never invent ម៉ / ន; 3h 20m is a readable fallback.
- Ellipsis ... as in English (Microsoft): កំពុងផ្ទុក...
- Max lengths: the repo lint counts code points after removing {params}, tags and ្ (a combining mark); vowel signs and other marks count. ព្រឹត្តិការណ៍ is 13 code points and lints at 11. Respect every max.
- Line breaking is the big Khmer risk. Measured in Studio (TextService, 2026-11-08): Roblox has no Khmer word breaking. It breaks at spaces; a space-free run too long for the line is cut wherever it overflows, even between a consonant and a pre-base vowel or ្រ (កើ -> ក | ើ; seen with េ ើ ោ ៃ and ក្រ, while កា stayed whole), which leaves a dotted circle at the start of the next line. A line can also start with ។ (measured). Rules:
  - Put a normal space at each natural phrase pause, which Khmer writing already does: ដើរចូលទៅក្នុងរង្វង់ភ្លឺ ដើម្បីលក់សត្វចិញ្ចឹមរបស់អ្នក។ Always put one before ដើម្បី, ប៉ុន្តែ, ឬ and និង.
  - Keep every space-free run narrower than its label: a run of n code points is about 0.3 x TextSize x n px wide (measured: 28 code points = about 160 px at TextSize 20). Rough budget: 10 code points on buttons and tags, 25 in wrapped body text.
  - Never put a space inside a word, before ។ ! ?, or before ៗ.
  - Never use zero-width spaces (U+200B), though Microsoft requires one between every word in Windows: measured, Roblox draws them at zero width but does not break at them, and they inflate length counts.
- Keyboard keys stay Latin, spaced: ចុច E ដើម្បីបើក / ចុច Shift ដើម្បីរត់

## Do not translate / keep as is
- Robux, Roblox, VIP, Premium, AFK, XP, promo codes (FREEPETS), usernames and display names, keybinds (E, Shift).
- Game title: keep the owner's title (Pet Hatch Tycoon). Khmer Wikipedia spells Roblox រ៉ូប្រុក្ស, but in a game keep Latin brand and title names; ask the owner before adding a Khmer title.
- Item and pet names are translated by meaning, not transliterated: Dragon -> នាគ, Lucky Potion -> ថ្នាំសំណាង.
- Script: Khmer Unicode only. Never romanized Khmer, never legacy-font text (Limon-era encodings show as Latin junk in Unicode).
- Spelling: Microsoft's normative dictionary is Chuon Nath's (1967). House rule: the modern subscript spellings over the older nikahit ones (Wiktionary marks សំរាប់ as an alternative form of សម្រាប់): សម្រាប់, ជម្រើស, កម្រិត, ទម្រង់, ចម្លង, not សំរាប់, ជំរើស, កំរិត, ទំរង់, ចំលង.
- House spelling ឲ្យ (Chuon Nath, Microsoft's examples, Wiktionary's main entry). ឱ្យ is equally correct and common (Khmer Wikipedia uses it); never mix the two in one game.
- Subscript ្ត and ្ដ look the same on screen but are different code points, so follow the dictionary word by word: Indic loanwords take ្ត (មិត្តភក្តិ, ប៉ុន្តែ, តន្ត្រី, ព្រឹត្តិការណ៍), native Khmer words take ្ដ (ម្ដង, ផ្ដល់, ស្ដាប់). House spellings: មិត្តភក្តិ, ម្ដង.

## Rendering on Roblox
- Font: the Roblox client ships one Khmer font, NotoSansKhmerUI-Regular.ttf (client file manifest). Measured in Studio, Khmer has identical widths in Source Sans, Gotham, Fredoka One, Luckiest Guy, Builder Sans and Arial, so every Font falls back to it. Expect plain Khmer beside stylized Latin.
- Shaping works: measured, ក្ក is as wide as ក (the subscript stacks), so HarfBuzz shaping (in Roblox since 2018, DevForum) handles Khmer. A lone vowel sign gets a dotted circle (U+25CC; measured widths show it); one in a string means a wrong code-point order or a mid-syllable wrap (see Typography).
- Bold: measured, Khmer keeps the same widths at Bold weight while Latin widens, so RichText <b> and bold fonts almost certainly leave Khmer regular (visual check unverified). Keep the <b> tags anyway; the highlighted word must read fine unbolded, and use color or size for emphasis that must show.
- Size: TextService gives Khmer the same line box as Latin (20 px at TextSize 20). Stacks go deep below the baseline (ស្ត្រី, ព្រឹត្តិការណ៍) and vowels sit high (ឡើង, ពេញ), and Noto "UI" fonts are drawn small to fit Latin line height. Whether marks clip in tight TextLabels or with TextScaled at phone size, and whether Khmer looks too small, is unverified: test those words and add padding or LineHeight if they clip.
- Wrapping: no Khmer word breaking and no break at U+200B (measured; see Typography). Preview long strings in Studio's km-kh test language at phone size and look for dotted circles at line starts.

## Mistakes machine translation makes here
- Bookish register: លោកអ្នកអាចទទួលបានរង្វាន់ -> បានរង្វាន់ហើយ!
- Over-polite openers on fun text: សូមមេត្តាចុចលេង -> លេង
- Gendered particles in system text: ទទួលបានហើយបាទ -> ទទួលបានហើយ!
- Experience as បទពិសោធន៍: ចូលចិត្តបទពិសោធន៍នេះ -> ចុចចូលចិត្តហ្គេម
- Claim as ទាមទារ (demand, legal claim): ទាមទាររង្វាន់ -> ទទួលយក
- Code as password: បញ្ចូលលេខសម្ងាត់ -> បញ្ចូលកូដ
- Potion as ទឹកថ្នាំ (ink): ទឹកថ្នាំសំណាង -> ថ្នាំសំណាង
- Food egg for a hatching egg: ស៊ុតនាគ -> ពងនាគ
- English punctuation copied: កូដមិនត្រឹមត្រូវ. / ...អស់, ប៉ុន្តែ -> កូដមិនត្រឹមត្រូវ។ / ...អស់ ប៉ុន្តែ
- Space before khan: ពេញហើយ ។ -> ពេញហើយ។
- Non-dictionary spellings: សំរាប់ / កំរិត -> សម្រាប់ / កម្រិត
- Broken encoding: deprecated ឣ (U+17A3) or ឤ (U+17A4), the invisible U+17B4 / U+17B5, or a vowel typed before the subscript -> use អ + vowel, delete the invisible signs, and type consonant + ្ + consonant + vowel + sign (ស + ្ + ត + ្ + រ + ី = ស្ត្រី)
- "2x" as "twice": កាក់ពីរដង on a pass name -> កាក់ x2
- Zero-width spaces (U+200B) between words, copied from Microsoft's Windows rule: invisible, no wrap point in Roblox -> delete them; plain spaces only at phrase breaks

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | លេង | |
| shop.title | ហាង | |
| shop.buy | ទិញ | |
| reward.claim | ទទួលយក | "take it"; ទទួលរង្វាន់ (receive the reward) also lints at 10 of 10 but is about twice as wide |
| rebirth.button | កើតជាថ្មី | Rebirth (Latin) if the game keeps genre words English |
| rebirth.confirm | ចង់កើតជាថ្មីឥឡូវនេះទេ? កាក់របស់អ្នកនឹងបាត់អស់ ប៉ុន្តែអ្នកនឹងរកកាក់បានច្រើន {multiplier} ដង ជារៀងរហូត! | assumes the boost multiplies coins; otherwise ...បាន Boost x{multiplier} ជារៀងរហូត! |
| coins.need_more | ត្រូវការកាក់ {amount} ទៀត! | fine for 1 |
| coins.count | {count} កាក់ | no plural form needed |
| egg.hatched | {pet}ថ្នាក់{rarity} ញាស់ចេញពីពងហើយ! | "a {rarity}-class {pet} hatched out of the egg!"; the pet is the subject of ញាស់ |
| rarity.legendary | រឿងព្រេង | reads នាគថ្នាក់រឿងព្រេង in egg.hatched |
| pet.name.dragon | នាគ | |
| chat.player_joined | {player} បានចូលហ្គេម | no ។ on chat lines |
| trade.request | {player} ចង់ដោះដូរជាមួយអ្នក | |
| prompt.open_shop | ចុច E ដើម្បីបើក | |
| pass.buy_price | ទិញដោយ {price} Robux | ដោយ ("with") stops it reading as "buy {price} Robux" |
| pass.coins2x | កាក់ x2 | |
| pass.vip | VIP | kept Latin: a pass name and a term players know from Roblox |
| reward.daily_title | រង្វាន់ប្រចាំថ្ងៃ | lints at 14 of 18 |
| reward.come_back | ត្រឡប់មកវិញក្នុង {time} ទៀត ដើម្បីយករង្វាន់បន្ទាប់! | needs {time} as 3 ម៉ោង 20 នាទី |
| codes.placeholder | បញ្ចូលកូដ | |
| codes.invalid | កូដនេះមិនត្រឹមត្រូវ ឬ ផុតកំណត់ហើយ។ | spaces around ឬ (Microsoft) also give a break point |
| social.like_reward | ចុចចូលចិត្តហ្គេម ដើម្បីបាន<b>ថ្នាំសំណាង</b>ឥតគិតថ្លៃ! | lints at 41 of 55; Khmer bold almost certainly does not show (see Rendering) |
| social.group_reward | ចូលរួមក្រុមរបស់យើង ដើម្បីដោះសោរង្វាន់ឥតគិតថ្លៃ! | |
| afk.warning | អ្នកកំពុង AFK! កម្រើកខ្លួន ដើម្បីរកកាក់បន្ត! | "keep earning" made concrete as coins; space before ដើម្បី gives a wrap point |
| leaderboard.title | អ្នកលេងកំពូល | |
| level.up | ឡើងកម្រិត! ឥឡូវអ្នកនៅកម្រិត {level} ហើយ! | |
| tutorial.sell | ដើរចូលទៅក្នុងរង្វង់ភ្លឺ ដើម្បីលក់សត្វចិញ្ចឹមរបស់អ្នក។ | |
| inventory.full | កាបូបពេញហើយ! លក់សត្វចិញ្ចឹមខ្លះ ដើម្បីមានកន្លែងទំនេរ។ | "your" dropped because it is obvious; lints at 48 of 60 |
| settings.music | តន្ត្រី | |
| settings.on | បើក | pair with បិទ |
| loading | កំពុងផ្ទុក... | Microsoft pattern កំពុង + verb + ... |
| event.ends_in | ព្រឹត្តិការណ៍ចប់ក្នុង {time} | lints at 19 of 28 before {time} adds about 11 (2 ថ្ងៃ 5 ម៉ោង); on a tight banner use នៅសល់ {time} ("{time} left") |
| item.op | ដាវនេះខ្លាំងពេក! | "too strong", the hype sense of OP that every reader gets |
| friends.boost | +{percent}% សម្រាប់មិត្តម្នាក់ៗ ដែលនៅ Server ជាមួយអ្នក | "boost" carried by the +%; Server Latin (unverified) |

## Sources
1. Microsoft Khmer Localization Style Guide (2011): https://download.microsoft.com/download/9/9/9/999ABAA3-9887-4D15-A0BA-762967FDC6C9/khm-khm-StyleGuide.pdf
2. Microsoft Localization Style Guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. CLDR Language Plural Rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR JSON, km number symbols: https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-numbers-full/main/km/numbers.json
5. CLDR JSON, km duration units: https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-units-full/main/km/units.json
6. Roblox Creator docs, Language codes: https://create.roblox.com/docs/production/localization/language-codes
7. Roblox client file manifest (NotoSansKhmerUI-Regular.ttf): https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/rbxManifest.txt
8. Roblox core UI translation table (no Khmer column): https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/translations/CoreScriptLocalization.csv
9. Khmer Wikipedia, Roblox (Robux kept Latin, ហ្គេម): https://km.wikipedia.org/wiki/Roblox
10. Khmer Wikipedia, Minecraft (អ្នកលេង, ល្បែង vs ហ្គេម): https://km.wikipedia.org/wiki/Minecraft
11. Google Play in Khmer (ហ្គេម, កម្មវិធី): https://play.google.com/store/apps/details?id=com.roblox.client&hl=km
12. Wikipedia, Khmer script (spacing, punctuation, encoding ambiguity): https://en.wikipedia.org/wiki/Khmer_script
13. Unicode UAX #14, Line Breaking Algorithm (class SA, ZWSP): https://www.unicode.org/reports/tr14/
14. DevForum, HarfBuzz typesetter (2018): https://devforum.roblox.com/t/support-for-arabic-text-and-other-languages-where-letters-are-connected/116447
15. Roblox locale API (km_kh flags; user-locale for a Khmer browser), checked 2026-11-08: https://locale.roblox.com/v1/locales and https://locale.roblox.com/v1/locales/user-locale
16. Wiktionary, Khmer entries ឲ្យ, ឱ្យ, មិត្តភក្តិ, ម្ដង, ផ្ដល់, ស្ដាប់, ញាស់, ថ្នាក់, ចំណូលចិត្ត: https://en.wiktionary.org/wiki/ឲ្យ
17. Studio measurements with TextService:GetTextSize and GetTextBoundsAsync, 2026-11-08 (fallback font, shaping, bold, wrapping, U+200B, widths vs English): this review
