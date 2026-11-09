# Albanian (sq-al) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `sq-al` (the only Albanian locale Roblox lists, so it serves Albania, Kosovo, North Macedonia and the diaspora alike; a bare `sq` column adds nothing and whether Roblox reads one is unverified) |
| Script, direction | Latin, LTR; the only non-ASCII letters are ë Ë ç Ç |
| Address the player as | informal singular "ti" (2nd person singular verbs: "Luaj", "Bli"); never "ju" or 2nd plural "Luani", "Blini" |
| Text expansion vs English | about +15-35% for sentences (unverified rule of thumb; this guide's reference set came out +16% while fitted to budgets); short titles up to +70% ("Top Players" -> "Lojtarët më të mirë") |
| Plural categories (CLDR) | cardinal: one, other; ordinal: one, many, other |
| Model confidence | medium: mid-resource language with no Roblox Albanian UI to anchor terms; models slip on ë/ç, clitics, agreement and Gheg forms |
| Native review before shipping | strongly recommended |

## Audience and register
- Albanian is read in Albania, Kosovo, western North Macedonia, parts of Montenegro and a large diaspora (Italy, Greece, Germany, Switzerland, UK, US). All of them share `sq-al`. Write Standard Albanian (gjuha standarde, the Tosk-based norm taught in schools in both Albania and Kosovo). No lekë prices, Albania-only holidays or town names.
- Roblox's own app and site are not translated into Albanian: Roblox's locale API flags `sq_al` for in-game content only (not full experience, not signup), checked 2026-11-08, so Albanian cannot be the account language. A player gets `sq-al` by picking it in the in-experience language menu (Roblox menu > Settings), which lists only the languages the developer enabled for that experience (Roblox, 2022): no Albanian in the experience's localization settings, no Albanian players. Not tested live (unverified); the API's display name is "Shqipe". Albanian kids see Robux, Premium, Friends, Communities and Favorites in the English UI. Roblox does not auto-translate Albanian either, so every key must be filled or players see English.
- Address one player with "ti". Microsoft's Albanian guide uses 2nd singular throughout ("kliko", "provoje përsëri") and replaces third-person "përdoruesi" with it. YouTubers say "bëni like" to their whole audience; a game UI talks to one player: "Bëj", "Shtyp", "Hyr".
- Buttons: 2nd singular imperative, Microsoft's pattern ("Kliko", "Anulo"): "Luaj", "Bli", "Merre", "Hap". Titles and labels: a noun, usually definite: "Dyqani", "Inventari", "Muzika". Ongoing actions: "Po ngarkohet…" or Microsoft's "Duke + participle": "Duke shkarkuar…".
- Simple tenses (Microsoft): "Mund të hysh pasi të fusësh kodin", not "Do të mund të hysh, pasi të kesh futur kodin".
- Hype that sounds natural: "Bravo!", "Super!", "Urra!", "Fitove!", "Mos e humb!", "Shkëlqyeshëm!" (Microsoft prefers it over the anglicism "Ekselent!"). Stiff or adult: "Ju lutemi", "i/e nderuar", "procedoni", "në mënyrë që", "Ju falënderojmë".
- Errors state the fact, not the player's fault: "Ky kod është i pavlefshëm", not "Ke shkruar kod të gabuar".
- Albanian news coverage of Roblox focuses on child safety, so parents are watching. Keep it kid-safe: "noob" only in friendly jokes; no insults ("budalla", "idiot", "plehra"), no pressure lines like "Bli tani ose do pendohesh!".

## Roblox and gaming vocabulary
| English | Albanian | note |
|---|---|---|
| Robux | Robux | Latin, never inflected in UI: "100 Robux", "Bli për 50 Robux". Not "Robux-ët". |
| Premium | Premium | "Roblox Premium"; uninflected. |
| game pass | (pass name); "Game Pass" if unavoidable | no settled Albanian word (unverified); Roblox's English UI says "Passes". In the shop just show the pass name. |
| developer product | blerje, produkt | players never see the term; name the item. |
| experience / game | lojë (pl. lojëra) | never "përvojë" (= experience as skill); press and Wikipedia say lojë. |
| obby | obby | (unverified); descriptions: "parkur me pengesa". |
| tycoon | tycoon | genre word kept (unverified); text: "ndërto perandorinë tënde". |
| simulator | simulator (simulatori) | established loanword, inflects normally. |
| rebirth | rilindje; verb rilindem | button "Rilindu"; "Rilindje" (8) as a noun label. |
| pet | kafshë (pl. kafshë; def. kafsha, kafshët) | feminine. "pet" in chat (unverified). "kafshë shtëpiake" is too long and means household pet. |
| egg / hatch | vezë / çel ("Çel vezën"), "Hap" | çel is the native verb for chicks hatching; results: "Nga veza doli: …". |
| coins | monedha (sg. monedhë) | not "para" (money) or "qindarka". |
| gems | xhevahirë; diamante if the art shows diamonds | (unverified which kids prefer). |
| boost | bonus; përforcim | "bonus" is an everyday loanword; "boost" in chat (unverified). |
| multiplier | shumëzues; "x2" | pick "x2" or "2x" once per game. |
| XP | XP; pikë përvoje | "+50 XP". |
| level / level up | nivel (niveli) / "Nivel i ri!" | not "Lart nivelin". |
| quest | mision (misioni) | "detyrë" sounds like homework. |
| leaderboard | renditja; title "Më të mirët" | "Tabela e renditjes" when space allows. |
| AFK | AFK | Latin caps, uninflected: "Je AFK". |
| noob | fillestar (UI); noob (jokes) | |
| OP | super i/e fortë; OP | "OP" among Albanian kids unverified. |
| VIP | VIP | "Server VIP", "Zona VIP". |
| trade | shkëmbim; verb shkëmbej | "trade" in chat (unverified). |
| inventory / backpack | inventari / çanta (çanta e shpinës) | keep whichever the source means. |
| daily reward | shpërblimi ditor | |
| codes | kodet; redeem = "Aktivizo" | placeholder "Shkruaj kodin" ("Fut kodin" is Microsoft's verb). |
| group | grup (grupi); komunitet | "Bashkohu me grupin tonë". Roblox's English UI renamed Groups to Communities (2024); "grup" stays the plain word, "komuniteti" matches the UI. |
| like / favorite | "Pëlqeje lojën" / "Shtoje te të preferuarat" | standard verb pëlqej; the spoken, code-mixed "Bëj like lojës" suits chat, not a polished banner (kids' preference unverified). Roblox shows a thumbs-up and a star. |
| server | server (serveri); server privat | inflect with no hyphen: "në serverin tënd". |
| friends | miq (sg. mik); shokë in casual text | Roblox's English UI went from Connections back to Friends (announced 2026-04-02). Never "lidhje" (= connections). |

## Grammar traps in UI strings
- Plurals with {count}: the noun changes after numbers above 1 ("1 monedhë", "5 monedha"; "1 nivel", "3 nivele") and so do verbs ("të duhet" / "të duhen"). Some nouns don't change ("1 kafshë, 3 kafshë"; "orë", "ditë", "vezë"). Safest: label plus colon, "Monedha: {count}", or a generic plural before the colon: "Të duhen edhe monedha: {amount}!".
- Gender: past and present verbs don't mark gender ("{player} hyri", "{player} fitoi"), but adjectives and participles do ("i gatshëm" / "e gatshme", "fitues" / "fituese"). Use verbs: "Fitove!", not "Je fitues!"; "{player} është gati" ("gati" never changes).
- Case around placeholders: names and inserted words cannot take endings. Prepositions "te", "tek" and "nga" take the nominative, so they are safe: "Dërgo te {player}", "Dhuratë nga {player}". "me", "për" and genitive "i/e" need endings, so add a noun that inflects: "Shkëmbe me lojtarin {player}", "kafsha e lojtarit {player}".
- "pas" (after, in) takes the ablative, so counted time is "pas 3 orësh", "pas 2 ditësh". A code-filled {time} stays in the base form ("pas 3 orë 20 min."): casual but clear (how strict kids are is unverified). Case-free label: "Koha e mbetur: {time}".
- The definite article is a suffix (dyqan -> dyqani), so a placeholder can never carry it. Inserted translated words arrive in one fixed form; keep pet and item names in the indefinite nominative ("Dragua") and build sentences that need no other form, for example after a colon.
- Adjectives follow the noun and agree: "Dragua legjendar", "kafshë legjendare". Articled adjectives also change their article by case: "bonus i përhershëm" -> "merr një bonus të përhershëm". Rarity tags: "Legjendar", "Epik", "Mitik" only change for gender; "I rrallë" / "E rrallë" also change the article. Keep {rarity} out of agreement: "{pet} ({rarity})".
- Possessives agree with the thing owned, not the player: "çanta jote", "niveli yt", "në serverin tënd", "kafshët e tua".
- Clitic doubling: a definite object takes a clitic pronoun: "për t'i shitur kafshët", "Merre shpërblimin", "Do t'i humbasësh monedhat". Leaving it out reads foreign.
- "do të" is the future ("will"); "do" alone is also "wants". "{player} do të shkëmbejë" reads as "will trade", so write "{player} dëshiron të shkëmbejë me ty".
- English noun stacks become genitive phrases: "Pet Shop" -> "Dyqani i kafshëve", "Coin Boost" -> "Bonus monedhash". Avoid overlong compounds (Microsoft).
- Capitalization: sentence case for titles and buttons ("Shpërblimi ditor", not "Shpërblimi Ditor"); lowercase after a colon; days, months, languages and nationalities are lowercase ("e hënë", "janar", "shqip").

## Typography and formatting
- No space before ! ? : ; and one space after: "Nivel i ri!", never "Nivel i ri !".
- Quotes: Microsoft's Albanian guide uses English straight quotes with punctuation after the closing mark: kliko "Bli". CLDR lists curly double and single quotes (U+201C/U+201D, U+2018/U+2019). Use straight "..." in UI (safe in every font); never mix in guillemets.
- Elision apostrophes are part of spelling: "t'i", "s'ka", "ç'ke". Dropping one changes the word ("ti" = you). "ta" (të + e) has no apostrophe: "për ta hapur".
- Ellipsis: Microsoft wants the single character (U+2026); it also saves two characters: "Po ngarkohet…". Dashes: spaced en dash for asides, hyphen in pairs like "hyrje-dalje".
- Numbers (CLDR): decimal comma, no-break space for thousands, no separator for 4 digits: "1250", "12 500", "1 250 000", "x1,5". English "1,250" reads as one and a quarter. Translators cannot fix a {param}: the reviewer flags {count}, {amount}, {price}, {level}, {percent} and {multiplier} to the developer, whose code must format them per `Player.LocaleId`.
- Percent: no space: "50%", "+25%".
- Durations (CLDR short units): "2 ditë 5 orë", "3 orë 20 min.", "45 sek.". Compact "3h 20m" and "2d 5h" use English letters ("d" and "m" are not Albanian abbreviations), so ask the developer to format {time} with these units (how kids read the compact form is unverified). They are longer: "Eventi mbaron pas 2 ditë 5 orë" is 30 characters.
- Ordinals take varying suffixes ("i 1-rë", "i 2-të", "i 4-t"), so avoid "{n}-të"; write "Vendi: {rank}".
- Keys: keep the letter: "Shtyp E". Mouse: "Kliko". Touch: "Prek". Space bar: "Hapësira" (Microsoft: "Tasti i hapësirës").

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, XP: Latin, uninflected in UI. Microsoft's rule for untranslated names: no suffix or hyphen ("Fjalëkalimi i Windows", not "Windows-it"). So "llogaria jote në Roblox", "Bli për 50 Robux". Press writes both "Roblox-it" and "Robloxin"; don't copy either.
- The game title as listed ("Pet Hatch Tycoon") unless the developer gives an Albanian title.
- Promo codes (FREEPETS, exact case), usernames and display names ({player}), key letters, "x2".
- Item and pet names made of ordinary words are translated ("Dragua", "Eliksir fati"); capitalize only the first word, the Albanian norm for multiword names.
- One script and one standard: no Gheg forms ("me luejt", "kon", "nuk po mundem me hy"), even though many Kosovo and northern kids speak Gheg at home. Standard: "të luash", "ka qenë", "nuk po mund të hyj".
- Never strip diacritics: ë and ç are separate letters of the alphabet ("Çanta", not "Canta"; "Shpërblimi", not "Shperblimi").

## Rendering on Roblox
- Albanian needs only Basic Latin plus ë Ë ç Ç (Latin-1 Supplement), which nearly every Latin font includes, so the risk is far lower than for Cyrillic or Vietnamese. Per-font coverage of Roblox's built-in and Creator Store fonts is unverified; the 2024 Builder font announcement states no character coverage.
- Risks: the dots of Ë and the cedilla of Ç clipped in all-caps or tight TextScaled labels ("SHPËRBLIMI DITOR"); a pixel or cartoon display font missing Latin-1 falling back to another font mid-word (unverified for any specific font); long words like "Shpërblimi" or "përhershëm" overflowing narrow buttons.
- Verify in Studio: test with a player locale of `sq-al`, open every panel with the longest strings, and paste "Çanta ËSHTË plot! Shpërblimi ditor, xhevahirë, çel vezën…" into each font face used.

## Mistakes machine translation makes here
- Missing diacritics, as kids type in chat: "Shperblimi ditor", "Canta jote" -> "Shpërblimi ditor", "Çanta jote".
- Polite or plural address: "Shtypni E", "Blini tani" -> "Shtyp E", "Bli tani".
- English title case: "Shpërblimi Ditor" -> "Shpërblimi ditor".
- English word order: "Legjendar Dragua", "Kafshë Dyqan" -> "Dragua legjendar", "Dyqani i kafshëve".
- Future misread: "{player} do të shkëmbejë me ty" -> "{player} dëshiron të shkëmbejë me ty".
- "experience" as përvojë: "Përvoja më e mirë në Roblox" -> "Loja më e mirë në Roblox".
- "Claim" as demand or assert: "Kërko", "Pretendo" -> "Merre".
- "Connections" calqued: "Lidhjet e tua" -> "Miqtë e tu".
- Number + noun: "Ke 1 monedha" -> "Monedha: 1".
- Inflected brands: "Bli me Robux-ët", "në Roblox-in" -> "Bli me Robux", "në Roblox".
- Missing elision: "Do ti humbasësh" -> "Do t'i humbasësh".
- Colloquial or Gheg forms: "lojra", "me luejt" -> "lojëra", "të luash".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Luaj | |
| shop.title | Dyqani | |
| shop.buy | Bli | |
| reward.claim | Merre | "merr" + clitic "e" (it); "Merr" also fine |
| rebirth.button | Rilindu | imperative of rilindem, like "Luaj"; the noun "Rilindje" for titles and counters ("Rilindje: 3") |
| rebirth.confirm | Rilindje tani? Do t'i humbasësh monedhat, por do të marrësh një bonus të përhershëm x{multiplier}. | "x" moved before the number; "1.5" should arrive as "1,5" (code) |
| coins.need_more | Të duhen edhe monedha: {amount}! | generic plural + colon; works when amount is 1 |
| coins.count | Monedha: {count} | "1,250" should be "1250" for Albanian (code issue) |
| egg.hatched | Nga veza doli: {pet} ({rarity})! | "out of the egg came"; natural and needs no "you" form. Rarity in brackets avoids gender agreement. "Çele: {pet}" is a valid shorter option |
| rarity.legendary | Legjendar | masculine dictionary form for every tag, whatever the pet's gender; pet names mix genders ("Dragua", "Mace"), so no one form agrees with all |
| pet.name.dragon | Dragua | not "Kuçedër" (a folklore monster) |
| chat.player_joined | {player} hyri në lojë | past tense, no gender |
| trade.request | {player} dëshiron të shkëmbejë me ty | "do të" would read as future |
| prompt.open_shop | Shtyp E për ta hapur | |
| pass.buy_price | Bli për {price} Robux | |
| pass.coins2x | Monedha x2 | noun first |
| pass.vip | VIP | |
| reward.daily_title | Shpërblimi ditor | |
| reward.come_back | Kthehu pas {time} për shpërblimin e radhës! | "pas" + code-filled time: see Grammar traps |
| codes.placeholder | Shkruaj kodin | |
| codes.invalid | Ky kod është i pavlefshëm ose ka skaduar. | |
| social.like_reward | Pëlqeje lojën dhe merr falas një <b>Eliksir fati</b>! | item named in sentence case |
| social.group_reward | Bashkohu me grupin tonë për një shpërblim falas! | "unlock" dropped to fit 55 |
| afk.warning | Je AFK. Lëviz që të vazhdosh të fitosh! | |
| leaderboard.title | Më të mirët | "Lojtarët më të mirë" is 19 > 16 |
| level.up | Nivel i ri! Tani je në nivelin {level}. | |
| tutorial.sell | Hyr në rrethin që shkëlqen për t'i shitur kafshët. | |
| inventory.full | Çanta jote është plot! Shit kafshë për të bërë vend. | |
| settings.music | Muzika | |
| settings.on | Aktiv | Off: "Joaktiv" (7), the pair Android's Albanian Settings uses; "Ndezur" (6) is over 5 |
| loading | Po ngarkohet… | single ellipsis character to fit 14 |
| event.ends_in | Eventi mbaron pas {time} | "eventi" is the common loanword; with "2 ditë 5 orë" it runs 30 > 28, so then use "Mbaron pas {time}" |
| item.op | Kjo shpatë është super e fortë! | "OP" kept is an option (unverified) |
| friends.boost | +{percent}% bonus për çdo mik në serverin tënd | |

## Sources
1. Microsoft Albanian localization style guide (PDF, via https://aka.ms/albanian-styleguide): https://download.microsoft.com/download/f3664c11-a6d5-4780-b058-41207b7a0cdb/sqi-alb-StyleGuide.pdf
2. Microsoft localization style guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. CLDR language plural rules (sq cardinal and ordinal): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR JSON, sq number symbols and grouping: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/sq/numbers.json
5. CLDR JSON, sq duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/sq/units.json
6. CLDR JSON, sq quotation marks and ellipsis: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-misc-full/main/sq/delimiters.json
7. Roblox locale API (sq_al flags: in-game only), checked 2026-11-08: https://locale.roblox.com/v1/locales?displayValueLocale=en_us
8. DevForum, "Cloud Localization Support Extended to 45 Languages" (2019; unsupported UI languages see English on platform): https://devforum.roblox.com/t/cloud-localization-support-extended-to-45-languages/337149
9. DevForum, "Friends Are Back!" (Connections -> Friends, 2026-04-02): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
10. DevForum, Builder font announcement (no coverage stated): https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222
11. BalkanWeb, Roblox and children (Roblox-it, lojtar, chat-it, avatarë, miq): https://www.balkanweb.com/arrogance-shperqendrim-dhe-ekstremizem-fenomeni-roblox-rrezik-apo-argetim-per-femijet/
12. Shqiptarja.com, Roblox and children (Robloxin, lojtarë, lojrash): https://shqiptarja.com/lajm/roblox-po-ndryshon-sjelljen-e-femijeve-ekspertet-per-report-tv-prindwrit-tw-kenw-kujdes-loja-krijon-varwsi
13. Albanian Wikipedia, Roblox (lojëra, përdorues, monedhë virtuale, Robux uninflected): https://sq.wikipedia.org/wiki/Roblox
14. Wiktionary, "dragua" (dragon; dragoi, dragonj; kuçedër): https://en.wiktionary.org/wiki/dragua
15. Wiktionary, "çel" (to hatch; çele, çeli): https://en.wiktionary.org/wiki/çel
16. Roblox language codes (sq-al, bare sq listed): https://create.roblox.com/docs/production/localization/language-codes
17. DevForum, in-experience language switcher (2022; players pick from the experience's enabled languages): https://devforum.roblox.com/t/localization-api-update-for-upcoming-in-experience-language-switcher/1974795
18. DevForum, "Introducing Roblox Communities" (Groups renamed, 2024-11-21): https://devforum.roblox.com/t/introducing-roblox-communities/3268307
19. Android SettingsLib, Albanian strings ("Aktiv", "Joaktiv"): https://github.com/aosp-mirror/platform_frameworks_base/blob/main/packages/SettingsLib/res/values-sq/strings.xml
20. Wiktionary, "pas" (preposition, ablative): https://en.wiktionary.org/wiki/pas
