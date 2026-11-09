# Polish (pl-pl) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `pl-pl` (the only Polish locale; no bare `pl` column needed) |
| Script, direction | Latin with ą ć ę ł ń ó ś ź ż, LTR |
| Address the player as | informal singular "ty", usually dropped into the verb ("Masz", "Kup", "Wróć"); lowercase "twój/ciebie" as Roblox's Polish UI writes it; never "Pan/Pani" |
| Text expansion vs English | about +20-30% on sentences (estimate); short buttons vary ("Buy" -> "Kup" is shorter, "Loading..." -> "Wczytywanie..." is +40%) |
| Plural categories (CLDR) | one (1), few (2-4, 22-24... but not 12-14), many (0, 5-21, 25-31...), other (fractions); ordinals: other only |
| Model confidence | medium -- fluent output, but models routinely break gendered past tense, number agreement and case endings around {params} |
| Native review before shipping | strongly recommended |

## Audience and register
Polish players are mostly in Poland, plus Polish-speaking kids abroad (UK, Ireland, Germany) who chose Polish. Write like a polished Polish mobile game talking to a 12-year-old: short, warm, lively, never official.
- Address one player with "ty" forms and drop the pronoun: "Masz nowego peta!", not "Ty masz nowego peta". Never "Pan/Pani": it reads like a bank, and Microsoft notes it forces split past-tense endings ("kupił(a)"). Use "wy" plural only when talking to the whole server ("Dołączcie do eventu!").
- Lowercase "twój, twoje, ciebie, cię", as Roblox's Polish client does mid-sentence ("Otrzymaliśmy twoje zgłoszenie", "przedmiotów twojego awatara"). Microsoft capitalizes "Twój" in product text; in a game it reads like a formal letter. Better still, drop the possessive: "Plecak jest pełny!".
- Buttons: imperative singular, as in Roblox's Polish UI ("Kup", "Zamknij", "Anuluj", "Dołącz", "Zaproś znajomych"). Never infinitive buttons ("Kupić"). Titles: nouns ("Sklep", "Ustawienia", "Ranking").
- Yes/no prompts take the infinitive question, as Roblox does ("Opuścić dzieło?"): "Zrobić rebirth teraz?", "Sprzedać wszystkie pety?".
- Hype that sounds native: "Super!", "Brawo!", "Gratulacje!" (Roblox's own word), "Ekstra!", "Ale szczęście!", "Wow!". One exclamation mark.
- Reads stiff or adult (Microsoft's avoid list and corporate habits): "dokonać zakupu" -> "kupić", "za pośrednictwem" -> "przez", "istnieje możliwość" -> "można", "jednakże/lecz" -> "ale", "Prosimy o...", "Uprzejmie informujemy". Sentence fragments are welcome: "Gotowe!", "Co dalej?".
- "żeby" and "by" are conversational; "aby" is slightly bookish (Roblox system text uses it). Prefer "żeby/by" in toasts and tutorials.
- Gamer slang in flavor text only, never in system messages: "OP", "AFK", "noob", "exp" ("expić" = farm XP), "eq" (gear/inventory, MMO slang per miejski.pl). Keep it kid-safe: no swearing-adjacent slang.

## Roblox and gaming vocabulary
| English | pl-PL | Note |
|---|---|---|
| Robux | Robux; plural Robuxy, genitive Robuxów | Roblox inflects it: "Kup Robuxy", "Za mało Robuxów", "450 Robuxów miesięcznie". With a {number} Roblox uses a label: "Dodatkowe Robuxy: {robux}" (see plurals) |
| Premium | Premium | Roblox UI: "Tylko Premium", "subskrypcja Premium" |
| game pass | przepustka | Roblox UI "Przepustka", Creator docs "Przepustki"; players also write "gamepass, gamepassy" |
| developer product | produkt | Creator docs: "Produkty dewelopera"; in game UI just name the item |
| experience / game | gra | Roblox's Polish UI says "projekt" ("Czy na pewno chcesz opuścić projekt?"); Creator docs and older client text say "gra" ("wybierz grę", "Opuść tę grę"). Never "doświadczenie" |
| obby, tycoon, simulator | obby, tycoon, symulator | Genre words; titles stay English |
| rebirth | rebirth (ten rebirth, zrób rebirth) | Players keep the English word (unverified); "Odrodzenie" (10 chars) if the game translates every term. Pick one register with pet |
| pet | pet (ten pet, peta, pety, petów) | Masculine; players' loanword (unverified in print). All-Polish games: "zwierzak" (then also "Odrodzenie"); never "zwierzę domowe". Colloquial "pet" also means a cigarette butt, harmless in a pet game |
| egg / hatch | jajko / wykluć się, otworzyć jajko | "Legendarne jajko"; avoid gendered "wykluł/wykluła" next to {pet} |
| coins / gems | monety / klejnoty | Players may say "gemy" (unverified); pick one per game |
| boost | bonus | Players also say "boost"; Roblox's "premia" (Premium bonus) sounds like a salary bonus |
| multiplier | mnożnik | "stały mnożnik 2x" |
| XP | XP / exp | Never "punkty doświadczenia" on a HUD |
| level up | awans, nowy poziom | "Awans!", "Poziom 12"; never "Awansowałeś" (gendered) |
| quest | misja / zadanie | "Codzienne zadania" |
| leaderboard | ranking | Roblox UI: "Ranking"; lobby board title "Najlepsi gracze" |
| AFK, noob, OP, GG | AFK, noob, OP, GG | Kept; verb "afczyć" is slang (miejski.pl), fine only in flavor text |
| VIP | VIP | "serwer VIP"; Roblox's private server is "serwer prywatny"; inflect with a hyphen: "VIP-a" |
| trade | wymiana / wymienić się | "Wymiana", "Prośba o wymianę"; players also say "trade" |
| inventory / backpack | ekwipunek / plecak | Roblox UI: "Plecak" (Backpack), "Wyposażenie" (avatar inventory); gamers shorten ekwipunek to "eq" (miejski.pl, MMO slang) |
| daily reward | codzienna nagroda | Button "Odbierz" |
| codes | kody | "Wpisz kod", button "Odbierz" (Polish code guides) |
| group | społeczność | Roblox renamed Groups to Communities: "Emblemat społeczności"; an everyday word kids know. Players still say "grupa", also fine |
| like / favorite | polub / dodaj do ulubionych | Roblox UI "Dodaj do ulubionych". The thumbs-up has no text label in the client strings, so "Polub grę" is the game's own wording; casual "Daj łapkę w górę" (YouTube phrase) |
| server | serwer | "na serwerze"; Roblox: "Serwer jest pełny" |
| friends / connections | znajomi | Roblox's Polish UI used "znajomi" for both ("Wyszukaj znajomych", "Zaproś znajomych"); never "połączenia" or "kontakty" |
| badge | odznaka | Roblox: "Otrzymujesz odznakę" |

## Grammar traps in UI strings
- **Plurals with {count}.** Three live forms: "1 moneta, 2 monety, 5 monet, 12 monet, 22 monety, 0 monet", fractions "1,5 monety". The verb changes too: "Zostały 3 jajka" but "Zostało 5 jajek". One string cannot cover this, so use the label form Microsoft prescribes ("Grupy: %u"): "Monety: {count}", "Brakuje ci monet: {amount}!", "Kup za Robuxy: {price}". Roblox's own client does the same ("Dodatkowe Robuxy: {robux}", "Pozostałe ROBUXY ({RBX_NUMBER})"). A noun before the number in the nominative is safe: "Poziom {level}".
- **"You" in the past tense has gender.** "Wyklułeś/Wyklułaś", "Zdobyłeś/Zdobyłaś", "Kupiłeś" assume a boy or a girl. Use present tense, perfective future, a noun, or impersonal forms, as Roblox and Microsoft do: "Zdobywasz nagrodę: {item}" (Roblox), "Nie pamiętasz hasła?" over "Zapomniałeś hasła?" (Microsoft), "Stracisz monety", "Nowy poziom!". Adjectives too: "Jesteś gotowy?" -> "Gotowe?"; "Jesteś pewien?" -> "Na pewno?". Never slash forms like "zdobyłeś(-aś)" in a kids' game.
- **Gender of {player}.** "{player} dołączył" assumes a boy. Use present tense ("{player} dołącza do gry", "{player} wygrywa!"), a colon ("Zwycięzca rundy: {player}"), or a masculine head noun the verb agrees with ("Gracz {player} dołączył do gry", like Roblox's "Dołączył do ciebie użytkownik {X}").
- **Case around placeholders.** Names and inserted items stay in the nominative, but Polish verbs and prepositions demand other cases. "Wymiana z {player}" needs the instrumental -> "Wymiana z graczem {player}"; "Kup {item}" turns "Mikstura" into the wrong form "Kup Mikstura" -> "Kup przedmiot: {item}". Roblox's own pattern: "przedmiot {RBX_NAME}", "użytkownika {RBX_NAME}".
- **Rarity agreement.** Adjectives agree with the noun: "Legendarny Smok" (m), "Legendarna Sowa" (f), "Legendarne Jajko" (n), and change by case ("legendarnego"). Translate rarity words in the masculine nominative (Pospolity, Rzadki, Epicki, Legendarny, Mityczny) and attach them to a masculine nominative head noun: "Nowy pet ({rarity}): {pet}!", "Jajko: {rarity}".
- **Word order and compounds.** English noun stacks flip: the head noun comes first with a genitive after ("Lucky Potion" -> "Mikstura szczęścia", "Coin Boost" -> "Bonus monet"), or becomes adjective + noun ("Fire Sword" -> "Ognisty miecz" or "Miecz ognia"). Product names keep the multiplier first: "2x monety".
- **Capitalization.** Sentence case for titles, buttons, item names and product names (Microsoft; Roblox UI "Zresetuj postać", "Kup Robuxy"): "Codzienna nagroda", "Najlepsi gracze", "Mikstura szczęścia". Days and months are lowercase ("sobota", "grudzień").
- **Possessives and pronouns.** Drop English "your": "Sell your pets" -> "Sprzedaj pety". When one is needed, "swój" works for every person: "Wybierz swojego peta".

## Typography and formatting
- No space before ! ? : ; (unlike French). Commas follow Polish rules: none before "i", "lub", "albo"; always before "żeby", "że", "który".
- Quotation marks: low-high „...” (Microsoft, and Roblox UI: „Kontynuuj”). Period goes outside the closing quote.
- Numbers: space as thousands separator (non-breaking), comma as decimal: "12 500 monet", "1,5x". English "1,250" from game code reads as "one and a quarter" in Polish -- flag it to the developer instead of patching the string.
- Percent: no space, as Roblox's Polish UI writes "10% premii"; as an adjective with a hyphen: "10-procentowy bonus".
- Durations: "3 h 20 min", "2 d 5 h", "45 s" -- Roblox writes "{N} min" and "{N} s"; "m" is metres; "godz." is the long abbreviation. Compact "3h 20min" is fine on a tight HUD timer; keep "min", never "3h 20m". The format inside {time} comes from game code.
- Ellipsis: three periods, no space before: "Wczytywanie..." (Roblox UI).
- Dashes: spaced en dash for a break in a sentence ("Event – tylko dziś!"), unspaced in ranges ("1–3 pety"); hyphen for inflected acronyms ("VIP-a", "SMS-a").
- Keys: letters stay ("Naciśnij E"); Space is "Spacja" (Roblox UI and Microsoft), "Enter", "Shift" stay English. PC copy "Kliknij", mobile copy "Dotknij" (Roblox: "Dotknij, aby wykonać ruch").
- Dates: dd.mm.rrrr ("25.12.2026"). Prices are always "Robux"/"Robuxy", never "zł".
- Microsoft keeps one-letter words (w, z, i, o, a) off the line end with a non-breaking space. Roblox honors U+00A0 (TextService measured no break at it, 2026-11-08), so the real U+00A0 character (not an escape) after "w" keeps "w sklepie" together in wrapped labels; optional in short UI text.

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, XP, GG, noob, obby, the "x" in "2x".
- The game title ("Pet Hatch Tycoon"): Polish code guides keep English titles as is ("PLS DONATE", "Base Battles").
- Promo codes (FREEPETS) exactly as typed, same case; usernames and display names.
- Avoid sentences that force "Roblox" to inflect; Roblox's own UI writes "platforma Roblox" ("Zaktualizuj platformę Roblox").
- Translate pet, item, egg and area names consistently once you translate the game ("Smok", "Mikstura szczęścia"); keep English only for names the community already uses.
- Never drop diacritics: "pełny" not "pelny", "Zrób" not "Zrob". Text without them looks like a careless chat message.

## Rendering on Roblox
- Checked against the font files shipped in the Roblox client of 2026-11-05: Builder Sans, Builder Extended, Builder Mono, Source Sans Pro, Montserrat, Roboto, Arimo, Nunito, Luckiest Guy, Bangers, Oswald, Press Start 2P, Comic Neue Angular, Titillium Web, Ubuntu, Fondamento, Grenze Gotisch, Special Elite and every other bundled face not named below contain all of ą ć ę ł ń ó ś ź ż, their capitals, „ ” and – (Inconsolata lacks only –).
- Missing Polish letters: **Fredoka One** (lacks ą ć ę ń ś ź ż and their capitals; has ł ó -- a staple of simulator UIs), Creepster, Permanent Marker, Denk One, Balthazar, Accanthis ADF Std (Fantasy), Highway Gothic and Roman Antique (Antique; these two also lack ł). Studio check 2026-11-08: no empty boxes -- the client draws the missing letters from a thin sans fallback, so "Żółty" in Fredoka One shows mixed fonts inside one word. For Polish, switch such labels to a full-coverage font (Luckiest Guy, Bangers, Builder Sans).
- Luau `string.upper` changes only ASCII letters: "żółw" becomes "żółW". Write uppercase text directly in the table ("ŻÓŁW").
- Accented capitals (Ż Ó Ś Ć Ź) and the ogonek on ą ę reach above and below Latin letters; check for clipping in tight TextScaled labels (unverified).
- Long words can't wrap ("Wczytywanie...", "społeczności"); with TextScaled the whole label shrinks instead. Give labels AutomaticSize or slack.
- Verify in Studio: set the test locale to pl-pl, paste the pangram "Zażółć gęślą jaźń" into every font the game uses at its smallest TextSize, then open the longest strings (rebirth confirm, inventory full) and the shortest buttons (settings.on, menu.play).

## Mistakes machine translation makes here
1. Gendered "you": "Wyklułeś legendarnego smoka!" -> "Nowy pet (Legendarny): Smok!"; "Zdobyłeś nagrodę" -> "Zdobywasz nagrodę".
2. Number agreement: "Masz 5 monety", "1 monet" -> "Monety: 5"; "Potrzebujesz 2 monet" -> "Brakuje ci monet: 2!".
3. Formal or corporate tone: "Czy Pan chce kontynuować?", "Prosimy wpisać kod" -> "Grasz dalej?", "Wpisz kod".
4. Wrong verb for game buttons: "Play" as "Odtwórz" (media) -> "Graj"; "Claim" as "Zażądaj" or "Zgłoś roszczenie" -> "Odbierz".
5. Platform terms translated literally: "experience" as "doświadczenie" -> "gra"; "connections" as "połączenia" -> "znajomi".
6. English Title Case: "Codzienna Nagroda", "Najlepsi Gracze" -> "Codzienna nagroda", "Najlepsi gracze".
7. English number formats: "1,250 monet", "1.5x" -> "1 250 monet", "1,5x".
8. Nominative names in the wrong slot: "Wymiana z {player}", "Kup {item}" -> "Wymiana z graczem {player}", "Kup przedmiot: {item}".
9. Possessive and pronoun overload: "Twój plecak jest pełny. Ty musisz sprzedać twoje pety." -> "Plecak jest pełny! Sprzedaj pety."
10. Stripped diacritics: "Zrob rebirth", "pelny", "Wroc" -> "Zrób rebirth", "pełny", "Wróć".
11. Officialese: "Dokonaj zakupu za pośrednictwem sklepu" -> "Kup w sklepie".
12. Hatching as biology: "Wylęgłeś smoka" -> "Nowy pet: Smok!" or "Otwórz jajko".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Graj | |
| shop.title | Sklep | |
| shop.buy | Kup | Same as Roblox UI |
| reward.claim | Odbierz | Never "Zażądaj" |
| rebirth.button | Rebirth | Kept as players say it; "Odrodzenie" (10) if the game translates every term |
| rebirth.confirm | Zrobić rebirth teraz? Stracisz monety, ale dostaniesz stały mnożnik {multiplier}x. | Perfective future "stracisz/dostaniesz" has no gender; decimals need a comma ("1,5x") |
| coins.need_more | Brakuje ci monet: {amount}! | Label form; no noun or verb agrees with the number |
| coins.count | Monety: {count} | Avoids "1 monety/5 monety"; expects "1 250", not "1,250" |
| egg.hatched | Nowy pet ({rarity}): {pet}! | Rarity agrees with masculine "pet", so "Sowa" or "Jajko" names stay correct; no gendered past tense |
| rarity.legendary | Legendarny | Masculine nominative, to agree with "pet" |
| pet.name.dragon | Smok | |
| chat.player_joined | {player} dołącza do gry | Present tense reads as a live announcement and has no gender; Roblox's head-noun pattern ("Twój znajomy, {RBX_NAME}, dołączył do projektu") gives the alternative "Gracz {player} dołączył do gry" |
| trade.request | {player} chce się z tobą wymienić | |
| prompt.open_shop | Wciśnij E, by otworzyć | Exactly 22; "Wciśnij" is as common in Polish game prompts ("Wciśnij dowolny klawisz") as Roblox's "Naciśnij", which makes it 23 |
| pass.buy_price | Kup za Robuxy: {price} | Plural-safe label, Roblox's own pattern ("Dodatkowe Robuxy: {robux}"); "Kup za {price} Robux" leaves Robux uninflected, which Roblox never does |
| pass.coins2x | 2x monety | Sentence case product name |
| pass.vip | VIP | |
| reward.daily_title | Codzienna nagroda | 17 of 18 |
| reward.come_back | Wróć za {time} po kolejną nagrodę! | |
| codes.placeholder | Wpisz kod | |
| codes.invalid | Ten kod jest nieprawidłowy lub wygasł. | |
| social.like_reward | Polub grę i odbierz darmową <b>Miksturę szczęścia</b>! | Item name in the accusative ("Mikstura" -> "Miksturę") because we own the sentence; 47 visible characters |
| social.group_reward | Dołącz do naszej społeczności po darmową nagrodę! | "społeczność" per Roblox's rename; "grupy" also understood |
| afk.warning | Jesteś AFK! Rusz się, żeby dalej zarabiać! | |
| leaderboard.title | Najlepsi gracze | 15 of 16 |
| level.up | Awans! Masz teraz poziom {level}. | Avoids "Awansowałeś/Awansowałaś" |
| tutorial.sell | Wejdź w świecący krąg, żeby sprzedać pety. | |
| inventory.full | Plecak jest pełny! Sprzedaj pety, żeby zrobić miejsce. | "Plecak" as in Roblox's Backpack; possessive dropped |
| settings.music | Muzyka | |
| settings.on | Wł. | Roblox UI's toggle label; "Włącz" is a verb |
| loading | Wczytywanie... | Roblox UI; exactly 14 |
| event.ends_in | Koniec wydarzenia za {time} | 28 with "2 d 5 h"; "Koniec eventu za {time}" if space runs short |
| item.op | Ten miecz jest OP! | miejski.pl's own OP example is about a sword |
| friends.boost | Bonus +{percent}% za każdego znajomego na serwerze | Leading "Bonus" avoids the genitive after % |

## Sources
1. Microsoft Polish Localization Style Guide -- https://download.microsoft.com/download/b/d/c/bdc253ac-dbf3-4261-86a2-ffedfa718425/pol-pol-StyleGuide.pdf
2. Unicode CLDR language plural rules chart -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox client CoreScript translations, pl column (ExtraContent/translations/CoreScriptLocalization.csv, Roblox build of 2026-11-05) -- local file from the Roblox install
4. Roblox client bundled fonts (content/fonts, same build), cmap checked for Polish letters and fallback rendered in Studio on 2026-11-08 -- local files from the Roblox install
5. Roblox Creator docs (pl-pl, AI-translated beta), passes -- https://create.roblox.com/docs/pl-pl/production/monetization/game-passes
6. android.com.pl, Roblox codes guide ("Odbierz", English game titles kept) -- https://android.com.pl/rozrywka/919529-kody-do-roblox-poradnik-lista/
7. Miejski Słownik Slangu, "OP" -- https://www.miejski.pl/slowo-Op
8. Miejski Słownik Slangu, "Afczyć" -- https://www.miejski.pl/slowo-Afczy%C4%87
9. Miejski Słownik Slangu, "Expić" -- https://www.miejski.pl/slowo-Expi%C4%87
10. Polish Wikipedia, Roblox (Robux inflected, "experiences" wording) -- https://pl.wikipedia.org/wiki/Roblox
11. Miejski Słownik Slangu, "Eq" -- https://www.miejski.pl/slowo-Eq
