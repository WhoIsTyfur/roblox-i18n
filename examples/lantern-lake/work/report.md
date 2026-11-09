# roblox-i18n report

Source en-us, 40 strings, mode all.

| Locale | Strings | Fixed by review | Disputed / native | Lint errors | Confidence high/med/low | Native review | Render risk |
|---|---|---|---|---|---|---|---|
| sq-al | 40 | 1 | 0 | 0 | 32/8/0 | strongly_recommended | low |
| ar-001 | 40 | 1 | 0 | 0 | 33/7/0 | strongly_recommended | medium |
| bn-bd | 40 | 1 | 0 | 0 | 31/9/0 | strongly_recommended | medium |
| nb-no | 40 | 1 | 0 | 0 | 32/8/0 | recommended | low |
| bs-ba | 40 | 0 | 0 | 0 | 31/9/0 | strongly_recommended | medium |
| bg-bg | 40 | 0 | 0 | 0 | 29/11/0 | strongly_recommended | medium |
| my-mm | 40 | 1 | 0 | 0 | 14/25/1 | strongly_recommended | medium |
| zh-cn | 40 | 1 | 0 | 0 | 35/5/0 | recommended | medium |
| zh-tw | 40 | 1 | 0 | 0 | 38/2/0 | recommended | medium |
| hr-hr | 40 | 2 | 0 | 0 | 34/6/0 | strongly_recommended | medium |
| cs-cz | 40 | 0 | 0 | 0 | 30/10/0 | strongly_recommended | medium |
| da-dk | 40 | 1 | 0 | 0 | 32/8/0 | recommended | low |
| nl-nl | 40 | 2 | 0 | 0 | 30/10/0 | recommended | low |
| en-gb | 40 | 0 | 0 | 0 | 38/2/0 | optional | low |
| et-ee | 40 | 1 | 0 | 0 | 34/6/0 | strongly_recommended | low |
| fil-ph | 40 | 0 | 0 | 0 | 28/12/0 | strongly_recommended | low |
| fi-fi | 40 | 0 | 0 | 0 | 35/5/0 | strongly_recommended | low |
| fr-fr | 40 | 0 | 0 | 0 | 36/4/0 | recommended | low |
| fr-ca | 40 | 0 | 0 | 0 | 34/6/0 | recommended | low |
| ka-ge | 40 | 1 | 0 | 0 | 29/11/0 | strongly_recommended | medium |
| de-de | 40 | 2 | 0 | 0 | 33/7/0 | recommended | low |
| el-gr | 40 | 0 | 0 | 0 | 35/5/0 | strongly_recommended | medium |
| hi-in | 40 | 1 | 0 | 0 | 29/11/0 | strongly_recommended | medium |
| hu-hu | 40 | 2 | 0 | 0 | 34/6/0 | strongly_recommended | medium |
| id-id | 40 | 1 | 0 | 0 | 36/4/0 | recommended | none |
| it-it | 40 | 0 | 0 | 0 | 35/5/0 | recommended | low |
| ja-jp | 40 | 0 | 0 | 0 | 34/6/0 | recommended | low |
| kk-kz | 40 | 1 | 0 | 0 | 29/11/0 | strongly_recommended | high |
| km-kh | 40 | 2 | 0 | 0 | 27/13/0 | strongly_recommended | medium |
| ko-kr | 40 | 1 | 0 | 0 | 37/3/0 | recommended | low |
| lv-lv | 40 | 2 | 0 | 0 | 29/11/0 | strongly_recommended | low |
| lt-lt | 40 | 1 | 0 | 0 | 34/6/0 | strongly_recommended | medium |
| ms-my | 40 | 0 | 0 | 0 | 32/8/0 | strongly_recommended | low |
| pl-pl | 40 | 3 | 0 | 0 | 31/9/0 | strongly_recommended | low |
| pt-br | 40 | 1 | 0 | 0 | 35/5/0 | recommended | low |
| pt-pt | 40 | 1 | 0 | 0 | 33/7/0 | recommended | low |
| ro-ro | 40 | 1 | 0 | 0 | 34/6/0 | recommended | medium |
| ru-ru | 40 | 2 | 0 | 0 | 31/9/0 | recommended | medium |
| sr-rs | 40 | 0 | 0 | 0 | 32/8/0 | strongly_recommended | medium |
| si-lk | 40 | 0 | 0 | 0 | 19/20/1 | strongly_recommended | medium |
| sk-sk | 40 | 1 | 0 | 0 | 23/17/0 | strongly_recommended | medium |
| sl-sl | 40 | 0 | 0 | 0 | 30/10/0 | strongly_recommended | medium |
| es-es | 40 | 1 | 0 | 0 | 36/4/0 | recommended | low |
| es-mx | 40 | 2 | 0 | 0 | 34/6/0 | recommended | low |
| sv-se | 40 | 0 | 0 | 0 | 35/5/0 | recommended | low |
| th-th | 40 | 0 | 0 | 0 | 38/2/0 | strongly_recommended | medium |
| tr-tr | 40 | 1 | 0 | 0 | 32/8/0 | recommended | medium |
| uk-ua | 40 | 1 | 0 | 0 | 33/7/0 | strongly_recommended | high |
| vi-vn | 40 | 2 | 0 | 0 | 35/5/0 | strongly_recommended | medium |

