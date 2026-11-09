# Hindi (hi-in) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `hi-in` only. Hindi has one Roblox locale, so the tool writes no bare `hi` column; whether Roblox would read one is unverified |
| Script, direction | Devanagari, LTR, spaces between words; Western digits 0-9; Latin kept for Robux, VIP, AFK and other brands and acronyms |
| Address the player as | "आप" with polite imperatives (खेलें, खरीदें, जाएँ), as Roblox's own Hindi UI does; never "तू", and never mix in "तुम" forms (खेलो) |
| Text expansion vs English | as the lint counts (no {params}): sentences -10% to +35%, one-word buttons up to 2x (Buy -> खरीदें, On -> चालू). Marks above and below take no width, but letters are taller and wider than Latin: budget +20-30% rendered width (estimate) |
| Plural categories (CLDR) | one (0 and 1), other; ordinals one, two, few, many, other |
| Model confidence | medium -- grammar is solid, but MT drifts into textbook Hindi, translates gamer words that should stay English, and defaults verbs to male |
| Native review before shipping | strongly recommended -- Hinglish word choices and gender workarounds need a native ear |

## Audience and register
- Roblox shipped a Hindi interface plus Hindi auto-translation of game strings in mid-2026 (Outlook Respawn, 2026-06-25). A player who sees `hi-in` text has Hindi set as their Roblox language: write Devanagari, never romanized Hinglish.
- Target the register Roblox itself uses in Hindi: everyday spoken grammar with English gaming nouns written in Devanagari. Its help center writes "Robux कमाएं", "फ़्रेंड रिक्वेस्ट", "एक्सपीरिएंस पासेस", "प्रोमो कोड कैसे रिडीम करें"; its Play Store page writes "दोस्तों के साथ", "शानदार सिमुलेटर", "टाइकून गेम्स", "तुरंत खेलें".
- Kids write the same mix. Hindi Play Store reviews of Roblox read like "भाई यह गेम बहुत अच्छा है, खेलने से मजा आ जाता है": Hindi sentence, English noun गेम. In chat and on YouTube they switch to Latin-script Hinglish ("OP pet mil gaya"); that belongs in chat, not in the table.
- Microsoft's Hindi guide asks for the same: conversational, short, never formal or technical. Its avoid list: चयन करें -> चुनें, परिवर्तित करें -> बदलें, संदर्भ लें -> देखें, अत: -> इसलिए.
- Buttons are polite imperatives: खेलें, खरीदें, बेचें. Some Indian game listings mix in तुम forms (Stumble Guys: "खेलो"); Roblox never does, so stay with आप. Gaming actions use Roblox's "English noun + करें" pattern (रिडीम करें, जॉइन करें): रीबर्थ करें, ट्रेड करें, हैच करें, क्लेम करें.
- Natural hype: वाह!, बढ़िया!, शानदार!, ज़बरदस्त!, लेवल अप! Keep the source's "!" count; do not add more.
- Reads stiff, textbook or adult: उपयोगकर्ता (say प्लेयर), क्रय करें (say खरीदें), पुनर्जन्म (religious; say रीबर्थ), स्तर (say लेवल), अग्रणी तालिका (say लीडरबोर्ड), क्रीडा (say गेम), आरंभ करें (say शुरू करें).
- Kid-safe: no "भाई", "यार" or "bro" in system text even though players use them, and no slang insults.

## Roblox and gaming vocabulary
Hinglish rule: brands and all-caps acronyms stay Latin; gaming nouns are transliterated into Devanagari; verbs and everyday words stay Hindi. A pure-Hindi coinage for a gaming noun reads stiff; an English verb without "करें" reads broken. English -s plurals are fine where no number is attached (Roblox: "अपने फ़्रेंड्स के लिए").

