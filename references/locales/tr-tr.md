# Turkish (tr-tr) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `tr-tr` (bare language column `tr` also fine: Turkish has one standard variant, so `tr` catches Turkish players in any region) |
| Script, direction | Latin plus ç ğ ı İ ö ş ü, LTR |
| Address the player as | informal singular "sen" everywhere; never "siz", never the polite "-iniz" forms ("giriniz") |
| Text expansion vs English | +10-30%: the reference set below runs +9% for sentences, +14% for short labels; fewer but longer words, and a short button can double ("Buy" -> "Satın Al") |
| Plural categories (CLDR) | one, other, but a noun after a number is always singular, so one string fits every count |
| Model confidence | medium: grammar is well covered; the risks are suffixes after {params}, i/İ casing, number formats and unconfirmed player slang (rebirth, pet, coin) |
| Native review before shipping | recommended |

## Audience and register
- Platform status: Roblox has been blocked in Turkey by court order since 2024-08-07 (child-safety grounds). Roblox registered a Turkish company on 2025-05-13, but Turkish Wikipedia, revised 2026-10-31, still says access is blocked; no report of a lift was found. Players in Turkey reach it through VPNs, and Turkish-speaking kids also play from Germany, the Netherlands, Austria and Northern Cyprus: write neutral standard Turkish, no lira prices or Turkey-only holidays.
- Use "sen" in every string. Microsoft's Turkish guide defaults to "siz" for software but allows "sen" for a younger audience and calls to action. Roblox's in-game Turkish UI uses sen throughout ("Bu deneyime katılmak için iznin yok", "Lütfen daha sonra tekrar dene"), as do roblox.com/tr buttons ("Şimdi Katıl", "Favorile"); only its newsroom uses siz.
- Never mix: "Satın al, hemen kazan!", not "Satın alın, hemen kazanırsın!".
- Buttons, tabs, toggles: sen-imperative or a noun, as in Roblox's Turkish UI ("Satın Al", "Arkadaş Ekle", "Envanter"): "Oyna", "Topla", "Mağaza". Not infinitives ("Oynamak") and not polite forms ("Oynayınız"), which read like a government form.
- Simple tenses and short verbs (Microsoft): "Seviye atladın!" not "Seviye atlamış bulunmaktasın".
- Natural hype: "Harika!", "Süper!", "Yaşasın!", "Kaçırma!", "Hemen dene!". Microsoft notes Turkish uses "!" less than English: keep it on rewards and toasts, drop it from neutral labels and instructions.
- Stiff or adult: "işbu", "gerçekleştiriniz", "Lütfen ... ediniz", "Maalesef" on every error. Don't blame the player: "Bu kod çalışmadı" rather than "Yanlış kod girdiniz".
- Kid-safe slang is fine in flavor text ("çok OP", "kasmak" for grinding); no insults ("salak", "ezik"), nothing crude.