## sq-al -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `catch.success`: You caught a {rarity} {fish}! -> Kape: {fish} ({rarity})! -- "Kape" can also be read as the command "Catch it!"
- `rarity.mythic`: Mythic -> Mitik -- masculine form; does not agree with a feminine fish name such as "Ngjalë fener" when inserted beside it
- `pass.auto_reel`: Auto Reel -> Autotërheqje -- coined compound; "auto-" often means "car" in Albanian and "tërheqje" also means towing or withdrawal, so it can read as "car towing"

## ar-001 -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.cast`: Cast -> رمي -- bare verbal noun 'throwing'; does not mention the line or rod, so the fishing sense comes only from context
- `hud.reel`: Reel -> سحب -- bare verbal noun 'pulling'; the same word commonly means 'withdraw' (money) or 'draw' (as in a lottery or gacha draw)
- `shop.rods`: Rods -> الصنارات -- the word can mean fishing rods or fish hooks
- `shop.buy_robux`: Buy for {price} Robux -> شراء بـ {price} Robux -- Robux left in Latin script inside Arabic text; likely intended
- `pass.auto_reel`: Auto Reel -> سحب تلقائي -- can also read as 'automatic withdrawal', the usual banking term, or 'auto draw'
- `pass.lucky_bait`: <b>Lucky Bait</b> doubles your rare fish chance! -> <b>طُعم الحظ</b> يضاعف فرصتك في صيد الأسماك النادرة! -- the verb usually means 'doubles' but can loosely mean 'multiplies'
- `sell.prompt`: Press E to sell -> اضغط على E للبيع -- Latin key letter 'E' in Arabic text; likely intended
- `ascend.confirm`: Ascend now? You will start over but catch rare fish {bonus}% more often. -> ارتقاء الآن؟ ستبدأ من جديد، لكنك ستصطاد الأسماك النادرة أكثر بنسبة {bonus}%. -- opens with a bare noun, 'Ascension now?', which is a little stiff
- `afk.kicked`: You were idle for too long and stopped fishing. -> بقيت بلا نشاط لفترة طويلة، فتوقفت عن الصيد. -- says the player stopped fishing, not that the game stopped or removed them; the unvoweled verbs can also be read as 'I'
- `event.ends`: Ends in {time} -> ينتهي بعد {time} -- verb is masculine, 'it ends', so it agrees with a masculine noun like 'event' but not a feminine one like 'storm'
- `daily.streak`: Day {day} streak! Come back tomorrow for more. -> اليوم {day} على التوالي! مكافآت أكثر في انتظارك غدًا. -- the word for 'the day' also means 'today', so it can read 'Today {day} in a row'; an ordinal would read more naturally

## bn-bd -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `rarity.mythic`: Mythic -> মিথিক -- English 'mythic' written in Bengali script; not a Bengali word, may be unclear to some players
- `ascend.button`: Ascend -> অ্যাসেন্ড -- English 'ascend' written in Bengali script; not a Bengali word, meaning may be unclear to players
- `ascend.confirm`: Ascend now? You will start over but catch rare fish {bonus}% more often. -> এখনই অ্যাসেন্ড করবে? আবার প্রথম থেকে শুরু করতে হবে, কিন্তু দুর্লভ মাছ {bonus}% বেশি ধরা পড়বে। -- uses the same transliterated English 'ascend'
- `codes.redeemed`: Code redeemed! Enjoy your reward. -> কোড রিডিম হয়েছে! পুরস্কার উপভোগ করো। -- uses transliterated English 'redeem'
- `daily.streak`: Day {day} streak! Come back tomorrow for more. -> টানা {day} দিনের স্ট্রিক! আরও পুরস্কার পেতে কাল আবার এসো। -- uses transliterated English 'streak'; the word before it already means 'in a row', so slightly redundant
- `group.join`: Join the group for 50 free bait! -> আমাদের গ্রুপে যোগ দিয়ে ফ্রিতে 50টি টোপ নাও! -- the number 50 is in Western digits inside Bengali text

## nb-no -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `pass.auto_reel`: Auto Reel -> Autosveiv -- coined compound, literally 'auto-crank'; understandable next to 'reel in'
- `ascend.button`: Ascend -> Stig opp -- literally 'rise up' or 'climb up'; a bit lofty, could read as physically going up
- `weather.storm`: A storm is coming! Rare fish are biting. -> En storm er på vei! Sjeldne fisker biter nå. -- says the storm is approaching, not that it is already here

