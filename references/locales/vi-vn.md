# Vietnamese (vi-vn) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `vi-vn` (Roblox's only Vietnamese locale; no bare `vi` column needed. Roblox's own client table names its column `vi`, but games use `vi-vn`) |
| Script, direction | Latin with tone marks (chữ Quốc ngữ), LTR |
| Address the player as | "bạn", often dropped ("Cần thêm 50 xu!"); never "mày", "ngươi", "quý khách" |
| Text expansion vs English | about +5-15% in characters (+7% on the reference set, +10% on its sentences); one-word labels can double ("Shop" -> "Cửa hàng"); stacked tone marks also make lines taller |
| Plural categories (CLDR) | CLDR 49 and later: one (i = 0 or n = 1), other; CLDR 48 and earlier: other only. Ordinals: one ("thứ nhất"), other. Nouns never inflect, so neither split changes a Roblox string |
| Model confidence | medium -- solid general Vietnamese, but tone-mark slips, stiff Sino-Vietnamese register and gamer vocabulary are frequent misses |
| Native review before shipping | strongly recommended -- one wrong tone mark silently changes the word ("Mua" buy, "Múa" dance, "Mưa" rain) |

## Audience and register
Vietnamese players are mostly teens on Roblox VNG, the local edition VNGGames has published since 13 August 2024. It has a 12+ age limit, and Vietnamese Wikipedia reports roblox.com blocked in Vietnam since May 2026. Overseas Vietnamese on the global client read the same column. "Roblox UI" below means the global client's vi strings; whether VNG shows the same wording is (unverified). Write like a cheerful Vietnamese mobile game talking to a 12-year-old: short, warm, a little hyped.
- Pronoun: "bạn", as in Roblox's own Vietnamese UI ("Bạn có muốn...", "Bạn đã mua ... thành công!"). Drop it when clear: "Cần thêm {amount} xu!" "Cậu" reads cute and peer-to-peer, so use it only in a deliberately cute game. "Mày/tao" is rude, "ngươi" archaic or villainous, "quý khách/quý vị" a shop counter.
- The game talking about itself: "chúng mình" (friendly), not corporate "chúng tôi". "Tụi mình" reads Southern-casual.
- Buttons: bare verb, no "Hãy": "Chơi", "Mua", "Nhận", "Bán hết". In sentences an imperative may take "Hãy" ("Hãy bán bớt thú cưng") or end with "nhé" for warmth ("Quay lại sau nhé!"). Southern "nha" is common in chat but less neutral than "nhé".
- "Vui lòng" (please) belongs to errors, where Roblox uses it ("Vui lòng thử lại sau"). Never use it in hype lines.
- Hype that sounds native: "Chúc mừng!", "Tuyệt vời!", "Đỉnh quá!", "Lên cấp!", "Siêu hiếm!". One exclamation mark.
- Reads stiff or adult: "Xin vui lòng", "Tiến hành tái sinh", "Thực hiện giao dịch", "Tải về không thành công". Use the modern voice Microsoft asks for: short everyday words, "Không tải được", "Tái sinh ngay".
- Standard (Northern) spelling and neutral words, per Microsoft: "Gửi" not "Gởi", "Chọn" not "Lựa". If a fandom already has a fixed term, follow it, even a Southern one like "trái ác quỷ".

