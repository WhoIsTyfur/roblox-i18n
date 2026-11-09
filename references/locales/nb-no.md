# Norwegian Bokmal (nb-no) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `nb-no`. It is Roblox's only Norwegian locale (no `no` or Nynorsk `nn` locale exists), so a bare `nb` column adds nothing; every Norwegian player who gets a translation reads this column |
| Script, direction | Latin, LTR; extra letters æ ø å Æ Ø Å (é in a few loans: "idé", "kafé") |
| Address the player as | informal singular "du" (deg, din/ditt/dine); never "De", never "dere" in UI, never generic "man" |
| Text expansion vs English | +14% over the reference set below (measured with sample values); sentences -21% to +45%, short labels up to +50% ("Shop" -> "Butikk"); closed compounds get long and cannot wrap |
| Plural categories (CLDR) | one, other (one = exactly 1, also "1,0": "1 mynt", "0 mynter", "2 mynter", "1,5 mynter"); ordinals have one form ("1. plass") |
| Model confidence | medium -- grammar is well covered, but models slip into Danish, Swedish or Nynorsk forms and split compounds, and Roblox ships no Norwegian app UI to copy terms from |
| Native review before shipping | recommended |

## Audience and register
- Roblox is everywhere among Norwegian kids: Barnevakten, citing Medietilsynet 2026, says more than four in five 9-12-year-olds play it and 65 percent of 13-14-year-olds. Write for a 10-year-old reader. (On 2026-10-19 the government said Roblox will get the 16-year limit planned for social media; that is a proposal, not law.)
- Roblox's own app has no Norwegian UI: its locale API enables Bokmål for in-experience content only, and its Norwegian help center holds just two gift-card terms pages. Players learn platform words from the English app ("Friends", "Robux", "Premium"); Norwegian parent guides even quote the English settings names. Your game may be the only Norwegian text they meet on Roblox, so it should read like a game written in Norwegian.
- Who sees this column: Player.LocaleId follows the language set on the Roblox account, and the in-experience Settings menu has a language switcher listing the languages the game supports. So add Norsk bokmål under Supported Languages in the game's localization settings. Whether Roblox picks Bokmål from a Norwegian device by itself is unverified; assume many Norwegian kids stay on English unless they switch.
- Use "du". Microsoft's Bokmål guide talks to the user as "du" throughout and lists "man" and stiff words (benytte, forsøke, anvende, påfølgende) as things to avoid: "Man kan kjøpe pass i butikken" -> "Du kan kjøpe pass i butikken".
- Buttons, tabs and commands use the imperative, not the infinitive: "Spill", "Kjøp", "Hent", "Bytt", "Avbryt". The imperative is the infinitive minus the final -e ("kjøpe" -> "Kjøp", "selge" -> "Selg") unless that leaves a hard cluster ("åpne" -> "Åpne", "lagre" -> "Lagre"). A double consonant is kept except m: "komme" -> "Kom", never "Komm".
- Tutorial and instruction text: the same imperative ("Gå inn i sirkelen", "Trykk på E"). Short yes/no fragments may use the infinitive, as Microsoft does ("Slette filen?"); a full "Vil du ...?" sounds friendlier in dialogs.
- Hype sounds natural as short, plain exclamations: "Nytt nivå!", "Kult!", "Wow!", "Du klarte det!". Avoid "Vennligst" (reads like a letter from the bank), stacked "!!!", and adult slang. Loanwords kids really use are fine ("OP", "AFK", "noob").
- Write standard, moderate Bokmål with -en forms for feminine nouns ("boken", "belønningen"), as Microsoft does and as this guide's examples do. a-forms ("boka", "belønninga") are correct and more casual, but mixing both in one game looks careless, so use them only if the whole game does. Never Nynorsk ("ikkje", "eg", "kva", "berre", "heim"), even though Nynorsk readers also get this column.

