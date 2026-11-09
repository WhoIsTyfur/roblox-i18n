# Sinhala (si-lk) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `si-lk` (Sinhala has one written variant, so a bare `si` column adds nothing) |
| Script, direction | Sinhala script, Unicode with ZWJ inside conjuncts, LTR; Latin for kept terms and all digits |
| Address the player as | ඔබ / ඔබේ, or no pronoun; never උඹ, තෝ or නුඹ (rude or intimate), never ඔබතුමා (ceremonious) |
| Text expansion vs English | about +10% in lint characters on the reference set, but about +45% in pixel width (unshaped estimate); one-word buttons 2-3.5x |
| Plural categories (CLDR) | one (0 and 1), other; ordinals: other only |
| Model confidence | low -- low-resource language with sharp spoken/literary diglossia, an invisible ZWJ in common words, and no Roblox Sinhala UI or Microsoft style guide to copy |
| Native review before shipping | strongly recommended |

## Audience and register
Roblox has no Sinhala UI: its locale API marks si_lk as usable for in-game content only, not for the app or sign-up, and the client's CoreScript translation table has no Sinhala column (checked 2026-11-08). Sri Lankan kids run Roblox in English and meet Robux, Friends, Communities and Premium in English. Sinhala is diglossic: literary Sinhala (news, textbooks, Wikipedia) has subject-verb agreement, spoken Sinhala has none. A friendly game writes polite spoken Sinhala:
- Finite verbs in spoken forms: -නවා, වුණා, ආවා, පිරිලා, නැහැ. Literary finite forms (ඇත, නොවේ, වේ, විය, ලැබිණි, -ේය / -ාය endings) are Android's system voice (පරීක්ෂා කර ඇත) and read like a notice in a game. Never mix the two in one string.
- Buttons: verb + න්න, the form Google Play's Sinhala UI uses (බෙදා ගන්න, තව දැන ගන්න): මිලදී ගන්න, ලබා ගන්න. Titles and labels: bare nouns (සාප්පුව, සංගීතය).
- Purpose clauses: spoken -න්න (ඉඩ හදන්න ... විකුණන්න) or the neutral literary infinitive -ීමට (විවෘත කිරීමට E ඔබන්න). Both are fine; only the finite verb must be spoken.
- "You" is ඔබ / ඔබේ, as in Google's Sinhala Play listing and Android (Wiktionary: ඔබ formal, ඔයා informal). Sinhala drops subjects freely, so drop it when the line still reads: බෑගය පිරිලා! ඔයා is warmer and common in speech to kids; use it only if the whole game is chatty, never beside ඔබ (unverified preference).
- Hype: short exclamations (නියමයි! සුපිරි!). Yes/no questions take ද: Rebirth කරනවාද?
- English loans act Sinhala: an English verb takes කරන්න (Rebirth කරන්න, Like කරන්න), an English noun takes එක / එකක් (Boost එකක්, Event එක). The Latin word itself never inflects.
- Kid-safe and culture-safe: most players are Buddhist, so never පුනර්භවය or නැවත ඉපදීම (religious rebirth) for Rebirth, and never විපාකය (karmic result) for a reward. Hatching is not gambling: avoid ලොතරැයි (lottery) and ජැක්පොට්.

