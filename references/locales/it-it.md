# Italian (it-it) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `it-it`. It is Roblox's only Italian locale, so every Italian-language player falls back to it; a bare `it` column is not needed |
| Script, direction | Latin, LTR |
| Address the player as | informal "tu" with tu-imperatives ("Compra", "Premi E", "Torna domani"); never "Lei", "voi" or impersonal infinitives ("Premere") |
| Text expansion vs English | +17% across this guide's reference set; sentences 0-30%, short labels +40-100%: "Buy" -> "Compra", "Claim" -> "Riscuoti", "Daily Reward" -> "Premio giornaliero" |
| Plural categories (CLDR) | one (exactly 1), many (exact millions: "1.000.000 di monete"), other (0, 2+, decimals); ordinals: many, other |
| Model confidence | high: big, well-documented language; the real risks are gendered participles around {player}, register drift to "Lei"/infinitives, and accent typos |
| Native review before shipping | recommended |

## Audience and register
Italian Roblox players are mostly kids and young teens in Italy. Write the way a polished Italian mobile game talks to a 12-year-old: short, warm, direct, never bureaucratic.
- Pronoun: "tu" everywhere, as Roblox's own Italian client and Microsoft's Italian voice do ("Vuoi continuare?", "Riprova"). Drop "tu" itself; the verb carries it: "Hai vinto!", not "Tu hai vinto!".
- Buttons take the tu-imperative, exactly like Roblox's Italian UI ("Compra", "Invita", "Blocca", "Esci", "Annulla", "Conferma", "Riprova"): "Gioca", "Vendi tutto", "Riscuoti". Older software used infinitives ("Selezionare", "Premere"); in a game they read like an instruction manual.
- Negative tu-imperative is "non" + infinitive: "Non uscire!", "Non chiudere il gioco". "Non esci" is a statement, not an order.
- Hype that sounds native and kid-safe: "Complimenti!" (Roblox uses it), "Grande!", "Fantastico!", "Mitico!", "Evvai!", "Che fortuna!". One exclamation mark, never "!!!".
- Reads stiff or adult: "Si prega di attendere", "La preghiamo di...", "Desideri effettuare...?", "Gentile giocatore", "qualora". Use "Attendi un attimo...", "Vuoi...?".
- Prefer present tense over future for game rules ("Perdi le monete, ma ottieni..."); Microsoft also advises avoiding the future unless something really will happen later.
- Avoid regional slang ("ganzo", "mo'", "uagliò") and anything with a vulgar twin ("figo" is borderline; never "figa"). Mild gamer slang is fine in flavor text: "OP", "noob", "pro".

