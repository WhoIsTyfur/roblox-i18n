# Danish (da-dk) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `da-dk` (no bare `da` column: Danish has one Roblox locale) |
| Script, direction | Latin, LTR; letters æ ø å Æ Ø Å; é in a few loans and stress marks ("idé", "én", "Kontrollér") |
| Address the player as | informal singular "du" (din/dit/dine, dig); never "De/Dem/Deres", never plural "I" in UI |
| Text expansion vs English | +15-30% for sentences; compounds make single words long ("Daily Reward" -> "Daglig belønning") (rule of thumb, unverified) |
| Plural categories (CLDR) | one, other (one = 1, plus any 0,x or 1,x with a nonzero decimal: "1 mønt", "1,5 dag", "0,5 dag"; other: "0 mønter", "2 mønter", "2,5 dage") |
| Model confidence | medium: grammar is well covered, but Norwegian/Swedish bleed, en/et gender and calques are common, and player slang is unverified |
| Native review before shipping | recommended |

## Audience and register
- Roblox's app and website are not in Danish: its locale API enables `da_dk` for in-game content only. Players still reach this column. Asked without a login from a Danish browser (tested 2026-11-08), the API returns in-game locale `da_dk` while the app stays `en_us`, so the device language decides; players can also pick any language the game lists in the in-game Settings menu (Roblox docs). Whether an account that saved English as its language still gets `da-dk` is unverified.
- Danish kids therefore know platform words in English (Robux, Premium, Friends, Communities) and read your game as the only Danish text in their Roblox session.
- Use "du" everywhere. Microsoft's Danish guide also says "du", not "De", and asks for everyday words: "få" not "opnå", "vores" not "vort", "flere" not "yderligere", "men" not "imidlertid", "om" not "hvorvidt".
- Buttons and commands: the imperative (= verb stem), as in Danish software: "Spil", "Køb", "Hent", "Gem", "Annuller". Not the infinitive: "At købe" or "Købe" -> "Køb".
- Questions in dialogs: Microsoft prefers "Vil du ...?" over a bare "Fortsæt?" and keeps "Er du sikker på, at ...?" for real data loss. "Rebirth now?" -> "Vil du lave rebirth nu?".
- Danish hype is understated. One "!" per sentence, short words: "Sejt!", "Tillykke!", "Nyt level!". Stacked superlatives ("Fantastisk utrolig mega-belønning!!!") read as a translated ad. Microsoft: don't overuse exclamation marks; pick stronger words.
- Spoken, light forms are fine: "Det her sværd" (spoken) rather than "Dette sværd" (written, stiffer). Avoid adult slang and swearing ("fedt" is fine, "pisse" is not).
- People: Danish role nouns are mostly neutral ("spiller", "vinder", "ven"). Never refer back to {player} with "han" or "hun"; repeat {player} or rephrase. Microsoft's "vedkommende" is correct but sounds like a letter from the council; avoid it in a kids' game.
- Write Danish, not Norwegian or Swedish: "Køb" (not "Kjøp"/"Köp"), "spil" (not "spill"), "ven" (not "venn"), "ikke" (not "ikkje"/"inte").

