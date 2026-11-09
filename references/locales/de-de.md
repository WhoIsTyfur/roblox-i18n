# German (de-de) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `de-de` (no bare `de` column: German is one Roblox locale, so de-at and de-ch players fall back to `de-de`) |
| Script, direction | Latin, LTR; letters ä ö ü Ä Ö Ü ß |
| Address the player as | informal singular "du" (dein, dir, dich); never "Sie", never plural "ihr" in UI |
| Text expansion vs English | +20-35% for sentences, short labels +50-100% ("Claim" -> "Abholen") (rule of thumb, unverified for Roblox) |
| Plural categories (CLDR) | one, other (one = exactly integer 1: "1 Münze", "2 Münzen", "1,5 Münzen") |
| Model confidence | high: high-resource language; the risks are register, gaming loanwords and inflection around placeholders |
| Native review before shipping | recommended |

## Audience and register
- Players are mostly 9-16. Roblox's own player-facing German uses "du": its in-game strings have "du/dein" in about 200 lines and "Sie" in one, and its chat says "Gib „/?“ ... ein". German gaming sites write to the same crowd with "ihr" (mein-mmo: "Gebt euren Code dort ein"), but a game UI talks to one player: use "du".
- Microsoft's German guide also requires "du" for anyone under 18. Its "Sie" examples are for adult software and are wrong here: "Kaufen Sie jetzt" -> "Jetzt kaufen".
- Buttons, tabs and menu items: infinitive, no "du" ("Spielen", "Kaufen", "Abholen", "Code eingeben"). Instructions and tutorial text: du-imperative ("Drücke E", "Lauf in den Kreis", "Hol dir ..."). Use the short spoken imperative where it sounds natural ("Beweg dich", "Komm wieder"), but pick one form per verb and keep it for the whole game.
- Hype sounds natural as short, punchy main clauses: "Neues Level!", "Ausgebrütet!", "Glückwunsch!". Avoid stacked exclamation marks and adult slang. Subjunctive and passive read like a manual: "Es könnte ein Fehler aufgetreten sein" -> "Das hat nicht geklappt".
- Light colloquial contractions are fine and friendly: "gibt's", "geht's", "Auf geht's!". Don't use regional dialect (Bavarian, Swiss, Austrian words); de-at and de-ch players read this same column.
- Gender: no gender colon or star. Roblox's legacy chat used "Dein:e Freund:in", but its current in-game strings (client of 2026-11-05) use none and write "Dein Freund {RBX_NAME} ist der Experience beigetreten". Prefer neutral words ("Bestenliste", "Team", "alle"); where none sounds natural, use the generic masculine ("für jeden Freund"). Microsoft's guide also avoids gender characters for readability.