## Roblox and gaming vocabulary
| English | Use in si-lk | Note |
|---|---|---|
| Robux | Robux | Latin, as Sinhala Wikipedia writes it; never රොබක්ස් |
| Premium | Premium | Roblox subscription name, Latin |
| game pass | Game Pass | in a shop just name the perk (2x කාසි) |
| developer product | the item's name | players never see the term |
| experience / game | ක්‍රීඩාව | Google's and Wikipedia's word; players say ගේම් එක (unverified); never අත්දැකීම (life experience) |
| player | ක්‍රීඩකයා, pl. ක්‍රීඩකයෝ | ක්‍රීඩකයින් in formal text |
| obby | Obby | Latin; explain as බාධක දිවීම (Madura's "obstacle race"); not Sinhala Wikipedia's බාධක පාඨමාලා, a calque (පාඨමාලාව is a school course) |
| tycoon / simulator | Tycoon / Simulator | Latin, as in game titles; never ධන කුවේරයා ("rich man") |
| rebirth | Rebirth | Latin + කරන්න |
| pet | සුරතල් සතා, pl. සුරතල් සතුන් | Madura's word; Pet in Latin only on a cramped label (unverified preference) |
| egg / hatch | බිත්තරය / බිත්තරය අරින්න | result line: බිත්තරයෙන් මකරා එළියට ආවා! |
| coins | කාසි | noun before number: කාසි 100 |
| gems | මැණික් | Sinhala Wikipedia's "gemstone" |
| boost | Boost | Boost එකක් ලැබුණා! |
| multiplier | x | 2x කාසි; දෙගුණ (double) is the native word |
| XP | XP | |
| level / level up | Level / Level එක ඉහළ ගියා | මට්ටම is the textbook word; one choice per game |
| quest | අභියෝගය | "challenge" (unverified); never මෙහෙයුම, a military or police operation (Madura lists it under "operation"); Quest in Latin also works |
| leaderboard | ලකුණු පුවරුව | "scoreboard"; board header හොඳම ක්‍රීඩකයෝ |
| AFK / noob / OP / VIP | AFK / noob / OP / VIP | Latin; never aim noob at the player |
| trade | හුවමාරුව / හුවමාරු කරගන්න | Trade කරන්න is the chat form (unverified) |
| inventory / backpack | අයිතම / බෑගය | අයිතම = items, Google's word |
| daily reward | දිනපතා තෑග්ග | තෑග්ග = gift; ත්‍යාගය = prize, also a lottery prize |
| codes | කේතය, pl. කේත | spoken කෝඩ්; the code itself stays Latin |
| free | නොමිලේ | Google Play's word |
| group | ප්‍රජාව | Roblox's English UI says Community since Nov 2024; කණ්ඩායම if the game's UI says group |
| like / favorite | Like / Favorite | the English Roblox buttons: Like එකක් දාන්න, Favorite කරන්න (spoken usage unverified) |
| server | සර්වරය | spoken සර්වර් එක |
| friends | මිතුරන්, sg. මිතුරා | Google's word; Roblox's English UI says Friends again since April 2026; never සම්බන්ධතා (connections); chatty යාළුවෝ |

## Grammar traps in UI strings
- Plurals with {count}: CLDR has one (0, 1) and other, but one string must serve all. Use the Sinhala quantity order, plural noun then number, right for 0, 1 and 1,250: කාසි {count}. For "N more" add ක් to the number: තව කාසි {amount}ක් අවශ්‍යයි! English order ({count} කාසි) reads as a calque.
- Endings fuse to numbers only. Case endings are written onto the word (-ට to, -ගේ / -ේ of, -ගෙන් / -න් from, -ක් a, -කට for). On a digit placeholder they are safe: {amount}ක්, Robux {price}කට. Never on {player}, {pet}, {rarity} or {time}: "Alexට" looks broken, and the ending differs for animate and inanimate nouns. Rephrase so the placeholder is a bare subject: {player} ඔබ සමඟ හුවමාරු කරගන්න කැමතියි; {time} ගියාම ...
- Gender: literary verbs agree with the subject (ඔහු පැමිණියේය "he came", ඇය පැමිණියාය "she came"); spoken verbs never do. A {player} subject always takes a spoken verb: {player} ක්‍රීඩාවට සම්බන්ධ වුණා. Use the common plural මිතුරන්; never put a gendered noun next to {player}.
- Animate vs inanimate: "there is" is ඉන්නවා for people and pets, තියෙනවා for things (සර්වරයේ ඉන්න මිතුරන් / බෑගයේ තියෙන අයිතම); "a" is -ෙක් on animates (මිතුරෙක්), -ක් on things (තෑග්ගක්).
- SOV with postpositions: the verb goes last, "with you" is ඔබ සමඟ. "Buy for {price} Robux" -> Robux {price}කට මිලදී ගන්න; "Come back in {time}" -> {time} ගියාම ... ආයෙත් එන්න!
- Modifiers precede the noun, so {rarity} {pet} keeps the English order: පුරාවෘත්ත මකරා.
- Spoken negation is නැහැ after the predicate: වලංගු නැහැ (not literary වලංගු නොවේ).
- Spelling: Google's own listing writes both මිලදී and මිල දී. Pick one per game; this guide uses මිලදී.
- No capitals in Sinhala; kept English words keep theirs (Level, Boost, VIP).
- Latin share: the repo lint fails a string whose letters are under half Sinhala. Two Latin "Level"s in level.up sit near that line; keep Sinhala words around Latin terms.

## Typography and formatting
- Western punctuation (. , ? ! :) with no space before. The kunddaliya ෴ is a historical full stop: never use it, nor the Devanagari danda ।.
- No full stop on buttons, titles, labels or placeholders. Toasts end with "!" or ".", never both.
- Quotation marks: “...” and ‘...’ (CLDR).
- Digits: ASCII 0-9 (CLDR default for si), group "," and decimal ".": 1,250 / 1.5. Never Sinhala Lith digits (෦-෯).
- Percent: no space: +{percent}% (CLDR #,##0%).
- Durations: CLDR puts the unit before the number: පැය 3 මිනි 20, දින 2 පැය 5 (short units දින, පැය, මිනි, තත්). Ask the developer to format {time} that way; "3h 20m" is a readable fallback. Either way never inflect {time}.
- Ellipsis: three ASCII dots fused to the word: පූරණය වෙමින්...
- Words are separated by spaces, so wrapping works as in English. Endings fuse with no space: 100ක්, 100කට.
- ZWJ (U+200D) is part of the spelling. Rakaransaya, yansaya and repaya are typed with al-lakuna ් + ZWJ: ක්‍රීඩා = ක ් U+200D ර ී ඩ ා. Without it the word shows a visible ් and a full ර. Never strip U+200D in tooling or swap it for U+200B or ZWNJ. The repo lint counts every ZWJ and vowel sign toward max length (it skips only ්), so Sinhala counts run high.
- Logical order: a vowel sign is typed after its consonant cluster even when drawn before it: ට්‍රේ = ට ් ZWJ ර ේ. Old non-Unicode text and bad converters store visual order (see Mistakes).
- Keyboard keys stay Latin: විවෘත කිරීමට E ඔබන්න

## Do not translate / keep as is
- Latin, byte-identical: Roblox, Robux, Premium, the game title, VIP, AFK, OP, XP, noob, promo codes (FREEPETS), keys (E), display names. Sinhala Wikipedia titles its article රොබ්ලොක්ස් but writes Roblox and Robux in Latin in the body, and players see Latin in the app: never transliterate.
- Latin by this guide's choice (see table): Rebirth, Boost, Level, Event, Like, Favorite, Obby, Tycoon, Simulator. Latin keeps them identical to the game's English icons and art; Sinhala-script spellings (ලෙවල්, බූස්ට්, ලයික්) also appear in writing (unverified), so if a game picks those, use them in every string. A string that ends up all Latin (Rebirth, VIP) needs keep:true or the lint flags it.
- Translate ordinary item, pet and rarity words: Dragon -> මකරා, Lucky Potion -> වාසනා පානය ("luck drink", unverified; never විෂ, poison), Legendary -> පුරාවෘත්ත, Coins -> කාසි.
- Sinhala script only: never romanized Sinhala ("Singlish", game eka), which players type in chat (unverified), and never Tamil script; Tamil-speaking Sri Lankans are a separate audience.

## Rendering on Roblox
- Roblox ships a Unicode Sinhala fallback font. All seven Windows player and Studio builds installed here (June-November 2026) contain content/fonts/NotoSansSinhalaUI-Regular.ttf (Noto Sans Sinhala UI 2.000), and RobloxPlayerBeta.exe names it beside its other Noto fallbacks and contains HarfBuzz code (local inspection 2026-11-08; Roblox docs do not document this). Sinhala should render whatever Font a label uses; stylized faces (Fredoka One, Luckiest Guy) have no Sinhala glyphs, so Latin words in the same line keep the stylized look.
- Coverage (fontTools): every modern letter, vowel sign, Lith digit and the kunddaliya, plus ZWJ and ZWNJ; only U+0D81 candrabindu (added 2020, unused in modern text) is missing. Its shaping features (akhn, rphf, vatu, pstf, pres, abvs, blws, psts) cover rakaransaya, yansaya, repaya and conjuncts. That Roblox applies them correctly is unverified.
- In Studio, set the test locale to si-lk and check: ක්‍රීඩා and ප්‍රජාව (rakaransaya), අවශ්‍යයි (yansaya), any repaya word the game uses, හොඳම and සෙල්ලම් (sign drawn left), පූරණය and සුරතල් (signs below), and that no dotted circle appears.
- Only Regular ships; the exe also names NotoSansSinhalaUI-VF.ttf and NotoSansSinhala-VF.ttf, which are not on disk. <b> may not look bold (unverified): keep the tags, never rely on bold for meaning.
- Height: the font's line box is 1.36 em, and Sinhala ink measured about 1.3x taller than Builder Sans at 40 px. Signs sit above (ි ී, repaya) and below (ු ූ). Allow about 1.3x Latin line height or AutomaticSize Y, and check TextScaled buttons at phone size.
- Width: sentences run about +45%, short buttons far more (ක්‍රීඩා කරන්න is about 3.5x "Play", unshaped estimate). Size buttons with AutomaticSize X or TextScaled.
- Wrapping should break at spaces like English; confirm it never splits a cluster (unverified).

## Mistakes machine translation makes here
- Dropped ZWJ: ක්රීඩා -> ක්‍රීඩා
- Visual-order debris, as on Google Play's Sinhala Roblox page: ටේ‍්‍රලරය -> ට්‍රේලරය
- Literary agreement on a player: {player} ක්‍රීඩාවට පැමිණියේය (masculine) -> {player} ක්‍රීඩාවට සම්බන්ධ වුණා
- Notice-board register: මෙම කේතය වලංගු නොවේ. -> මේ කේතය වලංගු නැහැ.
- "Experience" as life experience: නව අත්දැකීම් -> නව ක්‍රීඩා (Google's machine-translated Roblox listing does this)
- Tycoon translated: ධන කුවේරයන් -> Tycoon (same listing)
- Doubled noun and verb: ක්‍රීඩා ක්‍රීඩා කරන්න -> ක්‍රීඩා කරන්න (same listing, for "play games")
- Religious or karmic words: පුනර්භවය -> Rebirth; විපාකය -> තෑග්ග
- English number order: 100 කාසි -> කාසි 100
- Ending glued to a name: {player}ට ඔබ සමඟ trade කරන්න ඕනේ -> {player} ඔබ සමඟ හුවමාරු කරගන්න කැමතියි
- Wrong pronoun: උඹ / ඔබතුමා -> ඔබ, or none
- Transliterated brand, "connections": රොබක්ස් -> Robux; සම්බන්ධතා -> මිතුරන්

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | ක්‍රීඩා කරන්න | Google Play's listing says නොමිලේ ක්‍රීඩා කරන්න ("play free"); 11 lint chars vs 8 (ZWJ and signs count), size the button; if it cannot grow, යමු! ("let's go", 4) (unverified) |
| shop.title | සාප්පුව | |
| shop.buy | මිලදී ගන්න | 9 lint chars vs 8; ගන්න alone reads as "take" |
| reward.claim | ලබා ගන්න | "receive" |
| rebirth.button | Rebirth | kept Latin, needs keep:true |
| rebirth.confirm | දැන් Rebirth කරනවාද? ඔබේ කාසි නැති වෙනවා, නමුත් ස්ථිර {multiplier}x Boost එකක් ලැබෙනවා! | ස්ථිර = permanent |
| coins.need_more | තව කාසි {amount}ක් අවශ්‍යයි! | ක් fused to the number; fine for 1 |
| coins.count | කාසි {count} | noun then number |
| egg.hatched | බිත්තරයෙන් {rarity} {pet} එළියට ආවා! | "came out of the egg"; no ending touches {pet} |
| rarity.legendary | පුරාවෘත්ත | noun "legend" as a modifier, like පුරාවෘත්ත කතා; Madura glosses legendary only as mythical or "told in legends", so the rarity sense is unverified |
| pet.name.dragon | මකරා | Madura's word for dragon |
| chat.player_joined | {player} ක්‍රීඩාවට සම්බන්ධ වුණා | spoken වුණා has no gender |
| trade.request | {player} ඔබ සමඟ හුවමාරු කරගන්න කැමතියි | {player} stays a bare subject |
| prompt.open_shop | විවෘත කිරීමට E ඔබන්න | E stays Latin |
| pass.buy_price | Robux {price}කට මිලදී ගන්න | Sinhala price order, like රුපියල් 100කට |
| pass.coins2x | 2x කාසි | native alternative දෙගුණ කාසි |
| pass.vip | VIP | keep:true |
| reward.daily_title | දිනපතා තෑග්ග | |
| reward.come_back | {time} ගියාම ඊළඟ තෑග්ග ගන්න ආයෙත් එන්න! | "once {time} has passed"; works with any {time} format |
| codes.placeholder | කේතය ඇතුළත් කරන්න | |
| codes.invalid | මේ කේතය වලංගු නැහැ, නැත්නම් කල් ඉකුත් වෙලා. | spoken; වලංගු නොවේ is too stiff |
| social.like_reward | ක්‍රීඩාවට Like එකක් දාලා නොමිලේ <b>වාසනා පානයක්</b> ගන්න! | "put a Like on the game"; bold wraps the item and its ක් |
| social.group_reward | අපේ ප්‍රජාවට එකතු වෙලා නොමිලේ තෑග්ගක් ගන්න! | ප්‍රජාව matches Roblox's Community; "unlock" -> "get" |
| afk.warning | ඔබ AFK! දිගටම උපයන්න ටිකක් ඇවිදින්න! | "walk a little to keep earning" |
| leaderboard.title | හොඳම ක්‍රීඩකයෝ | "best players" |
| level.up | Level එක ඉහළ ගියා! දැන් ඔබ Level {level}. | spoken equational sentence, no copula |
| tutorial.sell | සුරතල් සතුන් විකුණන්න දිලිසෙන රවුමට ඇවිදගෙන යන්න. | purpose first, verb last |
| inventory.full | බෑගය පිරිලා! ඉඩ හදන්න සුරතල් සතුන් විකුණන්න. | "your" dropped |
| settings.music | සංගීතය | |
| settings.on | සක්‍රිය | Android's Sinhala word for enabled; 6 lint chars vs 5 because the ZWJ counts, but it draws as three clusters; Off = අක්‍රිය. Android's own ON/OFF (සක්‍රීයයි / ක්‍රියාවිරහිතයි) are too long |
| loading | පූරණය වෙමින්... | Android's exact Sinhala Loading string; friendlier ටිකක් ඉන්න... ("wait a bit") |
| event.ends_in | Event එක ඉවර වෙන්න තව {time} | no ending on {time} |
| item.op | මේ කඩුව නම් OP! | නම් = emphatic "this one" |
| friends.boost | සර්වරයේ ඉන්න හැම මිතුරෙක්ම ඔබට +{percent}% Boost එකක් දෙනවා | "every friend in the server gives you"; dative හැම මිතුරෙකුටම reads as the friends getting the boost; ඉන්න because friends are animate |

## Sources
1. Roblox locale API (si_lk in-game content only) -- https://locale.roblox.com/v1/locales
2. Roblox Creator Docs, Language codes -- https://create.roblox.com/docs/production/localization/language-codes
3. Roblox Windows client and Studio installs (content/fonts read with fontTools, RobloxPlayerBeta.exe strings, ExtraContent/translations/CoreScriptLocalization.csv), inspected 2026-11-08
4. Microsoft Localization Style Guides index (lists no Sinhala guide) -- https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
5. Unicode CLDR, Language Plural Rules -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
6. CLDR JSON, si numbers -- https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-numbers-full/main/si/numbers.json
7. CLDR JSON, si units -- https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-units-full/main/si/units.json
8. CLDR JSON, si delimiters and characters -- https://github.com/unicode-org/cldr-json/tree/main/cldr-json/cldr-misc-full/main/si
9. Google Play, Roblox listing in Sinhala -- https://play.google.com/store/apps/details?id=com.roblox.client&hl=si&gl=LK
10. Sinhala Wikipedia, Roblox -- https://si.wikipedia.org/wiki/රොබ්ලොක්ස්
11. Sinhala Wikipedia, Minecraft and video game articles -- https://si.wikipedia.org/wiki/මයින්ක්‍රාෆ්ට්
12. Wikipedia, Sinhala script (ZWJ forms, kunddaliya) -- https://en.wikipedia.org/wiki/Sinhala_script
13. Wikipedia, Sinhala language (diglossia, agreement) -- https://en.wikipedia.org/wiki/Sinhala_language
14. Wiktionary (කාසිය, බිත්තර, සංගීතය, කඩුව, ඔබ, ඔයා) and Wikipedia langlinks (මැණික්, කඩුව, බිත්තරය) -- https://en.wiktionary.org/wiki/ඔබ
15. Roblox DevForum, Friends Are Back (April 2026) -- https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
16. Roblox DevForum, Introducing Roblox Communities (Nov 2024) -- https://devforum.roblox.com/t/introducing-roblox-communities/3268307
17. Android framework Sinhala strings (Loading, ON/OFF, Cancel, Share, ඔබ) -- https://github.com/aosp-mirror/platform_frameworks_base/blob/main/core/res/res/values-si/strings.xml
18. Madura English-Sinhala dictionary (dragon, pet, potion, legendary, obstacle race, operation, challenge) -- https://www.maduraonline.com/