## bs-ba -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `rarity.mythic`: Mythic -> Mitski -- masculine adjective form; agrees with a masculine fish noun like "saran" but not with a feminine one like "jegulja" (eel), so it reads off next to the eel
- `pass.auto_reel`: Auto Reel -> Autoizvlačenje -- coined compound; "izvlacenje" on its own just means pulling out or extracting, so the fishing sense depends on context
- `trade.accept`: {player} accepted your trade -> Igrač {player} je prihvatio razmjenu -- verb is masculine; assumes the other player is male

## bg-bg -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `rarity.mythic`: Mythic -> Митичен -- masculine adjective form; agrees with the masculine word for "catch" in catch.success, but would not agree with a feminine fish name such as "Фенерна змиорка" on a card
- `shop.buy_robux`: Buy for {price} Robux -> Купи за {price} Robux -- keeps "Robux" in Latin script as the brand name
- `afk.kicked`: You were idle for too long and stopped fishing. -> Беше AFK твърде дълго, затова риболовът спря. -- keeps the English gaming acronym "AFK" in Latin script

## my-mm -- for a native speaker
- `rarity.mythic`: Mythic -> နတ်ဒဏ္ဍာရီ (ok)

Flagged by the blind back-translator, passed by the reviewer:
- `hud.cast`: Cast -> ပစ်ချရန် -- literally 'to throw down / drop'; a generic verb, out of context it could read as 'throw away'
- `ascend.button`: Ascend -> အဆင့်မြှင့်ရန် -- literally 'raise the level/rank'; the everyday word for an upgrade, nothing in it suggests a reset
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> လရောင်ကမ်းကွေ့မှာ ငါး {n} ကောင် ဖမ်းပါ -- Burmese has no capitals, so it is unclear whether this is a named place or just 'the moonlit bend of the shore'
- `settings.back`: Back -> နောက်သို့ -- formal wording; the root word also means 'next / later', so it could be misread as 'Next'
- `settings.sfx`: Sound Effects -> အသံ -- generic 'sound / voice'; does not say sound effects as opposed to music
- `event.ends`: Ends in {time} -> ပြီးဖို့ {time} ကျန်တယ် -- no subject; could read as time left for you to finish something rather than the event ending
- `group.join`: Join the group for 50 free bait! -> Community ထဲ ဝင်ပြီး ငါးစာ 50 ခု အခမဲ့ ရယူပါ! -- the word 'Community' is left in English, in Latin script, mid-sentence

## zh-cn -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> 收竿 -- literally 'take the rod in'; also commonly means packing up the rod / done fishing for the day
- `catch.escaped`: It got away... -> 鱼溜走了... -- uses three ASCII periods instead of the Chinese ellipsis
- `ascend.button`: Ascend -> 晋升 -- means a promotion in rank, as in a job or military rank; does not suggest a reset or prestige

## zh-tw -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `shop.equip`: Equip -> 裝備 -- the same word is also the noun "equipment"; on a button it reads as "Equip"
- `ascend.button`: Ascend -> 晉升 -- the word means a promotion in rank, as at work or in the military; nothing suggests starting over
- `weather.storm`: A storm is coming! Rare fish are biting. -> 暴風雨要來了！稀有魚紛紛上鉤！ -- says the storm is still coming, not that it is here now

## hr-hr -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `shop.free`: Free -> Gratis -- colloquial 'gratis'; the text elsewhere uses the standard word 'besplatno' for free
- `quest.claim`: Claim -> Preuzmi -- the same word is the usual software term for 'Download', so a bare button could be misread
- `trade.accept`: {player} accepted your trade -> {player} prihvaća razmjenu -- present tense; reads as 'accepts / is accepting' rather than clearly 'has accepted'

## cs-cz -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `sell.prompt`: Press E to sell -> Prodej klávesou E -- ambiguous: "Prodej" can also read as the noun "Sale" ("Sale with the E key"); also names the E key, which does not fit touch or gamepad players

## da-dk -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `quest.claim`: Claim -> Hent -- standalone 'Hent' is also the usual Danish UI word for 'Download'; reads as 'collect' only from context

## nl-nl -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> Inhalen -- bare 'inhalen' most commonly means 'overtake' or 'catch up'; the fishing sense relies on context
- `shop.equip`: Equip -> Uitrusten -- ambiguous: 'uitrusten' also commonly means 'to rest' or 'take a break'
- `shop.equipped`: Equipped -> Uitgerust -- ambiguous: 'uitgerust' also commonly means 'rested'
- `ascend.button`: Ascend -> Opstijgen -- everyday sense is 'rise' or 'take off' (as a plane does); no reset/prestige meaning comes through on its own
- `group.join`: Join the group for 50 free bait! -> Word lid van onze community voor 50 gratis aas! -- counting an uncountable noun ('50 aas') is slightly awkward

## en-gb -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `afk.kicked`: You were idle for too long and stopped fishing. -> You were idle for too long and stopped fishing. -- ambiguous: grammatically says you yourself stopped fishing, not that the game stopped you; does not say whether you were removed from the server