## Roblox and gaming vocabulary
| English | it-IT | Note |
|---|---|---|
| Robux | Robux | Invariable, capital R: "100 Robux", "i Robux"; Roblox UI: "Robux insufficienti" |
| Premium | Premium / Roblox Premium | Roblox UI: "Solo Premium" |
| game pass | pass (il pass) | Creator docs: "Pass", "pass di gioco"; Roblox client: "Pass privilegio"; players also say "gamepass" (unverified) |
| developer product | prodotto | Creator docs: "Prodotti per sviluppatori"; in game UI just name the item |
| experience / game | gioco | Roblox UI says "esperienza"; in-game text and players say "gioco" |
| obby, tycoon, simulator | obby, tycoon, simulator | Kept in titles; in prose "un simulatore" is fine |
| rebirth | rebirth (il rebirth) | Kept as the mechanic's name ("fare il rebirth"), like "drop" and "skin" (player usage unverified); "Rinascita" (9) if the game translates every term; one per game |
| pet | pet (il pet, i pet) | Masculine, invariable plural; Italian guides write "Pet leggendari", never "pets" |
| egg / hatch | uovo, plural le uova / far schiudere | "Uovo leggendario", "far schiudere le uova"; never "covare" (that is the hen sitting on it) |
| coins / gems | monete / gemme | "Monete x2"; diamonds are "diamanti" |
| boost | bonus (il bonus) | Roblox UI: "Bonus del 10%"; this guide's strings use "bonus"; "boost" is gamer slang; use one term per game |
| multiplier | moltiplicatore | Written "x2" before or after the noun: "Monete x2" |
| XP | XP | Kept; never "PE" on a HUD |
| level up | "Level up!" / "Nuovo livello!" | "Sei salito di livello" is gendered (see traps); "livellare", "uppare" are chat slang |
| quest | missione | "Missioni giornaliere" |
| leaderboard | classifica | Roblox UI: "Classifica"; board titles also use "Top giocatori" |
| AFK, noob, OP, GG, pro | AFK, noob, OP, GG, pro | Kept in English; "niubbo" is the Italian slang form, for chat only, not UI |
| VIP | VIP | "Server VIP" in games; Roblox UI says "server privato" |
| trade | scambio / scambiare | "Richiesta di scambio", "Scambia"; never "commercio" |
| inventory / backpack | inventario / zaino | Roblox UI: "Inventario", "Zaino" |
| shop | negozio | Roblox UI: "negozio degli avatar"; "Shop" also appears in Italian games |
| daily reward | premio giornaliero | Roblox UI uses both "premio" and "ricompensa"; "premio" is shorter |
| codes / redeem | codici / riscattare | "Riscatta", "Inserisci codice"; keep "Riscatta" for codes only, so it never collides with the Claim button |
| group | community (la) | Roblox client: "Emblema della community"; Creator docs still say "Gruppi"; "gruppo" is also understood (player usage unverified); Roblox's Italian join-button label is unverified |
| like / favorite | mi piace / preferiti | "Metti mi piace" (the social-media phrase; Roblox's thumbs-up label in Italian is unverified); client: "Vuoi aggiungere {RBX_NAME} ai preferiti?"; "metti like" is chat slang |
| server | server (il server, i server) | Invariable |
| friends / connections | amici | Roblox switched "Connessioni" back to "Amici" in April 2026; some client strings still say "contatto", but use "amici" |
| badge | badge (il badge) | Roblox is inconsistent: client "Contrassegno conferito", Creator docs "Distintivi"; use the common loanword "badge" in game text (player usage unverified) |

## Grammar traps in UI strings
- **Plurals with {count}.** Only 1 is singular in Italian (0 takes the plural: "0 monete"). "{count} monete" breaks at 1. Put the noun first as a label: "Monete: {count}", "Drago x{count}". Agreeing verbs break too: "Ti servono altre {amount} monete" -> "Monete insufficienti: ancora {amount}!". Roblox's own client needs two strings for this ("Hai ricevuto {N} punto!" / "punti!"); a LocalizationTable gets one.
- **Millions.** Spelled-out millions take "di": "1 milione di monete", "2 milioni di monete". Digits ("1.000.000") or "1 Mln" avoid the problem.
- **Gender of {player}.** Display names can be any gender, and Italian past participles with "essere" agree with the subject: "{player} si è unito" (wrong for a girl). Use verbs that take "avere", whose participle never agrees: "{player} ha raggiunto il server", "{player} ha vinto!". Roblox itself defaults to masculine ("Sei stato espulso") in places and rephrases in others; do the rephrase.
- **Gender of the reader.** "Sei pronto?", "Sei stato sconfitto", "Benvenuto!" assume a boy -> "Tutto pronto?", "Hai perso!", "Ti diamo il benvenuto!". Avoid "pronto/a" slashes, which Microsoft limits to forms.
- **Articles and prepositions before {item}/{pet}.** The article depends on the inserted word's gender and first letter (il Drago, lo Scudo, l'Arco, la Volpe), and fuses with prepositions (del, dello, dell', della). "Bonus del {item}" breaks on half the names. Use a colon, as Roblox does ("Hai ottenuto un premio: {REWARD_NAME}!"): "Bonus: {item}". Numbers elide too ("del 10%" but "dell'8%", "dell'11%", "dell'80%"), so write "+{percent}% di bonus", not "Bonus del {percent}%".
- **Rarity agreement.** Adjectives follow and agree with the noun ("volpe leggendaria", "drago leggendario"; capitalize only as a standalone tag: "Leggendario"). Translate rarities in the masculine (Comune, Raro, Epico, Leggendario, Mitico) and hang them on a masculine head noun: "pet {rarity}", "Uovo {rarity}".
- **Loanword articles and plurals.** English loanwords are invariable: "i pet", "i boost", "i server", "i codici" (Italian word, so it inflects). Articles follow the sound: "lo zaino", "lo shop", "l'evento", "il VIP", "la community".
- **Elision.** Feminine "una" elides, masculine "uno" does not: "un'arma", "un'isola", but "un uovo", "un evento". "Un'uovo" is a classic error.
- **Word order.** Adjective after noun; English compounds become noun + di/della + noun: "Lucky Potion" -> "Pozione della fortuna", "Golden Dragon" -> "Drago d'oro", "Coin Boost" -> "Bonus monete".
- **Capitalization.** Sentence case for titles, buttons and messages (Microsoft rule; Roblox UI "Azzera personaggio"): "Premio giornaliero", not "Premio Giornaliero". Days, months and languages are lowercase ("sabato", "dicembre", "italiano").

## Typography and formatting
- No space before ! ? : ; and one space after. No inverted marks.
- Accents: grave on most final vowels (è, à, ì, ò, ù: "più", "già", "può", "città"), acute on "perché", "poiché", "né", "sé". Capital "È" is a real letter; never "E'". "Po'" takes an apostrophe, not an accent; "qual è" has none.
- Quotation marks: straight double quotes "..." in UI, as Roblox's Italian client writes them (`Ora sei nella squadra "{RBX_NAME}".`); avoid single quotes. Print-style caporali «...» are correct Italian but rare in game UI.
- Numbers: period for thousands, comma for decimals: "1.250 monete", "x1,5". English-formatted "1,250" from game code reads as one-and-a-quarter; flag it to the developer rather than working around it in the string.
- Percent: no space, as Roblox writes it: "10%", "+25% di bonus".
- Durations: "3h 20min", "2g 5h", "45s". Microsoft's list gives h, min and s ("m" is meters, so prefer "min"); it has no day abbreviation, and "g" for giorni is the usual compact timer form (unverified; "gg" is office style). An English "2d" means nothing in Italian; the format inside {time} comes from game code, so flag it.
- Ordinals: "1°" masculine, "1ª" feminine ("1° posto"). Times are 24-hour: "18:30". Dates are dd/mm ("25/12").
- Ellipsis: keep it for work in progress: "Caricamento...". Roblox once had to cut its own string to "Caricam..." to fit; give labels room instead.
- Keys: the letter stays: "Premi E per aprire" (Roblox: "Premi {KEY_NAME}"). Named keys go in capitals, as Roblox's Italian client and Microsoft write them: "MAIUSC" (Shift), "BARRA SPAZIATRICE" (Space), "INVIO" (Enter), "TAB", "ESC"; "SPAZIO" is the short form when space is tight (unverified). Mobile copy says "Tocca", PC copy "Clicca" (Roblox: "Tocca per muovere", "Clicca per muovere").

## Do not translate / keep as is
- Roblox, Robux, Premium, and Roblox UI names when quoted exactly.
- The game title ("Pet Hatch Tycoon"): Italian guides and players name Roblox games by their English titles (Adopt Me, Grow a Garden).
- Promo codes (FREEPETS) exactly as typed, same case; usernames and display names.
- VIP, AFK, OP, XP, GG, noob, obby, tycoon, pet, server, badge, rebirth (unless the game picked "Rinascita"), and the multiplier "x".
- In-game egg and item names may stay English if the community already knows them (Aranzulla keeps "Cracked Egg", "Royal Egg"); once you translate a game's items, translate all of them consistently ("Drago", "Pozione della fortuna").
- Latin script only, with full accents; never strip them to fit a length limit.

## Rendering on Roblox
- Italian needs only six accented vowels (à è é ì ò ù, plus capitals), all in Latin-1. DevForum font-gap complaints concern Cyrillic, CJK and Arabic, not Latin accents; full coverage in every decorative font is (unverified).
- Test in Studio: "È PIÙ CITTÀ PERCHÉ" in every custom font the game uses, at the smallest TextSize. Accented capitals are taller and may clip at the top of tight TextScaled labels (unverified).
- Expansion is the main risk: give labels AutomaticSize or slack. "Caricamento...", "Premio giornaliero" and "Inserisci codice" sit exactly at typical limits.

## Mistakes machine translation makes here
1. Formal or manual register: "Premere E per aprire" -> "Premi E per aprire"; "Acquistare" -> "Compra"; "La preghiamo di riprovare" -> "Riprova".
2. Gendered participles: "{player} si è unito al gioco" -> "{player} ha raggiunto il server"; "Sei salito di livello!" -> "Level up! Hai raggiunto il livello 5."
3. English plural on loanwords: "i tuoi pets", "3 boosts" -> "i tuoi pet", "3 boost".
4. Apostrophe instead of accent, wrong accent: "E' pieno" -> "È pieno"; "perchè" -> "perché"; "pò" -> "po'"; "qual'è" -> "qual è".
5. Title Case from English: "Premio Giornaliero" -> "Premio giornaliero"; "Top Giocatori" -> "Top giocatori".
6. Claim as a legal claim or a request: "Rivendica", "Richiedi" -> "Riscuoti" (or "Ritira").
7. Play as music: "Suona" / "Riproduci" -> "Gioca".
8. Trade as commerce: "Commercia con {player}" -> "Scambia con {player}".
9. Hatch as brooding: "Hai covato un drago" -> "Uovo schiuso! Pet Leggendario: Drago!".
10. English adjective order: "Leggendario Drago" -> "Drago leggendario"; "Oro Drago" -> "Drago d'oro".
11. False friends: "eventualmente" means "possibly", not "eventually" ("Eventualmente sbloccherai" -> "Prima o poi sbloccherai"); "attualmente" means "currently".
12. Over-applying the old platform rename: "+10% per ogni connessione" -> "+10% per ogni amico".

## Reference translations
Lengths count visible characters without <b> tags. The repo's lint (`width()` in scripts/i18n.py) also drops {params}, so leave room for the inserted value yourself.

| key | translation | note |
|---|---|---|
| menu.play | Gioca | |
| shop.title | Negozio | |
| shop.buy | Compra | Same as Roblox UI |
| reward.claim | Riscuoti | "Ritira" also natural; never "Rivendica"/"Richiedi"; not "Riscatta" (codes) (which top games use most is unverified) |
| rebirth.button | Rebirth | Kept as the mechanic's name; "Rinascita" if the game translates every term |
| rebirth.confirm | Vuoi fare il rebirth ora? Perdi le tue monete, ma ottieni un bonus permanente x{multiplier}. | Present tense; "bonus" as in friends.boost; "x" before the number, Italian style |
| coins.need_more | Monete insufficienti: ancora {amount}! | Rebuilt so {amount} = 1 stays correct |
| coins.count | Monete: {count} | Label form avoids "1 monete" |
| egg.hatched | Uovo schiuso! Pet {rarity}: {pet}! | Rarity agrees with masculine "pet", so feminine pet names stay correct. Fixed text is 21: rarity + pet name must fit 19 ("Leggendario" + "Drago" = 16) |
| rarity.legendary | Leggendario | Masculine, to agree with "pet"/"Uovo" |
| pet.name.dragon | Drago | |
| chat.player_joined | {player} ha raggiunto il server | "avere" verb: no gender agreement |
| trade.request | {player} vuole fare uno scambio con te | |
| prompt.open_shop | Premi E per aprire | |
| pass.buy_price | Compra a {price} Robux | "a" is the idiomatic price preposition; fits 22 up to "10.000" |
| pass.coins2x | Monete x2 | |
| pass.vip | VIP | |
| reward.daily_title | Premio giornaliero | Exactly 18; "Ricompensa giornaliera" is too long |
| reward.come_back | Torna tra {time} per il prossimo premio! | |
| codes.placeholder | Inserisci codice | Exactly 16; article dropped to fit |
| codes.invalid | Codice non valido o scaduto. | |
| social.like_reward | Metti mi piace per una <b>Pozione della fortuna</b> gratis! | 52 visible. "Pozione fortunata" is a calque; Minecraft's Italian name is "Pozione di fortuna" |
| social.group_reward | Unisciti alla community e sblocca un premio gratis! | Matches Roblox's "community"; "gruppo" also fine |
| afk.warning | Sei AFK! Muoviti e continua a guadagnare! | |
| leaderboard.title | Top giocatori | "Migliori giocatori" is 18, over the limit; "Classifica" also works |
| level.up | Level up! Hai raggiunto il livello {level}. | "Level up!" kept as the gamer cry; "Nuovo livello!" if the game avoids English. Avoids gendered "Sei salito" |
| tutorial.sell | Entra nel cerchio luminoso per vendere i tuoi pet. | |
| inventory.full | Lo zaino è pieno! Vendi dei pet per fare spazio. | "zaino" as in Roblox UI |
| settings.music | Musica | |
| settings.on | On | Roblox's "Attivo"/"Acceso" are 6, over the limit; Roblox also ships "Off" untranslated |
| loading | Caricamento... | Exactly 14 |
| event.ends_in | Fine evento tra {time} | "L'evento finisce tra" overflows with "3h 20min" |
| item.op | Questa spada è OP! | |
| friends.boost | +{percent}% di bonus per ogni amico nel tuo server | Avoids "del {percent}%", which needs "dell'" before 8, 11, 80 |

## Sources
1. Microsoft Italian Localization Style Guide: https://download.microsoft.com/download/f/f/7/ff70427c-1f7e-429f-96be-724d2e49cd47/ita-ita-StyleGuide.pdf
2. Unicode CLDR language plural rules chart: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox client CoreScript translations, `it` column (ExtraContent/translations/CoreScriptLocalization.csv, Roblox build of 2026-11-05): local file from the Roblox install
4. Roblox newsroom (Italian), Amici fidati and "Connessioni" -> "Amici": https://about.roblox.com/it/newsroom/2026/04/expanding-trusted-friends
5. Roblox newsroom (English), same announcement, dated 2026-04-02: https://about.roblox.com/newsroom/2026/04/expanding-trusted-friends
6. Roblox Creator docs (it-it), passes: https://create.roblox.com/docs/it-it/production/monetization/game-passes
7. Roblox Creator docs (it-it), groups: https://create.roblox.com/docs/it-it/projects/groups
8. Roblox Creator docs, automatic translations (Italian is auto-translated): https://create.roblox.com/docs/en-us/production/localization/automatic-translations
9. Aranzulla, legendary pets in Adopt Me (pet, uova, schiudere, rarity words): https://www.aranzulla.it/come-avere-pet-leggendari-su-adopt-me-1282579.html
10. Focus Junior, gamer slang for kids (AFK, OP, niubbo, nerfare): https://www.focusjunior.it/?p=231370
11. games.gg Italian, Grow a Garden codes ("Riscatta" for codes; "richiedere le ricompense" shows the MT calque for Claim): https://games.gg/it/news/grow-a-garden-codes-come-riscattare/
12. DevForum, font coverage complaints (non-Latin scripts): https://devforum.roblox.com/t/theres-no-font-which-can-fullfill-all-my-use-cases-and-fit-game-style/3051353
13. Roblox Creator docs (it-it), badges ("Distintivi"): https://create.roblox.com/docs/it-it/production/publishing/badges
14. Minecraft Wiki (Italian), potions ("Pozione di fortuna" and the "Pozione di X" pattern): https://it.minecraft.wiki/w/Pozione
