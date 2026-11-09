# Japanese (ja-jp) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `ja-jp` (a bare `ja` column is optional; Japanese has one variant, so it may carry the same text) |
| Script, direction | Japanese: kanji + hiragana + katakana, Latin digits; horizontal LTR |
| Address the player as | no pronoun at all; not あなた (stiff, though Roblox's system text uses it), never 君 or お客様 |
| Text expansion vs English | 40-60% of the English character count, but each character is wide: pixel width about equal overall (measured on the reference set: Builder Sans +5%, Fredoka One -4%); short katakana labels up to +50% (ショップ vs Shop) |
| Plural categories (CLDR) | other (only one form) |
| Model confidence | high: plenty of training data; the usual misses are register, kanji level and gaming terms |
| Native review before shipping | recommended |

## Audience and register
Japanese Roblox players are mostly elementary and junior-high kids who also play Nintendo and mobile games. Aim for the voice of a polished Japanese kids' game: short, warm, energetic. Pick the form by string type and never mix plain and polite inside one string:
- Buttons, labels, titles: a noun or a dictionary-form verb, no です/ます. 購入, ショップ, 受け取る.
- Reactions to the player's own action: plain form plus ！. レベルアップ！ / タマゴから生まれた！ / コインが足りない！
- Questions, confirmations, system notices, errors: です/ます. 転生しますか？ / このコードは無効です。
- Calls to action (banners, tutorials, AFK nudges): volitional ～しよう！, or ～てね！ for a soft invitation. コミュニティに参加しよう！ / また来てね！
- Never use keigo (ご購入いただけます, なさいます) or business phrasing; it reads like a bank. Use 購入できます.
- Avoid ～してください on fun text; keep it for real instructions or errors.
- Kanji level: kids read elementary-school kanji. Prefer those; write harder words in kana or swap the word. 稼ぐ -> かせぐ, 獲得 -> ゲット / もらう, 孵化 -> 生まれる. Keep 購入 and 報酬 although 購 and 酬 are junior-high kanji: Roblox's own ja UI uses both (and ゲット), so kids know them by sight. ごほうび / 買う only in a game aimed at the youngest players.
- Drop "you". "You hatched a dragon!" -> ドラゴンが生まれた！, not あなたはドラゴンを孵化させました。

## Roblox and gaming vocabulary
| English | Use in ja-jp | Note |
|---|---|---|
| Robux | Robux | Latin script, as in Roblox's ja UI and docs. Players say ロバックス; don't write that in UI |
| game pass | ゲームパス | Roblox's ja UI and docs say パス (パスを追加); alone it is vague in a shop |
| developer product | the item's name | docs say デベロッパー製品; players never see that word |
| experience / game | ゲーム | Roblox's ja UI says バーチャル空間, but its newer strings switch to ゲーム; players say ゲーム |
| obby | アスレチック | players call obbies アスレ(チック); "Obby" only in parentheses |
| tycoon / simulator | タイクーン / シミュレーター | keep the long vowel ー on -er words |
| rebirth | 転生 | the usual Japanese term for a reset-for-bonus (what Japanese Roblox players say aloud is unverified). Not リバース in UI: it is also slang for throwing up. Never 再生 (= playback) |
| pet | ペット | |
| egg / hatch | タマゴ / 生まれる | タマゴから〇〇が生まれた！ 孵化 is fine for teens but 孵 is hard kanji |
| coins / gems | コイン / ジェム | count coins with 枚: 100枚. Pick ジェム or 宝石 once per game |
| boost / multiplier | ブースト / 倍 | 2x -> 2倍, 1.5x -> 1.5倍 |
| XP / level up | 経験値 (EXP on tiny labels) / レベルアップ | |
| quest | クエスト | ミッション for short daily tasks |
| leaderboard | ランキング | Roblox's ja charts page is ランキング; its in-game player list is スコアボード. Not リーダーボード |
| AFK | 放置 | 放置中 = idle; AFK is understood by teens but 放置 is clearer |
| noob | 初心者 | never 雑魚 (an insult) |
| OP | 強すぎ / 最強 | ぶっ壊れ (性能) is gamer slang for older players; never leave "OP" |
| VIP | VIP | Latin, never ブイアイピー |
| trade | トレード | トレードリクエスト, built like Roblox's 友達リクエスト |
| inventory / backpack | 持ち物 / バックパック | Roblox's ja UI: Inventory = 持ち物リスト, Backpack = バックパック |
| daily reward | ログインボーナス | the Japanese game term for a once-a-day claim; デイリー報酬 only for rewards earned by daily tasks |
| codes | コード | コードを入力 / コードを使う |
| group | コミュニティ | Roblox renamed groups to communities; its ja UI says 公式コミュニティに参加する. Not グループ |
| like / favorite | いいね / お気に入り | Roblox's ja UI: 「いいね」した, 投票 for voting, お気に入り. 高評価 there is only the Top Rated sort |
| server / private server | サーバー / プライベートサーバー | as in Roblox's ja UI |
| friends | 友達 | Roblox's ja UI since the April 2026 return to Friends: 友達, 友達リクエスト, 友達を追加. During the 2025 Connections period it showed つながり. フレンド is common in other Japanese games but is not Roblox's word |
| Premium | プレミアム | Roblox's ja UI: Robloxプレミアム, プレミアム限定 |
| shop | ショップ | Roblox's own store tab is ストア; either is fine, be consistent |

## Grammar traps in UI strings
- Plurals: none. "{count} Coins" -> {count}コイン works for 0, 1 and 1,250. Add a counter when it reads better: あと{amount}枚.
- Gender: none in Japanese. Add さん after other players' names in notices, as Roblox's own ja UI does ({RBX_NAME}さんに友達リクエストを送りますか？): {player}さんが参加しました. Never add it to the player's own name or to item names.
- Particles attach straight to placeholders, no space: {player}さんから / {pet}が / {level}に. Check the particle fits every value the slot can hold.
- Word order is verb-last, and the English order rarely survives. "Buy for {price} Robux" -> {price} Robuxで購入.
- Modifier before noun: an adjective slot like {rarity} breaks if rarity words are nouns (レジェンダリーの / レアな). Use a tag bracket instead: 【{rarity}】{pet}.
- Numbers + counters: 1人, 2倍, 3時間. "each friend" -> 友達1人につき.
- No capitalization in Japanese; Latin words keep their case (VIP, Robux).
- Durations, a rule for game code: "3h 20m" looks foreign, so a ja build formats {time} with Japanese units, 3時間20分 / 2日5時間 / 45秒, no spaces. reward.come_back and event.ends_in below assume it. If the game can't, keep the string short so the English format still reads.

## Typography and formatting
- Sentence punctuation is full width: 。、！？ Japanese games use full-width ！ and ？, and so does most of Roblox's own ja UI (友達リクエストを送信しますか？). Microsoft's guide prescribes half-width ! and ?, which suits software, not games. No space before them.
- When a sentence follows ！ or ？ on the same line, no space is needed in tight UI: レベルアップ！レベル5になった！
- No space between Japanese and digits or Latin words in game UI: 100コイン, Eキー (Microsoft's software guide adds one; game UI doesn't). Keep a half-width space between a number and a Latin word: 100 Robux, as Roblox writes {robux} Robux.
- Digits are half width (12, not １２). Thousands comma as in English: 1,250. Percent stays half width with no space: 50%.
- Quotes: 「」 for a name or text to type, 『』 for titles. Do not use "".
- Brackets: 【】 for tags and categories (【レジェンダリー】), half-width () for short asides.
- Ellipsis: three half-width periods, as Roblox's own ja UI writes it (読み込み中..., テレポート中...). The single … glyph also renders; just don't mix the two in one game.
- Range: 1から10 reads clearest for kids; 1～10 also renders fine on Roblox (Microsoft's build-error warning about ～ is about software builds, not a Roblox table).
- Line breaks: there are no spaces, so Roblox wraps between any two characters, even mid-word (see Rendering). Put a manual line break after a clause in long text.
- Keyboard keys: Latin, half width, + キー: Eキー.

## Do not translate / keep as is
- Robux, Roblox, VIP, promo codes (FREEPETS), usernames and display names, keybinds (E, Shift). Premium is translated: プレミアム, as in Roblox's ja UI.
- Game title: keep the English title (Pet Hatch Tycoon) unless the owner gives a Japanese one; a katakana reading can follow once in a description, never in UI.
- Item and pet names do get translated, usually into katakana (Lucky Potion -> ラッキーポーション, Dragon -> ドラゴン). Use katakana for loanwords, not romaji.
- Script: Japanese only. Never paste simplified or traditional Chinese forms (设置 -> 設定, 开始 -> 開始).
- Fill every key: Roblox auto-translates Japanese, and a missing key gets a machine string that may clash with your terms.

## Rendering on Roblox
Checked 2026-11-08 in Studio and in the PC client files; mobile clients unverified.
- Roblox's Latin fonts (Builder Sans, Fredoka One, Luckiest Guy, Gotham and so on) have no kana or kanji; Japanese falls back to Noto Sans CJK JP. The PC client ships NotoSansCJKjp-Regular.otf and a "NotoSansCJK Fallback" family, so kanji draw in Japanese forms. Expect plain sans-serif Japanese next to stylized Latin.
- RichText <b> and a Bold FontFace weight do bold the Japanese fallback (tested with Builder Sans, Fredoka One, Luckiest Guy and Gotham). Next to a heavy one-weight font like Fredoka One, plain Japanese looks thin; <b> or a Bold weight evens it out.
- TextWrapped breaks Japanese between any two characters, even mid-word (レベ / ル5). It keeps 。、！ and ー off the start of a line by carrying the previous character down; small kana like っ may still start a line.
- Each kana or kanji is 0.7 x TextSize wide; Builder Sans Latin averages about 0.4. One Japanese character takes the room of nearly two Latin ones, so max lengths in characters undercount Japanese width; judge by pixels.
- TextScaled: dense kanji (購, 報酬, 期限) blur first at small sizes; check 4-character buttons (受け取る) on a phone.
- No per-language font property exists (DevForum, April 2026), so a game wanting a cuter Japanese font must swap FontFace in code.

## Mistakes machine translation makes here
- あなた everywhere: あなたはレベル5になりました -> レベル5になった！
- Over-polite keigo: ご購入いただけます -> 購入できます
- Rebirth as 再生 or 復活: 再生する -> 転生する
- Experience as 経験 or 体験: この体験をお気に入りに追加 -> このゲームをお気に入りに追加
- Claim as 請求 or 主張: 請求 -> 受け取る
- Circle as 円, which reads as yen next to "sell": 光る円 -> 光る輪
- Free as フリー (= unrestricted): フリーのポーション -> 無料のポーション
- Hatch as ハッチ: ドラゴンをハッチした -> ドラゴンが生まれた！
- "2x" kept or as 2回 (= twice): 2回コイン -> コイン2倍
- Mixed register in one string: 転生しますか？コインはなくなるよ -> 転生しますか？コインはなくなります。
- Like as 好き or 気に入る: ゲームを好きになって -> ゲームに「いいね」して
- Old platform words: グループに参加 -> コミュニティに参加; フレンド -> 友達 (Roblox's current ja UI)

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | プレイ | Roblox's own Play button reads 参加 (join a server); inside a game's menu プレイ or スタート is right |
| shop.title | ショップ | |
| shop.buy | 購入 | Roblox's own Buy button says 購入; 買う for a very young audience |
| reward.claim | 受け取る | |
| rebirth.button | 転生 | |
| rebirth.confirm | 転生しますか？コインはなくなりますが、ずっと続く{multiplier}倍ブーストがもらえます！ | ずっと続く = permanent, kid-friendly; {multiplier}倍 works for 2 and 1.5 |
| coins.need_more | コインがあと{amount}枚足りない！ | 枚 counter; fine for 1 |
| coins.count | {count}コイン | no plural form needed |
| egg.hatched | 【{rarity}】{pet}が生まれた！ | brackets avoid the の/な problem with any rarity word |
| rarity.legendary | レジェンダリー | standard game rarity tier; 伝説 if the game uses kanji tiers |
| pet.name.dragon | ドラゴン | |
| chat.player_joined | {player}さんがゲームに参加しました | さん for other players |
| trade.request | {player}さんからトレードリクエストが届きました | compound like Roblox's 友達リクエスト; 39 chars with a 20-char name |
| prompt.open_shop | Eキーで開く | |
| pass.buy_price | {price} Robuxで購入 | |
| pass.coins2x | コイン2倍 | Japanese order: thing + 倍 |
| pass.vip | VIP | |
| reward.daily_title | ログインボーナス | what Japanese games call a daily claim; kids know it as ログボ |
| reward.come_back | 次の報酬まであと{time}！また来てね！ | needs {time} as 3時間20分 |
| codes.placeholder | コードを入力 | |
| codes.invalid | そのコードは無効か、期限切れです。 | |
| social.like_reward | ゲームに「いいね」して<b>ラッキーポーション</b>を無料でもらおう！ | Roblox's ja UI quotes 「いいね」 as the action name; item name translated |
| social.group_reward | 公式コミュニティに参加して無料の報酬をゲットしよう！ | Roblox now says コミュニティ; 公式コミュニティ is its label for a game's own group |
| afk.warning | 放置中！動いてかせぎ続けよう！ | かせぐ in kana |
| leaderboard.title | ランキング | Japanese term for a leaderboard |
| level.up | レベルアップ！レベル{level}になった！ | |
| tutorial.sell | 光る輪の中に入って、ペットを売ろう！ | 輪, not 円 (= yen) |
| inventory.full | バックパックがいっぱい！ペットを売って空きを作ろう！ | バックパック as in Roblox's ja UI |
| settings.music | BGM | the usual Japanese settings label; 音楽 also fine |
| settings.on | オン | pair with オフ |
| loading | 読み込み中... | Roblox's own Loading... string, word for word |
| event.ends_in | イベント終了まであと{time} | |
| item.op | この剣、強すぎる！ | OP dropped; ぶっ壊れ for an older audience |
| friends.boost | サーバー内の友達1人につき+{percent}%ブースト | 友達, Roblox's ja word for friends |

## Sources
1. Microsoft Japanese Localization Style Guide: https://aka.ms/japanese-styleguide
2. CLDR Language Plural Rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox game page in Japanese (Adopt Me!) and the ja localization bundles it loads (いいね, 投票, コミュニティ, 友達, 参加, ランキング): https://www.roblox.com/ja/games/920587237/Adopt-Me
4. Roblox Creator docs ja-jp, Passes: https://create.roblox.com/docs/ja-jp/production/monetization/passes
5. Roblox Creator docs ja-jp, Engagement-based payouts: https://create.roblox.com/docs/ja-jp/production/monetization/engagement-based-payouts
6. Roblox Creator docs ja-jp, Automatic translations: https://create.roblox.com/docs/ja-jp/production/localization/automatic-translations
7. DevForum, "Friends Are Back!" (2026-04-02): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217/1
8. Japanese Wikipedia, Roblox: https://ja.wikipedia.org/wiki/Roblox
9. Japanese beginner's guide to Roblox (obby = アスレチック): https://lifestyle.assist-all.co.jp/?p=74572
10. DevForum, "Add more CJK fonts..." (2026-04-09): https://devforum.roblox.com/t/add-more-cjk-fonts-as-well-as-different-font-properties-for-each-language/4566304
11. Roblox PC client, read 2026-11-08: ExtraContent/translations/CoreScriptLocalization.csv (in-game ja UI: 友達, つながり, バックパック, スコアボード, 購入, 読み込み中...) and PlatformContent/pc/fonts/NotoSansCJKjp-Regular.otf: shipped with every client install
12. Studio tests, 2026-11-08: TextService bounds and screen captures of Japanese with <b>, Bold weight and TextWrapped: run for this guide