## et-ee -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `catch.success`: You caught a {rarity} {fish}! -> Sinu saak: {rarity} {fish}! -- with the inserted names this reads e.g. "Müütiline Kuldne karpkala", with a capital letter on both words mid-phrase
- `pass.auto_reel`: Auto Reel -> Autokerimine -- the "auto-" prefix in Estonian compounds usually means "car", so it can also read as "car reeling"
- `ascend.button`: Ascend -> Ülendus -- a noun ("elevation/exaltation/promotion"), not a verb; uncommon, bookish word for a button
- `quest.claim`: Claim -> Võta vastu -- can also read as "Accept", as in accepting a new task, rather than collecting a reward
- `event.ends`: Ends in {time} -> Lõpeb {time} pärast -- grammatical only if {time} is in the genitive case, e.g. "5 minuti"; a plain number-plus-unit value may read wrong

## fil-ph -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `fish.lantern_eel`: Lantern Eel -> Igat-Parol -- literally "Eel-Lantern"; "parol" usually means the star-shaped Filipino Christmas lantern
- `shop.rods`: Rods -> Pamingwit -- singular; no plural marker, so it reads as one rod rather than a tab of rods
- `pass.auto_reel`: Auto Reel -> Auto Hila -- mixes English "Auto" with Filipino "Hila" (pull)
- `sell.done`: Sold {count} fish for {coins} coins! -> Naibenta mo ang isda (x{count})! Coins: +{coins} -- "Coins" left in English
- `sell.prompt`: Press E to sell -> Ibenta gamit ang E -- reads "using E" rather than "press E"; slightly stiff
- `ascend.button`: Ascend -> Mag-ascend -- English verb "ascend" with the Filipino prefix "mag-"; the English word may be unfamiliar to many players
- `ascend.confirm`: Ascend now? You will start over but catch rare fish {bonus}% more often. -> Mag-ascend na? Babalik ka sa simula, pero {bonus}% mas madalas kang makakahuli ng rare na isda. -- uses the English verb "ascend" with "mag-"
- `weather.storm`: A storm is coming! Rare fish are biting. -> May bagyong paparating! Kumakagat ang mga rare na isda. -- "bagyo" usually means a typhoon, so this can read as a typhoon warning
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> Manghuli ng isda sa Look ng Buwan: {n} -- "Look ng Buwan" is literally "Bay of the Moon"; "Look" (bay) can be misread at a glance as the English word "look"
- `codes.redeemed`: Code redeemed! Enjoy your reward. -> Na-redeem ang code! I-enjoy ang reward mo. -- heavy Taglish: "redeem", "enjoy" and "reward" are English words with Filipino prefixes
- `event.ends`: Ends in {time} -> Matatapos sa {time} -- ambiguous: "sa {time}" can mean "in {time}" (countdown) or "at {time}" (clock time)

## fi-fi -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `catch.success`: You caught a {rarity} {fish}! -> Saaliiksi jäi {rarity} {fish}! -- with the inserted labels the words appear capitalized mid-sentence, e.g. "Myyttinen Kultakarppi"
- `event.ends`: Ends in {time} -> Loppuu {time} päästä -- "päästä" needs {time} in the genitive, e.g. "5 minuutin"; reads wrong if {time} is a plain form like "5 minuuttia"

## fr-fr -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> Remonter -- literally 'bring back up'; on its own it could also read as 'go back up'
- `shop.rods`: Rods -> Cannes -- short for fishing rods; on its own the word can also mean walking canes
- `pass.auto_reel`: Auto Reel -> Remontée auto -- literally 'automatic raising'; the word alone also commonly means a ski lift or a comeback
- `pass.lucky_bait`: <b>Lucky Bait</b> doubles your rare fish chance! -> L'<b>Appât de chance</b> double tes chances de pêcher des poissons rares ! -- item name is a stiff literal 'bait of luck'; the word for luck then repeats as 'chances'
- `sell.prompt`: Press E to sell -> E pour vendre -- clipped; names the keyboard key E in the text itself
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> Poissons à pêcher, Baie Clair-de-Lune : {n} -- stilted, form-like phrasing; unclear whether {n} is the goal or how many are left
- `friends.boost`: Fishing with friends gives +{percent}% luck -> Pêcher avec tes amis donne +{percent} % de chance -- the word can read as luck or as odds; does not say a chance of what
- `afk.kicked`: You were idle for too long and stopped fishing. -> Tu as été AFK trop longtemps, alors ta pêche s'est arrêtée. -- keeps the English gamer acronym AFK; 'your fishing' could also read as 'your catch'

