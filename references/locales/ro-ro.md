# Romanian (ro-ro) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `ro-ro` (the only Romanian locale Roblox lists, so it serves Romania and Moldova alike; a bare `ro` column adds nothing) |
| Script, direction | Latin with ă â î ș ț, LTR; ș ț always comma-below (U+0219, U+021B; capitals U+0218, U+021A), never cedilla ş ţ |
| Address the player as | informal singular "tu" everywhere; never "dumneavoastră", "dvs." or 2nd person plural forms ("Apăsați") |
| Text expansion vs English | about +15-30% for sentences (this guide's reference set averages +16% after tightening); short labels +25-130% ("Play" -> "Joacă", "Buy" -> "Cumpără", "Daily Reward" -> "Recompensă zilnică") |
| Plural categories (CLDR) | cardinal: one, few, other (few = 0, 2-19, anything ending in 01-19 above 100, and all decimals; other = 20-99, 100, 120...); ordinal: one, other |
| Model confidence | medium -- grammar is well covered, but models slip into the formal register, cedilla letters and broken number agreement ("25 monede"); kid gamer slang is barely documented |
| Native review before shipping | recommended |

## Audience and register
- Roblox's own app is not in Romanian: the Roblox locale API (checked 2026-11-08) marks `ro_ro` as enabled for in-game content only, not for the app UI or sign-up. Romanian kids read Roblox itself in English, so platform words (Robux, Premium, Friends, Marketplace) reach them in English first. How a Romanian or Moldovan player gets `Player.LocaleId` = `ro-ro` is unverified: with `ro_ro` off for the app UI it is likely missing from the account language menu (perhaps reached only via device language). The Player Emulator only proves the column renders.
- Roblox does not auto-translate Romanian: without a `ro-ro` column, players see the source text.
- Use "tu" in every string: singular imperative on buttons ("Joacă", "Cumpără", "Apasă E"), 2nd person singular verbs in sentences ("Primești", "Ești AFK"). Roblox's Romanian Play Store listing ("Joacă", "Descoperă", "prietenii tăi") and Minecraft's Romanian files ("Alege o lume", "Apasă %s") both use tu.
- Microsoft's Romanian guide uses the plural imperative for its software, but it says young users prefer the singular and uses an informal tone for Copilot prompts. A kids' game follows the young users: "Cumpără", never "Cumpărați".
- Never the long infinitive on buttons ("Cumpărare", "Revendicare"); Microsoft dropped it as old style. Panel titles may be nouns: "Magazin", "Setări", "Recompensă zilnică".
- Continuous states use the reflexive form, as Microsoft prescribes: "Se încarcă…", "Se conectează…".
- Hype that sounds natural: "Super!", "Bravo!", "Felicitări!", "Nivel nou!", "Hai!", "Nu rata!". Stiff or adult: "Vă rugăm", "Doriți să…?", "efectuați", "în vederea", "utilizatorul". Ask with "Vrei să…?".
- Don't translate every "your" (Microsoft calls it over-localization): "Rucsacul e plin!", not "Rucsacul tău este plin!". The short "e" for "este" keeps toasts casual.
- Kid-safe slang only (AFK, OP, noob in jokes). No insults or crude words. Whether Romanian kids say rebirth, trade, pet-uri or game pass in English is unchecked against player sources: UI uses the Romanian term from the table, English slang only in flavor text.

## Roblox and gaming vocabulary
| English | Romanian | note |
|---|---|---|
| Robux | Robux | Latin, no article, no plural ending: "{price} Robux". |
| Premium | Roblox Plus / Premium | Roblox's Romanian listing (2026-11-08) advertises "Roblox Plus"; use what the current English UI shows. |
| game pass | game pass (unverified); in UI name the item | Roblox UI is English here; the shop shows "VIP", "Monede x2". |
| developer product | produs; ofertă | players never see the term. |
| experience / game | joc, jocuri | the listing uses both "jocuri" and "experiențe"; "experiență" also reads as XP, so say "joc". |
| obby | obby; parkour (unverified) | |
| tycoon | Tycoon (Latin) | the listing writes "în Tycoons". |
| simulator | simulator, pl. simulatoare | as in the listing. |
| rebirth | renaștere; button "Renaște" | players may say "rebirth" (unverified). |
| pet | animăluț, pl. animăluțe (neuter) | "animal de companie" is long and adult. "pet" in UI also reads as PET, the plastic bottle (DOOM3: PET, pl. PET-uri); "pet-uri" in player chat is likely but unverified. |
| egg / hatch | ou, pl. ouă / "Deschide oul", "a ieșit din ou" | never "a cloci" (to brood) or "a ecloza" (biology). |
| coins | monede (feminine: o monedă) | |
| gems | diamante; cristale | match the icon. |
| boost | bonus, pl. bonusuri | DOOM3 entry; "boost" in chat (unverified). |
| multiplier | multiplicator; write "x2" | DOOM3: masculine for the number sense. |
| XP | XP; puncte de experiență | Minecraft: "Nivel de experiență". Pick one per game. |
| level up | nivel nou | "Nivel nou! Ești la nivelul 5." |
| quest | misiune, pl. misiuni | listing: "misiuni epice". |
| leaderboard | clasament; "Top jucători" | |
| AFK | AFK | Latin capitals: "Ești AFK". |
| noob | începător (UI); noob (jokes) | "noob" is not in DOOM3; player spelling unverified. |
| OP | OP (unverified); super puternic | |
| VIP | VIP | DOOM3: plural VIP-uri; "server VIP", not "VIP server". |
| trade | schimb; "a face schimb" | "trade" in chat (unverified). |
| inventory / backpack | inventar / rucsac | Minecraft: "inventarul". |
| daily reward | recompensă zilnică | "premiu zilnic" when short. |
| codes | coduri; "Introdu codul" | redeem = "Folosește codul". |
| group | grup, pl. grupuri | listing: "Alătură-te unui Grup". |
| like / favorite | like (DOOM3, pl. like-uri): "Dă like" / "Adaugă la favorite" | |
| server | server, pl. servere; "pe server" | listing: "servere private"; Minecraft: "Intră pe server". |
| friends | prieteni | Roblox renamed Connections back to Friends in April 2026; the listing says "prietenii". Never "conexiuni". |

## Grammar traps in UI strings
- Number + noun has three shapes: 1 -> "o monedă"; 2-19 -> "5 monede"; 20 and up -> "20 de monede" (but "101 monede", "120 de monede"). One string per key, so "{count} monede" is wrong at 1 and at 20+.
  - Bad: "Ai {count} monede". Good: "Monede: {count}", "Îți mai trebuie monede: {amount}!".
  - Units and currency names on price labels are safe without "de": "{price} Robux", "{percent} %", "x{multiplier}".
- Adjectives follow the noun and agree in gender: "dragon legendar", "pisică legendară". Never "{rarity} {pet}" (English order) or "{pet} {rarity}" (agreement breaks for feminine pets). Use a fixed neuter noun: "un animăluț {rarity}: {pet}", with rarity labels written in the masculine singular ("Legendar", "Rar").
  - Romanian lowercases adjectives mid-sentence, so "un animăluț Legendar" reads as a tier label: acceptable, but if the game can send a lowercase rarity key, "un animăluț legendar" is cleaner.
- Past tense (perfect compus) is gender-neutral: "{player} a intrat în joc", "{player} a câștigat!". Adjectives about a player are not: "Ești pregătit?" excludes girls -> "Ești gata?" ("gata" never changes).
- "gratis" never changes; "gratuit" does ("un premiu gratuit", "o poțiune gratuită"). Prefer "gratis" next to inserted items.
- The definite article is a suffix and cannot attach to a placeholder: "{pet}-ul" breaks. Put inserted names after a colon or behind a noun: "Ai primit: {pet}", "animăluțul {pet}".
- Loanword endings follow DOOM3 word by word: a hyphen after a silent final letter or an acronym ("like-uri", "VIP-uri", "AFK-ul"), none otherwise ("serverul", "chaturi"). Robux and Roblox take none: "pe Roblox".
- Possession with a username: "lui {player}" works for any name ("rucsacul lui {player}"); don't decline a username.
- Negative imperative is "nu" + infinitive: "Nu pleca!", "Nu uita!", never "Nu pleacă!".
- Clitics join with a hyphen: "Mișcă-te", "Alătură-te", "să-ți", "Dă-i like".
- Time from now takes "peste", not "în": "Revino peste 3 h", "Se termină peste 2 z".
- Ordinals ("al 5-lea nivel") need agreement; write "nivelul {level}".
- English noun stacks become "de"/"pentru" phrases: "Coin Boost" -> "bonus de monede", "Pet Storage" -> "spațiu pentru animăluțe".
- Sentence case for titles and buttons ("Recompensă zilnică", "Top jucători"); Microsoft calls English title case an error.

## Typography and formatting
- ș ț Ș Ț are comma-below letters (U+0219, U+021B, U+0218, U+021A). The cedilla forms ş ţ (U+015F, U+0163) are Turkish/legacy and count as typos -- even Microsoft's Romanian guide slips one ("încercaţi"). Minecraft's Romanian file uses comma-below only.
- Post-1993 spelling: "â" inside words, "î" at the start and end ("înapoi", "câștigi", "coborî"); "sunt", "România". Prefixed words keep î: "reîncarcă".
- No space before ! ? : ; and one space after: "Bravo! Ai câștigat."
- Quotes: „…” (U+201E opening, U+201D closing), as CLDR and Microsoft say: „Poțiune de noroc”. Not "…" English pairs; «» only inside quotes.
- Dashes: en dash with spaces " – " as a separator (Microsoft); hyphen without spaces for clitics and loanword endings.
- Numbers (CLDR): decimal comma, dot for thousands, grouping from 4 digits: "1.250", "1,5". The canonical {count} arrives as "1,250", which a Romanian reads as 1.25 -- flag it to the developer. Same for "1.5" multipliers.
- Percent: non-breaking space before % ("25 %", U+00A0), per CLDR and Microsoft. Kids' games often write "25%"; it is informal, not wrong, so keep the space but don't flag a missing one as an error.
- Multiplier: Latin x before the number: "x2", "Monede x2".
- Durations (CLDR narrow): "2 z 5 h", "3 h 20 m"; Microsoft writes minutes as "min" ("3 h 20 min"). English "3h 20m" is passable (same letters); "2d 5h" is not -- day is "zi", so flag the "d" to the developer.
- Ellipsis: the single character … with no space before ("Se încarcă…"), as in Minecraft's Romanian file.
- Exclamation marks: Microsoft limits them in software; in a game, keep the source's count, never add one, and keep error messages calm ("Codul nu e valid sau a expirat.").
- Keys stay Latin: "Apasă E". Space bar: "Spațiu" (Microsoft: "Tasta Spațiu"); arrows: "Săgeată în sus".

## Do not translate / keep as is
- Roblox, Robux, Roblox Plus, Premium, Roblox Studio, Marketplace: Latin, no article, no declension ("pe Roblox", never "Roblox-ul"). Microsoft treats untranslated product names as articleless proper nouns.
- Game titles ("Pet Hatch Tycoon"): keep English; players search for the English title.
- Usernames and display names: never translate, decline or add an article.
- Promo codes ("FREEPETS"): exactly as given, same case; translate only the text around them.
- Key names (E, Q, Shift, Ctrl) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Poțiune de noroc", Minecraft's name for the luck potion); keep invented brand-like names only if the game treats them as brands.
- Gamer acronyms stay as typed: AFK, OP, XP, VIP. Don't respell English words Romanian-style ("nub", "trăid").

## Rendering on Roblox
- Glyph check (2026-11-08) of the font files in the local Roblox client (`content/fonts`): full Romanian set (ă â î ș ț in both cases, „ ”, …, en dash) in Builder Sans, Builder Extended, Builder Mono, Arimo, Montserrat, Nunito, Roboto (incl. Condensed, Mono), Source Sans Pro, Oswald, Ubuntu, Merriweather, Titillium Web, Bangers, Amatic SC, Josefin Sans, Kalam, Patrick Hand, Sarpanch, Guru, Grenze Gotisch, Jura, Zekton.
- No comma-below ș ț: Fredoka One, Luckiest Guy, Denk One, Permanent Marker, Creepster, Press Start 2P, Comic Neue Angular, Special Elite, Fondamento, Inconsolata, Roman Antique, Accanthis, Balthazar, Highway Gothic; Indie Flower lacks ț. Fredoka One, Denk One, Creepster, Permanent Marker, Roman Antique, Accanthis, Balthazar and Highway Gothic also lack ă.
- Luckiest Guy, Press Start 2P, Comic Neue, Special Elite and Fondamento do have the cedilla ş ţ. Never switch to cedilla to make a font work -- change the font.
- Missing glyphs fall back to another font, so one word mixes two faces ("Mișcă" with ș in the fallback). Which fallback Roblox uses today is unverified.
- Recommendation: for the ro locale, use Bangers (cartoon), Builder Sans, Montserrat or Nunito instead of Fredoka One or Luckiest Guy.
- Fredoka One, Sarpanch, Balthazar and Roman Antique lack the non-breaking space (U+00A0) used in "25 %"; check how it renders, or use a plain space in those faces.
- Ă Â Î carry marks above the cap height and Ș Ț a comma below the baseline: check that TextScaled labels clip neither.
- Verify in Studio: Player Emulator set to Romanian; open every panel with the longest strings ("Recompensă zilnică" is 18/18); check ă ș ț Ș Ț and numbers in each font face.

## Mistakes machine translation makes here
- Cedilla letters: "Câştigă", "Poţiune" -> "Câștigă", "Poțiune".
- Formal register: "Apăsați E pentru a deschide" -> "Apasă E ca să deschizi".
- Long-infinitive buttons: "Cumpărare", "Revendicare" -> "Cumpără", "Primește".
- "Claim" as "Revendică" (core sense: claiming a right or property back; reads stiff to kids) -> "Primește" (or "Colectează").
- "Crează" -> "Creează" (Roblox's own Romanian listing writes "CREAZĂ"; Microsoft lists "creează").
- Number agreement: "Ai 25 monede", "1 monede" -> "Monede: 25".
- English adjective order: "Legendar dragon" -> "dragon legendar".
- "experience" as experiență: "Cea mai tare experiență" -> "Cel mai tare joc".
- "hatch" as "clocește" -> "Deschide oul" / "a ieșit din ou".
- "invalid" -> "nevalid" or "nu e valid" (Microsoft uses "nevalid"; "invalid" also means a disabled person).
- "in {time}" as "în {time}" -> "peste {time}".
- Over-translated "your": "Rucsacul tău este plin" -> "Rucsacul e plin!".
- Old spelling: "sînt", "cîștigi" -> "sunt", "câștigi".
- Title case: "Recompensă Zilnică" -> "Recompensă zilnică".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Joacă | singular imperative, as in Roblox's listing |
| shop.title | Magazin | |
| shop.buy | Cumpără | |
| reward.claim | Primește | "Colectează" (10/10) also fine, pick one per game; "Revendică" is understood but stiff |
| rebirth.button | Renaște | imperative button; noun "Renaștere" (9) for the panel title |
| rebirth.confirm | Vrei să renaști acum? Pierzi monedele, dar primești un bonus permanent x{multiplier}. | x before the number; "1.5" should arrive as "1,5" |
| coins.need_more | Îți mai trebuie monede: {amount}! | colon avoids "1 monede" and "25 monede"; "trebuie" fits singular and plural |
| coins.count | Monede: {count} | "1,250" should be "1.250" for Romanian -- code issue |
| egg.hatched | Ai primit un animăluț {rarity}: {pet}! | rarity agrees with neuter "animăluț"; 39/40 with Legendar/Dragon, over with longer words ("Neobișnuit" -> 41): then "Animăluț {rarity}: {pet}!" |
| rarity.legendary | Legendar | masculine singular, agrees with "animăluț"; capitalized as a tier name |
| pet.name.dragon | Dragon | same as English, so mark it keep:true; "Balaur" is the folk-tale monster |
| chat.player_joined | {player} a intrat în joc | Minecraft's wording; perfect compus is gender-neutral |
| trade.request | {player} vrea să facă schimb cu tine | |
| prompt.open_shop | Apasă E ca să deschizi | Latin E; 22/22. Minecraft's "Apasă %s pentru a ..." pattern gives "Apasă E pentru a deschide" (26), too long; "ca să" is the casual equivalent. Fallback "Deschide (E)" |
| pass.buy_price | Cumpără: {price} Robux | price-label style needs no "de" at 20+; "Cumpără cu {price} Robux" would need "cu 100 de Robux" |
| pass.coins2x | Monede x2 | |
| pass.vip | VIP | kept; mark keep:true |
| reward.daily_title | Recompensă zilnică | 18/18; fallback "Premiu zilnic" |
| reward.come_back | Revino peste {time} pentru următoarea recompensă! | "peste", not "în"; 53/60 with "3 h 20 min" |
| codes.placeholder | Introdu codul | |
| codes.invalid | Codul nu e valid sau a expirat. | not "invalid" |
| social.like_reward | Dă like și primești gratis o <b>Poțiune de noroc</b>! | 53 with tags; Minecraft's potion name; "gratis" never agrees |
| social.group_reward | Intră în grupul nostru pentru o recompensă gratis! | |
| afk.warning | Ești AFK. Mișcă-te și câștigi în continuare! | 44/45; one "!" as in the source |
| leaderboard.title | Top jucători | "Clasament" also fine |
| level.up | Nivel nou! Acum ești la nivelul {level}. | cardinal after the noun, no ordinal |
| tutorial.sell | Intră în cercul strălucitor ca să-ți vinzi animăluțele. | |
| inventory.full | Rucsacul e plin! Vinde animăluțe ca să faci loc. | "your" dropped |
| settings.music | Muzică | |
| settings.on | Da | Minecraft's on/off pair is "Da"/"Nu"; "Pornit" is 6/5, and "Activ" fits but its Off partner "Inactiv" (7) would not |
| loading | Se încarcă… | reflexive for a running state; single ellipsis character |
| event.ends_in | Se termină peste {time} | 24/28 with "2 z 5 h"; "Evenimentul se termină peste {time}" is 36 |
| item.op | Sabia asta e OP! | "OP" usage unverified; "Sabia asta e super puternică!" if unsure |
| friends.boost | +{percent} % bonus pentru fiecare prieten de pe server | U+00A0 between {percent} and % |

## Sources
1. Microsoft Romanian localization style guide (PDF, via https://aka.ms/romanian-styleguide): https://download.microsoft.com/download/9/c/d/9cd86a60-685a-477f-9286-a610addd10e8/ron-rou-StyleGuide.pdf
2. CLDR plural and ordinal rules (ro): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-core/supplemental/plurals.json and .../supplemental/ordinals.json
3. CLDR JSON, Romanian number symbols, percent format and minimum grouping: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/ro/numbers.json
4. CLDR JSON, Romanian duration units: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-units-full/main/ro/units.json
5. CLDR JSON, Romanian quotation marks: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-misc-full/main/ro/delimiters.json
6. Roblox locale API (ro_ro: in-game content only, no app UI): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
7. DevForum, "Friends Are Back!" (Connections -> Friends, April 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
8. Roblox on Google Play, Romanian listing (tu register, jocuri/experiențe, prieteni, Grup, Roblox Plus, servere private, "CREAZĂ"): https://play.google.com/store/apps/details?id=com.roblox.client&hl=ro&gl=RO
9. Romanian Wikipedia, Roblox (Robux as "monede", "de" with large numbers): https://ro.wikipedia.org/wiki/Roblox
10. Minecraft Java Edition Romanian language file `minecraft/lang/ro_ro.json` (assets index 32, read from a local install): "a intrat în joc", "Apasă %s pentru a ...", "Poțiune de noroc", Da/Nu toggles, "Se încarcă", "Săgeată sus", comma-below only (checked again 2026-11-08).
11. dexonline, DOOM3 entries for like, VIP, PET, bonus, multiplicator, chat, gratis (noob absent): https://dexonline.ro/definitie/like (same pattern for the others)
12. Roblox client font files (`content/fonts`, client version-f0ea5da9412f4e35), cmap glyph check run locally 2026-11-08.