| English | hi-in | Note |
|---|---|---|
| Robux | Robux | Latin on every Roblox Hindi page; never रोबक्स |
| game pass | गेम पास / पास | Roblox help: "एक्सपीरिएंस पास", "VIP शर्ट जैसे पासेस" |
| developer product | प्रोडक्ट | players only see the item's own name |
| experience / game | गेम (masculine) | Roblox help uses एक्सपीरिएंस for the platform term; in game say गेम (charts page: "टॉप Roblox गेम्स"); avoid अनुभव, क्रीडा |
| obby / tycoon / simulator | ऑबी / टाइकून / सिमुलेटर | टाइकून and सिमुलेटर are Roblox's Play Store spellings; ऑबी (unverified) |
| rebirth | रीबर्थ, रीबर्थ करें | never पुनर्जन्म |
| pet / pets | पेट / पेट्स | पेट also means "stomach": keep it beside a pet name or use पेट्स. पालतू (the Hindi word) is unambiguous but is not the gamer word; a fallback where पेट stands alone (unverified which kids prefer) |
| egg / hatch | अंडा (अंडे) / हैच करें | अंडा is everyday Hindi; alt verb "अंडा खोलें" |
| coins | कॉइन | bare form next to numbers (see plurals); सिक्का changes form (सिक्का/सिक्के) |
| gems | जेम | never रत्न (bookish) |
| boost / multiplier | बूस्ट / 2x | never बढ़ावा ("encouragement"); keep "2x" Latin |
| XP / level up | XP / लेवल अप! | लेवल {level}; never स्तर |
| quest | मिशन | Roblox's Play Store text says "रोमांचक मिशन पर निकलें"; क्वेस्ट also seen (unverified which kids prefer) |
| leaderboard | लीडरबोर्ड | Roblox help term; board title टॉप प्लेयर्स |
| AFK, OP, VIP, PvP | Latin | never ओपी, वीआईपी; Roblox help writes "VIP शर्ट" |
| noob | नूब | a gaming noun, so Devanagari by the rule above; kids type Latin "noob" in chat (unverified which reads better in UI) |
| trade | ट्रेड, ट्रेड करें, ट्रेड रिक्वेस्ट (feminine) | Roblox help: "Roblox पर ट्रेड करना" |
| inventory / backpack | इन्वेंट्री / बैग | Roblox help spells इन्वेंट्री; kids call a backpack बैग; बस्ता feels dated (unverified) |
| daily reward | रोज़ाना इनाम | इनाम is everyday Hindi; Indian game listings also write रिवॉर्ड्स (Stumble Guys), so डेली रिवॉर्ड is a fair alt (unverified which kids prefer) |
| codes / redeem | कोड / रिडीम करें / कोड डालें | Roblox help: "प्रोमो कोड कैसे रिडीम करें"; plural stays कोड |
| group | कम्यूनिटी | Roblox renamed Groups to Communities; Hindi help: "कम्यूनिटीज़", "कम्यूनिटी कॉन्फ़िगर करें" (Play Store spells कम्युनिटी: use the help-center spelling throughout) |
| like / favorite | लाइक करें / पसंदीदा | game page button "पसंदीदा"; help: "किसी प्लेस को पसंदीदा कैसे बनाएँ" |
| server | सर्वर | game page tab "सर्वर" |
| friends | दोस्त (in game) / फ़्रेंड्स (platform feature) | English UI went from Connections back to Friends in April 2026; Hindi help says फ़्रेंड्स, फ़्रेंड रिक्वेस्ट |
| Premium | Premium | Latin; Roblox stopped selling Premium on 2026-04-30 and now sells Roblox Plus |
| shop | शॉप | game page tab says स्टोर; दुकान also fine |
| buy / sell / claim | खरीदें / बेचें / क्लेम करें | never दावा करें (a legal claim) |
| unlock / event / free | अनलॉक करें / इवेंट / फ़्री | Roblox uses both फ़्री and मुफ़्त |