## fr-ca -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.cast`: Cast -> Lancer -- on its own 'Lancer' can also read as 'Launch' or 'Start'
- `shop.rods`: Rods -> Cannes -- bare 'Cannes' without 'a peche' can also read as canes or walking sticks, or the city of Cannes
- `pass.lucky_bait`: <b>Lucky Bait</b> doubles your rare fish chance! -> <b>Appât de chance</b> double tes chances de pêcher des poissons rares! -- name reads literally 'bait of luck', a little stiff; 'chance' then 'chances' repeats
- `sell.prompt`: Press E to sell -> Touche E pour vendre -- ambiguous: 'Touche' reads as either the noun 'key' or the verb 'touch', so also 'Touch E to sell'
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> Poissons à pêcher, baie Clair-de-Lune : {n} -- terse, form-like wording
- `friends.boost`: Fishing with friends gives +{percent}% luck -> Pêcher avec tes amis donne +{percent} % de chance -- 'chance' can mean luck or odds; does not say odds of what
- `afk.kicked`: You were idle for too long and stopped fishing. -> Tu as été AFK trop longtemps, alors ta pêche s'est arrêtée. -- keeps the English acronym AFK

## ka-ge -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `shop.buy_robux`: Buy for {price} Robux -> ყიდვა {price} Robux-ად -- mixes scripts: Latin "Robux" with the Georgian case ending "-ad" hyphenated on; usual for brand names
- `sell.all`: Sell All -> გაყიდე ყველა -- imperative "sell!", while the other buttons use verb nouns like "Buying", "Selecting"
- `sell.prompt`: Press E to sell -> გასაყიდად დააჭირე E-ს -- mixes scripts: Latin key letter "E" with a Georgian case ending hyphenated on; usual for key names
- `ascend.button`: Ascend -> აღზევება -- bookish word meaning "rise, elevation", as in rising to power or glory

## de-de -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.cast`: Cast -> Werfen -- generic verb "throw"; not the usual fishing word for casting a line, which is "Auswerfen"
- `ascend.button`: Ascend -> Aufsteigen -- on its own can also read as "move up a rank" or "climb on/mount"

## el-gr -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> Μάζεψε -- on its own reads as "Collect" or "Gather up"; only the fishing context makes it mean reeling in
- `pass.auto_reel`: Auto Reel -> Αυτόματο μάζεμα -- could read as "Auto Collect"; only the fishing context makes it mean reeling in
- `sell.done`: Sold {count} fish for {coins} coins! -> Πούλησες ψάρια: {count}. Κέρδισες κέρματα: {coins}! -- two "label: number" phrases in a row; clear but stiff
- `ascend.button`: Ascend -> Άνοδος -- bare noun meaning "ascent" or "rise"; vague as a button label on its own
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> Πιάσε ψάρια στον Φεγγαρόλουστο Κόλπο: {n} -- number tacked on after a colon; reads like a form label, and it is unclear whether {n} is a target or progress
- `trade.sent`: Trade request sent to {player} -> Στάλθηκε αίτημα ανταλλαγής προς: {player} -- colon right after the preposition "to" is a little unnatural
- `codes.enter`: Enter a code -> Γράψε κωδικό -- the word for "code" also commonly means "password" in Greek; in a text box this could read as "Enter password"

## hi-in -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `rarity.mythic`: Mythic -> मिथिक -- English word 'mythic' spelled out in Devanagari, not a Hindi word; players who don't know the English term may not understand it
- `shop.buy_robux`: Buy for {price} Robux -> {price} Robux में खरीदें -- Robux kept in Latin script inside Devanagari text
- `pass.auto_reel`: Auto Reel -> ऑटो-खींचें -- awkward as a product name: English 'auto' in Devanagari plus a polite command form of 'pull', so it reads like an instruction rather than a name
- `pass.lucky_bait`: <b>Lucky Bait</b> doubles your rare fish chance! -> <b>लकी चारा</b> रेयर मछली पकड़ने का चांस दोगुना कर देता है! -- casual Hinglish: 'lucky', 'rare' and 'chance' are English words written in Devanagari
- `sell.prompt`: Press E to sell -> बेचने के लिए E दबाएँ -- key letter E in Latin script inside Devanagari text
- `ascend.button`: Ascend -> असेंड -- English word 'ascend' spelled out in Devanagari, not a Hindi word; most Hindi players will not know what it means
- `ascend.confirm`: Ascend now? You will start over but catch rare fish {bonus}% more often. -> अभी असेंड करें? आपको फिर से शुरू करना होगा, लेकिन रेयर मछली {bonus}% ज़्यादा बार मिलेगी. -- 'ascend' is English in Devanagari and likely not understood
- `daily.streak`: Day {day} streak! Come back tomorrow for more. -> लगातार {day} दिन की स्ट्रीक! और इनाम के लिए कल फिर आएँ. -- 'streak' is English in Devanagari and redundant with the Hindi word for 'consecutive' before it
- `group.join`: Join the group for 50 free bait! -> हमारी कम्यूनिटी जॉइन करें और 50 फ़्री चारे पाएँ! -- heavy Hinglish: 'community', 'join' and 'free' are English words in Devanagari; the plural 'chaare' treats bait as countable, slightly odd

## hu-hu -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `shop.rods`: Rods -> Botok -- bare 'bot' also just means 'stick'; reads as fishing rods only from the shop context
- `pass.auto_reel`: Auto Reel -> Autobehúzás -- coined compound; understandable but not a standard word