## Roblox and gaming vocabulary
| English | Vietnamese | Note |
|---|---|---|
| Robux | Robux | Invariable, capital R: "100 Robux". Roblox UI: "Mua Robux", "Không đủ Robux" |
| Premium | Premium / gói Premium | Roblox UI: "Gói Roblox Premium", "thành viên Premium". VNG users reportedly cannot buy Premium |
| game pass | gamepass / vé | Roblox's purchase UI calls a pass "Vé"; the AI-translated Creator docs say "Thẻ"; players say "gamepass". In game text, name the pass itself |
| developer product | vật phẩm | Creator docs: "Sản phẩm của nhà phát triển"; in game, name the item |
| experience / game | trò chơi / game | Roblox UI: "trải nghiệm"; players and Vietnamese press say "game", "tựa game" |
| obby, tycoon, simulator | obby, tycoon, simulator | Kept in game titles; in prose "game vượt chướng ngại vật" (unverified) |
| rebirth | Tái sinh | Short, clear. "Chuyển sinh" (common in Chinese-origin MMOs) and English "rebirth" also seen (unverified) |
| pet | thú cưng / pet | Vietnamese code guides use both ("thú cưng", "nhận Pet"); pick one per game |
| egg / hatch | trứng / ấp, mở trứng | Guides say "mở 99 quả trứng"; "nở" is intransitive (the egg hatches): "Trứng nở rồi!" |
| coins | xu | "{count} xu"; "tiền" = money in general, "vàng" = gold |
| gems | đá quý / kim cương | Match the icon: "kim cương" for a diamond, "đá quý" for a colored gem, "ngọc" for a round jewel or orb. One term per game; which players expect for plain "gems" is (unverified) |
| boost | tăng / thưởng / buff | Roblox UI: "Tiền thưởng 10%" for "10% bonus"; "buff" is gamer slang |
| multiplier | x2 (before the noun) | Vietnamese guides write "x2 EXP", "x2 tiền Beli"; "hệ số nhân" in full sentences |
| XP | EXP / kinh nghiệm | "x2 EXP, kinh nghiệm" in Blox Fruits guides |
| level up | lên cấp | "cấp" / "cấp độ" in UI; players also write "level" |
| quest | nhiệm vụ | "Nhiệm vụ hằng ngày" |
| leaderboard | bảng xếp hạng | Roblox UI: "Bảng Xếp Hạng"; "Top" is common in titles |
| AFK | AFK | Kept; Vietnamese articles gloss it, nobody translates it |
| noob | noob / gà | Teasing slang ("gà" = weak player, unverified); keep it out of system text |
| OP | bá đạo / OP | "bá đạo" is current gamer slang, used by GameK about Roblox games, and kid-safe. "imba" is MOBA slang, less known to young players (unverified) |
| VIP | VIP | Never translated |
| trade | giao dịch / trade | The usual name of a player-to-player trade system in Vietnamese games; Sforum's Pet Simulator 99 guide says "Giao dịch thú cưng". Roblox's purchase strings always say "giao dịch mua", so no clash. Avoid "trao đổi với bạn": it also reads "have a word with you" |
| inventory / backpack | kho đồ / ba lô | Roblox UI: "Kho Đồ", "Balo"; "ba lô" is the dictionary spelling |
| daily reward | quà hằng ngày | "Điểm danh" (check-in) is the usual mobile-game label for login streaks (unverified) |
| codes | code / mã | Players: "nhập code", "giftcode", "code đã hết hạn" |
| group | cộng đồng | Roblox renamed Groups to Communities; Vietnamese client: "Phù Hiệu Cộng Đồng". Players still say "group" |
| like / favorite | like (thích) / yêu thích | Roblox UI: "Yêu Thích", "thêm ... vào mục yêu thích". The client strings have no "Like" label (the game page shows a thumbs-up icon); the Roblox VNG label is (unverified) |
| server | máy chủ / server | Roblox UI: "Máy chủ đã đầy"; players write "server" |
| friends / connections | bạn bè | Roblox's client now says "Người quen" for connections ("Tìm Người quen"), but that means "acquaintance"; in game text say "bạn bè" / "người bạn" |
| badge | huy hiệu | Roblox UI: "Huy Hiệu" |

