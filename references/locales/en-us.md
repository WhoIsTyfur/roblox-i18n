# English (United States) (en-us) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `en-us`, plus the bare `en` column (default variant), so English players whose locale has no column get this text. If English is the game's source, the tool copies the source into both columns verbatim: source flaws ship unless the source itself is fixed |
| Script, direction | Latin, LTR |
| Address the player as | "you", with contractions ("You're", "You'll"); never "the player" or "one" |
| Text expansion vs English | Baseline. Into English from European sources text usually gets shorter. From Chinese, Japanese or Korean the character count grows a lot, but each CJK character is about two Latin letters wide, so on-screen width grows far less (W3C; exact ratio unverified) |
| Plural categories (CLDR) | Cardinal: one, other. Ordinal: one, two, few, other (1st, 2nd, 3rd, 4th) |
| Model confidence | high -- the model's strongest language; the risks are UK drift and Roblox renaming platform terms in 2024-2026 |
| Native review before shipping | optional |

## Audience and register
US Roblox players are mostly 9-16. They skim, and expect the voice of a front-page game: short, upbeat, second person.
- Contractions always: "You're AFK", not "You are AFK". "You can't trade yet", not "Trading is not possible".
- Buttons are a bare imperative verb: "Buy", "Claim", "Equip", "Auto Hatch". Not "Buying", "Click to Buy", "Purchase".
- Plain words over formal ones: buy (not purchase), get (not obtain), use (not utilize), start (not commence), "Not enough coins!" (not "Insufficient funds").
- Hype stays short: "Nice!", "New record!", "So lucky!". Not "Congratulations on your achievement."
- One "!" at most, and only on wins, rewards and calls to action. Errors stay calm: "That code is invalid or expired."
- Kid-safe: no swearing; "defeat" over "kill" in a cute game; "noob" only on items or self-jokes ("Noob Sword"), never aimed at the player. Skip fast-dating slang ("rizz", "skibidi") unless the game is built on that meme.

### Writing English source strings that localize well
English is usually the source language, and every other column is translated from it. Source strings decide what translators can do.
- One full sentence per entry, with named params filled by `FormatByKey`. Bad: `"You need " .. n .. " more coins!"`. Good: `Not enough coins! Need {amount} more.`
- Never build words in code: no `"coin" .. "s"`, no `rarity .. " " .. pet`. Other languages change word order, gender and case.
- Plural-proof the English too: tables have no plural forms, so "{count} Coins" shows "1 Coins". Write `Coins: {count}`.
- No bare one-word strings with two meanings. "Back" (go back, or the body part), "Open" (verb or state), "Free", "Light", "On" (toggle or preposition) each need their own key and a Context note, e.g. `settings.on` = "toggle state, pairs with Off".
- One string, one role: a "Rebirth" button and a "Rebirth" panel title get separate keys, even if the English matches.
- Keep each `<b>` tag around a whole phrase inside one entry; never split a sentence across entries to style part of it.
- Descriptive param names: `{player}`, `{amount}`, `{time}`, not `{1}`. Pass numbers already formatted ("1,250").
- Explain slang and puns in Context: "OP = overpowered". Translators cannot ask a toast what it meant.
- Turn AutoLocalize off on usernames, chat and leaderboards so names don't flood the table.
- For a ProximityPrompt, put only the verb in ActionText ("Open"); Roblox draws the right key or button per device, so "Press E" stays out of the string.