## id-id -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `fish.golden_carp`: Golden Carp -> Ikan Mas -- ikan mas is the everyday name for the common carp; literally 'gold fish', and some players may picture an ornamental goldfish
- `rarity.mythic`: Mythic -> Mitos -- a noun, 'myth', not the adjective 'mythic'; reads a little odd as a rarity tag
- `ascend.button`: Ascend -> Bangkit -- bangkit means rise up / get up / revive; on its own it does not suggest a prestige reset
- `weather.storm`: A storm is coming! Rare fish are biting. -> Badai datang! Ikan langka sedang menyambar umpan. -- badai datang can mean either 'a storm is coming' or 'the storm has arrived'
- `event.ends`: Ends in {time} -> Selesai dalam {time} -- selesai means 'done/finished', so it can also read as 'finished within {time}'
- `group.join`: Join the group for 50 free bait! -> Gabung komunitas kami dan dapatkan 50 umpan gratis! -- vague: 'community' does not say it is a Roblox group

## it-it -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> Recupera -- literally "Retrieve/Recover"; a generic verb whose fishing sense comes only from context
- `catch.success`: You caught a {rarity} {fish}! -> Hai preso un pesce {rarity}: {fish}! -- with rarity.mythic inserted it reads "un pesce Mitico", the adjective capitalized mid-sentence
- `shop.rods`: Rods -> Canne -- bare "canne" also means reeds or canes and is slang for joints; "fishing rods" is clear only from context
- `pass.auto_reel`: Auto Reel -> Autorecupero -- literally "auto-retrieve/auto-recovery"; coined compound that could read as a generic auto-recovery feature
- `ascend.button`: Ascend -> Ascendi -- formal, literary-sounding verb, uncommon in everyday Italian
- `daily.streak`: Day {day} streak! Come back tomorrow for more. -> Serie: giorno {day}! Torna domani per altri premi. -- bare "Serie" literally means "series"; the streak sense is clear only from context

## ja-jp -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `rarity.mythic`: Mythic -> ミシック -- katakana spelling of the English word "mythic"; a gaming loanword, not an everyday Japanese word
- `sell.prompt`: Press E to sell -> Eキーで売る -- names the E key in the text itself (Latin letter in Japanese text); untrue for touch or gamepad players
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> 月夜の入り江で魚を{n}匹つる -- can read as a named place or as "in a cove on a moonlit night"
- `codes.redeemed`: Code redeemed! Enjoy your reward. -> コードを使った！報酬をどうぞ！ -- first half is casual and has no subject, so it can read like "I used the code!"; second half is polite

## kk-kz -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.cast`: Cast -> Лақтыру -- verbal noun 'throwing'; generic 'throw', the casting sense comes only from context
- `hud.reel`: Reel -> Тарту -- verbal noun 'pulling'; generic 'pull/draw', the reeling-in sense comes only from context
- `fish.lantern_eel`: Lantern Eel -> Шам жыланбалық -- literally 'lamp eel'; 'шам' means lamp or candle; bare noun-noun compound reads slightly unusual
- `shop.rods`: Rods -> Қармақтар -- the word 'қармақ' can mean either fishing hook or fishing rod
- `shop.equip`: Equip -> Қолдану -- means 'use/apply', not specifically 'equip'
- `shop.buy_robux`: Buy for {price} Robux -> {price} Robux-қа алу -- mixes scripts: Latin 'Robux' with a Cyrillic case suffix '-қа'; 'алу' is literally 'get/take', read as 'buy' here
- `pass.auto_reel`: Auto Reel -> Автотарту -- coined compound; 'тарту' is generic 'pull'
- `sell.prompt`: Press E to sell -> Сату үшін E-ні бас -- mixes scripts: Latin key letter 'E' with a Cyrillic suffix '-ні'
- `weather.storm`: A storm is coming! Rare fish are biting. -> Дауыл келеді! Сирек балықтар жем қауып жатыр! -- says the storm is approaching, not that it is already here
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> Айлы шығанақта {n} балық аула -- place name translated as 'Айлы шығанақ', literally 'moonlit bay'; only the first word is capitalized, so it could read as a generic 'a moonlit bay'
- `quest.claim`: Claim -> Алу -- generic 'take/get'; the same verb is used for 'buy' in the shop
- `codes.redeemed`: Code redeemed! Enjoy your reward. -> Код қабылданды! Сыйлығың құтты болсын! -- second sentence is the traditional congratulation formula, literally 'may your gift be blessed'

## km-kh -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.backpack`: Backpack -> កាបូប -- the word also commonly means wallet or purse; not specifically a backpack
- `rarity.mythic`: Mythic -> ទេវកថា -- the noun 'myth/mythology', not an adjective like 'mythic'; inside catch.success it reads 'myth class'
- `afk.kicked`: You were idle for too long and stopped fishing. -> អ្នកនៅស្ងៀមយូរពេក ដូច្នេះបានឈប់ស្ទូចត្រីហើយ។ -- who stopped the fishing is left implied; reads as if you stopped it yourself