## Grammar traps in UI strings
- Plurals: CLDR puts 0 and 1 in "one". Count-safe pattern: masculine nouns not ending in -आ keep one form in the direct case, as cricket's "1 रन, 10 रन" does. So "{count} कॉइन", "{count} जेम", "{n} दिन" work for 0, 1 and 1,250. Next to a number avoid -आ nouns (1 सिक्का / 5 सिक्के), feminine nouns (चीज़/चीज़ें) and -s plurals ("1 कॉइन्स"). A verb agreeing with the counted noun still changes (1 कॉइन मिला / 5 कॉइन मिले): use चाहिए, which never changes, or a label like "+{count} कॉइन!".
- Oblique case: a postposition changes the plural (दोस्तों के लिए vs दोस्त के लिए). Don't put {count} + noun before के, में, से; use हर + singular: "हर दोस्त के लिए".
- Player gender: intransitive past and progressive verbs show it ("{player} आया/आई", "चाहता/चाहती है"). Use a ने-construction, where the verb agrees with the object instead: "{player} ने गेम जॉइन किया", "{player} ने आपको ट्रेड रिक्वेस्ट भेजी है".
- Reader gender: आप still takes gendered verbs (आप जीत गए/गई, आप खो देंगे/देंगी). Prefer imperatives, को-constructions and हैं: "आपको और कॉइन चाहिए!", "अब आप लेवल 5 पर हैं."
- Inserted item names: Hindi -आ adjectives agree with the noun (नया ड्रैगन / नई बिल्ली). Loan adjectives (लेजेंडरी, रेयर, एपिक) never inflect, so they are safe before {pet}. If a verb would agree with {pet}, put the pet after a colon: "आपने हैच किया: {rarity} {pet}!"
- Postpositions follow placeholders unchanged: "{player} का ड्रैगन", "{player} की टीम"; का/की/के agrees with the next noun, never with the name.
- Word order is SOV; the verb goes last and placeholders move: "Buy for {price} Robux" -> "{price} Robux में खरीदें".
- With आप as subject use अपना, not आपका: "अपने पेट्स बेचें", never "आप आपके पेट्स बेचें" (a common error per Microsoft).
- No articles and no capital letters in Devanagari; Latin brands keep their case (VIP, Robux). Title-case rules do not apply.

## Typography and formatting
- Sentence end: the Latin period "." -- Roblox's Hindi help, web and Play Store text all use it, and Microsoft requires it. Do not use the danda "।", and never mix the two in one game.
- "!" and "?" attach with no space: "लेवल अप!" Quotes: Roblox puts straight single quotes around UI names and messages ("एक 'पूरा हो गया' मैसेज"); a period goes after the closing quote, as Microsoft requires.
- Digits: Western 0-9 (CLDR default for hi; Roblox and Google Play use them). Never Devanagari digits (१,२५०), which Hindi Wikipedia uses.
- Grouping: CLDR and Indian apps group by lakh: 1,25,000, not 125,000. {count} arrives formatted by game code, so tell the developer rather than editing the string. Big-number words: हज़ार, लाख, करोड़ (CLDR short: हज़ार, लाख, क॰); Latin "1.2K" in a tight HUD (unverified).
- Percent: no space: "+20% बूस्ट".
- Durations are code-formatted. CLDR short forms: "3 घं॰ 20 मि॰", "2 दिन 5 घं॰"; narrow: "3 घं 20 मि". Pass these to the developer if {time} prints "3h 20m".
- Ellipsis: keep "..." for in-progress states, as Microsoft does: "लोडिंग...".
- Nukta: write ज़ and फ़ where English has z/f, as Roblox does (फ़्री, ज़्यादा, म्यूज़िक, फ़्रेंड्स). Never add one to क, ख, ग (गलत, खत्म), per Microsoft.
- Chandrabindu: जाएँ, पाएँ, आएँ, as Microsoft asks; when a vowel sign sits above the headline use the anusvara dot instead: खरीदें, करें, में. Roblox's own text mixes जाएँ and जाएं; pick the chandrabindu form and keep it game-wide.
- Keyboard keys stay Latin: "खोलने के लिए E दबाएँ".
- Strip stray zero-width joiners (U+200C, U+200D) that MT and copy-paste leave inside words. Lines break only at spaces; never split a conjunct.

