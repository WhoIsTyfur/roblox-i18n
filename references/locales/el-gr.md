# Greek (el-gr) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `el-gr` (the only Greek locale Roblox lists, so it serves Greece, Cyprus and the diaspora alike; a bare `el` column adds nothing, and whether Roblox reads one is unverified) |
| Script, direction | Greek, LTR; modern monotonic spelling (one accent mark, the tonos, plus the diaeresis ϊ ϋ ΐ ΰ) |
| Address the player as | informal singular "εσύ": "Παίξε", "σου"; never plural/polite "Παίξτε", "σας" |
| Text expansion vs English | about +20-30% for free sentences (unverified rule of thumb; this guide's reference set came out +16% while fitted to budgets); short titles up to +100% ("Shop" -> "Κατάστημα") |
| Plural categories (CLDR) | cardinal: one (n = 1), other (0, 2+ and 1,5 take other); ordinal: other only |
| Model confidence | medium: solid grammar, but models slip on tonos (capitals, enclitics), the Greek question mark, polite plural and gender agreement; no Greek Roblox UI to anchor terms |
| Native review before shipping | strongly recommended |

## Audience and register
- Roblox's app and site are not in Greek: the locale API flags `el_gr` for in-game content only (not full experience, not signup), checked 2026-11-08, so Greek cannot be the account language. A player gets `el-gr` by picking "Ελληνικά" in the in-experience language menu (Roblox menu > Settings), which lists only the languages the developer enabled for that experience (Roblox, 2022): no Greek in the localization settings, no Greek players. Not tested live (unverified). Greek kids see Robux, Premium, Friends, Communities and Favorites in English, and Roblox does not auto-translate Greek, so an empty key shows English.
- Greek players grew up with mostly untranslated games and keep many English gaming words (Microsoft's Greek guide notes that much of the audience prefers the English term for familiar tech concepts). Translate sentences; keep the slang words players actually use (table below).
- Address one player with the singular. Microsoft's Greek guide uses the polite plural ("Κάντε κλικ", "Αποθηκεύστε") because it writes for adults; a kids' game says "Πάτα", "Μάζεψε", "Έλα ξανά".
- Buttons: singular imperative ("Παίξε", "Πούλα", "Άνοιξε") or a short verbal noun, Microsoft's UI pattern ("Αγορά", "Φόρτωση", "Αναγέννηση"). Pick one style per screen. Never the plural imperative ("Αγοράστε").
- Use everyday words, not formal or katharevousa ones (Microsoft): "αν" not "εάν", "κάνω" not "πραγματοποιώ", "βρίσκω" not "εντοπίζω", "επιτυχία" not "επίτευξη". Drop "please": no "Παρακαλώ" in UI.
- Hype that sounds natural: "Τέλεια!", "Μπράβο!", "Τα κατάφερες!", "Πάμε!", "Φανταστικό!". Stiff or adult: "Συγχαρητήρια για την επιτυχή ολοκλήρωση", "Αξιότιμε παίκτη", "Παρακαλούμε περιμένετε".
- Kid-safe: "noob" only as friendly teasing; no insults ("χαζέ", "βλάκα"), no pressure lines like "Αγόρασε τώρα αλλιώς θα το χάσεις!".

## Roblox and gaming vocabulary
| English | Greek | note |
|---|---|---|
| Robux | Robux | Latin script, neuter plural, never inflected: "τα Robux", "100 Robux". Not "ρόμπουξ" in UI. |
| Premium | Premium | "το Roblox Premium" (Greek Wikipedia). |
| Roblox | το Roblox | neuter, as on Greek Wikipedia; unlocalized names take the neuter (Microsoft). |
| game pass | game pass; in the shop just the pass name | no settled Greek word (unverified); neuter "το game pass". |
| developer product | αγορά, πακέτο | players never see the term; name the item. |
| experience / game | παιχνίδι (pl. παιχνίδια) | Greek Wikipedia says παιχνίδια throughout. "εμπειρία" means life experience. |
| obby | obby | (unverified); descriptions: "πίστα με εμπόδια". |
| tycoon / simulator | Tycoon / Simulator in titles | text: "χτίσε την αυτοκρατορία σου"; "προσομοιωτής" reads technical. |
| rebirth | αναγέννηση (η); "κάνε αναγέννηση" | "rebirth" in chat (unverified). |
| pet | κατοικίδιο (το), pl. κατοικίδια | neuter; "ζωάκι" is a cute alternative; "pet" in chat (unverified). |
| egg / hatch | αυγό (το) / "Άνοιξε το αυγό" | "εκκολάπτω" is biology-textbook Greek. |
| coins | κέρματα (το κέρμα) | the default: shorter, and "Κέρματα: {count}" fits 16. "νομίσματα" (gold coins) is also correct; one per game. Which kids prefer is unverified. Not "λεφτά" (money). |
| gems | διαμάντια, πετράδια | match the art. |
| boost | μπόνους (το, indeclinable) | "ενίσχυση" sounds like military backup. |
| multiplier | "x2"; πολλαπλασιαστής (ο) | the noun is long; show "x2". |
| XP / level up | XP / επίπεδο (το); "Ανέβηκες επίπεδο!" | kids say "λέβελ" aloud (unverified); UI writes επίπεδο. |
| quest | αποστολή (η) | never "αναζήτηση" (= search). |
| leaderboard | κατάταξη (η); title "Οι κορυφαίοι" | "Πίνακας κατάταξης" (17) when it fits. |
| AFK / OP / VIP | AFK / OP / VIP | Latin caps, uninflected: "Είσαι AFK", "το VIP". OP among Greek kids (unverified); "πανίσχυρο" in plain text. |
| noob | αρχάριος (UI); noob (jokes) | |
| trade | ανταλλαγή (η) | "κάνουμε trade;" in chat (unverified). |
| inventory / backpack | αντικείμενα / σακίδιο (το) | never "απόθεμα" (= stock). Keep whichever the source means. |
| daily reward | καθημερινό δώρο | warmer and everyday; "ημερήσια ανταμοιβή" is office-formal. Reward elsewhere: δώρο. |
| codes | κωδικοί (ο κωδικός); redeem = "Εξαργύρωση" | placeholder "Γράψε κωδικό". |
| group | κοινότητα (η) | Roblox's English UI now says Communities (per the de-de guide); "ομάδα" means team. |
| like / favorite | "Κάνε like" / "Αγαπημένα" | thumbs-up and star in the English UI. "λάικ" (το, indeclinable) is a Greek loan noun (Greek Wiktionary); the exact phrase "κάνε like" is unverified. Facebook-style "Μου αρέσει" is the formal fallback. |
| server | server (ο), indeclinable: "στον server" | Greek Wiktionary lists σέρβερ as masculine (neuter also seen), and Microsoft gives server products the masculine. "διακομιστής" is too technical for kids. |
| friends | φίλοι (ο φίλος) | Roblox's English UI went from Connections back to Friends (April 2026). Never "συνδέσεις". |
| event | event (το); εκδήλωση | "εκδήλωση" sounds like a school event. |

## Grammar traps in UI strings
- Plurals with {count}: the noun changes ("1 κέρμα", "5 κέρματα"; "1 ώρα", "3 ώρες") and so does the verb ("λείπει 1 κέρμα", "λείπουν 5 κέρματα"); 0 takes the plural. Safest: label + colon, "Κέρματα: {count}", or make the plural noun the subject: "Σου λείπουν κέρματα: {amount}".
- Gender: past and present verbs never mark gender ("{player} μπήκε", "{player} κέρδισε"), but adjectives, participles and agent nouns do ("έτοιμος/έτοιμη", "νικητής/νικήτρια"). Use verbs: "{player} κέρδισε!", not "{player} είναι ο νικητής!".
- Articles before names: Greek normally says "ο Νίκος", but {player} has unknown gender. Start the sentence with the bare name ("{player} θέλει να...") and never write "ο {player}", "με τον {player}"; rephrase: "Ανταλλαγή με: {player}".
- Case: nouns and articles decline, but inserted words arrive in the nominative. "Πήρες τον {pet}" breaks ("Δράκος" would need "Δράκο"; a feminine pet needs "την"). Put {pet} and {item} after a colon or as a subject: "Πήρες: {pet}".
- Adjectives precede the noun and agree in gender: "Θρυλικός Δράκος", "Θρυλική Αλεπού", "Θρυλικό Κουνέλι". Never build "{rarity} {pet}"; write "{pet} ({rarity})" and keep rarity tags in the neuter, agreeing with "κατοικίδιο".
- Enclitic double accent: a word stressed on the third-to-last syllable gets a second tonos before "μου/σου/μας": "τα κέρματά σου", "η κοινότητά μας", "τα κατοικίδιά σου". Words stressed on the second-to-last syllable don't: "το δώρο σου".
- Final ν: always "δεν", "μην", "τον", "έναν"; "την/στην" keep ν before vowels and κ π τ ξ ψ (and μπ ντ γκ τσ τζ) and drop it before other consonants: "στην κοινότητα", but "στη μουσική".
- Imperative aspect: perfective for one tap ("Άνοιξε", "Αγόρασε"); everyday colloquial forms are fine and short ("Πάτα", "Πούλα").
- Capitalization: sentence case for titles and buttons ("Καθημερινό δώρο", not "Καθημερινό Δώρο"). Days, months and languages take a capital ("Δευτέρα", "Ελληνικά"); adjectives from countries don't ("ελληνικό").

## Typography and formatting
- Question mark: Greek uses ";" (U+003B): "Αναγέννηση τώρα;". Never "?" in Greek text. Type the plain semicolon; the separate Greek question mark U+037E normalizes to it anyway.
- The Greek semicolon is the raised dot "·" (ano teleia); Microsoft says not to use it in software. Use a period or comma instead.
- Tonos: every word of two or more syllables carries one in lowercase and sentence case: "Παίξε", not "Παιξε". On an initial capital it sits before the letter: "Έλα", "Όχι", "Άνοιξε". One-syllable words take none, except "ή" (or), "πού/πώς" in questions and a clitic that would be misread ("σού").
- ALL CAPS drops every tonos: "ΠΑΙΞΕ", "ΑΓΟΡΑ", "ΚΑΤΑΣΤΗΜΑ", never "ΠΑΊΞΕ". The diaeresis stays and appears where the accent used to show two separate vowels: "Μάιος" -> "ΜΑΪΟΣ". Disjunctive "Ή" (or) is said to keep its accent (unverified); keep "ή" out of all-caps strings.
- Final sigma: "ς" at the end of a word, "σ" elsewhere, "Σ" in caps: "Θρυλικός" -> "ΘΡΥΛΙΚΟΣ".
- Quotes: CLDR's Greek quotes are « » with “ ” inside. Microsoft software uses straight "..." for consistency. Use « » in game text and never mix styles.
- Ellipsis: one character, as Microsoft does: "Φόρτωση…". No space before ! ; : . and one space after.
- Exclamation marks: fine for hype ("Τα κατάφερες!"). Microsoft drops them from error messages: "Ο κωδικός δεν ισχύει.", not "Ο κωδικός δεν ισχύει!".
- Numbers (CLDR): decimal comma, period for thousands, grouped from 4 digits: "1.250", "12.500", "x1,5". English "1,250" reads as one and a quarter; the game code must format {count}, {amount} and {multiplier}.
- Percent: no space, "50%", "+10%".
- Durations (CLDR short units): "3 ώ. 20 λ.", "45 δευτ.", "2 ημέρες 5 ώ." (one day: "1 ημέρα"). CLDR's narrow forms ("3 ώ 20 λ", "2 η 5 ώ") are for tight banners only. Ask the code not to emit "3h 20m" or "2d 5h"; how Greek kids read the Latin letters is unverified.
- Ordinals ("1ος", "1η", "1ο") change with gender; write "Θέση: {rank}" instead of "{rank}ος".
- Keys: Latin letter as printed: "Πάτα E". Mouse "Κάνε κλικ", touch "Πάτησε" or "Άγγιξε". Space bar: "πλήκτρο διαστήματος" (Microsoft).

## Do not translate / keep as is
- Brand and platform names: Roblox, Robux, Premium, Roblox Studio; keep them in Latin script, never transliterated.
- Gaming acronyms: AFK, OP, VIP, XP, PvP stay in Latin caps.
- Game titles stay as the developer brands them ("Pet Hatch Tycoon"); Greek kids read Latin titles fine.
- Promo codes (FREEPETS), usernames and display names exactly as typed; never add an article or ending to them.
- Keybinds (E, Q, Shift) as Latin letters. The Greek capital "Ε" (U+0395) looks the same as Latin "E" (U+0045) but is a different character; the keybind must be the Latin one.
- Greeklish (Greek written in Latin letters, "geia sou") is common in kids' chat but never correct UI text. UI is always Greek script.

## Rendering on Roblox
- Greek needs the Greek and Coptic block (U+0370-03FF): 24 letters plus tonos vowels Ά Έ Ή Ί Ό Ύ Ώ ά έ ή ί ό ύ ώ, ϊ ϋ ΐ ΰ and final ς.
- Glyph check (2026-11-08) of the font files in the local Roblox client, `content/fonts`: Roblox's default UI font has no Greek. Builder Sans, Builder Extended and Builder Mono lack it, and so do Montserrat, Luckiest Guy, Fredoka One, Bangers, Nunito, Oswald, Titillium Web, Michroma, Denk One, Patrick Hand, Permanent Marker, Kalam, Creepster and Comic Neue Angular. Full Greek, tonos capitals and ΐ ΰ included: Roboto (also Condensed and Mono), Source Sans Pro (not its italic), Arimo, Ubuntu, Jura, Press Start 2P. Gotham (cloud font) not checked. This matches a DevForum reply on the Builder launch (Montserrat has no Greek, Gotham had it) and Google Fonts metadata.
- So every Greek string in a Builder Sans or cartoon-font game falls back to another font; which one is unverified (Arimo is the Greek-capable Arial clone in the client; the ru-ru guide cites an Arial fallback that broke TextScaled sizing). Risk: one label mixing two fonts, "x2" in the display font and the Greek in the fallback. Recommend the game set a Greek-capable FontFace (Roboto, Source Sans Pro, Ubuntu) for `el-gr`.
- Luau `string.upper` only changes ASCII, so "Παίξε" stays lowercase. A generic Unicode upper-caser gives "ΠΑΊΞΕ" (wrong, keeps the tonos). Write all-caps Greek directly in the table ("ΠΑΙΞΕ"). Roblox's rich text has `<uppercase>`/`<uc>` tags; whether they strip the tonos is unverified, so don't use them on Greek until tested.
- Capitals with tonos (Ά, Έ, Ώ) put the mark to the left of the letter, so they are wider; check them in tight TextScaled buttons.
- Verify in Studio: Player Emulator locale `el-gr`; paste "Ξεσκεπάζω την ψυχοφθόρα βδελυγμία ΞΕΣΚΕΠΑΖΩ Ά Έ Ή Ί Ό Ύ Ώ ϊ ΐ ς ;" into every FontFace the game uses; open the longest strings (rebirth.confirm, social.like_reward at 53/55) and the smallest buttons (rebirth.button at 10/10).

## Mistakes machine translation makes here
- Polite plural: "Αγοράστε τώρα", "Κάντε κλικ" -> "Αγόρασε τώρα", "Πάτα".
- Play as media playback: "Αναπαραγωγή" -> "Παίξε".
- Latin question mark: "Αναγέννηση τώρα?" -> "Αναγέννηση τώρα;".
- Tonos in caps or missing in lowercase: "ΚΑΤΆΣΤΗΜΑ" -> "ΚΑΤΑΣΤΗΜΑ"; "Φορτωση" -> "Φόρτωση".
- Second accent dropped: "τα κέρματα σου" -> "τα κέρματά σου".
- Plural after a number: "1 κέρματα" -> "Κέρματα: 1".
- Gender clash in "{rarity} {pet}": "Θρυλικός Κουνέλι" -> "Κουνέλι (Θρυλικό)".
- Wrong platform words: experience -> "εμπειρία" -> "παιχνίδι"; quest -> "αναζήτηση" -> "αποστολή"; friends -> "συνδέσεις" -> "φίλοι".
- Formal or archaic wording: "Εάν επιθυμείτε να πραγματοποιήσετε αγορά" -> "Αν θέλεις να αγοράσεις"; "{player} εντάχθηκε στο παιχνίδι" -> "{player} μπήκε στο παιχνίδι".
- Polytonic spelling from old texts: "ἀγόρασε", "τῶν" -> "αγόρασε", "των". Modern Greek is monotonic.
- Latin look-alikes inside Greek words, or a Greek "Ε" in "Πάτα E": breaks search and keybind hints; retype in the right script.
- "Please" kept: "Παρακαλώ γράψε κωδικό" -> "Γράψε κωδικό".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Παίξε | not "Αναπαραγωγή" |
| shop.title | Κατάστημα | "Μαγαζί" (6) is more casual |
| shop.buy | Αγορά | verbal noun; "Αγόρασε" (7) also fits |
| reward.claim | Πάρε το | "το" = the δώρο; "Παραλαβή" (9) on a noun-style screen |
| rebirth.button | Αναγέννηση | exactly 10/10 |
| rebirth.confirm | Αναγέννηση τώρα; Θα χάσεις τα κέρματά σου, αλλά θα πάρεις ένα μόνιμο μπόνους x{multiplier}. | Greek ";"; "x" before the number to match "Κέρματα x2"; "1.5" should arrive as "1,5" (code) |
| coins.need_more | Σου λείπουν κέρματα: {amount} | plural noun as subject works when amount is 1; no "!" on a failure |
| coins.count | Κέρματα: {count} | "1,250" should be "1.250" for Greek (code issue) |
| egg.hatched | Νέο κατοικίδιο: {pet} ({rarity})! | "you hatched" becomes "new pet" ("εκκόλαψες" is textbook); brackets avoid gender agreement; neuter rarity matches "κατοικίδιο" |
| rarity.legendary | Θρυλικό | neuter, agreeing with κατοικίδιο |
| pet.name.dragon | Δράκος | masculine |
| chat.player_joined | {player} μπήκε στο παιχνίδι | no article before the name; not "εντάχθηκε" |
| trade.request | {player} θέλει να κάνει ανταλλαγή μαζί σου | |
| prompt.open_shop | Πάτα E για άνοιγμα | Latin E |
| pass.buy_price | Αγορά με {price} Robux | 22/22 with the raw placeholder; "Αγόρασε με" is 24 |
| pass.coins2x | Κέρματα x2 | noun first, sentence case |
| pass.vip | VIP | |
| reward.daily_title | Καθημερινό δώρο | "Ημερήσια ανταμοιβή" is exactly 18 |
| reward.come_back | Έλα ξανά σε {time} για το επόμενο δώρο σου! | |
| codes.placeholder | Γράψε κωδικό | |
| codes.invalid | Ο κωδικός δεν ισχύει ή έχει λήξει. | period, not "!" |
| social.like_reward | Κάνε like στο παιχνίδι για ένα δωρεάν <b>Ελιξίριο τύχης</b>! | "like" is a Greek loan noun, the verb phrase unverified; item in sentence case |
| social.group_reward | Μπες στην κοινότητά μας και ξεκλείδωσε ένα δώρο! | community = Roblox's current name; "free" folded into δώρο |
| afk.warning | Είσαι AFK. Κουνήσου για να κερδίζεις! | imperfective "κερδίζεις" carries "keep earning" |
| leaderboard.title | Οι κορυφαίοι | "Κορυφαίοι παίκτες" is 17 > 16 |
| level.up | Ανέβηκες στο επίπεδο {level}! | "you went up to level {level}!" carries both halves; a bare "στο {level}" reads clipped |
| tutorial.sell | Μπες στον κύκλο που λάμπει για να πουλήσεις τα κατοικίδιά σου. | |
| inventory.full | Το σακίδιο γέμισε! Πούλα κατοικίδια για να κάνεις χώρο. | |
| settings.music | Μουσική | |
| settings.on | Ναι | Off: "Όχι"; "Ενεργό" is 6 > 5. Latin "ON"/"OFF" is also seen in games (unverified); never mix scripts in the pair |
| loading | Φόρτωση… | single ellipsis character |
| event.ends_in | Το event λήγει σε {time} | needs "2 ημέρες 5 ώ." from code, not "2d 5h"; that renders 31 > 28, so if the banner is tight use "Λήγει σε {time}" |
| item.op | Αυτό το σπαθί είναι OP! | "πανίσχυρο" if OP is not understood (unverified) |
| friends.boost | +{percent}% μπόνους για κάθε φίλο στον server σου | |

## Sources
1. Microsoft Greek localization style guide (PDF, via https://aka.ms/greek-styleguide): https://download.microsoft.com/download/3/9/6/3963b5d8-7e0d-49c7-868e-ad4b03a7eee5/ell-grc-StyleGuide.pdf
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR Greek number symbols and patterns: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/el/numbers.json
4. CLDR Greek quotation delimiters: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-misc-full/main/el/delimiters.json
5. CLDR Greek duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/el/units.json
6. Roblox locale API (el_gr: in-game content only), checked 2026-11-08: https://locale.roblox.com/v1/locales?displayValueLocale=en_us
7. Greek Wikipedia, Roblox (το Roblox, παιχνίδια, Robux, Premium): https://el.wikipedia.org/wiki/Roblox
8. DevForum, Builder font announcement (reply: Montserrat lacks Greek, Gotham had it): https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222
9. Google Fonts metadata, Montserrat (no Greek subset): https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/METADATA.pb
10. Google Fonts metadata, Luckiest Guy (Latin only): https://raw.githubusercontent.com/google/fonts/main/apache/luckiestguy/METADATA.pb
11. Friends are back, April 2026 (cited from the ru-ru and de-de guides, not re-fetched): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
12. Groups renamed Communities (cited from the de-de guide, not re-fetched): https://create.roblox.com/docs/de-de/projects/groups
13. DevForum, in-experience language switcher (2022; players pick from the experience's enabled languages): https://devforum.roblox.com/t/localization-api-update-for-upcoming-in-experience-language-switcher/1974795
14. Roblox rich text docs (`<uppercase>`/`<uc>` tags): https://create.roblox.com/docs/ui/rich-text
15. Greek Wiktionary, σέρβερ (masculine indeclinable, neuter also): https://el.wiktionary.org/wiki/σέρβερ
16. Greek Wiktionary, λάικ (neuter indeclinable loan noun): https://el.wiktionary.org/wiki/λάικ
17. Local glyph check of the Roblox client's `content/fonts` with fontTools, 2026-11-08 (no URL).