## Grammar traps in UI strings
- **Plurals with {count}.** Nouns never change: "{count} xu" is correct for 0, 1 and 1.250. Never add "những/các" to a counted noun ("5 những xu" is wrong). One string serves every number, whatever CLDR version a tool reports.
- **Classifiers.** Counting needs a classifier that depends on the noun: "1 con rồng", "2 thanh kiếm", "3 quả trứng". With an inserted {pet} or {item}, drop number and classifier: "Bạn nhận được {item}!", not "Bạn nhận được một con {item}" (wrong for a sword).
- **Word order.** Modifiers follow the noun, so "{rarity} {pet}" becomes "{pet} {rarity}": "Rồng Huyền Thoại". Compounds invert: "Lucky Potion" -> "Thuốc May Mắn", "Pet Shop" -> "Cửa hàng thú cưng", "Daily Reward" -> "Quà hằng ngày".
- **Gender of {player}.** Verbs and adjectives never change for gender: "{player} đã tham gia trò chơi" is safe. Only pronouns are gendered (anh ấy, cô ấy), so never refer back to {player} with one; repeat the name or restructure.
- **Possessives.** English stacks "your"; Vietnamese drops "của bạn" when obvious: "Sell your pets" -> "Bán thú cưng".
- **Tense words.** Add "đã" (done), "đang" (ongoing), "sẽ" (will) only where they help: "Bạn đang AFK", "Bạn sẽ mất hết xu". Stacking them on every verb reads like a translation.
- **Negation.** "không" = not, "chưa" = not yet. Use "chưa" for anything the player can still reach: "Chưa đủ cấp!" Errors are short and impersonal, per Microsoft: "Không mua được", not "Mua thất bại".
- **Capitalization.** Microsoft: sentence case for UI text, so buttons and titles are "Cửa hàng", "Quà hằng ngày", not "Quà Hằng Ngày". Roblox's own Vietnamese UI mixes both ("Bảng Xếp Hạng" next to "Xác nhận"), so don't copy it. Proper game names (pets, items, rarities, passes) capitalize each word like rank names: "Rồng", "Thuốc May Mắn", "Huyền Thoại".
- **Questions.** Confirms can be a fragment ("Tái sinh ngay?") or the full form Roblox uses ("Bạn có muốn ... không?"). Don't end with "không" without the "có" frame.

## Typography and formatting
- No space before . , ! ? : ; and one space after, as in English. No comma before "và" or "hoặc" (Microsoft).
- Quotes: Vietnamese text uses curly double quotes (“Rồng”). A period or comma goes after the closing quote.
- Numbers: period for thousands, comma for decimals: "1.250 xu", "x1,5". An English-formatted "1,250" from game code reads as one-and-a-quarter; flag it to the developer.
- Percent: no space ("10%", "+25%"). A space between number and unit ("100 Robux").
- Multiplier: write "x2" before the noun, as Vietnamese players do ("x2 Xu", "x2 EXP"). "2x" is understood but looks imported.
- Durations: use full words when they fit ("3 giờ 20 phút", "2 ngày 5 giờ"), as Roblox's own strings do ("{n} phút", "{n} giây") and Sforum's code guides ("x2 EXP 20 phút"). A countdown "03:20:00" is the safe short form. "3h 20p" is chat style: "h" for giờ is everyday, "p" for phút is informal (unverified for polished UI). An English "m" reads as meters. The {time} text comes from game code; ask for a Vietnamese format.
- Ellipsis: three periods, like Roblox's "Đang tải...".
- Hyphens: don't carry English hyphen compounds over: "easy-to-use" -> "dễ dùng".
- Keys: the key letter stays: "Nhấn E để mở" (Roblox: "Nhấn {KEY_NAME} để..."). PC copy says "Nhấp" or "Bấm", mobile copy "Chạm" (Roblox: "Chạm để Di Chuyển"). Space is "phím Cách"; Shift, Enter and Ctrl stay in English.
- Dates: dd/mm ("25/12"). Prices are always "{n} Robux", never "đ".
- Line breaks: every syllable is space-separated, so Roblox wraps inside words ("thú | cưng"). Give labels width instead of narrow multi-line buttons.