## Roblox and gaming vocabulary
| English | German in game UI | Note |
|---|---|---|
| Robux | Robux | Invariant: "1 Robux", "100 Robux". Roblox help: "Robux ist die virtuelle Währung von Roblox". |
| game pass | Pass, plural Pässe | Roblox help and Creator Hub say "Pässe" (Creator Hub also "Spielpässe"). Players also write "Gamepass" (unverified). |
| developer product | (name the item) | Creator Hub says "Entwicklerprodukt"; players never see that word, so name the item instead. |
| experience / game | Spiel | Roblox's in-game German now says "die Experience" (0 uses of "Erlebnis" in the 2026-11 client); help pages still say "Erlebnis". In game text write "Spiel": "dem Spiel beitreten". |
| obby / tycoon / simulator | Obby / Tycoon / Simulator | Genre words stay. "der Simulator", plural "Simulatoren". |
| rebirth | Rebirth | "Rebirth machen", "Rebirths: 5". "Wiedergeburt" is long and sounds religious. Slang verb "rebirthen" exists (unverified); avoid it in UI. |
| pet | Pet, plural Pets | "das Pet". Players keep the English word (unverified); "Haustier" sounds like a real cat at home. |
| egg / hatch | Ei, plural Eier / ausbrüten, schlüpfen | The player "brütet ein Ei aus"; the pet "schlüpft": "Dein Pet ist geschlüpft!" |
| coins / gems | Münzen / Juwelen | "Münzen" is the usual game-UI word; players also say "Coins". Gems: "Juwelen" (as in Supercell's German games) or "Edelsteine" (both unverified); pick one and keep it. |
| boost / multiplier | Boost / Multiplikator | "der Boost", plural "Boosts". In labels use "2x" rather than the word "Multiplikator". |
| XP / level up | XP / Neues Level! | "das Level", plural "Level" or "Levels". Fortnite and Pokémon German write "EP" (Erfahrungspunkte) (unverified); both are understood, pick one per game. |
| quest | Quest or Aufgabe | "die Quest". "Aufgabe" is clearer for young players; don't mix the two. |
| leaderboard | Bestenliste | Roblox's own player list says "Bestenliste". Gender-neutral, unlike "Top-Spieler". |
| AFK / noob / OP / VIP | AFK / Noob / OP / VIP | Kept as is. "der Noob", plural "Noobs". "Das Schwert ist OP!" |
| trade | tauschen, Tausch, Tauschanfrage | Roblox help: "Tauschen auf Roblox". Players also say "traden" (unverified); UI uses "tauschen". |
| inventory / backpack | Inventar / Rucksack | Both as in Roblox's own top bar and backpack. |
| daily reward | Tagesbelohnung | Or "Tägliche Belohnung" (18 chars). |
| codes | Codes; "Code einlösen", "Code eingeben" | German gaming sites write "Codes einlösen". |
| group | Community, plural Communitys | Roblox renamed groups to communities. German help: nav item "Communitys", button "Community beitreten". Don't write "Gruppe". |
| like / favorite | Like, liken / Favorit, "zu Favoriten hinzufügen" | Roblox's vote control is a bare thumbs-up icon; German help calls it "Daumen hoch". Duden lists "liken", so "Like das Spiel" is fine. Favorite: Roblox says "Als Favorit hinzufügen". |
| server | Server | "auf dem Server", as Roblox writes ("auf demselben Server"); never "in dem Server". |
| friends | Freunde | Roblox renamed friends to "Verbindungen" (in-game even "Connection") in July 2025 and back to "Freunde" in April 2026. Don't write "Verbindungen". |
| Premium | Premium | "Roblox-Premium-Mitgliedschaft"; "Premium-Spieler" for perks. |
| shop | Shop | Roblox's in-game German: "Besuche den Shop". Avoid "Laden" (also means "loading"). |

## Grammar traps in UI strings
- **Plurals with {count}.** Roblox has no plural selection, and "1 Münzen" is wrong. Safe patterns:
  - label + colon: "Münzen: {count}"
  - invariant words: "Noch {amount} nötig." works for 1 and 250
  - Robux, which never changes: "{price} Robux"

  Never "Münze(n)". Bad: "Du hast {count} Münzen" -> good: "Münzen: {count}".
- **Verb agreement with numbers.** "Es fehlen {amount} Münzen" breaks twice at 1 (it must be "es fehlt 1 Münze"). Name the noun first and let the number stand alone: "Nicht genug Münzen! Noch {amount} nötig."
- **Inserted nouns change form.** German articles and adjectives depend on the noun's gender and case, and some nouns change too: der Drache -> "einen Drachen". "Du hast einen {pet} ausgebrütet" fails for "Drache" (needs "Drachen"), "Katze" (needs "eine") and "Einhorn" (needs "ein"). Use a colon or parentheses: "Ausgebrütet: {pet} ({rarity})!"
- **Inserted adjectives can't inflect.** {rarity} arrives as a bare label ("Legendär"). "Ein {rarity} {pet}" gives "ein Legendär Drache", which is wrong; it should be "ein legendärer Drache". Put the rarity in parentheses or after a colon: "{pet} ({rarity})".
- **{player} has unknown gender.** German verbs don't mark gender, but role nouns and pronouns do: "{player} ist der Gewinner!" -> "{player} hat gewonnen!". Never refer back with "er" or "sie"; repeat {player} or use "du".
- **Prepositions and case around placeholders.** Write the case-governing word so the inserted value stays in its base form: "{player} möchte mit dir tauschen" (dir = dative), "auf deinem Server". Don't put {player} where it needs a genitive -s ("{player}s Pet"): names ending in s or x need an apostrophe instead. Use "Pet von {player}".
- **Word order.** The verb goes second in main clauses and last in subclauses, and separable verbs split: "Tritt unserer Community bei", "Komm wieder". Placeholders move freely because they are named. Reorder them instead of copying the English order.
- **Infinitive groups need a comma** with um/ohne/statt (Microsoft's guide makes it mandatory): "Lauf in den Kreis, um deine Pets zu verkaufen."
- **Compound nouns** are one word: "Tagesbelohnung", "Glückstrank". Hyphenate when an English part, number, acronym or brand joins in: "Event-Shop", "VIP-Bereich", "2x-Boost", "Robux-Preis", "Roblox-Premium-Mitgliedschaft". A space inside a compound is a classic error: "Pet Inventar" -> "Pet-Inventar".
- **Capitalization.** Every noun is capitalized, including English loans ("das Event", "die Pets", "der Boost"). Titles and buttons use sentence case, not English Title Case: "Tägliche Belohnung", "Neue Pets im Shop". Adjectives stay lowercase mid-phrase: "Neue legendäre Pets".

## Typography and formatting
- No space before ! ? : ; and no inverted marks: "Neues Level!", "Jetzt Rebirth machen?".
- Quotes are „...“ (low-high, U+201E / U+201C), as in Roblox's own chat strings: „Bestenliste“. Never English "...". Swiss style «...» is optional and not needed.
- Numbers: 1.250 for thousands, 1,5 for decimals (CLDR de). Code that formats by LocaleId gives de-ch players 1'250 and 1.5 (CLDR de-CH); that is correct too. The translator can't fix numbers that game code formats; report English-formatted values ("1,250", "1.5x") to the developer, as the skill's audit step does, so code formats them by the player's LocaleId.
- Percent: "10 %" with a no-break space (U+00A0), as CLDR de does. A plain space lets % wrap onto its own line; Roblox keeps U+00A0 together (measured in Studio) and its own German uses it ("60 FPS"). Roblox's client also writes "10% Bonus", so "+10%" is fine in tight badges. One style per game.
- Durations: CLDR short forms are "2 Tg. 5 Std.", "3 Std. 20 Min.", "45 Sek."; the narrow hour form is "5h". Don't use "m" for minutes (it means meters). English "3h 20m" -> "3 Std. 20 Min."
- Ellipsis: "Lädt..." with no space (Microsoft's UI rule), or Roblox's own "Laden ..." with a no-break space. Never a plain space before the dots. The single "…" character also works.
- Dashes: no em dash. Use a spaced en dash "–" or, better for short UI, a colon or a new sentence.
- Keys: keep the key letter as shown on the keyboard. "Drücke E zum Öffnen"; "Drücke die Taste E" only if space allows. Never translate E, Q, F, Shift, or controller glyph names.
- Multipliers: "2x Münzen", "x2". Keep ASCII "x"; the multiplication sign × is optional.

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, Noob, Obby, Tycoon.
- Game titles stay English: "Pet Hatch Tycoon". German sites keep Roblox titles as is ("Grow a Garden", "Anime Vanguards").
- Promo codes and their examples (FREEPETS), usernames, display names, {player}, keybinds, and emoji the source uses.
- Translate in-game item, pet and rarity names, and keep each name the same everywhere ("Lucky Potion" -> "Glückstrank").
- Eszett: always ß ("Spaß", "groß", "Straße"). Swiss German writes "ss", but Swiss players get this column and read ß without trouble. In ALL CAPS write "SS" ("GROSS"), never capital ẞ (see Rendering).

## Rendering on Roblox
- Builder Sans, the default, is safe: Roblox's own German in-game strings use ä ö ü ß „ “ – and U+00A0. Measured in Studio with TextService:GetTextSize over 20 Enum.Font faces (FredokaOne, LuckiestGuy, Bangers, Cartoon, Arcade and more): ä ö ü Ä Ö Ü ß „ “ – … get each font's own widths, but capital ẞ has the same width in 15 faces, a sign of a fallback glyph. Uploaded custom fonts are unverified: look at ß, Ä Ö Ü and „ “ in each.
- Luau `string.upper` only changes ASCII letters (checked in Studio): "Münzen" becomes "MüNZEN". Write uppercase text directly in the table ("MÜNZEN") or uppercase with a UTF-8-aware helper, and never upper-case ß.
- Wrapping (measured with TextService:GetTextSize, 2026-11-08): lines break only at spaces, never after a hyphen. A word or hyphenated compound wider than the label is cut mid-word with no hyphen (test string "Gratis-Geschenk" -> "Gratis-Ge" / "schenk"). Keep long compounds ("Tagesbelohnung", "Erfahrungspunkte") out of narrow wrapped labels, or use TextScaled.
- Capital umlauts (Ä Ö Ü) are taller than A O U; in tight frames with TextScaled, check that the dots aren't clipped (unverified).
- Verify in Studio: set the test locale to de-de, open every panel, and look at the longest strings (rebirth confirm, tutorial, inventory full) and the shortest buttons (max 8-10). The settings.on toggle must hold "Ein".

## Mistakes machine translation makes here
- Formal register: "Kaufen Sie jetzt!" -> "Jetzt kaufen!"; "Geben Sie den Code ein" -> "Code eingeben".
- Wrong verb for Claim: "Beanspruchen" (a legal claim) -> "Abholen".
- "Free" read as unoccupied: "Freie Belohnung" -> "Gratisbelohnung" / "kostenlose Belohnung". "gratis" is an adverb: "gratis einen Trank", not "einen gratis Trank".
- Over-translated gaming words: "Wiedergeburt" -> "Rebirth"; "Haustiere" -> "Pets"; "Verstärkung" -> "Boost"; "Rangliste der Top-Spieler" -> "Bestenliste".
- Outdated platform terms: "Verbindungen" -> "Freunde"; "Gruppe" -> "Community"; in-game "Erlebnis" -> "Spiel".
- Plural with a placeholder: "{count} Münzen" (wrong at 1) -> "Münzen: {count}".
- Unknown-gender insertions: "Du hast einen Legendär Drache ausgebrütet!" -> "Ausgebrütet: {pet} ({rarity})!".
- Calques: "Level hoch!" -> "Neues Level!"; "Mag das Spiel" for Like -> "Like das Spiel"; "in deinem Server" -> "auf deinem Server".
- Missing hyphen or a space inside compounds: "2x Boost Pass" -> "2x-Boost-Pass"; "Top Spieler" -> "Top-Spieler".
- English punctuation and numbers: "Press "E"" -> „E“; "1,250 Münzen" -> "1.250 Münzen" (flag for game code).
- Title Case copied from English: "Tägliche Belohnung Abholen" -> "Tägliche Belohnung abholen".
- False friends: "eventuell" isn't "eventually" (use "irgendwann"); "bekommen" means "get", not "become".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Spielen | Infinitive button. |
| shop.title | Shop | Same as English because Roblox's German says "Shop". |
| shop.buy | Kaufen | |
| reward.claim | Abholen | Not "Beanspruchen". |
| rebirth.button | Rebirth | Kept English; "Wiedergeburt" (12) is over the max. |
| rebirth.confirm | Jetzt Rebirth machen? Du verlierst deine Münzen, bekommst aber einen dauerhaften {multiplier}x-Boost. | Game code should send "1,5", not "1.5". |
| coins.need_more | Nicht genug Münzen! Noch {amount} nötig. | Rebuilt so {amount} = 1 stays correct. |
| coins.count | Münzen: {count} | Label pattern avoids "1 Münzen"; count should be formatted "1.250". |
| egg.hatched | Ausgebrütet: {pet} ({rarity})! | Avoids article and adjective inflection; params reordered. |
| rarity.legendary | Legendär | Bare form for tags. |
| pet.name.dragon | Drache | Masculine weak noun ("den Drachen"); never insert it after an article. |
| chat.player_joined | {player} ist dem Spiel beigetreten | Roblox's own join message has changed from "dem Erlebnis" to "der Experience"; game text keeps "Spiel", which players say. |
| trade.request | {player} möchte mit dir tauschen | "tauschen" as in Roblox help. |
| prompt.open_shop | Drücke E zum Öffnen | E kept. |
| pass.buy_price | Für {price} Robux kaufen | 22 chars at price "1.000", exactly the max; 23 at "10.000", so widen the button for 5-digit prices. |
| pass.coins2x | 2x Münzen | |
| pass.vip | VIP | Kept. |
| reward.daily_title | Tagesbelohnung | "Tägliche Belohnung" fits exactly (18) if preferred. |
| reward.come_back | Deine nächste Belohnung gibt's in {time}! | Adapted; "Komm in {time} wieder, um deine nächste Belohnung abzuholen!" is 69 with "3 Std. 20 Min.". |
| codes.placeholder | Code eingeben | |
| codes.invalid | Dieser Code ist ungültig oder abgelaufen. | |
| social.like_reward | Like das Spiel und hol dir gratis einen <b>Glückstrank</b>! | "gratis" is an adverb, so it goes before the article; "einen kostenlosen" runs to 57. |
| social.group_reward | Tritt unserer Community bei und hol dir ein Geschenk! | "Community" per Roblox's rename of groups; "Geschenk" already implies free. 53/55. |
| afk.warning | Du bist AFK! Beweg dich und verdien weiter! | "um weiter zu verdienen" ran over 45. |
| leaderboard.title | Bestenliste | Roblox's own word for its leaderboard; gender-neutral. |
| level.up | Neues Level! Du bist jetzt Level {level}. | |
| tutorial.sell | Lauf in den leuchtenden Kreis, um deine Pets zu verkaufen. | Comma before the um-infinitive is mandatory. |
| inventory.full | Dein Rucksack ist voll! Verkaufe Pets für mehr Platz. | |
| settings.music | Musik | |
| settings.on | Ein | Roblox's own settings menu uses "Ein" / "Aus". "An" is also correct. |
| loading | Lädt... | "Wird geladen..." is 15, over the max. |
| event.ends_in | Event endet in {time} | "das Event" is standard; fits 28 with "2 Tg. 5 Std.". |
| item.op | Dieses Schwert ist OP! | |
| friends.boost | +{percent} % Boost für jeden Freund auf deinem Server | Space before % is U+00A0. Generic masculine "Freund", as Roblox's own "Dein Freund". |

## Sources
1. Microsoft German localization style guide (deu-deu, PDF): https://aka.ms/german-styleguide
2. CLDR plural rules, German: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON, de and de-CH units and numbers: https://github.com/unicode-org/cldr-json/tree/main/cldr-json
4. Roblox client chat strings with German text (Roblox-Client-Tracker): https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/scripts/CoreScripts/Modules/Server/ServerChat/DefaultChatLocalization.lua
5. Roblox Help, "Wie man Robux erhält" (de): https://en.help.roblox.com/hc/de/articles/203313200
6. Roblox Help, "Eine Community finden und ihr beitreten" and "Xbox One App: Bewertung eines Erlebnisses" (de): https://en.help.roblox.com/hc/de/articles/203313490 , https://en.help.roblox.com/hc/de/articles/205355420
7. Roblox Player client strings, `ExtraContent/translations/CoreScriptLocalization.csv` (de column, client version-f0ea5da9412f4e35, 2026-11-05), in the local Roblox install
8. Duden, "liken" and "gratis": https://www.duden.de/rechtschreibung/liken , https://www.duden.de/rechtschreibung/gratis
9. Studio measurements, 2026-11-08: TextService:GetTextSize wrapping (U+00A0, hyphen, long words) and glyph widths across Enum.Font faces
10. Roblox Help search, de (Tauschen, Favoriten, Pass, Premium): https://en.help.roblox.com/api/v2/help_center/articles/search.json?query=Tauschen&locale=de
11. Roblox newsroom (de), Freunde -> Verbindungen, July 2025: https://about.roblox.com/de/newsroom/2025/07/advancing-safety-on-roblox-with-age-based-communication
12. Roblox newsroom (de), Friends are back, April 2026: https://about.roblox.com/de/newsroom/2026/04/expanding-trusted-friends
13. Roblox Creator Hub (de-de), Pässe: https://create.roblox.com/docs/de-de/production/monetization/passes
14. Roblox Creator Hub (de-de), Gruppen: https://create.roblox.com/docs/de-de/projects/groups
15. Roblox Creator Hub (de-de), Automatische Übersetzung: https://create.roblox.com/docs/de-de/production/localization/automatic-translations
16. Roblox, Was ist Roblox (de): https://about.roblox.com/de/what-is-roblox
17. mein-mmo, Roblox beginner guide (community register and loanwords): https://mein-mmo.de/roblox-einsteiger-tipps/
18. mein-mmo, Grow a Garden codes (codes, items, update wording): https://mein-mmo.de/grow-a-garden-codes/
19. mein-mmo, Roblox article index (loanwords in headlines): https://mein-mmo.de/roblox/
