# Malay (ms-my) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `ms-my` (Roblox's only Malay locale; no bare `ms` column needed). Never fill it by copying `id-id`: Indonesian words read as foreign, and a few are rude in Malaysia |
| Script, direction | Latin (Rumi), LTR; standard Malaysian spelling (DBP) uses the 26 basic letters, no diacritics. Never Jawi |
| Address the player as | "anda", lowercase mid-sentence; not "kamu"/"-mu" (familiar, and the pronoun of Indonesian UI), never spoken "awak", "kau", "hang" |
| Text expansion vs English | about +20% overall (+18% measured on the reference set); toasts and banners +20-35%; short buttons 0-33% ("Main", "Beli") |
| Plural categories (CLDR) | cardinal: other only; ordinal: one (1st, "pertama") and other ("ke-2"); nouns never change after a number |
| Model confidence | medium: grammar is reliable, but models drift into Indonesian, and Roblox itself has no Malay UI to anchor platform terms |
| Native review before shipping | strongly recommended |

## Audience and register
- Roblox does not offer its own app or website in Malay: its locale API lists `ms_my` as enabled for in-game content only, roblox.com/ms redirects to English, and Roblox's Play Store listing requested in Malay for Malaysia serves the Indonesian text. Malaysian kids therefore see Roblox's platform UI in English (or another language they picked), so your game is often the only Malay they read on Roblox. Roblox does not auto-translate into Malay, so they see Malay only if you ship the `ms-my` column. Roblox's in-game Settings menu has an "Experience Language" selector (in the client's own core UI strings), the likely way a player switches to `ms-my`; which languages it lists, and how many players reach `ms-my`, is (unverified): test in Studio and in a live server.
- Write everyday standard Malaysian Malay: correct DBP spelling, short common words, friendly. Not textbook, not chat shorthand ("x" for "tak", "sy", "dpt").
- Address the player as "anda". Kamus Dewan defines it as the "you" that ignores rank and age, and it is the only "you" Malaysian kids meet in Malay UI: Android (over 300 uses, no "kamu"), Google Play help, Microsoft's Malay guide and Minecraft's Malay translation (393 uses, no "kamu" or "awak") all use it, lowercase mid-sentence: "beg anda", "Anda perlukan 50 syiling lagi!". It reads neutral, not stiff, as long as the sentence around it is short. "kamu" is correct Malay but familiar (Kamus Dewan: more intimate), the way a teacher speaks to a pupil, and it is what Indonesian UI uses, so on screen it reads Indonesian; "awak" is spoken, not UI.
- Drop the pronoun where you can: buttons are bare verbs or nouns ("Main", "Beli", "Jual", "Tuntut", "Kedai"); "-kan" verbs give polite imperatives ("Masukkan kod"). No "Sila" on buttons or short toasts; keep it for real error help ("Sila cuba lagi." is Microsoft's own example, but "Cuba lagi!" suits kids).
- Short questions need no "Adakah": "Rebirth sekarang?", "Teruskan?" (Microsoft prefers such fragments).
- Contractions: "tiada" is fine anywhere; "tak" only now and then (Microsoft warns overuse sounds very informal).
- Hype that sounds Malaysian: "Tahniah!" (congratulations; not Indonesian "Selamat!"), "Syabas!", "Hebat!", "Wah, bertuahnya!", calls to action with "Jom": "Jom main!" (not Indonesian "Ayo", "Yuk"). Soft "-lah" is fine on exhortations: "Cubalah lagi!". One "!" per string.
- Kid-safe: no "bodoh", "bangang", "sial", "babi" as insults. "Noob" only in jokey flavor text, never aimed at the player.

## Roblox and gaming vocabulary
| English | ms-my | note |
|---|---|---|
| Robux | Robux | invariable: "100 Robux" |
| game pass | Game Pass, pas | players keep the English; "pas" in tight labels |
| developer product | produk | players never see the term; name the item |
| experience / game | permainan | Malay Wikipedia glosses Roblox's "Experience" as "pengalaman", but no player calls a game that; kids also say "game" |
| obby / tycoon / simulator | obby / tycoon / simulator | keep; "simulator" is also the Malay spelling |
| rebirth | Rebirth | keep; "Lahir Semula" is literal and does not fit a 10-character button |
| pet | pet | kept by pet-game players (unverified); "haiwan peliharaan" is correct but long; never Indonesian "hewan" |
| egg / hatch | telur / menetas, menetaskan | "Telur Legenda"; see grammar for the two verbs |
| coins / gems | syiling / permata | "syiling" is Kamus Dewan's word for a coin; never Indonesian "koin" |
| boost / multiplier | boost / pengganda | "Boost 2x"; "pengganda" is the dictionary word for a multiplier (Indonesian: "pengali") |
| XP / level up | XP / naik tahap | Minecraft's Malay uses "tahap" for levels; players also say "naik level" (fine in flavor text) |
| quest | misi | "quest" only inside proper names |
| leaderboard | Pemain Terbaik, papan pendahulu | "papan pendahulu" is the Malaysian UI term for a leaderboard (unverified); the title "Pemain Terbaik" is clearer to kids |
| AFK / noob / OP | AFK / noob / OP | keep; never spell out |
| VIP / Premium | VIP / Premium | never translate |
| trade | tukar, bertukar | "trade" also common in chat; Minecraft's Malay uses "dagangan" for villager trades (commerce, not pet swaps) |
| inventory / backpack | Inventori / beg | Minecraft: "Inventori"; never Indonesian "Inventaris", "tas", "ransel" |
| daily reward | Ganjaran Harian | "ganjaran" = reward (Kamus Dewan); "hadiah" means gift or prize |
| codes / redeem | kod / Tebus | "Masukkan kod"; redeem button "Tebus" (Google Play's Malay: "Tebus", "Masukkan kod anda"); never "kode" |
| group | komuniti | Roblox's player-facing UI now says Community (its core UI has "Community Emblem"; Creator docs still say group). "kumpulan" (Microsoft's Malay word for groups) if the game itself says group. Never "komunitas", "grup" |
| like / favorite | Like / kegemaran | players see the English "Like" button; never Indonesian "favorit" |
| server | server | players say "server"; Minecraft's Malay uses "pelayan" (formal, fine in settings) |
| friends / connections | rakan | Roblox's English UI shows "Connections"; in game text use "rakan" (Minecraft's Malay friends tab); "kawan" is casual but fine. Never Indonesian "teman" |
| shop / buy / sell | Kedai / Beli / Jual | never Indonesian "Toko" |
| claim | Tuntut | dictionary sense "claim"; "Ambil" (take) also fine. English "Claim" is seen in Malaysian apps (unverified) but not needed here |
| free | percuma | Minecraft's Malay: "Percubaan percuma"; never Indonesian "gratis" |
| event | acara | gamers also say "event" |
| lucky / luck | bertuah / tuah | "Ramuan Bertuah"; never Indonesian "hoki" |