## ko-kr -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `shop.buy_robux`: Buy for {price} Robux -> {price} Robux에 구매 -- the name "Robux" is kept in Latin letters inside Korean text

## lv-lv -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> Vilkt -- generic verb "pull/drag"; on a button it can also read as "Drag", nothing specific to reeling in
- `rarity.mythic`: Mythic -> Mītisks -- masculine adjective form; inserted next to a feminine fish name such as "Zelta karpa" it does not agree in gender
- `ascend.button`: Ascend -> Pacelties -- ambiguous: plain "rise / lift off", can read as physically moving upward

## lt-lt -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `pass.auto_reel`: Auto Reel -> Autotraukimas -- coined compound, not a standard word; understandable in a fishing game, though 'auto-' often means 'car' in Lithuanian compounds
- `ascend.button`: Ascend -> Pakilti -- plain verb meaning 'rise / go up / take off'; nothing marks it as a prestige or reset action

## ms-my -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `pass.auto_reel`: Auto Reel -> Tarik Auto -- 'Auto' is an English clipping; informal, though common in games
- `ascend.button`: Ascend -> Bangkit -- 'Bangkit' can mean rise up, get up or rise again; ambiguous on its own as a button
- `trade.accept`: {player} accepted your trade -> {player} menerima permintaan tukar anda -- 'menerima' means both 'received' and 'accepted'; can read as {player} only got the request
- `afk.kicked`: You were idle for too long and stopped fishing. -> Anda terlalu lama tidak aktif dan berhenti memancing. -- reads as if you stopped fishing yourself; does not say you were removed or that the game stopped you

## pl-pl -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `fish.lantern_eel`: Lantern Eel -> Węgorz latarniowy -- the adjective 'latarniowy' is rare and could also read as 'lighthouse' or 'streetlamp' eel

## pt-br -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `pass.auto_reel`: Auto Reel -> Auto Puxar -- English-style word order; reads like a calque rather than a natural Portuguese product name
- `ascend.button`: Ascend -> Ascender -- fairly formal, uncommon verb in everyday Brazilian Portuguese; sounds identical to 'acender' (to light)

## pt-pt -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> Recolher -- on its own the verb means pull in / retract / collect; reads as reeling in only because it replaces Cast during a bite
- `pass.auto_reel`: Auto Reel -> Autorrecolha -- coined compound; the noun 'recolha' usually means collection or pickup, so it can read as 'Auto-collect'
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> Peixes a pescar na Baía do Luar: {n} -- stiff, form-like phrasing; unclear whether {n} is the total goal or how many remain
- `afk.kicked`: You were idle for too long and stopped fishing. -> Estiveste demasiado tempo sem te mexer, por isso a pesca parou. -- says only that fishing stopped; nothing about being removed from the server
- `event.ends`: Ends in {time} -> Termina em {time} -- can also read as 'ends on/at {time}' if {time} is a date or clock time

## ro-ro -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `catch.success`: You caught a {rarity} {fish}! -> Ai prins un pește {rarity}: {fish}! -- with rarity.mythic inserted it reads 'un peste Mitic', a capitalized adjective mid-sentence
- `pass.auto_reel`: Auto Reel -> Trage automat -- a verb phrase rather than a product-style name; out of the fishing HUD context 'trage automat' can also read as 'fires automatically'
- `afk.kicked`: You were idle for too long and stopped fishing. -> Ai fost AFK prea mult timp, așa că nu mai pescuiești. -- vague: does not say you were kicked or disconnected

## ru-ru -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `fish.lantern_eel`: Lantern Eel -> Угорь-фонарик -- "фонарик" is the everyday word for a flashlight, so it can read as "flashlight eel"
- `shop.buy_robux`: Buy for {price} Robux -> Купить за {price} Robux -- currency name "Robux" kept in Latin script inside Cyrillic text
- `pass.auto_reel`: Auto Reel -> Автовытягивание -- coined compound noun, long and a bit clunky; literally "automatic pulling out"
- `ascend.button`: Ascend -> Возвышение -- lofty, bookish noun meaning a rise to higher rank; can also mean a raised spot or hill; a noun, not an action, on a button
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> Поймай рыбу в Лунной бухте: {n} шт. -- "шт." (pieces) is a shop or inventory unit; reads dry for a quest line

## sr-rs -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `rarity.mythic`: Mythic -> Митски -- masculine adjective form; does not agree with a feminine fish name such as the eel (jegulja) if read as describing it
- `shop.buy_robux`: Buy for {price} Robux -> Купи за {price} Robux -- Robux left in Latin script inside Cyrillic text, undeclined; likely deliberate as a brand name
- `pass.auto_reel`: Auto Reel -> Аутоизвлачење -- coined compound; 'izvlachenje' also commonly means a lottery draw or extraction, so on its own it does not clearly say reeling in fish

