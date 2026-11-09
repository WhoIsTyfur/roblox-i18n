# Chinese (Traditional) (zh-tw) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `zh-tw` (there is no bare `zh` column; Roblox also serves this column to `zh-hk` players) |
| Script, direction | Traditional Han (Hant) with Taiwan character forms, LTR, horizontal |
| Address the player as | 你 (informal); never 您, never 妳 |
| Text expansion vs English | Fewer characters (about 40-60% of English), but each Han glyph is full-width: sentences render at about 0.6-1.0x English width, while 1-4 letter buttons get wider (Play -> 開始遊戲, On -> 開啟) (estimate) |
| Plural categories (CLDR) | other only (cardinal and ordinal); Chinese has no plural forms |
| Model confidence | high: high-resource language; the real risks are Mainland vocabulary, Simplified->Traditional conversion errors and a stiff 您 register |
| Native review before shipping | recommended (a Taiwan reader; a Hong Kong reader too if HK players matter) |

## Audience and register
- Readers are mostly Taiwanese kids writing Taiwan Mandarin, plus Hong Kong players (zh-hk resolves here). Write Taiwan standard written Chinese; HK kids should read it fine (unverified with a HK reader).
- Use 你 everywhere and 你們 or 大家 for groups. Roblox's zh-tw client strings mostly use 您 (about 260 strings to 9 with 你, e.g. "您已閒置..."), and Microsoft's guide requires 您 in all software; both are account and system voice, which reads like customer service in a kids' game. Newer Roblox strings already use 你 ("你的好友 {RBX_NAME} 已加入體驗。"), and Minecraft's zh_tw file uses 你 in gameplay text (你死了！) and 您 only on account screens. 妳 is the female "you" some Taiwanese writers use: never use it, gender is unknown.
- Buttons are a bare verb or verb-object, 2-4 characters, no 請: 購買, 領取, 開始遊戲. Save 請 for real requests ("請稍後再試").
- Friendly Taiwan sentence-final particles, at most one per string: 喔 (not Mainland 哦), 吧, 囉, 啦. "快來領取吧！", "出發囉！".
- Hype that sounds natural: 太棒了！, 恭喜你獲得新寵物！, 好耶！, 超強！, 強到爆！. One ！ per sentence, never ！！！.
- Stiff, textbook or adult words to avoid: 倘若 -> 如果, 欲 -> 想, 予以, 之 (as "of"), 係 (formal "is"), 敬請.
- Kid-safe: no Taiwan slang that is vulgar (靠北, 屌, 幹, 機掰), even when players use it.
- Hong Kong: never write Cantonese colloquial forms (嘅, 咗, 唔, 啲, 係 as "is"); HK players expect standard written Chinese.

## Roblox and gaming vocabulary
| English | zh-tw | Note |
|---|---|---|
| Robux | Robux | Keep English, half-width. Roblox UI: 購買 Robux. Players say R幣; never in UI |
| Premium / Roblox Plus | Premium / Roblox Plus | Latin. Roblox stopped selling Premium on 2026-04-30 and now sells Roblox Plus (訂閱 Roblox Plus); existing members keep Premium. Roblox UI: Premium 限定 |
| game pass | 通行證 | Roblox zh-tw creator docs. One client string renders "Pass" as 特權券; the word on the player-facing Store tab is unverified (its labels render client-side). In game UI, name the pass instead (2 倍金幣) |
| developer product | 開發者產品 | Creator-facing; in player UI name the item instead (100 寶石) |
| experience / game | 遊戲 | In game text say 遊戲. 體驗 is Roblox's platform word (離開體驗) |
| obby | 障礙賽 / Obby | Players also say 跑酷 (unverified) |
| tycoon | 大亨 | e.g. 寵物孵化大亨 (unverified as player usage) |
| simulator | 模擬器 | 寵物模擬器 |
| rebirth | 轉生 | Not 重生, which reads as respawn |
| pet | 寵物 | Classifier 隻: 一隻寵物 |
| egg / hatch | 蛋 / 孵化, 孵出 | 3 顆蛋. Not 雞蛋 (a chicken egg you eat) |
| coins | 金幣 | |
| gems | 寶石 | 鑽石 if the icon is a diamond |
| boost | 加成 | Potion-style buffs: 增益 |
| multiplier | 倍率 / N 倍 | 2x -> 2 倍 |
| XP | 經驗值 / XP | Both common |
| level up | 升級 | Level = 等級, short form Lv. |
| quest | 任務 | |
| leaderboard | 排行榜 | Roblox UI term |
| AFK | 掛機 | Roblox's own idle-kick text uses 閒置 |
| noob | 新手 | 菜鳥 is teasing; fine in jokes only |
| OP | 強到爆 / 超強; 超 OP for teens | Teen gamers know "OP" (unverified for under-12s); plain words read at every age |
| VIP | VIP | |
| trade | 交易 | |
| inventory / backpack | 道具欄 / 背包 | Roblox UI: Inventory = 道具欄, Backpack = 背包 |
| item | 道具 | Roblox UI; 物品 also fine |
| daily reward | 每日獎勵 | |
| codes | 兌換碼 | Clearest in UI. Players also say 序號 (unverified frequency); pick one per game. Avoid bare 代碼: Roblox uses it for error codes (錯誤代碼) |
| group | 群組 | Roblox zh-tw docs; join = 加入群組 |
| like / favorite | 按讚 / 設為最愛 | Roblox UI: Favorite = 設為最愛, Unfavorite = 從最愛移除. Roblox's own word for Like is unverified; 按讚 is the everyday Taiwan word (Facebook, YouTube) |
| server | 伺服器 | Never 服務器 (Mainland) |
| friends | 好友 | Roblox renamed Connections back to Friends on 2026-04-02 (好友, 可信好友). Older client strings show 聯絡對象 or 連結: do not use |
| avatar | 虛擬人偶 | Roblox UI term |
| shop | 商店 | |
| badge | 徽章 | Roblox UI |
| report / block | 檢舉 / 封鎖 | Roblox UI; Mainland 舉報 / 屏蔽 are wrong here |

