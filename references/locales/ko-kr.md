# Korean (ko-kr) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `ko-kr` (the only Korean locale; no bare `ko` column needed) |
| Script, direction | Hangul (Kore), LTR, words separated by spaces |
| Address the player as | polite-casual 해요체 (`-아요/-어요`, `-세요`); never 당신, never 반말 or `-하십시오` |
| Text expansion vs English | -30 to -40% characters; rendered width from 25% narrower to 30% wider, by font and string (measured in Studio, see Rendering) |
| Plural categories (CLDR) | other (cardinal and ordinal) |
| Model confidence | high: well-resourced language; the real risks are particles after `{params}`, register mixing and loanword choice |
| Native review before shipping | recommended |

## Audience and register
- Korean Roblox players are mostly elementary and middle school kids. They read game text in the friendly 해요체 that Korean mobile and PC games use: `받을 수 있어요!`, `가방이 가득 찼어요!`.
- Microsoft's Korean guide prefers `-세요` over `-하십시오` for a natural, conversational tone and keeps `-하십시오` for legal text. Roblox's own Korean client strings never use `-하십시오` or 당신 and give instructions with `-세요` (`다시 시도하세요`). Do the same: `코드를 입력하세요`, not `코드를 입력하십시오`.
- Keep one register for the whole game. Roblox's client mixes 해요체 and 합니다체 (`Robux가 부족합니다`); a game should not. Do not mix 해요체 toasts with 합니다체 dialogs or with 반말 (`레벨 업했어!`). 합니다체 is correct but reads like a bank app to kids.
- Drop "you" and "your". Korean omits pronouns when the meaning is clear; 당신 sounds cold or adult. "Your backpack is full" -> `가방이 가득 찼어요!`
- Buttons and toggles are nouns or `-기` forms, never full sentences: `구매`, `받기`, `플레이`, `켜짐`. Not `구매해요`.
- Titles and labels take no period: `일일 보상`. Sentences in toasts end with `.` or `!`.
- Hype sounds natural with short noun endings and `!`: `레벨 업!`, `부화 성공!`, `전설 등장!`. Avoid stacked `!!!` and crude slang prefixes like 개- (`개사기`): kids use them, a polished game does not.

## Roblox and gaming vocabulary
| English | Use in Korean | Note |
|---|---|---|
| Robux | `Robux` | Roblox's Korean client, docs and App Store listing keep Latin `Robux` (`Robux 구매`, `Robux가 부족합니다`); `로벅스` never appears there. Players write `로벅스`; fine in casual text, but pick one per game. |
| game pass | `게임 패스` | Roblox Korean creator docs shorten it to `패스`; players say `겜패` (too slangy for UI). |
| developer product | `개발자 제품` (docs) | Players never see this term; use the item's own name in UI. |
| experience / game | `게임` in game text | Roblox's Korean UI says `체험`; inside your own game, `게임` is what kids say. |
| obby | `장애물 코스` | Players also say `오비` (unverified). |
| tycoon | `타이쿤` | Long-established loanword in Korea. |
| simulator | `시뮬레이터` | As in `펫 시뮬레이터 X`. |
| rebirth | `환생` | Standard in Korean idle and simulator games (no Roblox source uses it). Not `부활` (revive) or `재탄생`. |
| pet | `펫` | Not `애완동물` in UI. |
| egg / hatch | `알` / `부화` | `알을 부화시키다`, `부화 성공!` |
| coins | `코인` | Not `동전`. |
| gems | `보석` (or `젬`) | `다이아` if the game calls them diamonds. |
| boost | `부스트` | |
| multiplier | `배율`, or `N배` | "2x Coins" -> `코인 2배`. |
| XP | `경험치` | `XP` acceptable when space is tight. |
| level up | `레벨 업` | Pick `레벨 업` or `레벨업` and keep it. |
| quest | `퀘스트` | |
| leaderboard | `순위표`, `랭킹` | Roblox's own player list says `리더보드`. |
| AFK | `자리 비움` | System wording. Players say `잠수` (`잠수 중`); OK in casual lines. |
| noob | `뉴비` (new player), `초보` | Roblox's yellow default avatar is called `노브` by some players (unverified). |
| OP | `사기템` (item), `사기캐` (character) | Bare `사기` can read as "scam" in a shop; add 템. |
| VIP | `VIP` | |
| trade | `거래` | `교환` (swap) and `트레이드` also used by players. |
| inventory / backpack | `가방`, `인벤토리` | Roblox's top bar says `인벤토리`; `가방` is friendlier for "backpack". |
| daily reward | `일일 보상` | `출석 보상` if it is a login streak. |
| codes | `코드` | Korean mobile games call promo codes `쿠폰`; `코드` is what Roblox players search for. Keep one. |
| group | `그룹` | Verb is `가입하다`: `그룹에 가입하기`. |
| like / favorite | `좋아요` / `즐겨찾기` | `즐겨찾기` is on Roblox's Korean game page and in-game menu; `좋아요를 누르다` for like (Roblox's label unverified). |
| server | `서버` | Roblox's Korean game page tab. |
| friends / connections | `친구` | Roblox's Korean client says `친구`. Its 2025 "Connections" strings used `인맥` (not `연결`), and newer strings are back to `친구`. |
| Premium | `Premium` / `Roblox Plus` (Latin) | Client strings say `Roblox Premium`, `Premium 전용`; the Korean App Store text also says `ROBLOX PLUS` (Plus replacing Premium on 2026-04-30 is unverified). Use the game's English name. |

