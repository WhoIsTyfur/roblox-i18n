# Chinese (Simplified) (zh-cn) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `zh-cn` (no bare `zh` column; Roblox also sends zh-sg players here, while zh-hk goes to `zh-tw`) |
| Script, direction | Han, Simplified characters, LTR; no spaces between words |
| Address the player as | 你, never 您 (Roblox's own zh-cn client strings use 你 about 19 times as often as 您) |
| Text expansion vs English | Fewer characters (often 40-60% of English, estimate), but each glyph is about two Latin letters wide: plan 0.6-1.0x English width; 1-3 letter English buttons can get wider ("Buy" -> 购买) |
| Plural categories (CLDR) | other (cardinal and ordinal) -- no plural forms at all |
| Model confidence | high -- high-resource language; the real risks are stiff MT-style phrasing, Traditional/Taiwan leakage and wrong gaming terms |
| Native review before shipping | recommended |

## Audience and register
- Readers are Simplified Chinese speakers on global Roblox: players in mainland China on the global client (they call it 国际服), Singapore and Malaysia (zh-sg) and overseas Chinese families. Roblox's mainland China product (罗布乐思 / LuoBu) was a separate app with its own terms; do not borrow them. Roblox's client keeps a separate `zh-cjv` column for it, which once rendered "Buy Robux" as 购买罗宝.
- Write standard mainland written Mandarin (普通话) that reads like a polished mobile game: short, lively, plain words. Keep it kid-safe: no crude net slang (牛逼, 卧槽) and no teasing labels like 熊孩子.
- Use 你 or drop the pronoun. Chinese leaves pronouns out freely: "Your backpack is full" -> 背包已满！, not 你的背包已满了。
- Buttons are verbs or verb-object pairs of 2-4 characters with no 请 and no punctuation: 购买, 领取, 开始游戏, 确认.
- Hype and warmth come from short exclamations and one sentence-final particle at most: 恭喜！你获得了新宠物！ / 快来试试吧！ / 升级啦！ Particles 吧, 啦, 哦 soften a line; two in one string sounds babyish.
- Avoid textbook connectors that read adult: 倘若, 若要, 仅是 -> 如果, 要, 只是 (Microsoft's guide lists these as too formal).
- Confirmation dialogs use 确定要…吗？: 确定要重生吗？

## Roblox and gaming vocabulary
| English | zh-cn | note |
|---|---|---|
| Robux | Robux | Latin script, never translated; Roblox UI: 购买 Robux, Robux 不足. Players say R币 in chat; not in UI |
| game pass | 通行证 | Roblox UI and creator docs |
| developer product | 开发者产品 | creator-facing; in player text just name the item (道具, 礼包) |
| experience / game | 游戏 | Roblox UI mixes 体验 and 作品; in game text 游戏 reads naturally |
| obby | 跑酷 / 障碍跑酷 | players say 跑酷; never transliterate as 奥比 |
| tycoon | 大亨 | players also keep "tycoon" in Latin |
| simulator | 模拟器 | 蜂群模拟器 (Bee Swarm Simulator's Chinese name) |
| rebirth | 重生 | the term players use; 转生 also exists; never 再生 |
| pet | 宠物 | |
| egg / hatch | 蛋 / 孵化, 孵蛋, 开蛋 | not 鸡蛋 (a chicken egg) |
| coins | 金币 | not 硬币 (a physical coin) |
| gems | 宝石 | 钻石 if the art shows diamonds |
| boost | 加成 | not 提升 or 助推 when it is a multiplier bonus |
| multiplier, 2x | 倍率; 2 倍, 双倍 | "x2" also reads fine on badges |
| XP | 经验 / 经验值 | EXP in Latin is also common |
| level up / level | 升级 / 等级, 5 级, Lv.5 | |
| quest | 任务 | |
| leaderboard | 排行榜 | Roblox UI |
| AFK | 挂机 | Roblox's own UI says 闲置 for idle |
| noob | 萌新 | friendly; 菜鸟 is a mild tease, avoid in UI |
| OP | 强爆了, 太 OP 了 | OP is known to gamers; plain words are safer for kids (unverified for under-12s) |
| VIP | VIP | Latin |
| trade | 交易 | Pet Simulator 99's Chinese description: 交易宠物 |
| inventory / backpack | 背包 | Roblox UI: Backpack 背包, Inventory 道具库 |
| daily reward | 每日奖励 | |
| codes / redeem | 兑换码 / 兑换 | |
| group | 群组 | Roblox docs and DOORS' Chinese page. Players now see the Communities page (社区, renamed Nov 2024): 加入我们的社区 also fits |
| like | 点赞 | players and translated game pages: 请点个赞 |
| favorite | 最爱, 设为最爱 | Roblox client: 设为最爱, 添加至最爱. 收藏 is the generic app word; the roblox.com button label is unverified |
| server / private server | 服务器 / 私人服务器 | Roblox UI; players even call whole games 服务器 |
| friends | 好友 | Roblox renamed Connections back to Friends on 2026-04-02 (zh-hans newsroom: 好友, 可信好友). Older client strings still say 联系人: do not copy it |
| Premium / Roblox Plus | Premium / Roblox Plus | Latin. Roblox Plus replaced new Premium sign-ups on 2026-04-30; existing members keep Premium. Roblox writes Premium 会员, 仅限 Premium, Roblox Plus 订阅 |
| avatar | 虚拟形象 | Roblox UI |
| follow | 关注 | Roblox UI |

## Grammar traps in UI strings
- Plurals: none exist, so one string works for 0, 1 and 1,250. Never add 们 to things (金币们 is wrong): {count} 金币.
- Measure words: a number before a noun in a sentence needs a classifier (一只宠物, 一把剑, 一份奖励, 3 个蛋). Prefer the specific one over generic 个. Currency in UI drops it: 还差 {amount} 金币！
- Inserted nouns of unknown type ({pet}, {item}): skip the classifier or the wrong one shows (一只龙 vs 一条龙). 你孵出了{rarity}{pet}！ works for any pet.
- Adjacent Chinese params need no space or 的: {rarity}{pet} -> 传说小龙. Rarity words work as attributives without 的.
- Gender: spoken pronouns are the same, but written 他/她 differ. Never write a pronoun for {player}; repeat the name, use 对方, or restructure: “{player}”想和你交易.
- Word order: time and condition phrases go before the verb. "Come back in {time}" -> {time} 后再来; "Event ends in {time}" -> 活动将在 {time} 后结束.
- Aspect: completed actions take 了 or 已: “{player}”加入了游戏, 兑换码已过期。 Ongoing actions use 正在 or 中: 正在加入服务器, 加载中...
- Passives: English passives become active or use 已; avoid 被 except for bad things (你被踢出了服务器).
- No capitalization in Chinese; Latin terms keep their own case (Robux, VIP, Premium).

## Typography and formatting
- Use full-width punctuation inside Chinese text: ，。！？：；、 with no space around it. Roblox's zh-cn client strings do this throughout (35 full-width ！ to 0 half-width; ？：， the same). Microsoft's software convention (half-width ! ? : plus a space) does not match Roblox; do not follow it here.
- Use 、 for lists of items: 金币、宝石和宠物.
- Put a half-width space between Chinese and Latin words, digits and number {params}, as Roblox and Microsoft do: 购买 Robux, 已闲置 {RBX_NUM} 分钟, 还差 {amount} 金币！ No space next to full-width punctuation: 活动倒计时：{time}
- Player names: wrap {player} in “ ” with no spaces, Roblox's dominant pattern (54 of about 75 name params): “{player}”加入了游戏. The quotes set the name off, so no space is needed.
- Quotation marks: “ ” for names and labels (点击“领取”按钮); 《》 for game titles (《收养我吧！》).
- Ellipsis: three ASCII dots (加载中...), as Roblox (31 of 33 strings) and Microsoft do; …… is the print form. Never mix them in one game.
- Numbers: Arabic digits, comma thousands separator (1,250), percent with no space (+25%). Native large-number suffixes are 万 (10^4) and 亿 (10^8): 1.2万, 3.5亿 (no space; the suffix is part of the number). Gamers also read K/M/B; the formatter in game code decides, so tell the developer.
- Durations: units are 天, 小时, 分钟, 秒 (short form 时, 分): 2 天 5 小时, or 03:20:00 on timers. Write every {time} string so it reads correctly with either format; if {time} arrives as "3h 20m", flag it to the developer (a locale-aware formatter or a clock format fixes it) rather than blocking the translation.
- Multipliers: 2 倍 or 双倍 in prose; "x2" on a badge.
- Keys: 按 E; do not add 键 after a single key letter (Microsoft writes 按 Ctrl).
- Do not use the em dash: it looks like the character 一 (Microsoft's rule). Use ， or ：.
- No italics for Chinese; use <b> or color for emphasis.

## Do not translate / keep as is
- Roblox, Robux, Premium, Roblox Plus, VIP, Studio: Latin script. Do not use 罗布乐思 or 罗宝 (China-product names).
- Promo codes (FREEPETS), usernames, display names and keybinds (E, Shift, Space -> 空格键 is fine in prose).
- Game titles: use the developer's official Chinese title if one exists (Tower of Hell = 地狱之塔); otherwise keep the English title. Never half-translate a title or meme word.
- Meme and brand words with no settled Chinese form stay in Latin (Brainrot, Skibidi); mixing Latin into a Chinese line is normal.
- Write Simplified characters only: 游戏 not 遊戲, 宠物 not 寵物. Use mainland terms, not Taiwan ones: 通行证 not 特權券, 虚拟形象 not 虛擬人偶, 道具库 not 道具欄.

## Rendering on Roblox
- Roblox renders Chinese through a bundled CJK fallback font (Noto Sans CJK per a 2020 DevForum report, picking regional glyph shapes by the player's locale). Custom Latin fonts (Fredoka One, Gotham, Builder Sans) have no Chinese glyphs, so Chinese falls back while Latin letters and digits keep the custom font: expect mixed styles in one label.
- The 2023 Creator Marketplace font list has Noto Serif SC as its only Simplified Chinese font (no Noto Sans SC). Japanese fonts in it (M PLUS Rounded 1c) likely lack Simplified-only characters such as 们 and 这 (unverified per glyph): do not use them for zh-cn. There is no per-language font property; a game wanting a matching look swaps FontFace in code by locale.
- Bold or heavy weights may not carry over to the fallback font (unverified). Check headings for weight mismatch.
- TextScaled with Chinese had a staff-confirmed bug in 2019 (Chinese text did not scale; a fix was promised, never marked done); current status unverified. Test every TextScaled label at the smallest phone size.
- TextWrapped must break between characters because Chinese has no spaces; Roblox appears to do this, but whether it avoids starting a line with ，or。 is unverified.
- Dense characters blur at small sizes or with TextStroke: verify legibility of 12-14 px labels in Studio.
- In 2020, humanoid nameplates ignored the player's locale for glyph choice (fix unconfirmed); only glyph shapes differ, not readability.

## Mistakes machine translation makes here
- Transliterated genre words: 奥比 for obby (seen in a machine-translated Tower of Hell page) -> 跑酷.
- Mangled meme titles: half-translated "Steal a Brainrot" pages produce gibberish -> keep the English title.
- Literal eggs: 打开鸡蛋 -> 开蛋 / 孵蛋.
- "Claim" as 认领 or 要求 -> 领取. "Boost" as 助推 -> 加成. "Coins" as 硬币 -> 金币.
- Formal register: 您的奖励已准备就绪 -> 你的奖励来啦！
- Half-width punctuation glued to Chinese: 你准备好了吗? -> 你准备好了吗？
- Traditional characters or Taiwan terms leaking in: 遊戲通行證 -> 游戏通行证.
- "Friends" as 朋友 in social features -> 好友; "Connections" as 连接 or 联系人 -> 好友 (Roblox's name again since April 2026).
- "Play" as bare 玩 on a button -> 开始游戏.
- "On" toggle as 在 -> 开启 (off: 关闭).
- Pronoun overload: 你的背包是满的 -> 背包已满！
- Word-for-word idioms: "Drum roll..." -> 请稍等... (Microsoft's own example: rewrite, do not calque).

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | 开始游戏 | bare 玩 sounds wrong on a button |
| shop.title | 商店 | |
| shop.buy | 购买 | Roblox UI word |
| reward.claim | 领取 | |
| rebirth.button | 重生 | |
| rebirth.confirm | 确定要现在重生吗？你的金币会清零，但会获得永久 {multiplier} 倍加成。 | "lose" -> 清零 (reset to zero) |
| coins.need_more | 还差 {amount} 金币！ | works for 1 and any number |
| coins.count | {count} 金币 | |
| egg.hatched | 你孵出了{rarity}{pet}！ | no classifier, no space between Chinese params |
| rarity.legendary | 传说 | tier set: 普通, 稀有, 史诗, 传说, 神话 |
| pet.name.dragon | 小龙 | cute pet form; 巨龙 for an epic tone |
| chat.player_joined | “{player}”加入了游戏 | name in “ ”, no spaces, as Roblox's own join messages |
| trade.request | “{player}”想和你交易 | |
| prompt.open_shop | 按 E 打开 | 按 E 打开商店 also fits (7 chars) |
| pass.buy_price | {price} Robux 购买 | compact price-first shop button (as in 60 钻石购买); 花 {price} Robux 购买 is the chattier alternative. Native check wanted |
| pass.coins2x | 双倍金币 | |
| pass.vip | VIP | kept |
| reward.daily_title | 每日奖励 | |
| reward.come_back | {time} 后再来领取下一份奖励！ | time moved to front; ask for a Chinese {time} format |
| codes.placeholder | 输入兑换码 | |
| codes.invalid | 兑换码无效或已过期。 | |
| social.like_reward | 给游戏点赞，免费领取<b>幸运药水</b>！ | |
| social.group_reward | 加入我们的群组，即可解锁免费奖励！ | 社区 instead of 群组 matches the Communities page players see |
| afk.warning | 你已挂机！动一动才能继续赚钱！ | |
| leaderboard.title | 玩家排行榜 | "Top Players" as 顶级玩家 reads translated |
| level.up | 升级啦！你已达到 {level} 级。 | |
| tutorial.sell | 走进发光的圆圈，即可出售宠物。 | |
| inventory.full | 背包已满！出售一些宠物来腾出空间吧。 | |
| settings.music | 音乐 | |
| settings.on | 开启 | Roblox UI; off is 关闭 |
| loading | 加载中... | house choice: 加载 is the mainland word (Roblox itself writes 加载失败); its 正在载入... is also fine |
| event.ends_in | 活动倒计时：{time} | standard banner wording; 活动将在 {time} 后结束 also fits |
| item.op | 这把剑强爆了！ | 这把剑太 OP 了！ also works for older players |
| friends.boost | 本服务器每有一位好友，就能获得 +{percent}% 加成 | 好友, not 联系人 |

## Sources
1. Microsoft Simplified Chinese Localization Style Guide -- https://aka.ms/chinese-simplified-styleguide
2. Unicode CLDR language plural rules chart -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox client CoreScript translations (zh-cn, zh-tw, zh-cjv columns), mirrored by Roblox-Client-Tracker -- https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/translations/CoreScriptLocalization.csv
4. Roblox creator docs, zh-cn passes page -- https://create.roblox.com/docs/zh-cn/production/monetization/passes
5. Roblox creator docs, zh-cn groups page -- https://create.roblox.com/docs/zh-cn/projects/groups
6. About Roblox, zh-hans (machine-translated) -- https://about.roblox.com/zh-hans/what-is-roblox
7. Roblox game name/description API, zh-hans entries for Pet Simulator 99, Adopt Me!, Tower of Hell, Grow a Garden, Brookhaven, Bee Swarm Simulator, MM2, DOORS, Dress to Impress, Steal a Brainrot -- https://gameinternationalization.roblox.com/v1/name-description/games/{universeId}
8. TapTap Roblox forum, game recommendations thread (player vocabulary) -- https://www.taptap.cn/moment/15209170907170260
9. DevForum, Broken Foreign Language Text Scaling (2019) -- https://devforum.roblox.com/t/broken-foreign-language-text-scaling/246203
10. DevForum, Humanoid names do not render with correct CJK glyphs (2020) -- https://devforum.roblox.com/t/humanoid-names-do-not-render-with-correct-cjk-glyphs/674438
11. DevForum, Fonts in Creator Marketplace + 81 New Fonts (2023) -- https://devforum.roblox.com/t/fonts-in-creator-marketplace-81-new-fonts/2164977
12. DevForum, Add more CJK fonts request (2026) -- https://devforum.roblox.com/t/add-more-cjk-fonts-as-well-as-different-font-properties-for-each-language/4566304
13. Roblox Newsroom (zh-hans), Connections renamed back to Friends, 2026-04-02 -- https://about.roblox.com/zh-hans/newsroom/2026/04/expanding-trusted-friends
14. Roblox Newsroom (zh-hans), Introducing Roblox Plus, 2026-04-10 -- https://about.roblox.com/zh-hans/newsroom/2026/04/introducing-roblox-plus-subscription