## Grammar traps in UI strings
- Plurals: one form, so "{count} Syiling" is right for 0, 1 and 1,250. Never reduplicate after a number or a quantifier ("semua", "setiap", "banyak"): "5 pet-pet" -> "5 pet"; "setiap rakan-rakan" -> "setiap rakan". Microsoft allows reduplication only where plural must be explicit.
- Gender: none. "dia" covers everyone and verbs never agree: "{player} menyertai permainan" works for any name. Avoid gendered address ("abang", "adik", "bro").
- Modifiers follow the noun, so placeholder order flips: "{rarity} {pet}" -> "{pet} {rarity}" ("Naga Legenda"); "Daily Reward" -> "Ganjaran Harian"; "2x Coins" -> "Syiling 2x"; "Top Players" -> "Pemain Terbaik".
- "your" is "anda" after the noun: "syiling anda", "beg anda", "pet anda". Not "-mu" (familiar, Indonesian UI style) and not "-nya" (his/her/its).
- No articles. Classifiers depend on the noun ("seekor" for animals, "sebilah" for blades, "sebuah" for objects), so drop them before a placeholder: "Anda dapat seekor {pet}" breaks when {pet} is a robot; write "Anda dapat {pet}!".
- "dari" vs "daripada": "dari" for places and time ("dari lobi", "dari esok"), "daripada" for people, things and comparisons ("Hadiah daripada {player}", "lebih laju daripada kereta"). Models use "dari" everywhere.
- "di"/"ke" as prepositions stand apart ("di server", "ke kedai"); the passive prefix joins the verb ("dijual", "ditukar"). Do not bolt Malay affixes onto English words ("di-trade"); rephrase: "Pet ini sudah ditukar".
- "menetas" is intransitive (the egg hatches), "menetaskan" transitive: "Telur menetas!", "Anda menetaskan {pet}!". "Anda menetas" means you hatched out of an egg.
- "permanent" is "kekal" (Indonesian "permanen"); "next" is "seterusnya" or "berikutnya"; "want" is "mahu" (Indonesian "mau").
- Capitalization: Malay capitalizes only sentence starts and proper nouns, but titles, buttons and item names take Title Case (Microsoft for titles; Minecraft for items and screens: "Pedang Berlian", "Tetapan Perbualan"), with "dan", "di", "ke", "untuk", "yang", "daripada" lowercase when not first. Toasts and dialogs in sentence case. "anda" is capitalized only as the first word ("Anda Telah Mati!" in Minecraft) and stays lowercase everywhere else.