## Grammar traps in UI strings
- Plurals: none exist, so one string covers 0, 1 and 1,250: "{count} 金幣". Never add 們 to things (寵物們), and never add 一些 next to a number.
- Classifiers: a number inside a sentence wants a measure word: 隻 for animals and pets (一隻龍), 顆 for eggs (3 顆蛋), 把 for swords, 位 for people (每位好友), 個 as a fallback (Roblox: {itemCount} 個道具). Currencies (金幣, 寶石, Robux) and HUD counters take none: "還差 {amount} 金幣！", "{count} 金幣".
- {player}: verbs do not agree with gender, but 他 / 她 do. Avoid both: repeat {player} or use 對方 ("對方取消了交易").
- Word order: time and condition go before the verb. "in {time}" -> "{time} 後": "{time} 後再回來". "for each friend" moves to the front: "每位好友提供 +5% 加成".
- Multipliers: "{multiplier}x" -> "{multiplier} 倍"; "2x Coins" -> "2 倍金幣". "2x" survives only on tiny badges.
- Short modifiers attach without 的 (傳說龍, 幸運藥水); clauses take 的 (發光的圓圈). Inserted Han words join with no space: "{rarity}{pet}".
- Completion and questions: 了 for done events ("你孵出了龍！", "升級了！"); a yes/no question ends in 嗎？ ("要現在轉生嗎？").
- Capitalization does not exist; titles take no end punctuation. Latin words keep their own case (VIP, OP, Robux).
- 裡 vs 裏 vs 里: Taiwan writes 裡, Hong Kong 裏, and 里 is Simplified "inside". Use 中 or 內 when it reads as well ("伺服器中").

## Typography and formatting
- Chinese text takes full-width punctuation: ，。！？：；、. Roblox's zh-tw client strings never put half-width ! ? : after Han (full-width ！ 28, ？ 56, ： 60 strings). Microsoft's guide prescribes half-width : ; ! ? in software UI; Roblox does not follow it, so neither do we.
- No space before or after full-width punctuation.
- Put a half-width space between Han and Latin letters, digits, or a {param} edge that renders Latin or digits: "購買 Robux", "按 E 開啟", "{count} 金幣", "{player} 加入了遊戲". Roblox's zh-tw client does this in about 96% of mixed strings ("您已閒置 {RBX_NUM} 分鐘"), and Microsoft's guide requires it.
- No space between Han and a {param} that renders Han ({rarity}, {pet}).
- Quotes: 「」, nested 『』. Never "" or “”. Roblox writes 「/」鍵.
- List separator 、: 金幣、寶石和寵物.
- Ellipsis: …… (two U+2026); Roblox uses 正在傳送……. Never 。。。 or a lone "...".
- No em dash: it looks like 一 (Microsoft guide). Rephrase, or use ： or （）.
- Digits and Latin letters stay half-width: VIP, 12, never ＶＩＰ, １２.
- Numbers: comma thousands (1,250); percent with no space (+25%). Taiwanese count big numbers in 萬 and 億 (1.2萬); K/M abbreviations are understood.
- Durations read best localized: 3 小時 20 分, 2 天 5 小時, or a clock 03:20:00, as Roblox writes "{RBX_NUMBER} 秒". A raw "3h 20m" looks foreign: flag it to the developer, but translate anyway. The space after {time} follows its last character: "3h 20m 後" but "3 小時 20 分後".
- Item and rarity tags may use 【】, a Chinese game convention: 獲得【傳說】龍！ (optional).
- Line breaks fall between any two characters. Check that ，。！ never start a line and "Robux" is not split (unverified how Roblox wraps CJK).

