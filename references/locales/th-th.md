# Thai (th-th) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `th-th` (a bare `th` column is optional; Thai has one variant, so it may carry the same text) |
| Script, direction | Thai script (abugida), LTR; no spaces between words, a space marks a clause or sentence end; Arabic digits |
| Address the player as | no pronoun when the sentence works without one; คุณ when it needs one; never ท่าน, เธอ, นาย or แก |
| Text expansion vs English | measured in Studio on the reference strings: mostly 10-35% narrower than English (mean -13% vs Source Sans, -26% vs Fredoka One); one-word buttons up to +40% (รับรางวัล vs Claim). Layout line height equals Latin; stacked marks may still need padding (unverified) |
| Plural categories (CLDR) | other (only one form, cardinal and ordinal) |
| Model confidence | medium: Thai is well covered, but models add ครับ/ค่ะ, drift formal, misspell loanwords and cannot see line-breaking failures |
| Native review before shipping | strongly recommended |

## Audience and register
Thai Roblox players are mostly kids and young teens. Write short, lively, everyday Thai, like a friendly game host, not a bank, a government form or a school textbook. Microsoft's Thai guide already asks for conversational words over formal ones (พบ, not ประสบ; แต่, not อย่างไรก็ตาม); a kids' game goes one step further.
- Polite particles: never ครับ or ค่ะ/คะ in buttons, labels, titles, toasts or system text. They mark the speaker's gender (ครับ male, ค่ะ female), so the game would pick a gendered narrator, and written UI Thai leaves them out (Roblox's own Thai UI has none). ซื้อเลยค่ะ -> ซื้อเลย!
- Exception: dialogue from an NPC with a set gender may end lines with ครับ (male) or ค่ะ / คะ in questions (female). Keep one NPC consistent across every key.
- Gender-neutral softeners are fine, at most one per string: นะ (friendly nudge), เลย (go ahead, right now), กัน (let's), สิ (come on). กลับมาใหม่นะ! / รับเลย! / มาเล่นกัน!
- Skip จ้า/จ้ะ (cutesy, sounds like an adult talking down to a child) and กรุณา/โปรด on fun text. Keep โปรด for real errors about purchases or accounts: โปรดลองอีกครั้ง
- Drop "you"; Thai omits subjects naturally. When a pronoun is needed, use คุณ (Microsoft's choice). เธอ is gendered, นาย is male, ท่าน is honorific, แก is rude.
- Buttons and labels: bare verb or noun, no subject, no particle. เล่น / ซื้อ / รับรางวัล / ร้านค้า
- Hype: ! is natural, plus สุดยอด, เย้, ว้าว in moderation. Never 555 (Thai "lol") or slang like โคตร in UI.
- Questions: ไหม (รีเบิร์ธเลยไหม?), not the formal หรือไม่ that Roblox's system prompts use, nor the chat spelling มั้ย
- Prefer short everyday verbs: ได้ over ได้รับ in toasts, ใส่ over ป้อน, ใช้ไม่ได้ over ไม่สามารถใช้งานได้

## Roblox and gaming vocabulary
| English | Use in th-th | Note |
|---|---|---|
| Robux | Robux | Latin, as in Roblox's Thai UI (ซื้อ Robux). Thai Wikipedia writes โรบักซ์; never in UI |
| game pass | เกมพาส | Roblox th docs say พาส; เกมพาส is clearer in a shop (unverified which players write more) |
| developer product | the item's name | docs: ผลิตภัณฑ์ของนักพัฒนา; players never see that word |
| experience / game | เกม | Roblox's Thai system UI says ประสบการณ์ (เข้าร่วมประสบการณ์); its docs and Thai Wikipedia say เกม. In a game, always เกม |
| obby | ออบบี้ / ด่านกระโดด | (unverified) keep "Obby" in titles |
| tycoon / simulator | ไทคูน / ซิมูเลเตอร์ | keep English inside game titles; ซิมมูเลเตอร์ is a common variant spelling (unverified which kids prefer) |
| rebirth | รีเบิร์ธ | Thai game sites write Rebirth, รีเบิร์ธ, plain เกิดใหม่ or จุติ; รีเบิร์ท not seen. Button: รีเบิร์ธ, explained once with เกิดใหม่ (which kids prefer is unverified). Never การเกิดใหม่ on a button |
| pet | สัตว์เลี้ยง | as on Thai Roblox code sites; เพ็ท on tight labels (unverified) |
| egg / hatch | ไข่ / ฟักไข่, ฟักได้ | ฟักได้มังกร! = hatched a dragon |
| coins / gems | เหรียญ / เพชร | เพชร is the usual Thai game word for gems and diamonds (unverified for "gems"); if a game has both, gems = เจม |
| rarity | ตำนาน, หายาก | Thai game sites: ระดับตำนาน (Legendary); not the loanword เลเจนดารี |
| item / badge | ไอเท็ม / เหรียญตรา | Roblox's Thai spellings (not ไอเทม); keep เหรียญ for coins only |
| boost / multiplier | บูสต์ / x2, 2 เท่า | x2 on tags and names; 2 เท่า in sentences, works for 1.5 เท่า |
| XP / level up | EXP / เลเวลอัป | level = เลเวล; ระดับ only for tiers like rarity |
| quest | เควสต์ | daily quest = เควสต์รายวัน; ภารกิจ also fine |
| leaderboard | ตารางอันดับ / อันดับ | Roblox's Thai player list says ตารางอันดับ; a board title can be อันดับผู้เล่น; not ลีดเดอร์บอร์ด |
| AFK | AFK | Latin; Thai gamers use it as is |
| noob | มือใหม่ | นูบ is teasing slang; avoid in UI |
| OP | เทพ / โกง | เทพสุดๆ = godlike; โกง (lit. cheating) is player slang for overpowered; never leave "OP" |
| VIP | VIP | Latin |
| trade | เทรด | gamer loanword (unverified which kids prefer); Thai game sites write แลกเปลี่ยน, fine in explanations |
| inventory / backpack | คลัง / กระเป๋า | Roblox's Thai UI: คลังไอเท็ม (Inventory), แบ็คแพ็ค (its Backpack hotbar); for a game's pet storage, กระเป๋า is plainer |
| daily reward | รางวัลรายวัน | |
| codes | โค้ด | ใส่โค้ด / แลกโค้ด; not รหัส, which reads as a password or PIN (a few code sites write รหัสแลกรับ) |
| group | กลุ่ม | Roblox th docs: กลุ่ม, เข้าร่วมกลุ่ม; Roblox's newer "Community" label shows as ชุมชน |
| like / favorite | กดไลก์ / รายการโปรด | Roblox's Thai UI: รายการโปรด, เพิ่มไปยังรายการโปรด; its like button has no text label to copy |
| server | เซิร์ฟเวอร์ | as on Roblox th game pages; players shorten to เซิร์ฟ |
| friends | เพื่อน | Roblox's Thai UI says เพื่อน, เพิ่มเพื่อน in most strings and คนรู้จัก ("acquaintance") in its Connections-era friend prompts. In game text always เพื่อน |
| Premium | Premium | Roblox th docs: สมาชิก Premium |
| shop | ร้านค้า | Roblox th game page Store tab |

## Grammar traps in UI strings
- Plurals: none. "{count} Coins" -> {count} เหรียญ works for 0, 1 and 1,250. Never add พวก or ๆ to make a plural.
- Classifiers: Thai counts noun + number + classifier (สัตว์เลี้ยง 3 ตัว / ดาบ 1 เล่ม / ผู้เล่น 5 คน). Currency names count themselves ({amount} เหรียญ / {price} Robux). "each friend" -> ต่อเพื่อน 1 คน or เพื่อนแต่ละคน
- Gender: no agreement, so {player} needs nothing around it. The only gender traps are particles and pronouns (see register).
- Modifier after noun: "Legendary Dragon" -> มังกรระดับตำนาน (not ตำนานมังกร). For "{rarity} {pet}" write {pet}ระดับ{rarity}; ระดับ fits every rarity word (ระดับหายาก / ระดับตำนาน)
- Head-first compounds: Daily Reward -> รางวัลรายวัน; 2x Coins -> เหรียญ x2.
- Placeholders that hold digits or Latin ({count}, {price}, {player}, {time}) get a space on both sides (ต้องใช้อีก {amount} เหรียญ!). Placeholders that always hold Thai words ({pet}, {rarity}) attach directly (ฟักได้{pet}ระดับ{rarity}!)
- Aspect, not tense: แล้ว for done (เต็มแล้ว), กำลัง for in progress (กำลังโหลด...), จะ for what will happen.
- Avoid the ถูก passive (Microsoft rule): สัตว์เลี้ยงถูกขายแล้ว -> ขายสัตว์เลี้ยงแล้ว
- Restructure "in {time}" sentences: "Come back in {time}" -> อีก {time} กลับมาใหม่นะ, not กลับมาใน {time}. Countdown labels may keep จบใน {time} ("ends within").
- No capitalization in Thai. Latin words keep their case: VIP, Robux, AFK.

## Typography and formatting
- No sentence-final period, ever (Microsoft rule): end with the last word (โค้ดไม่ถูกต้อง) or with ! or ?. The period is only for abbreviations (ชม.)
- Thai uses a space where English uses a comma or period between clauses (เหรียญจะหายหมด แต่จะได้บูสต์). Commas only inside numbers and lists of numbers.
- ! and ? attach to the word, no space before; one space after when text follows (เลเวลอัป! ตอนนี้เลเวล 5 แล้ว)
- Space on both sides of digits and Latin words (Microsoft examples: มีส้ม 3 ผล, Windows ไม่สามารถ...): ซื้อด้วย 100 Robux.
- Digits are Arabic (1, 250), never Thai ๑๒๓ (government use). Thousands comma: 1,250. Percent attached: 50%.
- Quotes and parentheses as in English: "FREEPETS". Ellipsis stays ...: กำลังโหลด...
- Durations: ask game code to format {time} as 3 ชม. 20 นาที / 2 วัน 5 ชม. / 45 วินาที; 3h 20m is a readable fallback. ชม. is Microsoft's approved short form; never abbreviate วินาที
- ๆ (mai yamok, repeat): Royal Institute style spaces it (เด็ก ๆ), but Roblox's own Thai UI always attaches it (ใดๆ, ต่างๆ). Attach it (สุดๆ): Roblox breaks lines at a space, so a spaced ๆ can start a line. Avoid ฯลฯ in UI
- Line breaking, the big Thai risk. Measured in Studio (TextService, 2026-11-08): Roblox has no Thai word breaking. It breaks at spaces; a space-free run too long for the line is cut at any character, mid-word (วง|กลม, เลี้ย|ง), and a line may start with ! or ๆ. Rules:
  - Put a normal space at every natural clause pause, so the wrap lands there: เดินเข้าไปในวงกลมเรืองแสง เพื่อขายสัตว์เลี้ยง
  - Keep each space-free run short enough to fit one line: about 10 characters on buttons and tags, about 20 in wrapped body text (estimate; check at phone size).
  - Never add a space inside a word, before ! ?, or before a particle or ๆ: that creates a bad break (a line starting with นะ or ๆ).
  - Never use zero-width spaces (U+200B): measured, Roblox draws them at zero width but does not break at them, and they inflate length counts.
  - Avoid hard line breaks in table strings except in fixed-size panels.
- Max lengths count code points: Thai vowel and tone marks (ั ิ ี ุ ู ่ ้ ๊ ๋ ์) count but take no width, so Thai looks shorter than its count.
- Keyboard keys stay Latin, spaced: กด E เพื่อเปิด

## Do not translate / keep as is
- Robux, Roblox, VIP, Premium, AFK, promo codes (FREEPETS), usernames and display names, keybinds (E, Shift).
- Game title: keep the owner's title (Pet Hatch Tycoon). Roblox may auto-translate titles on its Thai pages (Adopt Me! shows as รับฉันมาเลี้ยง!), so ask the owner whether to set an official Thai title.
- Item and pet names are translated by meaning, not transliterated: Dragon -> มังกร, Lucky Potion -> ยาเพิ่มโชค (Thai code sites name potions ยา + effect, like ยาบิน).
- Gaming loanwords that Thai players use stay as Thai-script loanwords: เลเวล, บูสต์, เควสต์, อัปเดต, ออนไลน์
- Spell loanwords the Royal Institute way, not the common misspelling: เกม (not เกมส์), อัปเดต (not อัพเดท), ไลก์ (common ไลค์ is also seen).
- Fill every key: Roblox auto-translates Thai, and a missing key gets a machine string that may clash with your terms.

## Rendering on Roblox
- Roblox has shaped text with HarfBuzz since June 2018 (DevForum), so Thai vowels and tone marks should position correctly. No Thai-specific bug report for TextLabels found.
- Font: the Roblox client ships one Thai font, NotoSansThaiUI-Regular.ttf. Measured in Studio, Thai has identical widths in Source Sans, Gotham, Fredoka One, Luckiest Guy, Builder Sans and Arial, so every Font falls back to it. Expect plain Thai beside stylized Latin.
- Bold: measured, Thai keeps the same widths at Bold weight while Latin widens, so RichText <b> and bold fonts very likely leave Thai regular (visual check unverified). Keep the <b> tags anyway; use color or size for emphasis that must show.
- Stacked marks clip: a 2023 Translator Portal bug cut tone marks off the top of ซื้อ, เพื่อ, พี่ (fixed there). In games, check tight TextLabels and TextScaled text with ที่, น้ำ, ซื้อ, ปู่ (marks above and below) and add padding or LineHeight if they clip (unverified whether they do).
- Wrapping: no Thai word breaking (measured; see Typography). Preview long strings in Studio's th-th test locale at phone size and look for mid-word cuts.

## Mistakes machine translation makes here
- Gendered particles in UI: รับรางวัลแล้วครับ -> รับรางวัลแล้ว!
- Formal register: ท่านได้รับรางวัลเรียบร้อยแล้ว -> ได้รางวัลแล้ว!
- คุณ in every clause: คุณได้เลเวลอัป คุณอยู่เลเวล 5 -> เลเวลอัป! ตอนนี้เลเวล 5 แล้ว
- English punctuation copied: โค้ดไม่ถูกต้อง. / เหรียญจะหายไป, แต่ -> no period; space instead of comma
- Claim as อ้างสิทธิ์ (legal claim): อ้างสิทธิ์ -> รับ / รับรางวัล
- Code as รหัส (reads as password): ใส่รหัส -> ใส่โค้ด
- Friends as Roblox's Connections term: คนรู้จักในเซิร์ฟเวอร์ -> เพื่อนในเซิร์ฟเวอร์
- Experience as ประสบการณ์: กดไลก์ประสบการณ์นี้ -> กดไลก์เกมนี้
- 2x as twice: เหรียญ 2 ครั้ง -> เหรียญ x2 / เหรียญ 2 เท่า
- Rebirth as a noun phrase on a button: การเกิดใหม่ -> รีเบิร์ธ
- OP kept or rendered literally: ดาบนี้ OP / ดาบนี้มีพลังเกิน -> ดาบเล่มนี้เทพสุดๆ!
- Western word spacing: ต้องการ อีก 5 เหรียญ -> ต้องใช้อีก 5 เหรียญ
- Loanword misspellings: เกมส์ / อัพเดท -> เกม / อัปเดต

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | เล่น | |
| shop.title | ร้านค้า | matches Roblox's Store tab |
| shop.buy | ซื้อ | |
| reward.claim | รับรางวัล | รับ alone for tighter buttons; never อ้างสิทธิ์ |
| rebirth.button | รีเบิร์ธ | Thai game sites pair Rebirth with รีเบิร์ธ; เกิดใหม่ if the game avoids loanwords |
| rebirth.confirm | รีเบิร์ธเลยไหม? เหรียญจะหายหมด แต่จะได้บูสต์ {multiplier} เท่าติดตัวตลอดไป! | ติดตัวตลอดไป = "stays with you forever", kid-friendly for permanent |
| coins.need_more | ต้องใช้อีก {amount} เหรียญ! | fine for 1 |
| coins.count | {count} เหรียญ | no plural form needed |
| egg.hatched | ฟักได้{pet}ระดับ{rarity}! | Thai order: pet, then ระดับ + rarity; if pet names stay Latin, space around {pet} |
| rarity.legendary | ตำนาน | standard Thai game tier; reads ระดับตำนาน in egg.hatched |
| pet.name.dragon | มังกร | |
| chat.player_joined | {player} เข้าร่วมเกมแล้ว | |
| trade.request | {player} อยากเทรดกับคุณ | คุณ needed here; {player} ขอแลกไอเท็มกับคุณ if the game avoids เทรด |
| prompt.open_shop | กด E เพื่อเปิด | |
| pass.buy_price | ซื้อด้วย {price} Robux | ด้วย avoids reading as "buy {price} Robux" |
| pass.coins2x | เหรียญ x2 | เหรียญ 2 เท่า if the font makes x2 look odd |
| pass.vip | VIP | kept: Thai players use VIP in Latin |
| reward.daily_title | รางวัลรายวัน | |
| reward.come_back | อีก {time} กลับมารับรางวัลถัดไปนะ! | needs {time} as 3 ชม. 20 นาที |
| codes.placeholder | ใส่โค้ด | |
| codes.invalid | โค้ดนี้ไม่ถูกต้อง หรือหมดอายุแล้ว | space gives a break point; no period |
| social.like_reward | กดไลก์เกมนี้ รับ<b>ยาเพิ่มโชค</b>ฟรี! | item name translated; the Thai inside <b> likely stays regular weight (see Rendering) |
| social.group_reward | เข้าร่วมกลุ่มของเรา ปลดล็อกรางวัลฟรี! | เข้าร่วมกลุ่ม as in Roblox th docs |
| afk.warning | AFK อยู่นะ! ขยับตัวเพื่อฟาร์มต่อ! | ฟาร์ม = grind, common Thai gamer word |
| leaderboard.title | อันดับผู้เล่น | "player ranking" |
| level.up | เลเวลอัป! ตอนนี้เลเวล {level} แล้ว | |
| tutorial.sell | เดินเข้าไปในวงกลมเรืองแสง เพื่อขายสัตว์เลี้ยง | "your" dropped |
| inventory.full | กระเป๋าเต็มแล้ว! ขายสัตว์เลี้ยง เพื่อเพิ่มพื้นที่ | space before เพื่อ splits a 30-character run |
| settings.music | เพลง | |
| settings.on | เปิด | pair with ปิด |
| loading | กำลังโหลด... | Microsoft pattern กำลัง + verb + ... |
| event.ends_in | กิจกรรมจบใน {time} | กิจกรรม is the usual Thai word for a game event; อีเวนต์ also seen |
| item.op | ดาบเล่มนี้เทพสุดๆ! | เล่ม = classifier for swords; โกงสุดๆ is the slangier option |
| friends.boost | บูสต์ +{percent}% ต่อเพื่อน 1 คนในเซิร์ฟเวอร์ | |

## Sources
1. Microsoft Thai Localization Style Guide: https://download.microsoft.com/download/3/f/2/3f236167-639e-46f2-8201-554c36bcbf31/tha-tha-StyleGuide.pdf
2. CLDR Language Plural Rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox Creator docs th-th, Passes: https://create.roblox.com/docs/th-th/production/monetization/passes
4. Roblox Creator docs th-th, Engagement-based payouts: https://create.roblox.com/docs/th-th/production/monetization/engagement-based-payouts
5. Roblox Creator docs th-th, Groups: https://create.roblox.com/docs/th-th/projects/groups
6. Roblox game page in Thai (Adopt Me!): https://www.roblox.com/th/games/920587237/Adopt-Me
7. Roblox Creator docs, Automatic translations: https://create.roblox.com/docs/production/localization/automatic-translations
8. Thai Wikipedia, โรบล็อกซ์: https://th.wikipedia.org/wiki/โรบล็อกซ์
9. games.gg Thai, Adopt Me! codes (โค้ด, ฟักไข่, สัตว์เลี้ยง): https://games.gg/th/news/adopt-me-roblox-codes/
10. BlueStacks Thai, Catch and Tame codes: https://www.bluestacks.com/th/blog/redeem-codes/roblox-catch-and-tame-redeem-codes-th.html
11. DevForum, Thai tone marks clipped in Translator Portal (2023): https://devforum.roblox.com/t/bug-with-thai-translation-fonts-via-translator-portal/2397589
12. DevForum, HarfBuzz typesetter for connected scripts (2018): https://devforum.roblox.com/t/support-for-arabic-text-and-other-languages-where-letters-are-connected/116447
13. Roblox client strings, th-th column of CoreScriptLocalization.csv (build of 2026-11-05): %LOCALAPPDATA%/Roblox/Versions/<version>/ExtraContent/translations/
14. Wikipedia, Thai script (spacing, ๆ, numerals): https://en.wikipedia.org/wiki/Thai_script
15. Wikipedia, Thai language (particles, pronouns, classifiers): https://en.wikipedia.org/wiki/Thai_language
16. games.gg Thai, Steal a Brainrot and Plants vs Brainrots (Rebirth, รีเบิร์ธ, เกิดใหม่, จุติ, ระดับตำนาน): https://games.gg/th/steal-a-brainrot/ and https://games.gg/th/plants-vs-brainrots/
17. Studio measurements with TextService:GetTextSize, 2026-11-08 (wrapping, U+200B, fallback font, bold, width vs English) (this review)