## Roblox and gaming vocabulary
| English | Danish in game UI | Note |
|---|---|---|
| Robux | Robux | Invariant: "1 Robux", "100 Robux". Roblox's Danish terms: "Robux er digitalt indhold". |
| game pass | game pass, plural game passes | Roblox's Danish legal text keeps "game passes" in English. Players also write "gamepass" (unverified). |
| developer product | (name the item) | Roblox's Danish EEA terms say "udviklerprodukter" (e.g. game passes, eliksirer); players never see the word. |
| experience / game | spil (et spil, spillet) | Roblox's Danish help says "oplevelser"; inside a game that sounds like a brochure. "i spillet", not "i oplevelsen". |
| obby / tycoon / simulator | obby / tycoon / simulator | Genre words stay. "et tycoon-spil"; "en simulator", plural "simulatorer". Gender of "obby" unverified: avoid articles. |
| rebirth | rebirth (en rebirth, plural rebirths) | "genfødsel" is long and religious. Gender by analogy with "en genfødsel" (Microsoft's loanword rule); unverified in player use. |
| pet | pet, plural pets | Kids keep "pets" (unverified); "kæledyr" is correct but sounds like a real cat. Avoid definite forms ("pettet", "petsene"); write "dine pets". |
| egg / hatch | æg (et æg, æggene) / klække | "Du klækkede ..."; "åbne et æg" also works. |
| coins / gems | mønter (en mønt) / ædelsten or diamanter | "coins" is also used by players (unverified). Pick one gem word per game. |
| boost / multiplier | boost (et boost, plural boosts) / multiplikator | "et boost" is everyday Danish. In labels write "2x" instead of "multiplikator". |
| XP / level up | XP / Nyt level! | "et level", plural "levels"; "Du er nu level 5". Minecraft's Danish UI says "Niveau" (enchanting); "level" in a Roblox HUD is unverified gamer usage. One word per game. |
| quest | mission or opgave | "en mission" is natural; "quest" is understood. Don't mix in one game. |
| leaderboard | rangliste, topliste | Roblox's Danish help uses "ranglister" for its charts. Title: "Topspillere". |
| AFK / noob / OP / VIP | AFK / noob / OP / VIP | Kept. "en noob", plural "noobs" (unverified). "Det her sværd er OP!" |
| trade | bytte (verb), byttehandel, bytteanmodning | Roblox's Danish terms use "bytter" (verb) and "handelsaktivitet"; Minecraft's villager trades are "handel". Kids also say "trade" (unverified); UI uses "bytte". |
| inventory / backpack | rygsæk, taske, lager | Minecraft's Danish inventory is "Taske". Not "inventar": in Danish that means furniture and fittings. |
| daily reward | daglig belønning | Or "dagens belønning". |
| codes | koder; "Indtast kode", "Indløs kode" | "indløse" = redeem, as in Roblox's Danish terms. Keep "Indløs" for codes, not for Claim. |
| group | gruppe | Roblox's Danish EEA terms call Communities "fællesskaber" and still list "grupper"; its name rules write "gruppe-/fællesskabsnavne". The English UI kids see says "Communities". "gruppe" is shorter; "fællesskab" pushes social.group_reward to 59/55. |
| like / favorite | like, "giv et like" / favorit, "føj til favoritter" | The Like button has no Danish Roblox name (the app is English); Roblox's Danish help uses "synes godt om" only as the plain verb. "et like" is everyday Danish. |
| server | server (en server) | "på serveren", "på din server"; never "i serveren". |
| friends | venner (en ven) | Roblox's Danish help says "venner", "venneanmodninger". Roblox renamed Friends to Connections in July 2025 and back in April 2026; never write "forbindelser". |
| Premium | Premium | Roblox's Danish terms: "Premium-abonnement". |
| shop | butik | "shop" is also normal Danish (webshop); pick one. |

## Grammar traps in UI strings
- **Plurals with {count}.** "1 mønter" is wrong, and Roblox can't switch forms. Safe patterns:
  - label + colon: "Mønter: {count}"
  - put the noun before the number: "Ikke nok mønter! Du mangler {amount}."
  - Robux never changes: "{price} Robux"

  Never "mønt(er)" in a game; "X dag(e)" style is for software tables only.
- **en/et gender breaks inserted nouns.** Articles, adjectives and possessives agree with the noun: "en drage", "et egern"; "en sjælden drage", "et sjældent egern"; "din drage", "dit æg". "Du klækkede en {pet}" fails for every neuter pet. Use a colon or parentheses: "Du klækkede: {pet} ({rarity})!"
- **The definite article is a suffix.** "dragen", "ægget", "mønterne": you can't attach it to a placeholder ("{pet}en"). Keep inserted values bare, after a colon or in parentheses.
- **No double definiteness.** With an adjective, Danish uses "den/det/de" + adjective + bare noun: "den lysende cirkel", never "den lysende cirklen" (that is Swedish/Norwegian).
- **{player} and possessives.** Genitive is "-s" with no apostrophe ("Emmas pet"), but names ending in s, x or z take only an apostrophe ("Lucas' pet", "Alex' pet"). A placeholder can't know which, so write "pet fra {player}" or "{player} vil bytte med dig". Never the English "'s".
- **Word order (V2).** The verb comes second in main clauses: "Nu er du level {level}", not "Nu du er ...". In subclauses "ikke" goes before the verb: "hvis du ikke bevæger dig".
- **Pronouns after {player}.** Third-person possessives that point back to the subject are reflexive and gender-free: "{player} har solgt sine pets". MT writes "hans/hendes pets", which guesses a gender and means someone else's pets. Object form of "du" is "dig": "{player} vil bytte med dig".
- **Compounds are one word.** "dagsbelønning", "lykkeeliksir", "topspillere", "bytteanmodning". Splitting them ("særskrivning") is the classic error: "top spillere" -> "topspillere". Hyphenate when an acronym, number, name or English multi-word part joins: "VIP-område", "2x-boost", "Robux-pris", "Roblox-gruppe", "Premium-abonnement" (Microsoft's hyphen rules; last one is Roblox's own).
- **Capitalization.** Sentence case for titles and buttons, nouns lowercase (unlike German): "Daglig belønning", not "Daglig Belønning". Item and pet names that the game treats as names may stay capitalized ("Drage", "Lykkeeliksir"); be consistent.
- **Imperatives.** Add the accent when an -er imperative could be misread: "Kontrollér", "Markér" (Microsoft rule). Avoid hard consonant-cluster imperatives ("Ændr", "Forenkl"): "Change" -> "Skift".
- **Commas.** Danish puts a comma between two main clauses, also before "og" (Dansk Sprognævn), and Microsoft applies it to imperative clauses with different objects: "Klik på Start, og vælg ...", "Giv spillet et like, og få ...". This comma is not optional in any style. Only the comma before a subclause is optional under Dansk Sprognævn's rules; Microsoft keeps it ("Kom tilbage, når du er klar"). Either style is fine; use one per game. No comma before "og" in a list: "mønter, pets og æg".

## Typography and formatting
- No space before ! ? : ; and no inverted marks: "Nyt level!", "Vil du lave rebirth nu?". After a colon, capitalize only if a full sentence follows.
- Quotes: Microsoft's Danish guide uses double quotes in the 99-99 shape (”Topspillere”); plain straight "Topspillere" is fine too. »Topspillere« is also correct Danish. Never English “...” (66-99). Pick one style per game.
- Numbers: 1.250 for thousands, 1,5 for decimals, always a leading zero ("0,5", not ",5"). The translator can't fix numbers that game code formats; flag "1,250" and "1.5x" for the developer to format by LocaleId.
- Percent: space before %: "50 %", "+10 % boost" (Microsoft). In a cramped badge "+10%" is tolerable; keep one style per game.
- Durations: CLDR short forms are "2 dage 5 t.", "3 t. 20 min.", "45 sek."; narrow forms keep the space: "2 d 5 t", "3 t 20 m", "45 s". English "3h 20m" -> "3 t. 20 min." (or "3 t 20 m" in tight labels). "t" = timer (hours); never "h". Game code formats {time}: tell the developer which form fits.
- Don't end a sentence with an abbreviation and then "!": "... om 3 t. 20 min.!" looks broken. Move {time} to the middle of the sentence.
- Clock times: 24-hour, "13:00". Ordinals are number + period: "1. plads", "2. plads" (not "1st"); "#1" is fine on boards.
- Ellipsis: no space in UI text: "Indlæser...". The single "…" character also works.
- Dashes: no em dash; use a spaced en dash "–" or, better, a comma. Ranges use a hyphen: "1-5".
- Keys: "Tryk på E"; "tasten E" is not needed. Never translate E, Q, F, Shift or controller glyphs.
- Multipliers: "2x mønter" or "x2". Keep ASCII "x".

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, AFK, OP, XP, noob, obby, tycoon; "game pass" (Roblox's own Danish text keeps it).
- Game titles stay English: "Pet Hatch Tycoon". Danish Wikipedia keeps Roblox, Robux, Premium and avatar untranslated.
- Promo codes and their examples (FREEPETS), usernames, display names, {player}, keybinds, emoji.
- Translate in-game item, pet and rarity names, and keep each one identical everywhere: "Lucky Potion" -> "Lykkeeliksir" (Roblox's Danish terms call potions "eliksirer").
- Write æ ø å, never "ae oe aa" substitutes (except real names like "Aalborg"), and never Swedish ä/ö.

## Rendering on Roblox
- Glyph check (2026-11-08) of the font files in the local Roblox client (`content/fonts`): every Latin face, from Builder Sans and Source Sans to Luckiest Guy, Fredoka One and Press Start 2P, has æ ø å Æ Ø Å é É. Uploaded custom fonts still need checking.
- Luau `string.upper` only changes ASCII letters: "mønter" becomes "MøNTER". Store uppercase text directly ("MØNTER") or use a UTF-8-aware helper.
- TextWrapped breaks only at spaces, so long compounds ("bytteanmodning", "dagsbelønning") can't wrap; TextScaled shrinks the whole label instead. Prefer short words in buttons.
- The ring on Å rises above the font's ascent line in Luckiest Guy, Bangers, Josefin Sans, Montserrat, Roboto, Roboto Condensed and Special Elite (same font check). In a tight TextScaled label it can touch or cross the top edge; check capitalized titles ("ÅBN", "Årets event") in Studio (clipping unverified).
- Verify in Studio: set the test locale to da-dk, open every panel, and check the longest strings (rebirth confirm, come-back, group banner at 55/55) and the shortest buttons. settings.on must hold "Til".

## Mistakes machine translation makes here
- Norwegian/Swedish bleed: "Kjøp"/"Köp" -> "Køb"; "Spill" -> "Spil"; "den lysende cirklen" -> "den lysende cirkel".
- False friends: "inventar" (furniture) -> "rygsæk"; "Du må ikke ..." means "you may not", so "You must" -> "Du skal"; "eventuelt" isn't "eventually" -> "til sidst"; "Lær mere" -> "Læs mere" (Microsoft).
- "Free" read as freedom: "fri belønning" -> "gratis belønning".
- Wrong verb for Claim: "Gør krav på" (a legal claim) -> "Hent".
- Calques: "Level op!" -> "Nyt level!"; "Heldig eliksir" -> "Lykkeeliksir"; "Spillet tillader dig at ..." -> "I spillet kan du ...".
- Over-translated gaming words: "Genfødsel" -> "Rebirth"; "Kæledyr" in a pet sim -> "pets" (player usage unverified); "forbindelser" -> "venner"; in-game "oplevelse" -> "spil".
- Split compounds and missing hyphens: "top spillere" -> "topspillere"; "VIP område" -> "VIP-område"; "2x Boost" -> "2x-boost".
- English Title Case: "Daglig Belønning" -> "Daglig belønning".
- Gender guessed for inserted nouns: "Du klækkede en Legendarisk {pet}!" -> "Du klækkede: {pet} ({rarity})!".
- English genitive and commas: "Alex's pet" -> "Alex' pet"; "mønter, pets, og æg" -> "mønter, pets og æg".
- English numbers: "1,250 mønter" -> "1.250 mønter"; ".5x" -> "0,5x" (flag for game code).
- Stiff written register: "Handlingen kunne ikke fuldføres" -> "Det virkede ikke"; "samtlige" -> "alle"; "hvorledes" -> "hvordan".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Spil | Imperative; on a menu button nobody reads it as the noun "game". |
| shop.title | Butik | "Shop" also fine; pick one. |
| shop.buy | Køb | |
| reward.claim | Hent | Not "Gør krav på". "Modtag" is a stiffer alternative; "Indløs" is for codes. nb-no and sv-se use the same verb ("Hent", "Hämta"). |
| rebirth.button | Rebirth | Kept English; "Genfødsel" sounds religious. |
| rebirth.confirm | Vil du lave rebirth nu? Du mister dine mønter, men får et permanent {multiplier}x-boost. | "Vil du ...?" per Microsoft. Comma before "men". Game code should send "1,5", not "1.5". |
| coins.need_more | Ikke nok mønter! Du mangler {amount}. | Rebuilt so {amount} = 1 stays correct. |
| coins.count | Mønter: {count} | Label pattern avoids "1 mønter"; count should be "1.250". |
| egg.hatched | Du klækkede: {pet} ({rarity})! | Avoids en/et article and adjective agreement. |
| rarity.legendary | Legendarisk | Same form for en and et nouns, but still keep it out of agreement slots. |
| pet.name.dragon | Drage | Common gender: "en drage", "dragen". |
| chat.player_joined | {player} er kommet ind i spillet | "spillet", not "oplevelsen". Minecraft's Danish "{player} deltager nu i spillet" also works. |
| trade.request | {player} vil bytte med dig | |
| prompt.open_shop | Tryk på E for at åbne | 21/22. E kept. |
| pass.buy_price | Køb for {price} Robux | |
| pass.coins2x | 2x mønter | |
| pass.vip | VIP | Kept. |
| reward.daily_title | Daglig belønning | 16/18. Sentence case. |
| reward.come_back | Kom tilbage om {time}, og hent din næste belønning! | {time} moved mid-sentence so "min." never meets "!". 57/60 with "3 t. 20 min.", 53 with "3 t 20 m". |
| codes.placeholder | Indtast kode | |
| codes.invalid | Koden er ugyldig eller udløbet. | Full sentence with the definite noun, as Microsoft asks for messages. |
| social.like_reward | Giv spillet et like, og få en gratis <b>Lykkeeliksir</b>! | "et like" is everyday Danish; "Synes godt om spillet" is long and stiff. 50/55 without tags. Minecraft's Danish Potion of Luck is "Heldeliksir" (49), also fine. |
| social.group_reward | Meld dig ind i vores gruppe, og få en gratis belønning! | "gruppe", see vocabulary. 55/55, no margin. The comma joins two main clauses, so it stays in every comma style; if the label overflows, "Meld dig ind i gruppen, og få en gratis belønning!" is 50. |
| afk.warning | Du er AFK. Bevæg dig for at tjene videre! | "Flyt dig" would read as "get out of the way". |
| leaderboard.title | Topspillere | One word. "Rangliste" if the board isn't about players. |
| level.up | Nyt level! Du er nu level {level}. | Not "Level op!". |
| tutorial.sell | Gå ind i den lysende cirkel for at sælge dine pets. | No double definite. No comma before "for at". |
| inventory.full | Din rygsæk er fuld! Sælg nogle pets for at få plads. | |
| settings.music | Musik | |
| settings.on | Til | Pair with "Fra". |
| loading | Indlæser... | |
| event.ends_in | Eventet slutter om {time} | Fits only with CLDR narrow time: "2 d 5 t" -> 26/28, "12 t 30 m" -> 28. Short forms overflow ("2 dage 5 t." 30, "3 t. 20 min." 31); then use "Slutter om {time}" (22-23). "et event" is normal Danish. |
| item.op | Det her sværd er OP! | Spoken "Det her" fits the tone. |
| friends.boost | +{percent} % boost for hver ven på din server | "ven" is gender-neutral. |

## Sources
1. Microsoft Danish localization style guide (dan-dnk, PDF): https://aka.ms/danish-styleguide
2. Microsoft localization style guides index: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. CLDR plural rules (Danish): https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR JSON, Danish units (duration short and narrow forms): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/da/units.json
5. Roblox locale API (da_dk: in-game content only, not full platform): https://locale.roblox.com/v1/locales?displayValueLocale=da_dk
6. Roblox Help Center locale list (da, da-dk present): https://en.help.roblox.com/api/v2/help_center/locales.json
7. Roblox Help search, Danish, "Robux" (game passes, eliksirer, Premium-abonnement, handelsaktivitet, oplevelser): https://en.help.roblox.com/api/v2/help_center/articles/search.json?query=Robux&locale=da
8. Roblox Help search, Danish, "venner" (venneanmodninger, gruppe-/fællesskabsnavne): https://en.help.roblox.com/api/v2/help_center/articles/search.json?query=venner&locale=da
9. Roblox Help (da), "Anbefalinger og ranglister på Roblox" ("synes godt om" as a plain verb, ranglister): https://en.help.roblox.com/hc/da/articles/21416941036564
10. Roblox Help (da), EEA/UK/Switzerland terms (udviklerprodukter, game passes, eliksirer, fællesskaber, grupper, indløse, spil): https://en.help.roblox.com/hc/da/articles/52986395990932
11. Roblox locale API, in-game locus by device language (Accept-Language da-DK -> ugc `da_dk`, app `en_us`; tested 2026-11-08): https://locale.roblox.com/v1/locales/user-localization-locus-supported-locales
12. Roblox Creator Docs, in-game language switcher and Player.LocaleId: https://create.roblox.com/docs/production/localization/localize-with-scripting
13. Dansk Sprognævn, "Komma - det korte overblik" (comma between main clauses; optional comma before subclauses): https://dsn.dk/hjaelp-til-dansk/kommaoevelser/komma-det-korte-overblik/
14. Minecraft Java 26.3 Danish language file `minecraft/lang/da_dk.json` (Taske, Niveau, Heldeliksir, TIL/FRA, handel), read 2026-11-08 from Mojang's asset index
15. Roblox client font files (`content/fonts`, version-f0ea5da9412f4e35), cmap and glyph bounds read locally with fontTools 2026-11-08
16. Danish Wikipedia, Roblox (spil, spiller, Robux, Premium, avatar): https://da.wikipedia.org/wiki/Roblox
17. Roblox client chat localization (no Danish strings ship with the client): https://github.com/MaximumADHD/Roblox-Client-Tracker/blob/roblox/scripts/CoreScripts/Modules/Server/ServerChat/DefaultChatLocalization.lua
18. Friends -> Connections -> Friends rename dates, taken from the de-de guide's Roblox newsroom source (not re-fetched): https://about.roblox.com/de/newsroom/2026/04/expanding-trusted-friends