## Do not translate / keep as is
- Robux, Roblox, Roblox Plus, Premium, VIP, Roblox Studio: English, half-width. Never R幣 or 羅布幣.
- The game title stays English ("Pet Hatch Tycoon") unless the developer supplies a Chinese title.
- Usernames, display names and promo codes (FREEPETS): never translate; codes keep their exact case.
- Keyboard keys stay Latin with spaces: "按 E 開啟", "按 Shift 衝刺".
- Gamer acronyms Taiwan players use in English: OP, VIP, AFK (alongside 掛機), XP (alongside 經驗值), PvP.
- Translate item and pet names: Lucky Potion -> 幸運藥水, Dragon -> 龍.
- Script: Traditional only, Taiwan forms (裡, 著, 台). No Simplified character may appear, not even in a name or tag.

## Rendering on Roblox
- Roblox ships Noto Sans CJK and picks Taiwan glyph forms through the OpenType locl feature when the client locale is zh-tw (DevForum, 2020). GUI text and chat follow the locale; Humanoid nameplates rendered Japanese glyph forms, and no fix was confirmed.
- Custom fonts (Fredoka One, Luckiest Guy, Builder Sans) contain no Han. Han falls back to the default CJK font while Latin keeps the custom font, so one label shows two fonts; there is no per-language font property (DevForum, April 2026). Accept it, or switch Font in code from the player's locale.
- Whether bold weights render for fallback Han is unverified; check headers in Studio.
- Chinese strings are short, so TextScaled can blow them up huge. Cap them with UITextSizeConstraint. Older DevForum threads report CJK TextScaled bugs; current status unverified.
- Verify in Studio: emulate locale zh-tw, check that a glyph with regional forms such as 骨 shows the Taiwan form, look for tofu boxes, and check wrapping on the longest strings.