## Roblox and gaming vocabulary
| English term | use in en-us | note |
|---|---|---|
| Robux | Robux | Same form for singular and plural: "1 Robux", "100 Robux". Never "Robuxes", "R$" in sentences |
| game pass | Pass / Game Pass | Roblox's Creator Hub docs now say "Passes"; players write "gamepass". Shop tab: "Passes" |
| developer product | (the item's name) | Players never see this term. Say "Coin Pack", "Lucky Potion", "Item" |
| experience / game | game | Roblox switched back to "games" (about April 2026, exact date unverified). Checked 2026-11-08: roblox.com's charts page is titled "Top Roblox Games"; the Roblox Plus announcement and Creator Hub article text say "game" |
| obby, tycoon, simulator | obby, tycoon, simulator | Lowercase mid-sentence; "sim" is casual. Capitalize in titles |
| rebirth | Rebirth / rebirth | Noun and verb: "Rebirth now?", "3 rebirths". Keep the game's own term if it says Prestige or Ascend |
| pet, egg, hatch | pet, egg, hatch | "Hatch", "Auto Hatch", "Hatch 3"; "Egg" in item names ("Forest Egg") |
| coins, gems | coins, gems | Lowercase mid-sentence ("Earn more coins!"), capitalized in labels and titles ("Coins: 1,250") |
| boost, multiplier | boost, multiplier | "2x Coins Boost", "+25% boost" |
| XP, level up | XP, Level up! | "XP" caps, no periods. "level up" is the verb, "level-up" the noun or adjective ("level-up reward") |
| quest | Quest / Quests | Some games use "Mission" or "Task"; follow the source game |
| leaderboard | Leaderboard / Top Players | "Top Players" is the canonical source's title; "Most Coins" style titles are common too (observed, unverified) |
| AFK, noob, OP, VIP | AFK, noob, OP, VIP | Keep exactly. AFK, OP, VIP in caps; "noob" lowercase unless it starts a title |
| trade | Trade / trading | "Trade", "Trade Request", "Accept", "Decline" |
| inventory / backpack | Backpack (tools), Inventory or Pets (storage) | Roblox's own hotbar is the Backpack; keep the source game's word |
| daily reward | Daily Reward | Also "Daily Spin", "Streak" |
| codes | Codes, Redeem, Enter code | Button "Redeem" or "Claim"; codes themselves never change |
| group | community | Default when translating into English: Roblox renamed player-facing Groups to Communities on Nov 21, 2024, so players see "Community" on the page they join. Creator Hub and the APIs still say Group. In an English-source game, keep the source's word |
| like / favorite | Like / Favorite | Two different buttons (thumbs up, star). US spelling "Favorite", never "Favourite" |
| server | server, private server | "Server Luck", "Join a private server" |
| friends | friends | Roblox renamed Friends to Connections in 2025, then back to Friends in April 2026 and told creators to use "Friends" in game UI. Never write "connections" |
| Premium | Premium (legacy) / Roblox Plus | Roblox Plus launched April 30, 2026 and new Premium sign-ups stopped with it; existing members keep Premium. Games can detect Plus (`MarketplaceService:GetRobloxSubscriptionDetailsAsync`, field `IsSubscribed`), so "Plus perk" strings are fine where the game checks it. A perk gated on `MembershipType.Premium` stays labeled Premium |

## Grammar traps in UI strings
- Plurals with {count}: no plural selection, and {count} can be 0 or 1. Use a label or drop the counted noun. Bad: `You have {count} pets` ("1 pets"). Good: `Pets: {count}` or `Pets owned: {count}`. Never "pet(s)".
- a/an before a param: "a {rarity} {pet}" gives "a Epic Dragon", "a Uncommon Owl". Rephrase: `New pet: {rarity} {pet}!`. Keep "a/an" only before a fixed word: "a permanent {multiplier}x boost".
- Gender: English needs none, except pronouns. Repeat the name or use "they": `{player} left the trade.`, not "...his trade".
- Possessive: `{player}'s pet` works for every name, including ones ending in s or digits. Never `{player}' pet`.
- Ordinals: "{rank}th" breaks for 1, 2, 3, 21, 22, 23. Write `#{rank}` or `Rank {rank}`.
- Word order from Romance sources: adjective first. "Dragon Legendary" -> "Legendary Dragon"; "Potion of Luck" -> "Lucky Potion".
- Verb vs noun spelling: "level up" / "level-up", "log in" / "login", "set up" / "setup", "power up" / "power-up".
- Capitalization (house rule): keep the source game's casing. With no English source to follow, use Title Case for titles, tabs, product names and multi-word buttons ("Daily Reward", "Top Players", "Auto Hatch"), as the canonical source does. Microsoft prefers sentence case on UI labels, but that is productivity-app advice. Inside Title Case keep a, an, the, and, but, or, and prepositions of four letters or fewer (to, of, in, on, for, with, from) lowercase unless first or last. Sentence case for every sentence, toast, tutorial line and placeholder ("Enter code"). No Title Case On Whole Sentences.
- Inserted item names keep their capitals mid-sentence: "Like the game to get a free Lucky Potion!"

## Typography and formatting
- No space before ! ? : ; or %. One space after a sentence. Oxford comma in lists: "coins, gems, and pets".
- Never "!!" or "?!". One "!" per string at most.
- Quotes: double quotes, with periods and commas inside: Type "FREEPETS" to claim. Use straight ' and " in strings to match the source; Roblox matches source text exactly, so "You're" with a curly apostrophe is a different entry.
- Numbers: comma for thousands, period for decimals: 1,250 and 1.5x. Convert literal numbers from European sources ("1.250" -> "1,250", "1,5x" -> "1.5x"). HUD abbreviations: 1.2K, 3.4M, 5B, capital letter, no space.
- Multiplier: "2x" (lowercase x, no space), as the canonical source writes it; "x2" only if the game already uses it. That "2x" is the more common US form is observed practice (unverified). Percent: "+25%".
- Durations: "3h 20m", "2d 5h", "45s": no periods, no space between number and unit. In full sentences spell units out: "in 3 hours".
- Clock times 12-hour with AM/PM: "5:00 PM". Dates with the month as a word: "Nov 8" or "November 8", never "11/8" or "08/11".
- Ellipsis: three periods, no space before: "Loading...".
- Avoid dashes in UI strings; use a period or colon instead.
- Keys: capital letter, no quotes: "Press E to open", "Hold Shift to sprint". Prefer device-neutral verbs ("Select", "Use") over "Click" or "Tap" when the string shows on every device.

## Do not translate / keep as is
- "Roblox" and "Robux" exactly as written; never translate, abbreviate or pluralize Robux.
- Game titles ("Pet Hatch Tycoon"), promo codes ("FREEPETS", case and all), display names, keybinds (E, Shift, Space).
- Gamer acronyms stay caps: AFK, OP, VIP, XP, NPC.
- Meme and brand names keep their original spelling, even when not English: "Tung Tung Tung Sahur", "Tralalero Tralala".
- Translating INTO en-us from another source: give items, pets and places natural English names ("Poción de la Suerte" -> "Lucky Potion"), unless the developer marks them as names to keep.
- If a game ships only `en`, UK players see US spelling; that is expected. `en-gb` has its own guide.

## Rendering on Roblox
- Plain English (ASCII) has no glyph risk in Builder Sans, Roblox's platform font, or the common fonts. Gotham and Arial were scheduled for removal on May 28, 2024, with games still set to them auto-swapped to Montserrat and Arimo.
- Real risks are layout, not glyphs: TextScaled shrinks a long sentence until it is unreadable, and many display fonts run wider than Builder Sans (unverified per font). In Studio, check each string at its max length on a phone-size viewport.
- `<b>` and other tags show as raw text unless the TextLabel has RichText on. Check the banner with the Lucky Potion string.
- Full coverage in every catalog display font is unverified; straight quotes and apostrophes are the safest choice there, curly quotes and symbols like the ellipsis character are not.

## Mistakes machine translation makes here
- UK spelling and words: "Favourite", "Colour", "Armour", "Mum", "Maths", "Sweets" -> "Favorite", "Color", "Armor", "Mom", "Math", "Candy".
- False friends from Spanish/Portuguese: "Cargando..." -> "Charging..." -> "Loading..."; "Actualmente tienes 5 mascotas" -> "Actually you have 5 pets" -> "You have 5 pets".
- "ganar/ganhar" always as "win": "Win coins by selling pets" -> "Earn coins by selling pets". Win is for matches and prizes.
- German "bekommen": "You become 100 coins" -> "You get 100 coins".
- Over-formal calques: "Do you wish to realize the rebirth?" -> "Rebirth now?"; "Insufficient coins" -> "Not enough coins!"
- Dropped articles and plurals from Russian, Polish, Chinese, Japanese, Korean sources: "Sell pet to make place" -> "Sell pets to make room."
- Outdated or literal platform terms: "experience" -> "game", "connections" -> "friends", "Robuxes" -> "Robux", "Experience Points" -> "XP", "Pass of game" -> "Game Pass".
- French "Renaissance" or Spanish "Renacer" rendered as "Rebirthing" or "Reborn": the button is "Rebirth".
- Number formats copied from the source: "1.250 Coins", "x1,5" -> "1,250 coins", "1.5x".
- Title Case or caps on sentences: "You Need More Coins To Buy This" -> "You need more coins to buy this."
- Punctuation inflation from the source: "¡¡Nuevo récord!!" -> "New record!!" -> "New record!"

## Reference translations
This is the source language, so a line identical to the source needs no note. Three lines fix source flaws ("1 coins", "a Epic"): they show what to write when translating into English from another language, and what to propose to the developer when English is the source.

| key | translation | note |
|---|---|---|
| menu.play | Play | |
| shop.title | Shop | |
| shop.buy | Buy | |
| reward.claim | Claim | |
| rebirth.button | Rebirth | |
| rebirth.confirm | Rebirth now? You'll lose your coins but get a permanent {multiplier}x boost. | "a" sits before "permanent", so it never touches the number |
| coins.need_more | Not enough coins! Need {amount} more. | Rephrased: the source gives "You need 1 more coins!" when amount is 1 |
| coins.count | Coins: {count} | Rephrased: "{count} Coins" shows "1 Coins" |
| egg.hatched | New pet: {rarity} {pet}! | Rephrased: "a {rarity}" gives "a Epic". Also fits 40 with a 12-letter rarity and 14-letter pet, which the source does not. Keep the source wording only if no rarity starts with a vowel sound |
| rarity.legendary | Legendary | |
| pet.name.dragon | Dragon | |
| chat.player_joined | {player} joined the game | No period, like other system lines |
| trade.request | {player} wants to trade with you | |
| prompt.open_shop | Press E to open | If this is a ProximityPrompt, ship ActionText "Open" and let Roblox draw the key |
| pass.buy_price | Buy for {price} Robux | |
| pass.coins2x | 2x Coins | |
| pass.vip | VIP | |
| reward.daily_title | Daily Reward | |
| reward.come_back | Come back in {time} for your next reward! | |
| codes.placeholder | Enter code | Sentence case for placeholders |
| codes.invalid | That code is invalid or expired. | No "!" on errors |
| social.like_reward | Like the game to get a free <b>Lucky Potion</b>! | |
| social.group_reward | Join our community to unlock a free reward! | Roblox's player-facing name since Nov 2024. In an English-source game the source "group" is copied as is; "group" also if the game's other UI still says group |
| afk.warning | You're AFK. Move to keep earning! | |
| leaderboard.title | Top Players | |
| level.up | Level up! You're now level {level}. | |
| tutorial.sell | Walk into the glowing circle to sell your pets. | |
| inventory.full | Your backpack is full! Sell pets to make room. | |
| settings.music | Music | |
| settings.on | On | Toggle state; pairs with "Off" |
| loading | Loading... | |
| event.ends_in | Event ends in {time} | |
| item.op | This sword is OP! | Kept as gamer slang |
| friends.boost | +{percent}% boost for each friend in your server | "friend", not "connection" (Roblox reverted in April 2026) |

## Sources
1. Microsoft Localization Style Guides index (points English apps to the Writing Style Guide): https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
2. Microsoft Writing Style Guide, Top 10 tips (contractions, sentence case, Oxford comma): https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice
3. Microsoft Writing Style Guide, Capitalization: https://learn.microsoft.com/en-us/style-guide/capitalization
4. Microsoft Writing Style Guide, Numbers: https://learn.microsoft.com/en-us/style-guide/numbers
5. Microsoft Writing Style Guide, Exclamation points: https://learn.microsoft.com/en-us/style-guide/punctuation/exclamation-points
6. Microsoft Globalization, String concatenation: https://learn.microsoft.com/en-us/globalization/internationalization/concatenation
7. CLDR plural rules (en cardinal and ordinal): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
8. Roblox DevForum, "Friends Are Back!" (April 2, 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217/1
9. Roblox DevForum, "Introducing Roblox Communities" (Nov 21, 2024): https://devforum.roblox.com/t/introducing-roblox-communities/3268307
10. Roblox Newsroom, "Introducing Roblox Plus" (April 10, 2026): https://about.roblox.com/newsroom/2026/04/introducing-roblox-plus-subscription
11. "Roblox has games again" (The Verge, syndicated, undated): https://briefly-stg.herokuapp.com/anchor/Video_games/story/roblox-has-games-again
12. Roblox Creator Hub, Passes: https://create.roblox.com/docs/production/monetization/game-passes
13. Roblox Creator Hub, Localize with scripting (FormatByKey, Context, params): https://create.roblox.com/docs/production/localization/localize-with-scripting
14. Roblox Creator Hub, Localization overview (source language, AutoLocalize): https://create.roblox.com/docs/production/localization
15. Roblox DevForum, "Getting the Best out of the Roblox Localization Tools": https://devforum.roblox.com/t/getting-the-best-out-of-the-roblox-localization-tools/2807522
16. Roblox DevForum, "Tips and Tricks for Translators" (ambiguous "back"): https://devforum.roblox.com/t/tips-and-tricks-for-translators/2807526
17. Roblox DevForum, "Introducing Builder Font + Deprecating Gotham and Arial": https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222
18. iD Tech, Roblox terms dictionary (obby, noob, AFK usage): https://www.idtech.com/blog/roblox-terms-parents-dictionary
19. Roblox Creator Hub, MarketplaceService (GetRobloxSubscriptionDetailsAsync for Plus, PromptPremiumPurchase deprecated): https://create.roblox.com/docs/reference/engine/classes/MarketplaceService
20. roblox.com Charts page, live en-us title "Top Roblox Games" (checked 2026-11-08): https://www.roblox.com/charts
21. W3C Internationalization, Text size in translation (CJK width vs character count): https://www.w3.org/International/articles/article-text-size