## Roblox and gaming vocabulary
| English | Turkish | note |
|---|---|---|
| Robux | Robux | Latin, as Roblox writes it; suffix after an apostrophe: "100 Robux'a", "Robux'ın" (see grammar traps). |
| Premium | Premium | Roblox's in-game UI keeps it: "Premium'a Özel", "Roblox Premium". |
| game pass | gamepass; geçiş | Roblox's AI-translated creator docs say "Geçiş"; players say "gamepass" (unverified). In the shop, show the pass name. |
| developer product | geliştirici ürünü | players never see the term; name the item. |
| experience / game | oyun | Roblox's in-game menus say "deneyim" ("Deneyime Dön"); a game's own text says "oyun". Never "tecrübe". |
| obby | obby; parkur | "parkur" in descriptions (unverified which kids prefer). |
| tycoon | tycoon | kept in English in titles (unverified); "işletme oyunu" if it must be explained. |
| simulator | simülatör | as on roblox.com/tr. |
| rebirth | rebirth; yeniden doğuş | "Yeniden Doğuş" is 13 chars; kids say "rebirth yapmak/atmak" (unverified). One term per game. |
| pet | evcil hayvan; pet | "evcil hayvan" in sentences; "pet" (plural "petler") in tight labels and chat (unverified). |
| egg / hatch | yumurta; yumurta açmak, yumurtadan çıkmak | button "Aç"; toast "Yumurtadan Ejderha çıktı!". |
| coins | altın | "coin" common in chat (unverified); never "madeni para" (sounds like a bank). |
| gems | elmas | standard in Turkish mobile games (unverified). |
| boost | bonus; güçlendirme | "boost" also said by players (unverified). |
| multiplier | çarpan; "2x" | "2x Altın"; in prose "2 kat". |
| XP | XP; deneyim puanı | "+50 XP"; pick one per game. |
| level up | seviye atlamak | "Seviye atladın!"; "level atladım" is chat only. |
| quest | görev | Roblox's Turkish event posts. |
| leaderboard | liderlik tablosu | Roblox's in-game player list and newsroom say "Liderlik Tablosu"; "En İyiler" is Roblox's charts tab. |
| AFK | AFK | Latin; "AFK kaldın" avoids a suffix. |
| noob | acemi; noob | "noob" only in jokes. |
| OP | OP; aşırı güçlü | "çok OP" in flavor text (unverified how widespread). |
| VIP | VIP | "VIP sunucu", "VIP oda". |
| trade | takas; takas yapmak | Roblox's own word ("Takas"); "trade" in chat. |
| inventory / backpack | envanter / çanta | Roblox: "Envanter", "Sırt Çantası"; plain "çanta" fits tight toasts. |
| daily reward | günlük ödül | "ödül" is Roblox's word. |
| codes | kodlar; kodu kullan | redeem button "Kullan"; placeholder "Kodu gir". |
| group | grup | "Grubumuza katıl" (p -> b before a vowel). |
| like / favorite | beğen / favorile | "Favorile" is Roblox's button on web and in game; its thumbs-up label unverified. |
| server | sunucu | "Sunucular" tab on roblox.com/tr; private server "özel sunucu" (Roblox's in-game wording). |
| friends | arkadaşlar | Roblox renamed Connections back to "Arkadaşlar" in April 2026; in-game buttons "Arkadaş Ekle". Never the old "Bağlantılar" or "Etkileşim Ağı". |
| event | etkinlik | Roblox's Turkish newsroom; "event" in chat. |
| item | eşya; öğe | Roblox uses "öğe" for avatar items; "eşya" sounds more natural for game loot. |

## Grammar traps in UI strings
- Vowel harmony: suffixes copy the last vowel of the word before them. Two-way a/e: "oyunda", "seviyede". Four-way ı/i/u/ü: "oyunun", "evin", "Roblox'un", "Jailbreak'in". An initial d/c turns t/ç after ç f h k p s ş t: "Roblox'ta", not "Roblox'da".
- A {param}'s value is unknown, so no suffix can be chosen. Microsoft: no suffixes on unknown placeholder content. "{player}'a" fits "Ali" but not "Ece" (Ece'ye) or "Mert" (Mert'e). Keep the placeholder bare:
  - as the subject: "{player} oyuna katıldı", "{player} seninle takas yapmak istiyor";
  - after a colon: "Takas isteği gönderildi: {player}", "Kazanan: {player}";
  - behind a fixed noun that carries the suffix: "{player} adlı oyuncuya hediye gönder" (Roblox's own UI: "{RBX_NAME} adlı kullanıcıyı ...", "{RBX_NAME} öğesini ...").
  - Never the hack "{player}'(y)a" in player-facing text.
- Numbers too: the suffix follows the spoken number ("6'ya" altı, "7'ye" yedi, "10'a" on, "100'e" yüz). Never "{level}'e"; use the ordinal period and suffix a fixed noun: "{level}. seviyeye ulaştın", or "Seviye {level}". TDK: "15." or "15'inci", never "15.'inci".
- Translated words inserted at runtime ({rarity}, {pet}) are unknown too: keep them in the nominative. Good: "Yumurtadan {rarity} {pet} çıktı!" (subject). Bad: "{rarity} {pet}'i çıkardın!".
- Proper names and fixed English words take an apostrophe before inflectional suffixes, chosen by pronunciation, not spelling. Roblox's own Turkish: "Roblox'ta", "Jailbreak'in", "Hub'a", "Family Zone'u", "Year Infinity'yi". Game title: "Pet Hatch Tycoon'da" (taykun). Plural and derivational suffixes take no apostrophe (TDK: "Ahmetler", "Türkçe").
- Robux: Roblox's in-game Turkish writes "Robux'a", "ROBUX'tan" and back-unrounded forms "Robux'ın" ("yeterli Robux'ın yok"), never "Robux'un". So the accusative is "Robux'ı". "Roblox" takes "Roblox'un", "Roblox'u".
- Letters and abbreviations are inflected as spoken letters (Microsoft: "SMTP'ye", "API'si"): "E'ye bas", "F'ye bas". Always safe: "E tuşuna bas" (the suffix sits on "tuş").
- Plurals: the noun after a number stays singular: "1 altın", "5 altın", "{count} Altın". Bad: "{count} altınlar", "5 petler".
- No grammatical gender; "o" is he and she. {player} needs no agreement, and adjectives never agree: "Efsanevi Ejderha", "Efsanevi Kedi".
- Word order: verb last; move placeholders freely, keep each exactly once: "{player} seninle takas yapmak istiyor". No articles: drop "a/the"; "bir" only when it means "one".
- The question particle mı/mi/mu/mü is a separate word and harmonizes: "Emin misin?", "Hazır mısın?". "de/da" meaning "too" is separate ("Sen de katıl!"); the locative is attached ("sunucuda").
- Possessive "your" usually becomes a suffix, not a word: "Çantan dolu!" (not "Senin çantan dolu!").
- Noun + noun compounds add -(s)I to the head: "Altın Bonusu", "Pet Deposu"; adjective + noun takes none: "Günlük Ödül".
- Capitalization: Roblox's Turkish UI capitalizes each word in buttons and titles ("Satın Alım Tamamlandı", "Pazar Yeri", "Şimdi Katıl"); follow it there, sentence case for sentences. After a colon, a fragment starts lowercase (Microsoft).

## Typography and formatting
- No space before ! ? : ; and one space after.
- Quotation marks: straight "..." in UI strings (Microsoft); don't mix with curly ones in one game.
- Em dash: Microsoft says Turkish doesn't use it; rewrite with a comma, colon or parentheses. Ranges and minus take no spaces: "3-5", "-5".
- Numbers (TDK): period for thousands, comma for decimals: "1.250", "1,5". A {count} preformatted as "1,250" reads as 1.25, and multiplier "1.5" should be "1,5"; flag both to the developer.
- Percent: the sign goes before the number, no space (TDK, Microsoft): "%10", "+%25 bonus". Never "10%".
- Multiplier: keep the source shape "2x Altın"; "2 kat" in prose.
- Durations: CLDR short forms are "gün", "sa.", "dk.", "sn." (Microsoft: "25 dk."); compact timers drop the periods: "3sa 20dk", "2g 5sa" (g for gün; game usage unverified). If code outputs "3h 20m", flag it: "h" and "m" mean nothing in Turkish.
- Ellipsis: three periods, no space before (Microsoft): "Yükleniyor...".
- Keys stay Latin capitals: "E'ye bas", "Shift'e bas" or "E tuşuna bas".
- Never drop Turkish letters: "Mağaza", "Satın Al", not "Magaza", "Satin Al". Kids type ASCII in chat, but it looks broken in a polished UI.
- Casing: i <-> İ and ı <-> I. Hand-type all-caps titles: "GÜNLÜK ÖDÜL", "İKSİR DÜKKANI", never "IKSIR".
- Agglutination makes long single words ("arkadaşlarınla", "satamıyorsun"); Roblox doesn't hyphenate, so enable TextWrapped. No abbreviations in titles (Microsoft).

## Do not translate / keep as is
- Robux, Roblox, Premium, VIP, Roblox Studio: Latin; suffixes after an apostrophe ("Roblox'ta").
- Game titles ("Pet Hatch Tycoon"): keep in English; players search the English title.
- Usernames and display names: never translate, transliterate or suffix.
- Promo codes ("FREEPETS"): exactly as given, same case; translate only the text around them.
- Key names (E, Q, Shift) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Şans İksiri"). Whether a capitalized item name takes an apostrophe ("Şans İksiri'ni" or "Şans İksirini") is unsettled, so keep it bare: "Şans İksiri kazan".
- Keep established gamer loanwords (OP, AFK, XP, VIP, obby); don't invent transliterations ("lakki poşın").

## Rendering on Roblox
- Turkish adds six letters (ç ğ ı ö ş ü) plus dotted capital İ. ç ö ü are Latin-1; ğ ı İ ş Ğ Ş are Latin Extended-A, the first to go missing in a decorative font.
- Checked 2026-11-08 in the font files Roblox ships (content/fonts): Builder Sans, Source Sans Pro, Montserrat, Luckiest Guy and Bangers have all 12 Turkish letters. Fredoka One, Creepster, Denk One, Permanent Marker, Balthazar and Accanthis ADF lack ğ Ğ İ ş Ş; Comic Neue Angular lacks ğ Ğ ı İ; Highway Gothic and Roman Antique lack ğ Ğ ı İ ş Ş. Avoid those for Turkish; what Roblox draws instead is unverified.
- Luckiest Guy and Bangers draw lowercase i as a dotless capital, identical to ı: "çiftlik" shows as "ÇIFTLIK", which reads "çıftlık". In these caps fonts write the string in capitals yourself: "ÇİFTLİK".
- İ and Ğ rise above cap height (in Luckiest Guy about 30% taller than I) and Ş Ç hang below the baseline: give TextScaled boxes headroom.
- Code: tested in Studio 2026-11-08: string.upper("iksir") gives "IKSIR" (should be "İKSİR"), ç ğ ı ö ş ü stay lowercase, and string.lower turns "I" into "i", not "ı". Store caps text in the table as written; never auto-case Turkish.
- Verify in Studio: Player Emulator set to Turkish; paste "Pijamalı hasta yağız şoföre çabucak güvendi." and "PİJAMALI HASTA YAĞIZ ŞOFÖRE ÇABUCAK GÜVENDİ." into every font face used; open the panels with the longest strings.

## Mistakes machine translation makes here
- Suffix glued to a placeholder: "{player}'a hediye gönder" -> "{player} adlı oyuncuya hediye gönder".
- Suffix on a number placeholder: "{level}'e ulaştın" -> "{level}. seviyeye ulaştın".
- Plural after a count: "{count} altınlar" -> "{count} altın".
- Register mix: "Hareket edin, kazanmaya devam et!" -> "Hareket et, kazanmaya devam et!".
- Polite form: "Lütfen kodu giriniz" -> "Kodu gir".
- Wrong i casing: "IKSIR", "Ipucu" -> "İKSİR", "İpucu".
- ASCII letters: "Satin Al", "Magaza" -> "Satın Al", "Mağaza".
- Joined question particle: "Eminmisin?" -> "Emin misin?".
- "Claim" as "Talep Et" (a legal claim) -> "Topla" or "Al".
- "Redeem" as "Telafi Et" -> "Kullan".
- "Level up!" as "Seviye yükselt!" (an order) -> "Seviye atladın!".
- English number formats: "1,250 Altın", "10% bonus" -> "1.250 Altın", "%10 bonus".
- Em dash copied: "Bu kılıç — OP!" -> "Bu kılıç çok OP!".
- "experience" as "deneyim" in game copy: "En iyi Roblox deneyimi" -> "Roblox'taki en iyi oyun".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Oyna | sen-imperative |
| shop.title | Mağaza | Roblox's own Store label |
| shop.buy | Satın Al | 8/8; "Al" if a font runs wide |
| reward.claim | Topla | "Ödülü Al" (8) also fine; never "Talep Et" |
| rebirth.button | Rebirth | "Yeniden Doğuş" is 13 > max 10; players' word (unverified) |
| rebirth.confirm | Şimdi rebirth yapmak ister misin? Altınlarını kaybedersin ama kalıcı {multiplier}x bonus kazanırsın. | multiplier must arrive as "1,5", not "1.5" |
| coins.need_more | {amount} altın daha lazım! | singular noun works for 1 |
| coins.count | {count} Altın | "1,250" must be "1.250" (code issue) |
| egg.hatched | Yumurtadan {rarity} {pet} çıktı! | params stay nominative, no suffix |
| rarity.legendary | Efsanevi | |
| pet.name.dragon | Ejderha | |
| chat.player_joined | {player} oyuna katıldı | no gender, no suffix on the name |
| trade.request | {player} seninle takas yapmak istiyor | |
| prompt.open_shop | Açmak için E'ye bas | 19/22; "E tuşuna bas" is the safe pattern for any key |
| pass.buy_price | {price} Robux'a Satın Al | price in the dative, as Roblox writes "ROBUX'a"; 22/22 with a 5-character price, "{price} Robux'a Al" if longer |
| pass.coins2x | 2x Altın | |
| pass.vip | VIP | |
| reward.daily_title | Günlük Ödül | |
| reward.come_back | Sonraki ödülün için {time} sonra tekrar gel! | needs "3sa 20dk", not "3h 20m" |
| codes.placeholder | Kodu gir | |
| codes.invalid | Bu kod geçersiz ya da süresi dolmuş. | |
| social.like_reward | Oyunu beğen, ücretsiz <b>Şans İksiri</b> kazan! | item kept bare, no suffix |
| social.group_reward | Grubumuza katıl, ücretsiz ödül kazan! | "kilidini aç" (unlock) is a clunkier calque |
| afk.warning | AFK kaldın. Hareket et, kazanmaya devam et! | "AFK kaldın" avoids a suffix on AFK; "devam et" keeps "keep earning" |
| leaderboard.title | En İyi Oyuncular | 16/16; Roblox's "Liderlik Tablosu" is 17; fallback "Liderler" |
| level.up | Seviye atladın! Artık {level}. seviyedesin. | ordinal period; suffix on "seviye", not the number |
| tutorial.sell | Evcil hayvanlarını satmak için parlayan çembere gir. | |
| inventory.full | Çantan dolu! Yer açmak için evcil hayvan sat. | "your" becomes the suffix -n |
| settings.music | Müzik | |
| settings.on | Açık | its pair "Kapalı" is 6 chars; check the toggle width |
| loading | Yükleniyor... | three periods (Microsoft) |
| event.ends_in | Etkinlik bitiyor: {time} | needs "2g 5sa"; alt "Kalan süre: {time}" |
| item.op | Bu kılıç çok OP! | "aşırı güçlü" in formal copy |
| friends.boost | Sunucundaki her arkadaşın için +%{percent} bonus | percent sign before the number |

## Sources
1. Microsoft Turkish localization style guide (PDF, via https://aka.ms/turkish-styleguide): https://download.microsoft.com/download/c/7/e/c7e1f405-1a5a-418d-a56d-3a8c183cabd9/tur-tur-StyleGuide.pdf
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. TDK, apostrophe rules (kesme işareti): https://www.tdk.gov.tr/icerik/yazim-kurallari/kesme-isareti/
4. TDK, writing numbers (sayıların yazılışı): https://www.tdk.gov.tr/icerik/yazim-kurallari/sayilarin-yazilisi/
5. Roblox newsroom, Turkish, "Arkadaşlar Geri Döndü" (Connections -> Friends): https://about.roblox.com/tr/newsroom/2026/04/expanding-trusted-friends
6. Roblox newsroom, Turkish, "Av'a Katıl: Roblox 20" (görev, liderlik tablosu, apostrophe suffixes): https://about.roblox.com/tr/newsroom/2026/09/join-the-hunt-roblox-20
7. Roblox newsroom, Turkish, The Hollow event (etkinlik, ödül, öğe/eşya): https://about.roblox.com/tr/newsroom/2026/10/the-hollow-halloween-survival-event
8. roblox.com Turkish game page (Favorile, Mağaza, Sunucular, deneyim): https://www.roblox.com/tr/games/12127610294/Boxed-Evolution
9. roblox.com Turkish simulator spotlight (simülatör, arkadaşlarınla): https://www.roblox.com/tr/spotlight/simulation
10. Roblox creator docs tr-tr, Geçişler (AI-translated; Geçiş, Geliştirici ürünleri): https://create.roblox.com/docs/tr-tr/production/monetization/game-passes
11. Turkish Wikipedia, Roblox (2024 access block, still in force at the 2026-10-31 revision; Turkish company): https://tr.wikipedia.org/wiki/Roblox
12. Roblox in-game UI strings with the tr column (Robux'ın, Takas, özel sunucu, Arkadaş Ekle, Sırt Çantası, sen address), mirrored from the client: https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/translations/CoreScriptLocalization.csv
13. Roblox client fonts, content/fonts in the Roblox install, cmaps and glyph outlines read with fontTools on 2026-11-08 (no URL)
14. Luau string library source (toupper/tolower per byte), confirmed by a Studio test 2026-11-08: https://github.com/luau-lang/luau/blob/master/VM/src/lstrlib.cpp
15. CLDR Turkish unit abbreviations (gün, sa., dk., sn.): https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-units-full/main/tr/units.json