## Mistakes machine translation makes here
- Mainland vocabulary in Traditional characters: 服務器 -> 伺服器, 視頻 -> 影片, 設置 -> 設定, 默認 -> 預設, 加載 -> 載入, 質量 -> 品質 (or 畫質), 信息 -> 訊息, 網絡 -> 網路, 用戶 -> 玩家, 點擊 -> 點選 (or 按). Roblox's own machine-translated zh-tw creator docs leak 服務器 and 數據存儲: never copy terms from them.
- One-to-many conversion errors: 游戲 -> 遊戲, 一只龍 -> 一隻龍, 3 小時后 -> 3 小時後, 頭发 -> 頭髮, 夥伴 not 伙伴.
- Simplified characters left in: 为你 -> 為你, 这个 -> 這個, 升级 -> 升級, 金币 -> 金幣. Scan every string; one stray character looks broken to a Taiwan reader.
- Rebirth as 重生 (respawn) -> 轉生.
- Formal or gendered address: 您的背包已滿 -> 你的背包滿了; 妳 -> 你.
- Mainland slang and tone: 小伙伴們 -> 大家, 親 -> drop it, 666 / 牛 -> 超強.
- Calques: "你需要 5 更多金幣" -> "還差 5 金幣"; "喜歡這個遊戲" for Like -> "幫遊戲按讚".
- Ambiguous word for codes: 輸入代碼 (reads as program or error code) -> 輸入兌換碼.
- Half-width punctuation and missing spaces: "背包滿了!" -> "背包滿了！"; "購買Robux" -> "購買 Robux".
- Hong Kong forms in a Taiwan column: 軟件 -> 軟體, 質素 -> 品質, 上載 -> 上傳, 數據 -> 資料, 解像度 -> 解析度. HK players know the Taiwan forms from Taiwan media (unverified whether any reads as wrong).
- Rarity wording drifting between strings: use 傳說 for Legendary in every key (傳奇 is not wrong, but never mix them); likewise 普通, 稀有, 史詩, 神話.

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | 開始遊戲 | |
| shop.title | 商店 | |
| shop.buy | 購買 | |
| reward.claim | 領取 | |
| rebirth.button | 轉生 | Not 重生 |
| rebirth.confirm | 要現在轉生嗎？你會失去所有金幣，但能獲得永久 {multiplier} 倍加成。 | "Nx boost" -> "N 倍加成" |
| coins.need_more | 還差 {amount} 金幣！ | Reads right for 1 too |
| coins.count | {count} 金幣 | No classifier in a counter |
| egg.hatched | 你孵出了{rarity}{pet}！ | Han params, no spaces; 【{rarity}】 is an option |
| rarity.legendary | 傳說 | Keep the whole rarity set consistent |
| pet.name.dragon | 龍 | |
| chat.player_joined | {player} 加入了遊戲 | |
| trade.request | {player} 想和你交易 | |
| prompt.open_shop | 按 E 開啟 | Key stays Latin, spaced |
| pass.buy_price | 用 {price} Robux 購買 | |
| pass.coins2x | 2 倍金幣 | Matches the N 倍 pattern for 3x and {multiplier}; 雙倍金幣 is fine for 2x alone |
| pass.vip | VIP | Kept English |
| reward.daily_title | 每日獎勵 | |
| reward.come_back | {time} 後再回來領取下一份獎勵！ | For "3h 20m"; if {time} comes localized (3 小時 20 分), drop the space: {time}後 |
| codes.placeholder | 輸入兌換碼 | |
| codes.invalid | 兌換碼無效或已過期。 | |
| social.like_reward | 幫遊戲按讚，免費領取<b>幸運藥水</b>！ | Like = 按讚 |
| social.group_reward | 加入我們的群組，解鎖免費獎勵！ | |
| afk.warning | 你在掛機喔！動一動才能繼續賺金幣！ | Added 金幣 for "earning" |
| leaderboard.title | 頂尖玩家 | |
| level.up | 升級了！你現在是 {level} 級。 | |
| tutorial.sell | 走進發光的圓圈，就能出售你的寵物。 | |
| inventory.full | 背包滿了！賣掉一些寵物來空出位置吧。 | |
| settings.music | 音樂 | |
| settings.on | 開啟 | Roblox UI; Off = 關閉 |
| loading | 載入中…… | |
| event.ends_in | 活動倒數 {time} | 倒數 is the Taiwan word for countdown |
| item.op | 這把劍強到爆！ | Slang hype every age reads; 這把劍超 OP！ for a teen-skewing game |
| friends.boost | 伺服器中每位好友提供 +{percent}% 加成 | 中 avoids 裡 / 裏 |

## Sources
1. Microsoft Chinese (Traditional, Taiwan) localization style guide: https://aka.ms/chinese-traditional-styleguide (zho-twn-StyleGuide.pdf)
2. Unicode CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox client strings, zh-tw column: `ExtraContent/translations/CoreScriptLocalization.csv` in the Roblox Studio install (build version-f0ea5da9412f4e35, 2026-11-05)
4. Roblox on the Taiwan App Store (zh-TW listing): https://apps.apple.com/tw/app/roblox/id431946152
5. Roblox newsroom (zh-hant), Connections renamed back to Friends, 2026-04-02: https://about.roblox.com/zh-hant/newsroom/2026/04/expanding-trusted-friends
6. Roblox Creator Docs zh-tw, passes (AI-translated): https://create.roblox.com/docs/zh-tw/production/monetization/game-passes
7. Roblox Creator Docs zh-tw, groups (AI-translated): https://create.roblox.com/docs/zh-tw/projects/groups
8. Wikipedia zh, IT term conversion table (zh-cn / zh-tw / zh-hk): https://zh.wikipedia.org/wiki/Module:CGroup/IT
9. DevForum, CJK glyph variants by locale: https://devforum.roblox.com/t/humanoid-names-do-not-render-with-correct-cjk-glyphs/674438
10. DevForum, custom fonts and Traditional Chinese fallback (2026): https://devforum.roblox.com/t/add-more-cjk-fonts-as-well-as-different-font-properties-for-each-language/4566304
11. FlashGet Kids zh-tw Adopt Me guide, used only as an example of Mainland leakage (服務器, 雞蛋): https://parental-control.flashget.com/zh-tw/roblox-adopt-me
12. Roblox Plus page (zh-hant), Premium sales end 2026-04-30: https://about.roblox.com/zh-hant/what-is-roblox-plus
13. Minecraft Java zh_tw language file (`minecraft/lang/zh_tw.json` in the game assets), for kids'-game address form
