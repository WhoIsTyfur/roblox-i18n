# Croatian (hr-hr) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `hr-hr` (bare `hr` also fine: Croatian has one variant on Roblox). Never share text with `sr-rs` or `bs-ba` |
| Script, direction | Latin (with č ć đ š ž), LTR. Never Cyrillic |
| Address the player as | informal singular "ti" everywhere; never "vi"/"Vi" |
| Text expansion vs English | about +10-30% for sentences (the reference set below averages +9%, written tight); one-word buttons and titles up to 2x ("Shop" -> "Trgovina") |
| Plural categories (CLDR) | one, few, other |
| Model confidence | medium -- LLMs drift into Serbian/Bosnian forms (ekavian, "da li", "muzika") and miss gender and case agreement |
| Native review before shipping | strongly recommended |

## Audience and register
- Write standard Croatian: ijekavian, Croatian vocabulary, Latin script. It is read in Croatia and by Croats in Bosnia and Herzegovina and abroad. No dialect words (kajkavian "kaj", Dalmatian "ća").
- Roblox's own UI is not in Croatian. Roblox's locale API (checked 2026-11-08) has `hr_hr` enabled for in-game content only, not for the full site and app, and roblox.com/hr/ served English while /de/ served German. Players read Roblox itself in English and know the English gaming words; your game may be the only Croatian they see on Roblox.
- How a player gets `hr-hr`: `Player.LocaleId` is the locale on the player's Roblox account, and players can switch language in the in-game Settings menu, which offers the languages the game supports (Roblox docs). So add Croatian under Supported Languages in the game's localization settings, or Croatian players cannot pick it. Whether a Croatian device language sets `hr-hr` by itself is unverified; test with Studio's Player Emulator.
- Use "ti" in every string. Microsoft's guide uses lowercase "vi" for software but allows an informal, playful tone for games; Minecraft's Croatian, the closest kid-game model, uses ti ("Otvori svoj inventar", "Pritisni %s"). Never mix: "Pritisni E i preuzmi nagradu", not "Pritisnite E i preuzmi".
- Buttons that act at once: 2nd-person singular imperative, the Microsoft rule for direct commands: "Igraj", "Kupi", "Preuzmi", "Odustani". Titles and tabs: nouns ("Trgovina", "Postavke"). Ongoing process: verbal noun ("Učitavanje...").
- Hype is short exclamations: "Bravo!", "Super!", "Hura!", "Nova razina!", "Sretno!" (never Serbian "Srećno"). Stiff, adult phrasing to avoid (Microsoft's list): "izvršiti kupnju", "u svrhu", "biti u mogućnosti" -> "kupiti", "za", "moći".
- Drop the possessives English needs: "Ruksak je pun!", not "Tvoj ruksak je pun!". If one is needed, use reflexive "svoj" (Microsoft prefers "Poslužite se svojom adresom" over "Koristite vašu adresu").
- Don't blame the player in errors; it also avoids gendered past tense: "Kod ne vrijedi" rather than "Unio si pogrešan kod" (unio/unijela).
- Kid-safe: no insults ("glupan", "kreten"); "nub" only in a friendly joke.

## Roblox and gaming vocabulary
| English | Croatian | note |
|---|---|---|
| Robux | Robux | Latin, undeclined in UI, like a currency code ("123,45 EUR" per Microsoft): "Kupi za 100 Robux". hr.wikipedia also leaves it undeclined. Players decline it in chat ("robuxi", unverified). |
| Premium | Premium | as Roblox brands it; hr.wikipedia: "Roblox Premium članstvo". |
| game pass | game pass | players keep it in English (unverified); in the shop just show the pass name. |
| developer product | proizvod, paket | players never see the term; name the item. |
| experience / game | igra | never "iskustvo" in UI (= experience points). hr.wikipedia notes Roblox calls games "iskustva"; players say "igra". |
| obby | obby; parkour | "parkour" in descriptions (hr.wikipedia spelling; not Serbian "parkur"). Which one players say is unverified. |
| tycoon | tycoon | keep English; "tajkun" in Croatia mostly means someone who got rich shadily in the privatization years (hr.wikipedia). |
| simulator | simulator | |
| rebirth | preporod; verb preporoditi se | "Ponovno rođenje" is 16 chars and sounds religious. |
| pet | ljubimac, pl. ljubimci | "pet"/"petovi" in chat (unverified); UI says ljubimac. |
| egg / hatch | jaje (pl. jaja) / izleći se | "Ljubimac se izlegao"; button "Otvori". |
| coins | novčići (novčić, m.) | friendlier than "kovanice". |
| gems | dragulji (dragulj, m.) | "dijamanti" if the art shows diamonds (Minecraft: "Dijamant"). |
| boost | pojačanje; bonus | "boost" in player chat (unverified). |
| multiplier | množitelj; "x2" | |
| XP | XP; bodovi iskustva | Minecraft: "razina iskustva". Pick one per game. |
| level up | nova razina | "level" in chat (unverified); never "nivo" (Serbian/colloquial). |
| quest | zadatak; misija | |
| leaderboard | ljestvica; najbolji igrači | |
| AFK | AFK | Latin. |
| noob | početnik (UI); nub (jokes) | |
| OP | ludo jak; prejak | "OP" also used by gamers (unverified). |
| VIP | VIP | |
| trade | razmjena; razmijeniti | Minecraft: "Razmjene". Ijekavian: not "razmena". |
| inventory / backpack | inventar / ruksak | inventar as in Minecraft; never Serbian "ranac". |
| daily reward | dnevna nagrada | weekly: "tjedna nagrada" (not "nedeljna"). |
| codes | kodovi; "Unesi kod" | redeem = "iskoristi kod", never "otkupi" (buy back). |
| group | grupa | "Pridruži se našoj grupi", "Učlani se". |
| like / favorite | lajk, "Lajkaj igru" / favoriti, "Dodaj u favorite" | lajk is established colloquial; Roblox's own labels don't exist in Croatian. |
| server | server | Use "server": the word players see in Roblox's English UI and use in chat. Microsoft and Minecraft's Croatian (66 strings, no "server") use the purist "poslužitelj": correct but stiff for kids. |
| friends | prijatelji | Roblox's UI has no Croatian, so players see the English "Friends"/"Connections"; in game always "prijatelji", never "veze" or "kontakti". |

## Grammar traps in UI strings
- Plurals: one (1, 21, 31; not 11), few (2-4, 22-24; not 12-14), other (0, 5-20, 25-30). Decimals follow their last digit (1,1 is one, 2,3 is few, 1,5 is other). Nouns change: "1 nagrada, 2 nagrade, 5 nagrada"; "1 jaje, 3 jajeta, 5 jaja"; "1 novčić, 2 novčića, 5 novčića". One string per key, so never put {count} before a countable noun.
  - Bad: "{amount} novčića" -> "1 novčića", "21 novčića". Good: "Novčići: {count}", "Treba ti još novčića: {amount}!".
  - Safe after a number: undeclined units "{price} Robux", "{percent} %", "x{count}", and ordinals "{level}. razina".
- Gender of {player}: past tense agrees ("pridružio se" m., "pridružila se" f.). Use present tense ("{player} se pridružuje igri", "{player} ti nudi razmjenu") or a colon ("Pobjeda: {player}!"). No slashes like "pridružio/la" (Minecraft's Croatian uses them; a polished game doesn't).
- Gender of "you": "Izlegao si", "Spreman si?", "Neaktivan si" are gendered. Use future, present or a noun: "Dobit ćeš...", "Krećemo?", "AFK si!".
- Adjectives agree with the noun: legendarni zmaj (m.), legendarna mačka (f.), legendarno štene (n.). Translate rarity labels in the masculine, agreeing with an implied "ljubimac", and write "{rarity} ljubimac ... {pet}", never "{rarity} {pet}".
- Case: names cannot be declined. Keep {player} and {pet} in the nominative (subject or after a colon), or let a head noun take the case: "Pozovi igrača {player}", not "Pozovi {player}a"; "Razmjena s igračem {player}", not "s {player}om".
- Clitics (je, se, si, ti, ću, li) go in second position: "Ruksak je pun!", "{player} ti nudi razmjenu", "Želiš li kupiti?".
- Questions: "Želiš li...?", never Serbian "Da li želiš...?". After modal verbs use the infinitive: "Moraš pričekati", not "Moraš da sačekaš".
- Future tense: "kupit ćeš", "dobit ćeš" (infinitive loses -i, written apart); never Serbian fused "kupićeš". Verbs in -ći keep it: "doći ćeš".
- English noun stacks become noun + genitive or adjective: "Coin Boost" -> "pojačanje novčića", "Pet Storage" -> "spremište ljubimaca", "Daily Reward" -> "Dnevna nagrada".
- Capitalization: sentence case for titles and buttons ("Najbolji igrači"); item names capitalize only the first word ("Napitak sreće"); days and months lowercase ("subota", "prosinac"); non-sentence text in parentheses lowercase ("(preporučeno)", Microsoft).
- No articles: "a Rare Dragon" -> "rijedak zmaj" (ijekavian; Serbian "redak").

## Typography and formatting
- No space before ! ? : ; and one space after: "Bravo! Nova razina!".
- Quotation marks „...” (Microsoft: U+201E opening, U+201D closing); Minecraft's Croatian closes with “ (U+201C). Pick one per game. Never '...'. Don't quote button names.
- Dash: en dash with spaces " – " ("Ovaj mač – ludo jak!"); Croatian has no em dash (Microsoft). Ranges: "10 – 15".
- Numbers: group separator period, decimal comma (CLDR): "1.250", "1,5". A {count} preformatted as "1,250" reads as 1,25 (one and a quarter) to a Croatian player, and "x1.5" looks English -- flag both to the developer; only code can fix them.
- Percent: no-break space (U+00A0) before % (Microsoft, CLDR "#,##0 %"): "+10 %". In this guide that space is a real U+00A0; reproduce it. This repo's pipeline keeps it (UTF-8, no normalization), and in Studio it renders as wide as a space and never breaks, Fredoka One included (measured for the French guide, 2026-11-08). Whether a CSV upload to the localization portal keeps it is unverified.
- Multiplier: Latin x: "x2", "Novčići x2". Never the Cyrillic "х".
- Durations (CLDR short): "3 h 20 min", "45 s", "2 dana"; narrow: "2 d. 5 h", "20 m". Code-formatted "3h 20m" is readable; ask the developer for the spaced CLDR form.
- Ordinal = numeral + period: "5. razina", "1. mjesto". Abbreviations take a period ("maks.", "npr."); acronyms don't ("XP", "VIP").
- Ellipsis: three dots or "…", no space before: "Učitavanje...".
- Keys stay Latin; key = "tipka" (Serbian "taster"): "Pritisni E", "Otvori tipkom E". Space bar = "razmaknica" (Minecraft). Mouse: "klikni".
- Words run long ("Učitavanje", "zarađivati", "ljubimaca"); enable TextWrapped, never hand-hyphenate.

## Do not translate / keep as is
- Robux, Roblox, Premium, VIP, Roblox Studio: Latin, undeclined in UI.
- Game titles ("Pet Hatch Tycoon"): keep English; players search the English title.
- Usernames and display names: never translate, transliterate or decline; give them a head noun when a case is needed.
- Promo codes ("FREEPETS"): exactly as given, same case; translate only the text around them.
- Key names (E, Q, Shift) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Napitak sreće", Minecraft's Croatian name for the Potion of Luck); brand-like invented names may stay English.
- Established loanwords keep their Croatian spelling ("lajk", "bonus", "avatar", "server"); don't invent phonetic ones ("pet simjulejtor").
- Script and variant: Latin only. Serbian also uses Cyrillic, and Serbian and Bosnian text is not Croatian even when readable -- never copy the `sr-rs` or `bs-ba` column into `hr-hr`.

## Rendering on Roblox
- Croatian needs Latin Extended-A: č ć đ š ž and Č Ć Đ Š Ž (U+010C-010D, U+0106-0107, U+0110-0111, U+0160-0161, U+017D-017E). š ž are also in Windows-1252, so a font can have them and still lack č ć đ.
- Checked in the font files Roblox ships (client build of 2026-11, regular faces): all ten letters are in Builder Sans/Extended/Mono, Source Sans Pro, Montserrat, Arimo, Roboto, Nunito, Oswald, Ubuntu, Titillium Web, Bangers, Luckiest Guy, Press Start 2P, Amatic SC, Comic Neue Angular, Indie Flower, Kalam, Patrick Hand, Special Elite, Michroma, Jura, Merriweather, Fondamento, Grenze Gotisch and Josefin Sans.
- Missing č ć đ Č Ć Đ: Fredoka One, Permanent Marker, Creepster, Highway Gothic, Accanthis ADF Std, Balthazar, Roman Antique (also ž Ž); Denk One lacks all ten. Don't set hr-hr text in these; switch the font for this locale.
- How Roblox draws a missing glyph (fallback font or empty box) is unverified; either way "Učitavanje" breaks inside a cartoon word. Carons and acutes on capitals (Č Ć Š Ž) add height and can clip in tight TextScaled labels or ALL-CAPS styles.
- string.upper and string.lower handle ASCII only: code that uppercases "Učitavanje" gives "UčITAVANJE". Write ALL-CAPS text in the translation itself or ask for UTF-8-aware code; č ć đ š ž are 2 bytes, so string.sub can split them.
- Write digraphs as two letters (d+ž, l+j, n+j), never the single code points U+01C4-01CC; most fonts lack them.
- Verify in Studio: Player Emulator set to hr-hr; open every panel with the longest strings; paste the pangram "Gojazni đačić s biciklom drži hmelj i finu vatu u džepu nošnje. ČĆĐŠŽ" (checked: all 30 letters, dž lj nj included) into each font face used. If letters fall back, pick a font from the full-coverage list.

## Mistakes machine translation makes here
- Ekavian (Serbian) forms: "Sledeća nagrada", "vreme", "mesto" -> "Sljedeća nagrada", "vrijeme", "mjesto".
- Serbian vocabulary: "Muzika", "Prodavnica", "nivo", "ranac", "hiljada", "taster", "Podešavanja", "Sačuvaj" -> "Glazba", "Trgovina", "razina", "ruksak", "tisuća", "tipka", "Postavke", "Spremi".
- Serbian syntax: "Da li želiš da kupiš?" -> "Želiš li kupiti?"; "kupićeš" -> "kupit ćeš".
- "experience" as iskustvo: "Najbolje iskustvo na Robloxu" -> "Najbolja igra na Robloxu".
- "Claim" as zatražiti (= request): "Zatraži" -> "Preuzmi"; "redeem" as otkupiti: "Otkupi kod" -> "Iskoristi kod".
- Gendered past with a username: "{player} se pridružio igri" -> "{player} se pridružuje igri".
- Gendered "you": "Izlegao si legendarnog zmaja!" -> "Legendarni ljubimac se izlegao: Zmaj!".
- Number + noun: "Imaš {count} novčića" -> "Novčići: {count}".
- Formal register and possessives: "Pritisnite E", "Vaš ruksak je pun" -> "Pritisni E", "Ruksak je pun!".
- Title Case: "Dnevna Nagrada", "Napitak Sreće" -> "Dnevna nagrada", "Napitak sreće".
- Missing diacritics or ASCII stand-ins: "Ucitavanje", "Udji u krug" -> "Učitavanje", "Uđi u krug".
- Literal rebirth: "Ponovno rođenje" (too long, religious) -> "Preporod".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Igraj | 2sg imperative, as in Minecraft's Croatian |
| shop.title | Trgovina | "Dućan" (5) if tighter; never "Prodavnica" |
| shop.buy | Kupi | |
| reward.claim | Preuzmi | "Uzmi" also fine; not "Zatraži" |
| rebirth.button | Preporod | |
| rebirth.confirm | Preporod sada? Izgubit ćeš novčiće, ali dobit ćeš trajno pojačanje x{multiplier}. | "1.5" must reach the player as "1,5" -- code issue |
| coins.need_more | Treba ti još novčića: {amount}! | colon avoids "1 novčića" |
| coins.count | Novčići: {count} | "1,250" should be "1.250" -- code issue |
| egg.hatched | {rarity} ljubimac se izlegao: {pet}! | verb and rarity agree with "ljubimac", so the pet's gender doesn't matter; 37/40 with Legendarni + Zmaj |
| rarity.legendary | Legendarni | masculine, agrees with implied "ljubimac" |
| pet.name.dragon | Zmaj | masculine |
| chat.player_joined | {player} se pridružuje igri | present tense avoids pridružio/pridružila |
| trade.request | {player} ti nudi razmjenu | |
| prompt.open_shop | Otvori tipkom E | "Pritisni E za otvaranje" is 23 > 22 |
| pass.buy_price | Kupi za {price} Robux | Robux undeclined |
| pass.coins2x | Novčići x2 | |
| pass.vip | VIP | kept: acronym Croatian uses as is |
| reward.daily_title | Dnevna nagrada | |
| reward.come_back | Vrati se za {time} po sljedeću nagradu! | best with "3 h 20 min" |
| codes.placeholder | Unesi kod | |
| codes.invalid | Kod ne vrijedi ili je istekao. | |
| social.like_reward | Lajkaj igru i dobij besplatan <b>Napitak sreće</b>! | |
| social.group_reward | Pridruži se našoj grupi i otključaj besplatnu nagradu! | 54/55; "dobij" (5) if it overflows |
| afk.warning | AFK si! Pomakni se i nastavi zarađivati! | avoids gendered "neaktivan/neaktivna" |
| leaderboard.title | Najbolji igrači | 15/16; "Ljestvica" if tighter |
| level.up | Nova razina! Sada si na razini {level}. | never "nivo" |
| tutorial.sell | Uđi u svjetleći krug i prodaj ljubimce. | two imperatives read more natural than "Za prodaju ljubimaca uđi..." and avoid gendered "kako bi prodao" |
| inventory.full | Ruksak je pun! Prodaj ljubimce i oslobodi mjesto. | "your" dropped |
| settings.music | Glazba | never "Muzika" |
| settings.on | Da | Minecraft's bare on/off values are Da/Ne; its "Label: value" form uses "Uključeno" (9), too long here. Avoid "Uklj.", which reads as cut off |
| loading | Učitavanje... | 13/14 |
| event.ends_in | Događaj traje još {time} | 26/28 with "2 d. 5 h"; "event" is player slang (unverified) |
| item.op | Ovaj mač je ludo jak! | "OP" kept by some gamers (unverified) |
| friends.boost | Pojačanje +{percent} % za svakog prijatelja na serveru | no-break space before %; "server", not "poslužitelj" (see vocabulary) |

## Sources
1. Microsoft Localization Style Guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
2. Microsoft Croatian localization style guide (PDF, via https://aka.ms/croatian-styleguide): https://download.microsoft.com/download/0/6/2/0626b4d3-ed24-4c11-8676-ec5aa03576c7/hrv-hrv-StyleGuide.pdf
3. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR JSON, Croatian number symbols and percent pattern: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/hr/numbers.json
5. CLDR JSON, Croatian duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/hr/units.json
6. Roblox locale API (hr_hr: in-game content only, not full experience): https://locale.roblox.com/v1/locales
7. Roblox language codes page: https://create.roblox.com/docs/production/localization/language-codes
8. roblox.com/hr/charts served in English, roblox.com/de/charts in German (2026-11-08): https://www.roblox.com/hr/charts
9. Croatian Wikipedia, Roblox (Robux undeclined, "iskustva", Premium): https://hr.wikipedia.org/wiki/Roblox
10. Minecraft Java 1.21.4 Croatian language file (game UI conventions): https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21.4/assets/minecraft/lang/hr_hr.json
11. Roblox's bundled fonts, cmap tables read from the installed client's content/fonts folder (build version-f0ea5da9412f4e35, 2026-11-08); family list: https://create.roblox.com/docs/reference/engine/datatypes/Font
12. Roblox docs, in-game language switcher (players pick from the game's languages): https://create.roblox.com/docs/production/localization/localize-with-scripting
13. Roblox docs, Player.LocaleId (the account locale) and Supported Languages: https://create.roblox.com/docs/reference/engine/classes/Player and https://create.roblox.com/docs/production/localization
14. CLDR JSON, Croatian plural rules: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-core/supplemental/plurals.json
15. Croatian Wikipedia, Tajkun (negative sense) and Parkour (spelling): https://hr.wikipedia.org/wiki/Tajkun and https://hr.wikipedia.org/wiki/Parkour