## Roblox and gaming vocabulary
| English | Bokmål in game UI | Note |
|---|---|---|
| Robux | Robux | Invariant: "1 Robux", "100 Robux". Roblox's Norwegian terms: "Robux (Roblox' valuta i spillet)". Compounds take a hyphen: "Robux-pris". |
| game pass | pass (et pass, passet, pass, passene) | "VIP-pass", "Kjøp pass". Players may write "gamepass" (unverified). |
| developer product | (name the item) | "utviklerprodukt" is creator jargon; players never see it. |
| experience / game | spill (et spill, spillet) | Roblox's legal text says "opplevelser"; Wikipedia notes it is the official word, but parents' guides and players say "spill". |
| obby / tycoon / simulator | obby / tycoon / simulator | Genre words stay: "en obby, obbyen". "simulator" is also Norwegian (simulatoren, simulatorer). |
| rebirth | Rebirth (button), "rebirth" in text | Kept: with no Norwegian Roblox UI, players have only ever seen this mechanic as "Rebirth" (inferred; the Danish and Swedish guides keep it too). "Gjenfødsel" (10) sounds religious. Kids turn loans into -e verbs (campe, kicke), but keep those out of UI: "Klar for rebirth?", not "Rebirthe nå?". |
| pet | kjæledyr (et kjæledyr, kjæledyret, kjæledyr, kjæledyrene) | Correct, and its invariant plural makes "1 kjæledyr" and "5 kjæledyr" both right. Kids may say "pets" (unverified), but "pets" breaks with {count} and inflected forms ("petsene"). |
| egg / hatch | egg (invariant plural) / klekke (ut) | "Klekk egget!", "Egget klekkes...". Bokmålsordboka: "klekke egg". |
| coins / gems | mynter (en mynt) / diamanter or edelsteiner | Match the icon: a diamond icon -> "diamanter", a colored gem -> "edelsteiner" (Minecraft's Bokmål says "Diamant"). One word per game; which kids prefer is unverified. |
| boost / multiplier | bonus or boost / "2x" | "bonus" (en bonus) is plain Norwegian; "boost" is gamer speech, not in the dictionary. Show multipliers as "2x", not "multiplikator". |
| XP / level up | XP / "Nytt nivå!", "nivå 5" | "XP-en" with a hyphen. Minecraft's Bokmål says "erfaringsnivå". Players say "levle" (unverified); keep it out of UI. |
| quest | oppdrag (et oppdrag, invariant plural) | Short and natural; "quest" is understood. |
| leaderboard | toppliste / Toppspillere | One word each. |
| AFK / noob / OP | AFK / noob / OP | All three are in Barnevakten's glossary of words Norwegian kids use. "Du er AFK", "Sverdet er OP". |
| VIP | VIP | "VIP-en", "VIP-pass", "VIP-område". |
| trade | bytte (verb and noun), byttehandel | Barnevakten writes "byttehandel" and "byttehandle". Button "Bytt". Not "handle", which reads as shopping or business. |
| inventory / backpack | ryggsekk / lager | Norwegian "inventar" means furniture; Minecraft's Bokmål uses "Forråd". |
| daily reward | daglig belønning | Adjective + noun, two words. |
| codes | koder (en kode, koden); "Løs inn kode" | Roblox's Norwegian terms use "løse inn" / "innløses" for redeeming. |
| group | gruppe (gruppen) | Roblox's English UI now says "Communities", but Barnevakten (2026) still writes "grupper", and "gruppe" needs no English. "community" in Norwegian text is unverified among kids; "fellesskap" is a stiff calque. |
| like / favorite | like (imperative "Lik") / favoritt, "Legg til i favoritter" | "like" is the everyday Norwegian verb for a thumbs-up ("lik og del"); "Lik spillet" is short and clear in context. "Gi spillet tommel opp" is the longer fallback. |
| server | server (serveren, servere) | Microsoft writes "serverne". Always "på serveren", "privat server". |
| friends | venner (en venn, vennen, venner, vennene) | Roblox renamed Connections back to Friends on 2026-04-02. Never "tilkoblinger" or "forbindelser". |
| Premium | Premium | "Premium-abonnement", as in Roblox's Norwegian terms. |
| shop / chat | butikk / chat, chatte | Bokmålsordboka lists "chatte" (chatter, chattet). |

## Grammar traps in UI strings
- **Plurals with {count}.** One = exactly 1, so "{count} mynter" breaks at 1. Safe patterns:
  - label + colon: "Mynter: {count}"
  - invariant nouns: egg, kjæledyr, oppdrag, sverd, poeng, Robux ("{count} kjæledyr" is right for 1 and 500)
  - number standing alone: "Du mangler {amount}."

  Never "mynt(er)". Bad: "Du har {count} mynter" -> good: "Mynter: {count}".
- **Gender agreement inside the string.** The noun's gender (en/ei/et) picks the article and the forms of ny/nytt, hver/hvert, din/ditt/dine: "hver venn" but "hvert egg"; "ny drage" but "nytt egg"; "ryggsekken din" but "egget ditt". Check each against the noun you chose.
- **Inserted nouns.** Never put an article or adjective before {pet} or {item}: "en {pet}" fails for neuter pets ("et lam"), and "{rarity} {pet}" gives "Sjelden lam" (needs "Sjeldent"). Never glue an ending to a placeholder ("{pet}en"). Use a colon or parentheses: "Nytt kjæledyr: {pet} ({rarity})!".
- **{player} has unknown gender.** Verbs don't change for person or gender, and predicate adjectives don't split he/she: "{player} ble med i spillet", "{player} er klar". Never refer back with "han" or "hun"; repeat {player} or switch to "du".
- **Genitive with names.** No "{player}s": names ending in s give "Thomass", Microsoft's own warning. Write "kjæledyret til {player}" (preferred) or "{player} sitt kjæledyr". Fixed names ending in s, x or z take an apostrophe: "Roblox' valuta".
- **Double definiteness.** Adjective + definite noun needs both den/det/de and the suffix: "den glødende sirkelen", "det nye egget". Not "den glødende sirkel" (Danish) or "glødende sirkelen".
- **Possessive after the noun.** "ryggsekken din", "myntene dine". "din ryggsekk" sounds emphatic or Swedish.
- **Verb second.** A fronted word pushes the subject behind the verb: "Nå er du på nivå 5", not "Nå du er på nivå 5". In subclauses "ikke" comes before the verb: "hvis du ikke beveger deg".
- **Time prepositions.** "om" for a point ahead ("om 3 t" = in 3 hours), "i" for a span ("i 3 timer" = for 3 hours): "Eventet slutter om {time}".
- **"å", not "og", before an infinitive:** "Husk å hente belønningen", not "Husk og hente".
- **Compounds are closed.** "kjæledyrbutikk", "toppspillere", "lykkedrikk". Splitting them (særskriving) is the most visible Norwegian error. Hyphenate when a part is an acronym, digit or brand: "VIP-pass", "2x-bonus", "Robux-pris", "Roblox-kontoen". Acronyms inflect after a hyphen: "XP-en", "VIP-en".
- **Capitalization.** Sentence case for titles, buttons and tabs: "Daglig belønning", not "Daglig Belønning". Weekdays, months and languages are lowercase ("mandag", "norsk"). Item and pet names: capital first letter only, everywhere ("Lykkedrikk", "Gylden drage").
- **Commas.** Always before "men", and after a subordinate clause that opens the sentence ("Hvis du står stille, blir du AFK"), but not before one that follows ("Du blir AFK hvis du står stille"). Microsoft also keeps the optional comma between imperative clauses: "Velg et egg, og trykk på Klekk."

## Typography and formatting
- No space before ! ? : ; ("Nytt nivå!"). Semicolons are rare in Norwegian (Microsoft); use a period or comma instead.
- Quotes are « » (CLDR and Microsoft); inner quotes U+2018/U+2019. Microsoft writes UI element names without quotes: "Trykk på Hent".
- Numbers: space as thousands separator (CLDR uses a no-break space, U+00A0): "1 250", "1 000 000"; decimal comma: "1,5". Game code formats numbers, so flag English values ("1,250", "1.5x") for the developer to format by LocaleId. Use a normal space in Roblox: Fredoka One, a common simulator font, has no U+00A0 glyph.
- Percent: "10 %" with a space (CLDR). In a tight HUD badge "+10%" is tolerable (unverified); keep one style per game.
- Durations: CLDR short forms "2 d 5 t", "3 t 20 min", "45 sek" (t = timer); narrow "3t 20m". English "3h 20m" -> "3 t 20 min".
- Abbreviations take periods ("f.eks.", "ca.", "kl. 18.00"); units don't ("min", "km"). Ordinals: digit + period, "1. plass", never "1st".
- Ellipsis: three periods. No space in short UI labels ("Laster inn...", as Minecraft's Bokmål writes "Laster inn venneliste..."); Microsoft drops the space after commands but spaces it in running text ("Vent litt ..."). Pick one for status labels per game.
- Dashes: Microsoft says the em dash is never used in Norwegian. Use a spaced en dash " – " sparingly, unspaced in ranges ("1–10").
- Keys: keep the key as printed ("E", "Q", "F"). Microsoft writes "trykke på": "Trykk på E". Shift -> "Skift", Spacebar -> "Mellomrom", Enter stays.
- Multipliers: ASCII "x": "2x mynter", "1,5x".

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, noob, obby, tycoon.
- Game titles stay English: "Pet Hatch Tycoon". Promo codes (FREEPETS), usernames, display names, {player}, keybinds and emoji too.
- Translate item, pet and rarity names, and use each name the same way everywhere ("Lucky Potion" -> "Lykkedrikk").
- Never replace æ ø å with ae, oe/o or aa: "aa" is pre-1917 spelling, and dropping the marks changes words ("får" = get, "far" = father; "så" = so or saw, "sa" = said).
- Bokmål only. Don't add Nynorsk forms for Western Norway players; Roblox has no Nynorsk column.

## Rendering on Roblox
- æ ø å Æ Ø Å (Latin-1 Supplement) are covered: a cmap check of the 2026-11 Roblox client's bundled fonts found them, plus é « », in all 60 Latin fonts (Builder Sans, Montserrat, Arimo, Source Sans Pro, Fredoka One, Luckiest Guy, Bangers, Press Start 2P and the rest). Only the Indic, Thai, Khmer, Myanmar, Georgian and emoji fonts lack them. Uploaded custom fonts are unchecked.
- U+00A0 is missing from Fredoka One, Sarpanch, Balthazar and Roman Antique, and "–" from Inconsolata: write normal spaces and avoid dashes in those fonts.
- Luau `string.upper` and `string.lower` change only ASCII: "nivå" becomes "NIVå". Write capitals directly in the table ("NYTT NIVÅ!") or use a UTF-8-aware helper.
- Each of æ ø å is 2 bytes: code that truncates with `string.sub` or counts with `#` can split a letter into a broken glyph; `utf8.len` and `utf8.offset` are safe.
- TextWrapped breaks at spaces, so long compounds ("kjæledyrbutikken", "gjenfødselsbonusen") cannot wrap, and TextScaled shrinks the whole label instead. Whether Roblox also breaks after a hyphen is unverified. Keep narrow buttons to short words.
- The ring on Å and the slash in Ø reach the top of the line box: check for clipping in tight TextScaled frames (unverified).
- Verify in Studio: set the test locale to `nb-no`, put "ÆØÅ æøå «» – é 1 250 10 %" in a TextLabel in every font the game uses, then open the longest strings (rebirth confirm, tutorial, inventory full) and the 8-10 character buttons at phone size.

## Mistakes machine translation makes here
- Danish or Swedish spelling: "Køb nu" / "Köp nu" -> "Kjøp nå"; "efter" -> "etter"; "hvad" -> "hva".
- Nynorsk mixed in: "Du har ikkje nok mynter" -> "Du har ikke nok mynter"; "kva" -> "hva".
- Split compounds and Title Case: "Topp Spillere", "Daglig Belønning", "kjæledyr butikk" -> "Toppspillere", "Daglig belønning", "kjæledyrbutikk".
- Stiff register: "Vennligst skriv inn koden", "Man må ..." -> "Skriv inn kode", "Du må ...".
- Infinitive or misspelled buttons: "Kjøpe", "Spille", "Hente" -> "Kjøp", "Spill", "Hent"; "Komm tilbake" -> "Kom tilbake".
- Claim as "Krev" (= demand) or "Gjør krav på" -> "Hent".
- "i" for a future point: "Kom tilbake i 3 timer" -> "Kom tilbake om 3 t".
- Danish-style definiteness and possessives: "den glødende sirkel", "din ryggsekk er full" -> "den glødende sirkelen", "ryggsekken din er full".
- English genitive on names: "{player}s kjæledyr" -> "kjæledyret til {player}".
- Gender slips: "et sjelden egg", "hver egg", "en {pet}" -> "et sjeldent egg", "hvert egg", "Nytt kjæledyr: {pet}".
- English number format: "1,250 mynter", "1.5x" -> "Mynter: 1 250", "1,5x".
- Wrong gaming words: "inventar" (furniture) -> "ryggsekk"; "overmektig" -> "OP"; "tilkoblinger" -> "venner"; "handle" (go shopping) for trade -> "bytte".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Spill | Imperative, as in Minecraft's Bokmål "Spill" button. |
| shop.title | Butikk | |
| shop.buy | Kjøp | Imperative, not "Kjøpe". |
| reward.claim | Hent | Not "Krev". |
| rebirth.button | Rebirth | Kept as the genre word players know from English simulators; "Gjenfødsel" (10/10) only if the whole game avoids English terms. |
| rebirth.confirm | Klar for rebirth? Du mister myntene dine, men får en permanent {multiplier}x-bonus. | Avoids a loan verb; comma before "men" is required. Code should send "1,5", not "1.5". |
| coins.need_more | Ikke nok mynter! Du mangler {amount}. | Rebuilt so {amount} = 1 stays correct (34 chars with "1 250"). |
| coins.count | Mynter: {count} | Label pattern avoids "1 mynter"; count should arrive as "1 250". 13/16 there, but 7 digits ("1 250 000") reach 17: abbreviate big counts. |
| egg.hatched | Nytt kjæledyr: {pet} ({rarity})! | Avoids article and adjective agreement; "Nytt" matches neuter "kjæledyr". 35 chars with Drage/Legendarisk. |
| rarity.legendary | Legendarisk | 11/12. -isk adjectives don't change in neuter. |
| pet.name.dragon | Drage | Masculine (en drage). Bokmålsordboka also allows "drake"; Minecraft's Bokmål uses "drage". |
| chat.player_joined | {player} ble med i spillet | Minecraft's Bokmål uses "logget seg på" for servers; "ble med i spillet" reads friendlier. |
| trade.request | {player} vil bytte med deg | |
| prompt.open_shop | Trykk på E for å åpne | 21/22; "Trykk E for å åpne" (18) if space is tight. |
| pass.buy_price | Kjøp for {price} Robux | 20/22 with price "1 000". |
| pass.coins2x | 2x mynter | Sentence case; "Doble mynter" (12) also fits. |
| pass.vip | VIP | Kept. |
| reward.daily_title | Daglig belønning | 16/18. |
| reward.come_back | Kom tilbake om {time} for neste belønning! | "om" for a time ahead; time like "3 t 20 min". |
| codes.placeholder | Skriv inn kode | 14/16. |
| codes.invalid | Koden er ugyldig eller utløpt. | |
| social.like_reward | Lik spillet og få en gratis <b>Lykkedrikk</b>! | 39/55. Item name capitalized as a name (Minecraft's Bokmål has "Lykkebrygg" for its luck potion). "Gi spillet tommel opp og få ..." (49) if "Lik" feels too bare. |
| social.group_reward | Bli med i gruppen vår og lås opp en gratis belønning! | 53/55; "for å låse opp" ran to 57. "gruppe", not the English UI's "Communities". |
| afk.warning | Du er AFK! Beveg deg for å tjene videre! | 40/45. |
| leaderboard.title | Toppspillere | Closed compound; "Toppliste" also works. |
| level.up | Nytt nivå! Nå er du på nivå {level}. | Verb-second word order after "Nå". |
| tutorial.sell | Gå inn i den glødende sirkelen for å selge kjæledyrene dine. | Double definiteness; possessive after the noun. 60/70. |
| inventory.full | Ryggsekken din er full! Selg kjæledyr for å få plass. | Invariant plural "kjæledyr". |
| settings.music | Musikk | |
| settings.on | På | Pair with "Av". |
| loading | Laster inn... | 13/14. No space before the dots in a short label; "Laster inn ..." (14) is also correct. |
| event.ends_in | Eventet slutter om {time} | 26/28 with "2 d 5 t"; a 10-character duration overflows, so use "Slutter om {time}" there. |
| item.op | Dette sverdet er OP! | |
| friends.boost | +{percent} % bonus for hver venn på serveren din | Space before %; "hver" matches masculine "venn". |

## Sources
1. Microsoft Norwegian Bokmål localization style guide (PDF): https://aka.ms/Norwegian-bokmal-styleguide
2. CLDR plural rules (nb, no): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR JSON, nb numbers, duration units and quotation delimiters: https://github.com/unicode-org/cldr-json/tree/main/cldr-json
4. Roblox locale API (nb_no enabled for in-experience content, not the full app): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
5. Roblox Creator Hub, Language codes (Bokmål row, nb-no): https://create.roblox.com/docs/production/localization/language-codes
6. Roblox Help (no), Norway gift card and credit terms (Robux, Premium-abonnement, innløses, skaperopplevelser); one of only two Norwegian articles: https://en.help.roblox.com/hc/no/articles/17138376393620
7. Roblox newsroom, Connections back to Friends (2026-04-02): https://about.roblox.com/newsroom/2026/04/expanding-trusted-friends
8. Barnevakten, Roblox guide for parents (usage stats, spill, venner, grupper, byttehandel): https://www.barnevakten.no/app/roblox/
9. Barnevakten, Ordliste for dataspill (AFK, noob, OP, Norwegianized verbs): https://www.barnevakten.no/ordliste-for-dataspill/
10. Norwegian Wikipedia, Roblox (spill vs «opplevelser», Robux): https://no.wikipedia.org/wiki/Roblox
11. Minecraft Java Edition lang file no_no.json ("Norsk bokmål"), via Mojang's asset index: https://piston-meta.mojang.com/mc/game/version_manifest_v2.json
12. Bokmålsordboka (gamer, chatte, drake/drage, klekke, kjæledyr, belønning): https://ordbokene.no
13. DevForum, Introducing Builder font (Gotham -> Montserrat, Arial -> Arimo): https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222
14. Roblox Creator Docs, Localize with scripting (in-experience language switcher) and Player.LocaleId reference: https://create.roblox.com/docs/production/localization/localize-with-scripting
15. Roblox Creator Docs, Localization overview (Supported Languages setting): https://create.roblox.com/docs/production/localization
16. Barnevakten, Må alle barn under 16 ut av Roblox? (2026-10-20): https://www.barnevakten.no/ma-alle-barn-under-16-ut-av-roblox/
17. cmap check of the fonts bundled with the Roblox client (content/fonts, version-f0ea5da9412f4e35, 2026-11-08), run by the reviewer