## Do not translate / keep as is
- Robux, Roblox, Premium, Roblox Plus, VIP, XP, AFK, OP, PvP, and multipliers like "2x".
- Game titles stay Latin, as on Roblox's Hindi pages ("Adopt Me!", "Dress to Impress", "Steal a Brainrot"): "Pet Hatch Tycoon".
- Promo codes (FREEPETS), usernames and display names, keybinds (E, Shift), URLs.
- Item and pet names: transliterate an English fantasy name (लकी पोशन, ड्रैगन); use the Hindi word when a kid would say it (तलवार for sword, बिल्ली for cat, अंडा for egg).
- Script: Devanagari for everything outside this list. Romanized Hindi ("Shop kholne ke liye E dabao") never goes in `hi-in`.

## Rendering on Roblox
- The Roblox Windows client ships NotoSansDevanagariUI-Regular.ttf in content/fonts (seen in a 2026-11 install) as the Devanagari fallback. A 2026 DevForum post says Hindi has proper font support while Tamil and Telugu still show boxes; a 2019 post saying Hindi shows boxes is outdated.
- Only the Regular weight of that Noto ships. Builder Sans (Roblox's UI font) and stylized fonts (Fredoka One, Luckiest Guy) have no Devanagari, so Hindi falls back to plain Noto beside stylized Latin ("VIP", numbers). Unverified: whether Bold FontWeight or RichText <b> makes this fallback visibly bold. Keep the tags, check the emphasis shows, and add color if not.
- Two built-in fonts do carry Devanagari (cmaps checked in the shipped files, 2026-11-08): Sarpanch, a squared display face whose Regular and Bold files ship with the client, and Kalam (handwritten). A game that wants a styled or truly bold Hindi look can set its Hindi labels to Sarpanch; check its shaping in Studio first (unverified).
- Devanagari stacks marks above the headline (ि ी े ै ं ँ, reph र्) and below the baseline (ु ू ृ ्). With TextScaled or a tight label height, check tops and bottoms are not clipped on "क्लेम करें", "कम्यूनिटी", "ड्रैगन".
- Check shaping in Studio with the hi-in test locale: the short-i sign sits before its consonant (कि, not क ि), conjuncts join (क्ल, ड्र, स्त), and no dotted circles (◌) appear (unverified for every conjunct; no broken cases reported).
- Max lengths: the skill's lint skips {params}, tags, nukta and virama but counts every other vowel sign, anusvara and chandrabindu, though marks above or below the headline add no width (खेलें counts 5 and is about 2 letters wide). A string inside its budget fits; one slightly over may still fit, so check rendered width in Studio before cutting words.

## Mistakes machine translation makes here
1. Textbook Hindi: "अधिक सिक्के क्रय करें" -> "और कॉइन खरीदें".
2. Rebirth as religion: "अभी पुनर्जन्म लें?" -> "अभी रीबर्थ करें?"
3. Claim as a legal claim: "दावा करें" -> "क्लेम करें" or "इनाम लें".
4. Boost as encouragement: "{percent}% बढ़ावा" -> "+{percent}% बूस्ट".
5. Male default for players: "{player} गेम में शामिल हुआ" -> "{player} ने गेम जॉइन किया".
6. Male default for the reader: "आप लेवल 5 पर पहुँच गए!" -> "अब आप लेवल 5 पर हैं."
7. Counted -s plural: "1 कॉइन्स" -> "1 कॉइन".
8. Stomach joke: "Pets full!" -> "पेट भर गया!" (reads "I'm full") -> "पेट्स की जगह भर गई!"
9. Wrong possessive: "आप आपके पेट्स बेचें" -> "अपने पेट्स बेचें".
10. Danda and Devanagari digits: "आपको १०० कॉइन मिले।" -> "आपको 100 कॉइन मिले."
11. Brands in Devanagari: "रोबक्स में खरीदें", "वीआईपी" -> "Robux में खरीदें", "VIP".
12. Mixed address: "यहाँ खेलो, फिर खरीदें" -> "यहाँ खेलें, फिर खरीदें".
13. Romanized Hinglish in the column: "Shop kholne ke liye E dabao" -> "खोलने के लिए E दबाएँ".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | खेलें | Roblox's own verb |
| shop.title | शॉप | alt दुकान; Roblox's game page tab says स्टोर |
| shop.buy | खरीदें | |
| reward.claim | क्लेम करें | 9 of 10 as the lint counts; alt "इनाम लें"; never "दावा करें" |
| rebirth.button | रीबर्थ | |
| rebirth.confirm | अभी रीबर्थ करें? आपके कॉइन चले जाएँगे, लेकिन आपको हमेशा के लिए {multiplier}x बूस्ट मिलेगा. | "हमेशा के लिए" = permanent; कॉइन and बूस्ट are the subjects, so no reader gender |
| coins.need_more | आपको {amount} और कॉइन चाहिए! | और = more; correct for 1 |
| coins.count | {count} कॉइन | bare form is right for 0, 1 and many |
| egg.hatched | आपने हैच किया: {rarity} {pet}! | colon keeps the verb clear of the pet's gender; "अंडे से निकला: ..." or "{pet} मिला!" agree with the pet and break on feminine names (बिल्ली) |
| rarity.legendary | लेजेंडरी | loan adjective, never inflects; spelling लीजेंडरी also seen (unverified which dominates) |
| pet.name.dragon | ड्रैगन | |
| chat.player_joined | {player} ने गेम जॉइन किया | ने-construction: same text for any gender |
| trade.request | {player} ने आपको ट्रेड रिक्वेस्ट भेजी है | rephrased as "sent you a trade request" to avoid चाहता/चाहती |
| prompt.open_shop | खोलने के लिए E दबाएँ | E stays Latin |
| pass.buy_price | {price} Robux में खरीदें | natural shop phrasing (₹99 में खरीदें); the lint counts 17 of 22, since {price} is not counted. Label form "खरीदें: {price} Robux" for a very narrow button |
| pass.coins2x | 2x कॉइन | |
| pass.vip | VIP | kept: acronym, Latin on Roblox's Hindi pages ("VIP शर्ट") |
| reward.daily_title | रोज़ाना इनाम | alt डेली रिवॉर्ड |
| reward.come_back | अगला इनाम पाने के लिए {time} बाद फिर आएँ! | |
| codes.placeholder | कोड डालें | everyday verb for typing a code in; Roblox help writes "अपना कोड एंटर करें", also fine |
| codes.invalid | यह कोड गलत है या एक्सपायर हो चुका है. | Roblox's promo-code help says "एक्सपायर हो सकते हैं"; alt "खत्म हो चुका है" |
| social.like_reward | गेम को लाइक करें और फ़्री <b>लकी पोशन</b> पाएँ! | item name transliterated |
| social.group_reward | फ़्री इनाम अनलॉक करने के लिए हमारी कम्यूनिटी जॉइन करें! | कम्यूनिटी = Roblox's current name for groups; 52 of 55 as the lint counts |
| afk.warning | आप AFK हैं. कमाते रहने के लिए चलें-फिरें! | |
| leaderboard.title | टॉप प्लेयर्स | Roblox uses टॉप and प्लेयर्स |
| level.up | लेवल अप! अब आप लेवल {level} पर हैं. | हैं avoids reader gender |
| tutorial.sell | अपने पेट्स बेचने के लिए चमकते घेरे में जाएँ. | घेरा = ring or circle |
| inventory.full | आपका बैग भर गया है! जगह बनाने के लिए पेट्स बेचें. | |
| settings.music | म्यूज़िक | alt संगीत |
| settings.on | चालू | Roblox help pairs चालू / बंद |
| loading | लोडिंग... | "लोड हो रहा है..." is 16 code points, over 14 |
| event.ends_in | इवेंट {time} में खत्म होगा | होगा agrees with इवेंट (masculine) |
| item.op | यह तलवार OP है! | native तलवार beats स्वॉर्ड |
| friends.boost | आपके सर्वर में हर दोस्त के लिए +{percent}% बूस्ट | हर + singular avoids the oblique plural |

## Sources
1. Microsoft Hindi Localization Style Guide -- https://aka.ms/hindi-styleguide
2. CLDR Language Plural Rules -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON, Hindi units and numbers -- https://github.com/unicode-org/cldr-json (cldr-units-full/main/hi/units.json, cldr-numbers-full/main/hi/numbers.json)
4. Roblox Help (hi), Robux पाने के तरीके -- https://en.help.roblox.com/hc/hi/articles/203313200
5. Roblox Help (hi), फ़्रेंड्स कैसे बनाएं -- https://en.help.roblox.com/hc/hi/articles/203313580
6. Roblox Help (hi), एक्सपीरिएंस पासेस -- https://en.help.roblox.com/hc/hi/articles/203314040
7. Roblox Help (hi), किसी प्लेस को पसंदीदा कैसे बनाएँ -- https://en.help.roblox.com/hc/hi/articles/203313670
8. Roblox Help (hi), Roblox पर ट्रेड करना -- https://en.help.roblox.com/hc/hi/articles/203313310
9. Roblox Help (hi), Roblox Premium मेंबरशिप -- https://en.help.roblox.com/hc/hi/articles/360024256251
10. Roblox Help (hi), community join requirements and in-experience leaderboard -- https://en.help.roblox.com/hc/hi/articles/39978135454228 and https://en.help.roblox.com/hc/hi/articles/204343250
11. roblox.com in Hindi, charts and a game page -- https://www.roblox.com/hi/charts and https://www.roblox.com/hi/games/920587237/Adopt-Me
12. Google Play, Roblox listing in Hindi (Roblox's description, player reviews, and the Stumble Guys description shown beside it) -- https://play.google.com/store/apps/details?id=com.roblox.client&hl=hi&gl=IN
13. Outlook Respawn, Roblox adds Hindi support -- https://respawn.outlookindia.com/gaming/gaming-news/roblox-adds-hindi-support-for-players-and-creators-in-india
14. Roblox Creator docs, Automatic translations -- https://create.roblox.com/docs/production/localization/automatic-translations
15. DevForum, "Add Telugu, Tamil and Lao fonts" (2026-04-03) -- https://devforum.roblox.com/t/4555745
16. DevForum, "Cloud Localization Support Extended to 45 Languages" (2019 reply on Hindi boxes) -- https://devforum.roblox.com/t/337149
17. DevForum, "Friends Are Back!" (2026-04-02) -- https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
18. Keywords Studios, The rise of Hinglish -- https://www.keywordsstudios.com/en/about-us/news-events/news/the-rise-of-hinglish-localizing-for-the-indian-market/
19. CurseForge, RR Hinglish Language Pack (Latin-script Hinglish made by players) -- https://www.curseforge.com/minecraft-bedrock/addons/rr-hinglish-language-pack
20. Hindi Wikipedia, रोब्लॉक्स (formal register for contrast) -- https://hi.wikipedia.org/wiki/रोब्लॉक्स
21. Roblox Help (hi), प्रोमो कोड कैसे रिडीम करें? -- https://en.help.roblox.com/hc/hi/articles/360029650831
22. Roblox Windows client, content/fonts and content/fonts/families (font files and their cmaps, checked 2026-11-08)
