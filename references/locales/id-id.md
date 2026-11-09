# Indonesian (id-id) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `id-id` (the only Indonesian locale; no bare `id` column needed). Never fill `ms-my` by copying this column: Malay is a separate language with its own words |
| Script, direction | Latin, LTR; standard spelling (EYD) uses only the 26 basic letters, no diacritics |
| Address the player as | informal "kamu" and the suffix "-mu"; never "Anda", never Jakarta slang "lo/gue" |
| Text expansion vs English | about +15-30% (estimate); affixed verbs make long single words ("menetaskan", "kedaluwarsa"), but core buttons stay short ("Main", "Beli", "Toko") |
| Plural categories (CLDR) | other only (cardinal and ordinal); nouns never change after a number |
| Model confidence | medium: grammar is reliable, but models default to stiff "Anda", leak Malay words and keep English adjective order |
| Native review before shipping | recommended |

## Audience and register
- Players are Indonesian kids and teens. Write everyday standard Indonesian: correct spelling, short common words, relaxed tone. Not textbook, not street slang, no SMS shortcuts ("yg", "dgn", "gak").
- Address the player as "kamu" / "-mu". Roblox's own in-experience UI does this (about 270 "kamu" strings against 4 "Anda" in its Indonesian CoreScript file: "Kamu tidak memiliki cukup Robux"), and Indonesian gaming sites write to readers the same way. "Anda" (Microsoft, older Roblox help pages) reads like a bank or a teacher. Never mix the two in one game.
- Buttons are bare verbs or nouns: "Main", "Beli", "Klaim", "Jual", "Toko". Instructions use the plain imperative with no "silakan", "mohon" or "tolong" (Microsoft's Indonesian guide says to drop them): "Masukkan kode", not "Silakan masukkan kode".
- Prefer the short everyday form (Microsoft: "butuh" over "membutuhkan"): "Kamu butuh 50 koin lagi!", "Gabung komunitas kami", "dapat" over "memperoleh".
- Short questions need no "apakah": "Rebirth sekarang?", "Lanjutkan?".
- Hype sounds natural with "Keren!", "Mantap!", "Hore!", "Wah, hoki banget!"; calls to action with "Ayo" or "Yuk": "Ayo gabung!". One "!" per string: Roblox folds "Congratulations! You've earned X!" into "Selamat, kamu mendapat X!".
- Kid-safe: no "anjay", "anjir", "njir" (softened forms of the insult "anjing"), no "goblok", "bego". "Noob" only in jokey flavor text, never aimed at the player.
- For server-wide messages, "semua pemain" or "kalian" is fine: "Event dimulai, ayo semua ke lobi!".

## Roblox and gaming vocabulary
| English | id-id | note |
|---|---|---|
| Robux | Robux | invariable, capitalized: "100 Robux"; never "Robuks" |
| game pass | Gamepass | players and gaming sites write "Gamepass" as one word; roblox.com writes "pas" ("Tidak ada pas yang tersedia"), the AI-translated creator docs "pass" |
| developer product | produk | players never see the term; name the item. Creator docs: "produk pengembang" |
| experience / game | game | Roblox's platform UI says "pengalaman virtual"; inside a game kids say "game" (Roblox's own Indonesian also has "konten game", "Volume game") |
| obby / tycoon / simulator | obby / tycoon / simulator | keep; "simulator" is also the Indonesian spelling |
| rebirth | Rebirth | keep; Indonesian guides write "opsi Rebirth". "Kelahiran kembali" is literal and stiff |
| pet | pet | pet-game players keep "pet"; "hewan peliharaan" (Adopt Me's Indonesian page) is correct but long for UI |
| egg / hatch | telur / menetaskan | players also say "egg" and "nge-hatch"; "Telur Legendaris" in UI |
| coins / gems | koin / permata | many players keep "gems"; "koin", never "coins" |
| boost / multiplier | boost, bonus / pengali | Roblox: "Bonus 10%"; in names use "2x": "Koin 2x" |
| XP / level up | XP / naik level | "+50 XP"; "Naik level!" not "Level naik!" |
| quest | misi | "quest" kept only inside proper names |
| leaderboard | Papan Peringkat, Pemain Teratas | Roblox's own label is "Papan Peringkat"; "Teratas" is roblox.com's "Charts" |
| AFK / noob / OP | AFK / noob / OP | keep all three; never spell out |
| VIP / Premium | VIP / Premium | never translate |
| trade | tukar, bertukar | Adopt Me's Indonesian page: "tukar dan kumpulkan"; "trade" also common in chat |
| inventory / backpack | Inventaris / Tas Ransel | both are Roblox's own Indonesian labels; "tas" alone when short |
| daily reward | Hadiah Harian | "hadiah" (Roblox: "Hadiah ini tidak tersedia"); never "ganjaran", which is stiff and can also mean punishment |
| codes | kode | Roblox help writes "me-redeem kode"; in UI "Masukkan kode" is enough |
| group | komunitas | Roblox renamed groups to communities; its Indonesian UI says "Komunitas" ("Lambang Komunitas"). Some kids still say "grup" |
| like / favorite | like / Favorit | roblox.com shows "Favorit" ("Tambahkan ke Favorit"), the in-game inspect menu "Jadikan Favorit". The thumbs-up has no text label on roblox.com, so use the players' word "like"; "sukai" is the formal verb |
| server | server | "di server ini"; "pindah server" for server hopping |
| friends / connections | teman | Roblox's Indonesian UI shows "Teman" ("Undang Teman") and also "Koneksi" for the connections list ("Cari Koneksi"). In game text use "teman" |
| shop / buy | Toko / Beli | roblox.com's game page tab is "Toko" |
| free | gratis | Roblox: "secara GRATIS". Never "percuma": KBBI lists a "free" sense, but Indonesians read it as "in vain"; it is the Malay UI word |
| big spender | sultan | gamer slang for a player who spends a lot of Robux; fine in flavor text |

## Grammar traps in UI strings
- Plurals: Indonesian has one form, so "{count} Koin" is right for 0, 1 and 1.250. Never reduplicate after a number or a quantifier ("setiap", "semua", "banyak"): "5 pet-pet" -> "5 pet"; "setiap teman-teman" -> "setiap teman". Bare nouns are already generic: "Jual pet kamu". "para" only for people: "para pemain".
- Gender: none. "dia" covers everyone and verbs never agree, so "{player} bergabung ke game" works for any name. Avoid gendered address words ("Bang", "Kak", "Bro", "Sis").
- Modifiers follow the noun, so placeholder order flips: "{rarity} {pet}" -> "{pet} {rarity}" ("Naga Legendaris"); "Daily Reward" -> "Hadiah Harian"; "Lucky Potion" -> "Ramuan Hoki"; "Top Players" -> "Pemain Teratas".
- Possessives also follow: "your coins" -> "koinmu" or "koin kamu". Attach "-mu" to native nouns ("koinmu", "tasmu"); after English loans or a placeholder write "kamu" apart ("pet kamu"); hyphenate after an abbreviation ("VIP-mu"). Never "{pet}mu".
- No articles. Classifiers ("seekor", "sebuah") depend on the noun, so drop them before a placeholder: "Kamu dapat seekor {pet}" breaks when {pet} is a robot; write "Kamu dapat {pet}!".
- "di" and "ke" as prepositions stand apart ("di server", "ke toko", "di mana"); the passive prefix joins the verb ("dijual", "ditukar"). Indonesian affixes on English roots take a hyphen: "di-upgrade", "me-redeem" (Roblox's help writes "me-redeem"). Prefer a native verb when one exists: "ditingkatkan" over "di-upgrade".
- "menetas" is intransitive (the egg or the creature in it hatches), "menetaskan" transitive (you hatch it): "Telurnya menetas!", "Naga Legendaris menetas!", "Kamu menetaskan telur!". "Kamu menetas" means you came out of an egg.
- Capitalization: buttons, titles and product names in Title Case, except function words such as "dan", "di", "ke", "dari", "untuk", "yang" when not first (EYD rule for titles; Roblox: "Tambahkan Teman", "Beli Sekarang", "Ketuk untuk Bergerak"). Toasts and dialogs in sentence case: "Masukkan kode". Pet and item names stay capitalized mid-sentence.

## Typography and formatting
- Punctuation as in English: no space before ! ? : ; (Microsoft). No colon before a list of verbs: "Kamu bisa jual, tukar, dan simpan pet".
- Quotes: curly “...”, with ‘...’ inside a quote (both Microsoft's guide and CLDR). Straight "..." is an acceptable keyboard fallback; pick one style per game.
- Numbers: period for thousands, comma for decimals: "1.250 Koin", "boost 1,5x". An English "1,250" reads as "one point two five" here, so game code must format {count}, {amount} and {multiplier} for `id-id`. Percent has no space: "Bonus 10%".
- Durations (CLDR short units): hari "hr", jam "j", menit "mnt", detik "dtk" -> "3 j 20 mnt", "2 hr 5 j". Never ship English "3h 20m": "h" reads as "hari" (days). The compact "3j 20m" also appears in games (unverified as a norm).
- Clock time uses a period: "14.30"; short dates are day first: "8/11/26".
- Ellipsis: three periods, no space: "Memuat...".
- Keys: Indonesia uses the US QWERTY layout, so "E" stays "E": "Tekan E untuk membuka" (Roblox: "Tekan {KEY_NAME} untuk ..."). On touch prompts use "Ketuk", as Roblox does ("Ketuk untuk Bergerak", "Ketuk di sini untuk chat").

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, XP, noob, Gamepass, obby, tycoon, Rebirth.
- The game title "Pet Hatch Tycoon": keep English unless the developer supplies an Indonesian title (roblox.com shows dev-supplied ones, for example "Adopsi Saya!" for Adopt Me).
- Display names, usernames, promo codes ("FREEPETS"), keybinds, number formats inside codes.
- "event", "item", "server", "level", "like" are everyday words for Indonesian players: keep them; don't force "acara", "barang", "peladen", "tingkat".
- Spelling is Indonesian only: "uang" not "wang", "karena" not "kerana", "coba" not "cuba", "kedaluwarsa" not "kadaluarsa".

## Rendering on Roblox
- Indonesian needs only basic Latin letters, digits and ASCII punctuation, which every Roblox font (Builder Sans, Gotham, Source Sans and the decorative fonts) includes. No shaping, no diacritics, nothing to clip.
- The real risk is length. Long affixed words cannot break: "kedaluwarsa", "menetaskan", "Pengalaman Virtual" in a narrow button either overflow or make TextScaled shrink the whole label. Give labels AutomaticSize or slack.
- Test in Studio with the Indonesian test locale: "Kode tidak valid atau sudah kedaluwarsa." and "Pemain Teratas" at the smallest phone width, plus every toast with a long {player} name.

## Mistakes machine translation makes here
1. Stiff register: "Apakah Anda ingin melakukan rebirth sekarang?" -> "Rebirth sekarang?"; "Silakan masukkan kode" -> "Masukkan kode".
2. Malay leakage: "percuma" -> "gratis", "kedai" -> "toko", "tetapan" -> "pengaturan", "kemas kini" -> "pembaruan", "boleh" for "can" -> "bisa" ("boleh" means "may" here), "pasukan" (troops in Indonesian) -> "tim", "butang" -> "tombol", "ganjaran" -> "hadiah", "sila" -> drop it.
3. English adjective order: "Legendaris Naga" -> "Naga Legendaris"; "Harian Hadiah" -> "Hadiah Harian".
4. Reduplicated plurals: "100 koin-koin" -> "100 koin"; "Jual pet-pet kamu" -> "Jual pet kamu".
5. Literal gaming terms: "Kelahiran Kembali" -> "Rebirth"; "Jauh dari keyboard" -> "AFK"; "Terlalu kuat" in hype text -> "OP banget".
6. Wrong verb: "Kamu menetas Naga" -> "Kamu menetaskan Naga"; "Level naik!" -> "Naik level!".
7. Misspellings models copy from the web: "kadaluarsa" -> "kedaluwarsa", "di jual" -> "dijual", "dimana" -> "di mana", "aktifitas" -> "aktivitas", "resiko" -> "risiko".
8. Ambiguous price button: "Beli 100 Robux" reads as buying Robux -> "Beli: 100 Robux".
9. English duration and number formats left in place: "3h 20m" -> "3 j 20 mnt"; "1.5x" -> "1,5x".
10. Mixed address: "Koinmu habis, Anda perlu..." -> "Koinmu habis, kamu perlu..."; never "lo/gue" either.

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Main | roblox.com's page title uses "Mainkan"; "Main" is the in-game norm |
| shop.title | Toko | |
| shop.buy | Beli | |
| reward.claim | Klaim | "Ambil" also works |
| rebirth.button | Rebirth | kept as players say it |
| rebirth.confirm | Rebirth sekarang? Koinmu akan hilang, tapi kamu dapat boost {multiplier}x permanen. | |
| coins.need_more | Kamu butuh {amount} koin lagi! | correct for any {amount}, including 1 |
| coins.count | {count} Koin | no plural form needed |
| egg.hatched | {pet} {rarity} menetas! | "The Legendary Dragon hatched!"; order flipped; 36 at max name lengths. The literal "Kamu menetaskan {pet} {rarity}!" reaches 44 |
| rarity.legendary | Legendaris | |
| pet.name.dragon | Naga | |
| chat.player_joined | {player} bergabung ke game | |
| trade.request | {player} ingin bertukar denganmu | |
| prompt.open_shop | Tekan E untuk membuka | 21 of 22 |
| pass.buy_price | Beli: {price} Robux | colon stops it reading as "buy N Robux"; "Beli seharga {price} Robux" fits only 3-digit prices |
| pass.coins2x | Koin 2x | noun first, like every Indonesian modifier; "Koin 2x Lipat" (13) and "Koin Ganda" also natural (gaming sites write "XP ganda"); avoid English-order "2x Koin" |
| pass.vip | VIP | kept: players use the English abbreviation |
| reward.daily_title | Hadiah Harian | Title Case |
| reward.come_back | Kembali dalam {time} untuk hadiah berikutnya! | {time} must use Indonesian units |
| codes.placeholder | Masukkan kode | |
| codes.invalid | Kode tidak valid atau sudah kedaluwarsa. | Roblox's spelling "kedaluwarsa" |
| social.like_reward | Like game ini dan dapatkan <b>Ramuan Hoki</b> gratis! | "hoki" (KBBI-listed loan, "luck") is the everyday word; "Ramuan Keberuntungan" fits at exactly 55. If the game keeps English item names, write "Lucky Potion" everywhere |
| social.group_reward | Gabung komunitas kami untuk membuka hadiah gratis! | "komunitas" per Roblox's rename |
| afk.warning | Kamu AFK. Bergerak agar terus dapat koin! | "earning" made concrete as coins |
| leaderboard.title | Pemain Teratas | |
| level.up | Naik level! Sekarang kamu level {level}. | |
| tutorial.sell | Masuk ke lingkaran bercahaya untuk menjual pet kamu. | "kamu" apart after the loan "pet" |
| inventory.full | Tas ranselmu penuh! Jual pet agar ada tempat lagi. | Roblox's "Tas Ransel" |
| settings.music | Musik | |
| settings.on | Nyala | Roblox's own toggle word; exactly 5 |
| loading | Memuat... | Roblox's CoreScripts keep "Loading..."; "Memuat..." is the standard UI word |
| event.ends_in | Event usai dalam {time} | "Event berakhir dalam {time}" fits only if {time} is 7 characters or less |
| item.op | Pedang ini OP banget! | "banget" is casual but kid-normal; keep it to flavor and hype text, not system messages. "sangat OP" sounds like a textbook |
| friends.boost | Bonus +{percent}% untuk setiap teman di server ini | "your server" = the server you are in; avoids "server-mu" |

## Sources
1. Microsoft Indonesian Localization Style Guide: https://download.microsoft.com/download/c/2/8/c2804555-f6ed-4db9-9e3b-ddf754159bd3/ind-idn-StyleGuide.pdf
2. Unicode CLDR language plural rules chart: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON, Indonesian units, numbers, quotation marks and date/time formats: https://github.com/unicode-org/cldr-json/tree/main/cldr-json (main/id: units.json, numbers.json, delimiters.json, ca-gregorian.json)
4. Roblox client CoreScript translations, id column (ExtraContent/translations/CoreScriptLocalization.csv, Roblox build of 2026-11-05): local file from the Roblox install
5. Roblox Help (id), account safety (older "Anda" style): https://en.help.roblox.com/hc/id/articles/203313380-Menjaga-Keamanan-Akun-Anda
6. Roblox Help (id), redeeming gift cards ("kamu", "me-redeem"): https://en.help.roblox.com/hc/id/articles/115005566223-Cara-me-redeem-dan-menggunakan-Gift-Card
7. roblox.com game page in Indonesian, Adopt Me ("Favorit", "Toko", "Teratas", "pas", "pengalaman virtual", "hewan peliharaan"): https://www.roblox.com/id/games/920587237/Adopt-Me
8. Roblox Creator docs (id-id, AI-translated), Passes: https://create.roblox.com/docs/id-id/production/monetization/passes
9. EYD V, capital letters (titles, "Anda"): https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-huruf/huruf-kapital/
10. Duniagames, Pet Simulator 99 rank-up guide (kept English terms, "kamu"): https://duniagames.co.id/amp/discover/article/rank-up-cepat-pet-simulator-99-roblox/en
11. Duniagames, what a Roblox Gamepass is ("Gamepass", "XP ganda"): https://duniagames.co.id/amp/discover/article/apa-itu-gamepass-roblox-ini-fungsi-dan-cara-membuatnya
12. IDN Times Duniaku, Roblox for beginners ("teman", "koneksi", "komunitas", "item"): https://duniaku.idntimes.com/game/mobile/cara-bermain-roblox-untuk-pemula-v3z02-00-b8vrp-xxl3b0
13. KBBI entries "hoki", "percuma", "ganjaran": https://kbbi.kemendikdasmen.go.id/entri/hoki (same path for the others)
14. EYD V, hyphen with affixes on foreign words ("mem-back up"): https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-tanda-baca/tanda-hubung/