## si-lk -- for a native speaker
- `rarity.mythic`: Mythic -> අද්භූත (ok)

Flagged by the blind back-translator, passed by the reviewer:
- `shop.buy_robux`: Buy for {price} Robux -> Robux {price}කට මිලදී ගන්න -- Robux left in Latin script
- `ascend.button`: Ascend -> උසස් වෙන්න -- the everyday sense is getting promoted, as in a job or rank

## sk-sk -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `ascend.button`: Ascend -> Vzostup -- a noun ("ascent, rise"), not a command; reads as a label rather than an action
- `quest.catch_n`: Catch {n} fish at Moonlit Bay -> Chyť ryby v Mesačnej zátoke: {n} -- number after the colon; unclear whether {n} is the target or the progress so far

## sl-sl -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `shop.equip`: Equip -> Uporabi -- generic 'use', not specifically 'equip'
- `pass.auto_reel`: Auto Reel -> Samonavijanje -- coined compound word; reads like 'self-winding', as for a watch
- `ascend.button`: Ascend -> Vzpon -- a noun, 'ascent/climb', not a verb; could read as physically climbing
- `weather.storm`: A storm is coming! Rare fish are biting. -> Prihaja nevihta! Redke ribe zdaj prijemajo. -- says the storm is approaching, not that it has arrived

## es-es -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> Recoger -- on its own 'Recoger' most often means 'pick up' or 'collect'; it reads as reeling in only from the fishing context
- `catch.success`: You caught a {rarity} {fish}! -> ¡Has pescado: {fish} ({rarity})! -- the colon between 'you caught' and the fish is a UI-style break, slightly stiff in Spanish but clear
- `rarity.mythic`: Mythic -> Mítico -- masculine form; after a feminine fish name such as 'Carpa dorada' or 'Anguila farol' it does not agree in gender, though it reads acceptably as a tag in parentheses
- `pass.auto_reel`: Auto Reel -> Autorrecogida -- coined word, not standard Spanish; 'recogida' suggests pickup or collection rather than reeling in
- `quest.claim`: Claim -> Reclamar -- in everyday Spanish 'reclamar' leans toward 'demand' or 'complain'; common in games for claiming rewards, so still understandable
- `afk.kicked`: You were idle for too long and stopped fishing. -> Has estado demasiado tiempo sin moverte, así que has dejado de pescar. -- says only that your fishing stopped, not that you were removed from the game; reads a little as if you stopped by choice

## es-mx -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `hud.reel`: Reel -> Recoger -- on its own "Recoger" usually means "pick up" or "collect"; it reads as "reel in" only from the fishing context
- `rarity.mythic`: Mythic -> Mítico -- masculine form; beside feminine fish names such as "Carpa dorada" or "Anguila farol" in catch.success it may read as a gender mismatch
- `pass.auto_reel`: Auto Reel -> Autorrecogida -- coined compound "Autorrecogida"; reads as auto-pickup/auto-collect rather than clearly auto-reel
- `afk.kicked`: You were idle for too long and stopped fishing. -> Estuviste AFK demasiado tiempo y dejaste de pescar. -- phrased as if you stopped fishing yourself; does not say you were kicked or disconnected

## sv-se -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `pass.auto_reel`: Auto Reel -> Autoveva -- coined compound, literally 'auto-crank'
- `ascend.button`: Ascend -> Avancera -- means advance or move up; on its own it does not suggest a reset or prestige
- `quest.claim`: Claim -> Hämta -- literally 'fetch'; with no object it is also the usual word for 'Get' or 'Download'

## th-th -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `afk.kicked`: You were idle for too long and stopped fishing. -> ไม่ได้ขยับตัวนานเกินไป เลยหยุดตกปลาแล้ว -- no stated subject; it says only that fishing stopped, not that the player was removed from the game

## tr-tr -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `trade.sent`: Trade request sent to {player} -> Takas isteği gönderildi: {player} -- {player} is only implied to be the recipient by the colon

## uk-ua -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `shop.equip`: Equip -> Взяти -- "Взяти" literally means "take"; on a shop card it could read as taking or getting the rod rather than equipping it
- `shop.buy_robux`: Buy for {price} Robux -> Купити за {price} Robux -- the word "Robux" is left in Latin script

## vi-vn -- for a native speaker

Flagged by the blind back-translator, passed by the reviewer:
- `codes.enter`: Enter a code -> Nhập code -- uses the English loanword 'code' rather than Vietnamese 'ma'; casual gamer usage
- `codes.redeemed`: Code redeemed! Enjoy your reward. -> Nhập code thành công! Tận hưởng phần quà nhé! -- uses the English loanword 'code'; casual gamer usage
- `afk.kicked`: You were idle for too long and stopped fishing. -> Bạn AFK quá lâu nên đã dừng câu cá. -- unclear who stopped it: reads as either 'you stopped fishing' or 'fishing was stopped'; says nothing about being removed from the game; keeps the English abbreviation 'AFK'