## Do not translate / keep as is
- Roblox, Robux, Premium, Roblox Studio, VIP, AFK, EXP/XP, Boss, obby, tycoon.
- The game title ("Pet Hatch Tycoon"): Vietnamese guides and press keep English titles ("Blox Fruits", "Pet Simulator 99", "Grow a Garden").
- Promo codes (FREEPETS) exactly as typed, same case; usernames and display names.
- Pet, item and area names: translate once and keep them consistent ("Rồng", "Thuốc May Mắn"). Keep the English name only if the fandom already uses it (Grow a Garden guides write "Owl pet").
- Script: Latin with every diacritic (ă â đ ê ô ơ ư plus five tone marks). Never strip marks: "Choi" for "Chơi" is a typo at best. Save text as precomposed Unicode (NFC). Some Vietnamese keyboards (Unikey's "tổ hợp" mode) type combining marks instead, and how Roblox draws those is (unverified).

## Rendering on Roblox
- Checked in the 2026-11-05 client's font files: these have all 146 vowel and đ forms Vietnamese needs: Builder Sans (the default), Builder Mono/Extended, Source Sans Pro, Roboto (+Condensed, Mono), Arimo (Legacy Arial), Montserrat, Nunito, Oswald, Bangers, Amatic SC, Merriweather, Josefin Sans, Jura, Patrick Hand, Grenze Gotisch and Guru.
- Missing 86-102 of them (ơ ư ạ ả ấ and so on): Fredoka One, Luckiest Guy, Titillium Web, Ubuntu, Permanent Marker, Press Start 2P, Comic Neue Angular, Creepster, Denk One, Fondamento, Indie Flower, Kalam, Michroma, Sarpanch, Special Elite, Highway Gothic, Roman Antique, Accanthis, Balthazar, Zekton and Inconsolata.
- Fredoka One and Luckiest Guy are simulator-UI staples; Fredoka One lacks even ă, đ and Đ. Tell the developer to swap them for vi (Nunito or Bangers keep the cartoony look). A 2020 DevForum report shows Roblox drawing missing glyphs from an Arial-like fallback one character at a time, so expect mixed fonts inside one word ("R" in Fredoka, "ồ" in the fallback). That this still holds for Vietnamese is (unverified).
- Gotham is a cloud asset, not in the local font folder, so it was not checked (unverified).
- Stacked marks (ầ ẫ ặ ổ) are taller and the dot below (ạ ộ) hangs lower: expect clipping in tight TextScaled labels, worst in ALL CAPS ("HUYỀN THOẠI"). Avoid all-caps for vi (unverified, test).
- Test in Studio at the smallest TextSize, in every font the game uses: "Rồng Huyền Thoại ẤP TRỨNG Ỷ ữ ặ ộ đ Đ".

## Mistakes machine translation makes here
1. Tone-mark slips that change the word: "Múa" -> "Mua" (buy), "Chới" -> "Chơi" (play), "Rong" -> "Rồng" (dragon).
2. English adjective order: "Huyền Thoại Rồng" -> "Rồng Huyền Thoại"; "May Mắn Thuốc" -> "Thuốc May Mắn".
3. Play as media: "Phát" -> "Chơi". Claim as a demand: "Yêu cầu" -> "Nhận".
4. Server as a person: "Người phục vụ" (waiter) -> "Máy chủ". Trade as commerce: "Thương mại" -> "Giao dịch".
5. Literal level up: "Cấp độ lên!" -> "Lên cấp!"
6. Hatch used transitively: "Bạn đã nở một con rồng" -> "Bạn ấp được Rồng!" or "Trứng nở ra Rồng!"
7. Stiff or adult register: "Xin vui lòng tiến hành tái sinh" -> "Tái sinh ngay?"; "Quý khách" -> "Bạn".
8. Wrong pronoun: "mày", "ngươi" or "cậu" mixed with "bạn" in one game -> "bạn" everywhere.
9. Over-pluralizing: "Bán những thú cưng của bạn" -> "Bán thú cưng".
10. Title Case calqued from English: "Phần Thưởng Hằng Ngày" -> "Quà hằng ngày".
11. Southern spellings and words in neutral UI: "Gởi" -> "Gửi", "Lựa" -> "Chọn".
12. Copying Roblox's connections rename into game text: "+10% cho mỗi người quen" -> "+10% cho mỗi người bạn".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Chơi | |
| shop.title | Cửa hàng | Players also say "shop" |
| shop.buy | Mua | Same as Roblox UI |
| reward.claim | Nhận | Roblox: "Nhận Miễn Phí" |
| rebirth.button | Tái sinh | |
| rebirth.confirm | Tái sinh ngay? Bạn sẽ mất hết xu, nhưng nhận hệ số nhân x{multiplier} vĩnh viễn. | "buff x{multiplier}" is the casual alternative; code must send "1,5", not "1.5" |
| coins.need_more | Bạn cần thêm {amount} xu! | No plural form, so {amount} = 1 is fine |
| coins.count | {count} xu | Needs "1.250" formatting from code |
| egg.hatched | Bạn ấp được {pet} {rarity}! | Order flipped; no classifier, so any pet name fits |
| rarity.legendary | Huyền Thoại | Capitalized as a tier name; reads right after {pet} |
| pet.name.dragon | Rồng | |
| chat.player_joined | {player} đã tham gia trò chơi | Gender-free |
| trade.request | {player} muốn giao dịch với bạn | "trao đổi với bạn" can read as "wants a word with you" |
| prompt.open_shop | Nhấn E để mở | Roblox's pattern |
| pass.buy_price | Mua bằng {price} Robux | "bằng" = paying with; "Mua với" is a calque. Roblox's "với giá" pattern makes 23 at "1.000", over 22; this is 20 |
| pass.coins2x | x2 Xu | Vietnamese "x2" order |
| pass.vip | VIP | |
| reward.daily_title | Quà hằng ngày | "Phần thưởng hằng ngày" is 21, over 18 |
| reward.come_back | Quay lại sau {time} để nhận quà tiếp theo nhé! | |
| codes.placeholder | Nhập code | "Nhập mã" also correct; players say "code" |
| codes.invalid | Code không hợp lệ hoặc đã hết hạn. | |
| social.like_reward | Like game để nhận <b>Thuốc May Mắn</b> miễn phí! | "Like" as players say it, matching the thumbs-up icon; "Bấm Thích" is the formal option |
| social.group_reward | Tham gia cộng đồng của chúng mình để nhận quà miễn phí! | "cộng đồng" per Roblox's rename; 55/55, so drop "của chúng mình" if the banner shrinks |
| afk.warning | Bạn đang AFK! Di chuyển để kiếm tiếp nhé! | |
| leaderboard.title | Top người chơi | "Bảng xếp hạng" if the board shows ranks |
| level.up | Lên cấp! Bạn đã đạt cấp {level}. | |
| tutorial.sell | Bước vào vòng tròn phát sáng để bán thú cưng nhé. | |
| inventory.full | Ba lô đã đầy! Hãy bán bớt thú cưng để có chỗ trống. | "bán bớt" = sell some |
| settings.music | Âm nhạc | |
| settings.on | Bật | Same as Roblox UI |
| loading | Đang tải... | Same as Roblox UI |
| event.ends_in | Sự kiện còn {time} | "Sự kiện kết thúc sau {time}" overflows 28 with long times |
| item.op | Thanh kiếm này bá đạo quá! | "thanh" = sword classifier; "OP quá" also seen |
| friends.boost | +{percent}% thưởng cho mỗi người bạn cùng máy chủ | "người bạn", not "người quen" |

## Sources
1. Microsoft Vietnamese Localization Style Guide (via aka.ms/vietnamese-styleguide) -- https://download.microsoft.com/download/b/f/e/bfecb1b4-21ab-48fd-a48c-c2471b026f8f/vie-vnm-StyleGuide.pdf
2. Unicode CLDR language plural rules chart -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR plurals.xml, release-48 (vi: other only) vs release-49 (vi: one, other) -- https://github.com/unicode-org/cldr/blob/release-49/common/supplemental/plurals.xml
4. Roblox client CoreScript translations, vi column (ExtraContent/translations/CoreScriptLocalization.csv, Roblox build of 2026-11-05) -- local file from the Roblox install
5. Roblox client font files (content/fonts, build of 2026-11-05), Vietnamese glyph coverage checked with fontTools -- local files from the Roblox install
6. Roblox Creator docs (vi-vn, AI-translated), passes -- https://create.roblox.com/docs/vi-vn/production/monetization/game-passes
7. Wikipedia tiếng Việt, Roblox (Roblox VNG, 12+ limit, Premium, 2026 block) -- https://vi.wikipedia.org/wiki/Roblox
8. GameK, Roblox tag page (Vietnamese gaming press wording) -- https://gamek.vn/roblox.htm
9. Sforum (CellphoneS), Pet Simulator 99 codes (thú cưng, mở trứng, giao dịch) -- https://cellphones.com.vn/sforum/code-pet-simulator-99
10. Sforum, Blox Fruit codes (nhập code, x2 EXP, level, server, hết hạn) -- https://cellphones.com.vn/sforum/code-blox-fruit
11. Sforum, Grow a Garden codes (English item names kept, Pet, Exp) -- https://cellphones.com.vn/sforum/code-grow-a-garden
12. Sforum, "AFK là gì" -- https://cellphones.com.vn/sforum/afk-la-gi
13. Sforum, "Noob là gì" (noob, newbie, feed) -- https://cellphones.com.vn/sforum/noob-la-gi
14. DevForum, Source Sans missing Cyrillic glyphs (per-character Arial fallback, 2020) -- https://devforum.roblox.com/t/source-sans-cyrillic-characters-missing/483144