## Typography and formatting
- Punctuation as in English: no space before ! ? : ; and one space after (Microsoft). No comma before "dan" in a list: "Beli, jual dan tukar pet".
- Quotes: straight "..." first, '...' inside (Microsoft); CLDR also lists curly double quotes. Pick one per game.
- Numbers are formatted like English: comma for thousands, period for decimals (CLDR): "1,250 Syiling", "boost 1.5x". So English-formatted {count}, {amount} and {multiplier} are already right; never copy Indonesian "1.250" or "1,5x". Percent has no space: "10%". Compact forms (CLDR): "K" for ribu, "J" for juta: "1.2J Syiling", not English "1.2M".
- Microsoft spells out 0-9 in running text; ignore that in game UI, where numbers come from code: "3 pet", "Tahap 5".
- Ordinals: "pertama" for 1st, then "ke-" plus a hyphen with digits: "Tempat ke-2", "Hari ke-7".
- Durations (CLDR narrow units): hari "h", jam "j", minit "min", saat "s" -> "3 j 20 min", "2 h 5 j". Never ship English "3h 20m": "h" reads as hari (days). When there is room, "2 hari 5 jam" is clearest.
- Clock time is 12-hour with PG/PTG (CLDR): "2:30 PTG"; short dates are day first: "8/11/26".
- Ellipsis: three periods, no space: "Memuatkan...".
- Keys: keys printed in English stay English (Microsoft): "Tekan E untuk membuka". On touch prompts use "Ketik" (Android's Malay: "Ketik untuk ..."); "Ketuk" is Roblox's Indonesian wording.

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, XP, noob, obby, tycoon, simulator, Rebirth, Game Pass, boost.
- The game title "Pet Hatch Tycoon": keep English unless the developer supplies a Malay title.
- Display names, usernames, promo codes ("FREEPETS"), keybinds.
- Script: Rumi (Latin) only. Jawi is official in Malaysia but no Roblox game text uses it; `ms-my` means Rumi.
- Spelling is Malaysian only: "kod" not "kode", "muzik" not "musik", "wang" not "uang", "kerana" not "karena", "cuba" not "coba", "haiwan" not "hewan", "komuniti" not "komunitas", "kekal" not "permanen", "tamat tempoh" not "kedaluwarsa", "Legenda" not "Lagenda" (a common misspelling) or "Legendaris" (Indonesian; not in Kamus Dewan).

## Rendering on Roblox
- Malay in Rumi needs only basic Latin letters, digits and ASCII punctuation, which every Roblox font (Builder Sans, Gotham, Source Sans and the decorative fonts) includes. No shaping, no diacritics, nothing to clip. No Malay-specific font problems were found.
- The real risk is length. Affixed words cannot break ("Memuatkan", "kosongkan", "menetaskan"), and sentences run 20-35% longer than English, so a narrow button either overflows or TextScaled shrinks the whole label. Give labels AutomaticSize or slack.
- Verify in Studio with the ms-my test locale (not yet done for this guide): the like banner (54 of 55), "Tekan E untuk membuka" (21 of 22) at the smallest phone width, "{count} Syiling" with a 7-digit count, and every toast with a 20-character {player}.

## Mistakes machine translation makes here
1. Indonesian leakage (Roblox's own "Malay" store text is Indonesian, so models learn it): "gratis" -> "percuma", "toko" -> "kedai", "gabung" -> "sertai", "bisa" -> "boleh", "teman" -> "rakan", "koin" -> "syiling", "pengaturan" -> "tetapan", "tas" -> "beg", "Selamat!" -> "Tahniah!", "Ayo" -> "Jom".
2. Rude false friends: "butuh" (need) is a vulgar word in Malaysia (Kamus Dewan marks it coarse): "Kamu butuh 50 koin lagi!" -> "Anda perlukan 50 syiling lagi!". "gampang" (easy) recalls "anak gampang", an insult: "Gampang!" -> "Senang saja!".
3. Indonesian spelling: "kode" -> "kod", "musik" -> "muzik", "kedaluwarsa" -> "tamat tempoh", "tidak valid" -> "tidak sah", "permanen" -> "kekal", "Inventaris" -> "Inventori".
4. Indonesian address: "Koinmu habis" -> "Syiling anda habis"; capital "Anda" mid-sentence -> "anda".
5. Wrong rarity word: "Legendaris" or "Lagenda" -> "Legenda".
6. Stiff register: "Adakah anda ingin melakukan rebirth sekarang?" -> "Rebirth sekarang?"; "Sila masukkan kod" -> "Masukkan kod".
7. English adjective order: "Legenda Naga" -> "Naga Legenda"; "Harian Ganjaran" -> "Ganjaran Harian".
8. Reduplicated plurals: "100 syiling-syiling" -> "100 syiling".
9. Literal gaming terms: "Lahir Semula" -> "Rebirth"; "Jauh dari papan kekunci" -> "AFK"; "Terlalu berkuasa" -> "OP".
10. English durations: "3h 20m" -> "3 j 20 min".
11. Ambiguous price button: "Beli 100 Robux" reads as buying Robux -> "Beli: 100 Robux".
12. Wrong preposition: "Hadiah dari {player}" -> "Hadiah daripada {player}".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Main | Minecraft's Malay "Main" |
| shop.title | Kedai | |
| shop.buy | Beli | |
| reward.claim | Tuntut | Kamus Dewan: to claim what is yours. "Ambil" (take) also works; avoid English "Claim" |
| rebirth.button | Rebirth | kept as players say it |
| rebirth.confirm | Rebirth sekarang? Syiling anda akan hilang, tetapi anda dapat boost {multiplier}x yang kekal. | |
| coins.need_more | Anda perlukan {amount} syiling lagi! | right for any {amount}, including 1; never "butuh" |
| coins.count | {count} Syiling | English-formatted "1,250" is already Malaysian format; "1,000,000 Syiling" is 17 of 16, so show 7+ digits compact ("1.2J Syiling") |
| egg.hatched | {pet} {rarity} menetas! | "A Legendary Dragon hatched!"; order flipped, 36 at max lengths. Not "Anda menetaskan {pet} {rarity}!" (44 of 40 at max); if the game wants "you", "Anda dapat {pet} {rarity}!" fits (39) |
| rarity.legendary | Legenda | |
| pet.name.dragon | Naga | |
| chat.player_joined | {player} menyertai permainan | Minecraft's Malay uses the same verb |
| trade.request | {player} mahu bertukar dengan anda | |
| prompt.open_shop | Tekan E untuk membuka | 21 of 22 |
| pass.buy_price | Beli: {price} Robux | colon stops it reading as "buy N Robux" |
| pass.coins2x | Syiling 2x | noun first |
| pass.vip | VIP | |
| reward.daily_title | Ganjaran Harian | Title Case |
| reward.come_back | Datang lagi dalam {time} untuk ganjaran seterusnya! | {time} must use Malay units ("3 j 20 min") |
| codes.placeholder | Masukkan kod | |
| codes.invalid | Kod itu tidak sah atau sudah tamat tempoh. | |
| social.like_reward | Like permainan ini untuk dapat <b>Ramuan Bertuah</b> percuma! | 54 of 55; "Like" matches the English button players see. Minecraft's Malay calls potions "Posyen"; "Ramuan" is the plain Malay word |
| social.group_reward | Sertai komuniti kami untuk membuka ganjaran percuma! | "komuniti" per Roblox's Communities rename; "kumpulan" if the game still says group |
| afk.warning | Anda AFK. Gerak untuk terus dapat syiling! | 42 of 45; "earning" made concrete as coins (use the game's own currency word) |
| leaderboard.title | Pemain Terbaik | "best players"; "Pemain Teratas" also fine |
| level.up | Naik tahap! Kini anda di tahap {level}. | |
| tutorial.sell | Berjalan masuk ke bulatan bercahaya untuk menjual pet anda. | "bulatan", not Indonesian-leaning "lingkaran" |
| inventory.full | Beg anda penuh! Jual pet untuk kosongkan ruang. | |
| settings.music | Muzik | |
| settings.on | Hidup | 5 of 5; Android's Malay toggle states are "Hidup"/"Mati". Minecraft's Malay uses "BUKA"/"TUTUP" |
| loading | Memuatkan... | Microsoft's own example |
| event.ends_in | Acara tamat dalam {time} | 25 with "2 h 5 j", 28 with "3 j 20 min"; "23 j 59 min" makes 29 of 28, so if the timer shows hours and minutes use "Tamat dalam {time}" |
| item.op | Pedang ini memang OP! | |
| friends.boost | Boost +{percent}% untuk setiap rakan dalam server ini | "your server" = the server you are in |

## Sources
1. Microsoft Malay (Malaysia) Localization Style Guide: https://download.microsoft.com/download/97c8474f-dd92-459b-9349-07993da9166a/may-mys-StyleGuide.pdf
2. Unicode CLDR language plural rules chart: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON, Malay numbers, units, quotation marks and date/time formats: https://github.com/unicode-org/cldr-json/tree/main/cldr-json (main/ms: numbers.json, units.json, delimiters.json, ca-gregorian.json)
4. Roblox locale API (ms_my enabled for in-game content only, not the full app): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
5. Roblox Creator docs, language codes (Malay = ms / ms-my): https://create.roblox.com/docs/production/localization/language-codes
6. Roblox Creator docs, localization overview (account-level translation setting): https://create.roblox.com/docs/production/localization
7. roblox.com in Malay (redirects to the English page): https://www.roblox.com/ms/games/920587237/Adopt-Me
8. Roblox on Google Play requested in Malay for Malaysia (serves the Indonesian description): https://play.google.com/store/apps/details?id=com.roblox.client&hl=ms&gl=MY
9. Malay Wikipedia, Roblox ("pengalaman" for Experience, "pelayan", "mata wang maya"): https://ms.wikipedia.org/wiki/Roblox
10. Minecraft Java Edition 26.3 ms_my language file (community translation: "anda", "Rakan", "Inventori", "Muzik", "percuma", "tidak sah", "tamat tempoh", "Memuatkan"): Mojang asset index, https://resources.download.minecraft.net
11. DBP PRPM dictionary (Kamus Dewan): butuh, gampang, legenda, legendaris, syiling, ganjaran, pengganda, anda, kamu, awak, percuma, bulatan, tuntut: https://prpm.dbp.gov.my/Cari1?keyword=butuh
12. Android (AOSP) Malay strings, values-ms: "Hidup"/"Mati" states, "Ketik untuk ...", "anda": https://android.googlesource.com/platform/frameworks/base/+/refs/heads/main/packages/SystemUI/res/values-ms/strings.xml
13. Google Play Help in Malay, redeem a gift card or code ("Tebus", "Masukkan kod anda"): https://support.google.com/googleplay/answer/3422659?hl=ms
14. Roblox client core UI string table, ExtraContent/translations/CoreScriptLocalization.csv (no Malay column; "Experience Language" setting, "Community Emblem", Indonesian "Ketuk"): shipped with every Roblox Player install
15. Roblox Creator docs, groups (still "group"; Communities is the player-facing surface): https://create.roblox.com/docs/projects/groups