## Grammar traps in UI strings
- **Plurals.** Korean has no plural agreement; one string works for 0, 1 and 1,250. Do not add `들` to counted nouns: `코인들` -> `코인`. Use a counter after the number: `{amount}개` (coins, items), `{n}마리` (pets), `{n}명` (people), `{n}번` (times).
- **Particles after placeholders.** The particle depends on whether the word ends in a consonant: `드래곤을` but `토끼를`, `레벨이` but `코인이`. Game code does not choose for you. In order of preference:
  1. Player names: add ` 님` with a space (standard spelling after a name, and how Roblox's Korean UI writes `{RBX_NAME} 님이`) and attach the particle to it: `{player} 님이 게임에 참가했어요`. Always correct, and polite.
  2. Put a fixed noun after the placeholder: `{level}레벨이에요`, `{amount}개 더 필요해요`.
  3. Rephrase so the placeholder ends a noun phrase: `{rarity} {pet} 부화 성공!`
  4. Last resort, the convention Microsoft and Roblox's own prompts use: `{pet}을(를)`, `{player}이(가)`. Correct, but looks robotic in a game.
- **Fixed Latin words** take the particle of their Korean reading: `Robux` (로벅스) -> `Robux를`, `Robux가`; `Premium` (프리미엄) -> `Premium을`, `Premium이`.
- **Never put a particle straight after a number.** `{level}이에요` breaks: 2 is read 이, so it needs `예요`. Write `{level}레벨이에요`.
- **No gender.** Korean has no grammatical gender; avoid 그/그녀 and refer to players as `{player} 님`.
- **Word order is SOV.** Verbs go last and placeholders move: "Buy for {price} Robux" -> `{price} Robux에 구매`; "Event ends in {time}" -> `이벤트 종료까지 {time}`.
- **Inserted modifiers.** A translated rarity works as a noun before the pet: `전설 드래곤`. Translate rarities as bare nouns (`전설`, not `전설의`) so they combine cleanly.
- **Compound spacing.** Spaces change meaning: `작은 아버지` is a short father, `작은아버지` an uncle. Established compounds attach: `손가방`. For game terms, pick one spacing (`일일 보상`, `레벨 업`) and reuse it everywhere.
- **No capitalization** in Hangul. Latin terms keep their own case: `VIP`, `XP`, `Robux`.

## Typography and formatting
- Korean uses Western punctuation with no space before it: `부화 성공!`, `환생할까요?`.
- Quotation marks: Roblox's Korean UI puts names in straight single quotes (`'{BADGE_NAME}'`); use `' '` for item names, `" "` for quoted speech. When a line names a button, put the label in square brackets, as Microsoft's Korean UI style does: `[구매] 버튼을 누르세요`.
- Ellipsis: keep `...` attached: `로딩 중...`.
- Numbers: comma thousands, `1,250`. Korean counts in 만 (10,000) and 억, but HUD numbers come from game code, not the table: keep the game's K/M/B suffixes, which Roblox simulators show in every language, unless code can output `1.2만` (Korean player preference unverified).
- Percent and multiplier attach to the number: `+20%`, `2배`.
- Counters and units may attach to Arabic digits (standard spelling allows it): `3개`, `10분`. Latin units take a space: `100 Robux`.
- Durations: `3시간 20분`, `2일 5시간`, `45초`. Ask for code that formats `{time}` this way; Latin `3h 20m` is readable but looks unfinished.
- Line breaking: Roblox wraps Korean at spaces and splits a word only when it alone is wider than the box (tested in Studio). Keep particles attached (`가방이`, not `가방 이`) and avoid long unspaced compounds.
- Keys: key name, a space, then `키`: `E 키를 눌러 열기`. No `키` in combinations: `Shift+E`.
- Rich text: particles go right after the closing tag, no space: `<b>행운 포션</b>을`.

## Do not translate / keep as is
- `Roblox` and `Robux` in UI (Latin, as Roblox's Korean product text does). `로블록스` only in prose such as descriptions.
- Product and subscription names: `Roblox Plus`, `Premium`, `VIP`.
- Promo codes (`FREEPETS`), usernames and display names, keybinds (`E`, `Shift`).
- Game titles: Roblox's Korean game pages show most titles in English (Adopt Me! stays `Adopt Me!`); translate a title only as a deliberate marketing choice. Korean fan sites call it `입양하세요!`.
- Made-up item or pet brand names: transliterate (`드래곤`, `포션`) rather than invent pure Korean words; keep invented proper nouns phonetic.
- One script only: never mix Hanja or Japanese kana into Korean UI.

## Rendering on Roblox
- A DevForum post says the Roblox client ships Noto Sans CJK and picks the regional variant by language code; Hangul renders with the default fonts (forum claim, not Roblox docs).
- Studio test, 2026-11-08 (`TextService:GetTextBoundsAsync`, size 20): Hangul measured the same width in Fredoka One, Gotham, Gotham Bold, Builder Sans (Regular and Bold) and Source Sans. Hangul is drawn by one shared fallback face whatever font the label sets, while Latin letters and digits keep the label's font, so `100 Robux에 구매` shows two fonts. A 2026 DevForum post reports the same for Chinese.
- Measured widths, Korean vs English: `rebirth.confirm` 441 vs 545 px (Fredoka One), 428 vs 452 (Source Sans); `inventory.full` 309 vs 374 and 303 vs 313; `afk.warning` 310 vs 284 and 304 vs 235. Narrow Latin fonts (Source Sans, Builder Sans) gain the least, so test toasts at phone size in the game's real font.
- Still unverified: whether the fallback draws Hangul bold for Bold weights or `<b>` (widths did not change, but CJK glyph widths rarely do), and how `TextScaled` shrinks mixed lines. Check these visually at phone size.

## Mistakes machine translation makes here
- 당신 for "you": `당신은 레벨 업했습니다` -> `레벨 업! 이제 5레벨이에요.`
- Formal register in a kids' game: `코인이 부족합니다` -> `코인이 {amount}개 더 필요해요!`
- Fixed particle after a placeholder: `{pet}를 부화했어요` (breaks on `드래곤`) -> `{rarity} {pet} 부화 성공!`
- Plural `들` on counted nouns: `{count} 코인들` -> `{count} 코인`
- "Claim" as a legal claim: `청구` / `주장` -> `받기`
- "Rebirth" as revival: `부활` / `재탄생` -> `환생`
- "Like the game" as "love the game": `게임을 좋아하세요` -> `게임에 좋아요를 누르고`
- "Experience" as life experience: `경험` -> `게임` (or `체험` for Roblox platform text)
- AFK spelled out: `키보드에서 떠나 있어요` -> `자리 비움 상태예요!`
- "Buy for": `100 Robux를 위해 구매` -> `100 Robux에 구매`
- OP as a scam: `이 검은 사기예요` -> `이 검, 완전 사기템이에요!`
- Sentence-style buttons: `구매합니다` / `플레이하세요` -> `구매` / `플레이`

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | 플레이 | Roblox's Korean pages say `Roblox에서 플레이하기`; `시작` also works. |
| shop.title | 상점 | Same word as Roblox's Store tab. |
| shop.buy | 구매 | Roblox's own Buy button; `구매하기` (4) also fits. |
| reward.claim | 받기 | |
| rebirth.button | 환생 | |
| rebirth.confirm | 지금 환생할까요? 가진 코인은 모두 사라지지만 영구 {multiplier}배 부스트를 받아요. | `{multiplier}x` -> `{multiplier}배`; works for 2 and 1.5. |
| coins.need_more | 코인이 {amount}개 더 필요해요! | Counter `개` avoids a particle after the number. |
| coins.count | {count} 코인 | No plural form needed. |
| egg.hatched | {rarity} {pet} 부화 성공! | Rephrased to avoid `을(를)` after `{pet}`. |
| rarity.legendary | 전설 | Bare noun so `{rarity} {pet}` reads `전설 드래곤`. |
| pet.name.dragon | 드래곤 | `용` also fine; games usually use `드래곤`. |
| chat.player_joined | {player} 님이 게임에 참가했어요 | ` 님` fixes the particle for any name; Roblox's friend-join message is `친구 {RBX_NAME} 님이 체험에 참가했어요`. |
| trade.request | {player} 님이 거래를 요청했어요 | |
| prompt.open_shop | E 키를 눌러 열기 | `E` kept; `키` after a space. |
| pass.buy_price | {price} Robux에 구매 | Latin Robux as in Roblox's purchase prompts; `로벅스에 구매` only if the game already writes 로벅스. |
| pass.coins2x | 코인 2배 | |
| pass.vip | VIP | Kept in English. |
| reward.daily_title | 일일 보상 | |
| reward.come_back | {time} 후에 다음 보상을 받을 수 있어요! | Needs `{time}` as `3시간 20분`. |
| codes.placeholder | 코드 입력 | |
| codes.invalid | 유효하지 않거나 만료된 코드예요. | |
| social.like_reward | 게임에 좋아요를 누르고 무료 <b>행운 포션</b>을 받으세요! | Particle outside `</b>`. |
| social.group_reward | 그룹에 가입하고 무료 보상을 받으세요! | |
| afk.warning | 자리 비움 상태예요! 계속 코인을 벌려면 움직이세요! | `코인을` added: bare `벌려면` reads incomplete. `자리 비움` is understood at every age; `잠수 중이에요!` is the casual option. |
| leaderboard.title | 상위 플레이어 | `최고의 플레이어` reads like a "Best Player" award; `랭킹` is the common short board title. |
| level.up | 레벨 업! 이제 {level}레벨이에요. | `레벨` after the number carries the particle. |
| tutorial.sell | 빛나는 원 안으로 들어가서 펫을 판매하세요. | |
| inventory.full | 가방이 가득 찼어요! 펫을 판매해서 공간을 만드세요. | |
| settings.music | 음악 | |
| settings.on | 켜짐 | State form; Off = `꺼짐`. Roblox's own toggles say `켜기`/`끄기`; either pair works, keep one. |
| loading | 로딩 중... | Roblox's own loading text is `불러오는 중...` (9); both are natural. |
| event.ends_in | 이벤트 종료까지 {time} | |
| item.op | 이 검, 완전 사기템이에요! | `사기템` = OP item; kid-safe, no `개-`. |
| friends.boost | 같은 서버의 친구 1명당 +{percent}% 부스트 | `친구`, as in Roblox's current Korean client. |

## Sources
1. Microsoft Korean Style Guide (PDF, via the style guide index): https://download.microsoft.com/download/5/b/6/5b62389f-4e3b-4c77-bc18-94efba2fa7bb/kor-kor-StyleGuide.pdf
2. Microsoft Localization Style Guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. Roblox game pages in Korean (즐겨찾기, 상점, 서버, 체험; Adopt Me! title in English): https://www.roblox.com/ko/games/1098856813/Split-Screen-Testing-Controls and https://www.roblox.com/ko/games/920587237/Adopt-Me
5. Roblox Creator Docs, Korean, passes (Robux, 체험, 패스, 개발자 제품): https://create.roblox.com/docs/ko-kr/production/monetization/game-passes
6. Roblox on the Korean App Store (Robux, 친구, ROBLOX PLUS, Roblox Premium): https://apps.apple.com/kr/app/roblox/id431946152
7. Roblox client CoreScript strings with the `ko` column (build 0.727, 2026-06; Robux, 친구/인맥, 님, Premium, 켜기, 불러오는 중, register counts), mirrored by Roblox-Client-Tracker: https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/translations/CoreScriptLocalization.csv
8. Roblox Plus press release, 2026-04 (reported in search results; returned 403 on review): https://www.businesswire.com/news/home/20260410099173/en
9. DevForum, "Add the HTML lang attribute" (Noto Sans CJK in the client): https://devforum.roblox.com/t/add-the-html-lang-attribute/444641
10. DevForum, "Add more CJK fonts..." (2026, CJK fallback to default font): https://devforum.roblox.com/t/add-more-cjk-fonts-as-well-as-different-font-properties-for-each-language/4566304
11. DeskIn Korean blog on AFK in Roblox (AFK, 자리 비움, 잠수, 파밍): https://deskin.io/ko/resource/blog/what-does-afk-mean-in-roblox-and-how-players-use-it
12. BlueStacks Korean Roblox games roundup (입양하세요!, 펫 알, 부화, 펫 시뮬레이터): https://www.bluestacks.com/ko/blog/game-guides/roblox/rl-popular-games-details-ko.html
13. Korean Roblox guide site using 로벅스 in player-facing text: https://yellowit.co.kr/tag/roblox/
