# French (France) (fr-fr) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `fr-fr`, and this text also fills the bare `fr` column: French speakers in Belgium, Switzerland and Africa read it too (`fr-ca` has its own column) |
| Script, direction | Latin, LTR; needs é è ê ë à â î ï ô û ù ü ç œ and « » |
| Address the player as | informal "tu" (tu, ton, ta, tes, toi); never "vous" |
| Text expansion vs English | +19% over the 34 reference strings below (646 -> 770 visible characters); sentences +15-30%; one-word buttons often double ("Buy" -> "Acheter", "Shop" -> "Boutique") |
| Plural categories (CLDR) | one (0 and 1, also 1,5), many (exact millions), other |
| Model confidence | high: huge training corpus; the real risks are "vous", typography, placeholders and key letters |
| Native review before shipping | recommended |

## Audience and register
- Players are 9-16 and spread across France, Belgium, Switzerland and French-speaking Africa. Write standard French a kid anywhere reads naturally: no France-only slang ("cheaté", "abusé", "ouf", "chelou", "wesh"), no Quebec forms ("magasiner", "c'est l'fun"), no Belgian/Swiss number words (write digits).
- Always "tu". Roblox's own French store listing talks to players with tu ("Joue à des millions de jeux", "Retrouve tes amis"). Roblox's Creator Hub and Microsoft's French style guide use "vous" because they address adults; ignore that for a kids' game.
- Buttons, tabs and one-word commands: infinitive, as in French software UI: "Jouer", "Acheter", "Récupérer", "Valider", "Fermer".
- Anything that reads as a sentence to the player (toasts, tutorials, prompts, placeholders): tu imperative: "Reviens demain !", "Entre un code", "Bouge pour continuer à gagner !".
- Hype is short: "Bravo !", "Génial !", "Super !", "C'est parti !", "Nouveau record !". "Félicitations !" on every toast and "Veuillez..." read as school or bank letters.
- Prefer plain, short phrasing over formal: "Il est nécessaire de posséder davantage de pièces" -> "Pas assez de pièces !".
- "jeu" for the game, "partie" for a session or round ("rejoindre la partie"). For PvP, "éliminer" reads cleaner and kid-safer than "tuer".
- Kid-safe: no swearing, even mild ("merde", "putain"); "noob" never aimed at the player.

## Roblox and gaming vocabulary
| English | Use in fr-fr | Note |
|---|---|---|
| Robux | Robux | brand, invariable, capital R: "1 Robux", "100 Robux" |
| Premium | Roblox Plus / Premium | brand names, never translated; Roblox Plus launched 30 April 2026 and new Premium sign-ups stopped; existing members keep Premium (Roblox FR newsroom) |
| game pass | pass (m.) | Roblox Creator Hub FR: "un pass", plural "passes"; name it in game: "Pass VIP"; players also write "gamepass" |
| developer product | produit pour développeurs | Creator Hub term only; players never see it, so name the item: "Pack de 1 000 pièces" |
| experience / game | jeu (m.) | Roblox's 2026 French newsroom says "jeux"; the store listing mixes "jeux" and "expériences"; in game say "jeu" ("expérience" also means XP) |
| obby | obby (m.) | keep; "parcours d'obstacles" only when explaining |
| tycoon | tycoon (m.) | keep in titles and genre talk; never "magnat" |
| simulator | simulateur (m.) | in sentences; keep English inside game titles |
| rebirth | renaissance (f.); button "Renaître" | default: translate. Dexerto FR writes "renaissances"; players often say "rebirth" aloud, but younger kids may not know the English word and "renaître" explains the reset. "Rebirth" only if the game's glossary keeps it; never mix |
| pet | animal, pl. animaux (m.) | default; French guides (Dexerto, Gamewave) write "animaux"; irregular plural; "familier" sounds RPG; "pet(s)" is player talk, only if the game's glossary keeps it |
| egg / hatch | œuf (m.) / faire éclore | "éclore" has no object: "faire éclore un œuf"; "ouvrir un œuf" is also natural |
| coins | pièces (f.) | French guides keep "Coins" only when quoting an untranslated English UI |
| gems | gemmes (f.) | "diamants" only if the icon is a diamond |
| boost | boost (m.) | "un boost x2"; "bonus" (m.) is equally standard; pick one per game |
| multiplier | multiplicateur (m.) | write it after the noun: "Pièces x2" |
| XP | XP | "+50 XP"; avoid an article; "points d'expérience" in long text |
| level up | niveau supérieur | "Niveau 5 atteint !"; players say "level up" aloud, don't write it |
| quest | quête (f.) | "Quête du jour" |
| leaderboard | classement (m.) | "Top joueurs" also works as a title |
| AFK | AFK | keep; universal among French players, and it dodges gendered "inactif/inactive" |
| noob | noob | players use it; in UI only self-mocking, never at the player; "débutant" in neutral text |
| OP | OP | keep in flavor text ("trop OP"); "surpuissant" in neutral text |
| VIP | VIP | keep: "le pass VIP", "Zone VIP" |
| trade | échange (m.) / échanger | players say "trade", "trader"; UI says échange |
| inventory / backpack | inventaire (m.) / sac (m.) | "sac à dos" only when there is room and it matters |
| daily reward | récompense du jour | "récompense quotidienne" when 22 characters fit |
| codes | code (m.) | "Entre un code", button "Valider"; French guides keep "Redeem" only when quoting English UI |
| group | communauté (f.) | Roblox renamed Groups to Communities (Nov 2024); Creator Hub FR calls the site section "Communautés" and keeps "groupe" for creator teams: "Rejoins notre communauté" |
| like | like (m.) / liker | "Like le jeu" (kids know "Like et abonne-toi"), "Mets un like au jeu"; never "Aime le jeu" (reads "love the game"); Roblox's FR vote label (unverified) |
| favorite | favori (m.) | "Ajoute le jeu à tes favoris"; exact Roblox FR button text (unverified) |
| server | serveur (m.) | "sur ton serveur"; "serveur privé" (Creator Hub FR) |
| friends / connections | amis | Roblox FR renamed "Connexions" back to "Amis" in April 2026; trusted = "Amis de confiance" |
| shop | boutique (f.) | standard in French game UIs |

## Grammar traps in UI strings
- Plurals: one string per key, and French "one" covers 0 and 1 ("0 pièce", "1 pièce", "2 pièces"), while exact millions take "de" ("1 000 000 de pièces"). So "{count} pièces" is wrong for 0, 1 and millions. Put the noun first, label style: "Pièces : {count}", "Pièces manquantes : {amount}". Never "pièce(s)".
- {player} and "tu" have no known gender. No adjective or être-participle about them: "{player} est arrivé" -> "{player} a rejoint la partie"; "Tu es prêt ?" -> "C'est parti ?"; "Tu es inactif" -> "Tu es AFK". Avoir-participles don't agree, so "{player} a gagné !" is safe.
- Inserted nouns ({pet}, {item}) have unknown gender and may start with a vowel. No article or preposition right before a placeholder: "un {pet}" fails for "Licorne" (f.), "de {pet}" for "Ours" (d'Ours), "le {pet}" for "Aigle" (l'Aigle). Use a colon or parentheses: "Tu as obtenu : {pet} !".
- Rarity adjectives agree with the pet ("Dragon commun", "Licorne commune"). Keep {rarity} in its own slot, "({rarity})", and prefer epicene tags: Rare, Épique, Légendaire, Mythique.
- Adjectives follow the noun: "Legendary Dragon" -> "Dragon légendaire", "Golden Egg" -> "Œuf doré".
- English noun stacks become "de" phrases: "Coin Boost" -> "Boost de pièces", "Speed Potion" -> "Potion de vitesse", "Pet Egg" -> "Œuf d'animal".
- Sentence case for titles, buttons and item names: "Top Players" -> "Classement", "Lucky Potion" -> "Potion de chance". Capitals keep their accents: "ÉVÉNEMENT", "À BIENTÔT".
- Elide and contract in fixed text: "l'événement" (not "le événement"), "au niveau" (not "à le niveau"), "d'or" (not "de or").
- Tenses: présent, passé composé, futur simple. No passé simple; avoid the subjunctive (rewrite with "pour" + infinitive).

## Typography and formatting
- No-break space (U+00A0) before ? ! : ; and %, and inside « »: "Bravo !", "Prêt ?", "Pièces : 120", "+10 %". In this guide those spaces are real U+00A0; reproduce them. Don't use U+202F (narrow no-break space): Microsoft's French guide uses U+00A0 throughout, and U+202F renders narrower in Roblox fonts, so a mix looks uneven.
- Quotation marks « texte » with no-break spaces inside; never "..." around UI names.
- Apostrophe: straight ' everywhere (house choice). Microsoft's French guide prefers the curly ’ but allows straight when the developer asks; players type ' in chat and codes, and MT mixes the two. If the game's French text already uses ’, follow it; never mix in one game.
- Numbers: thousands separated by a no-break space, decimal comma: "1 250", "1,5". The game fills {count}, {amount}, {multiplier} in English format, so "1,250" (which a French reader takes as 1.25) and "1.5" appear. Flag it to the developer: format numbers per locale or drop thousands separators.
- Multipliers: lowercase x after the noun or number: "Pièces x2", "boost x{multiplier}".
- Durations: "3 h 20 min", "2 j 5 h", "45 s", no-break space between number and unit, no periods; "m" means meters. If {time} arrives as "3h 20m", flag it.
- Ordinals: "1er" / "1re", "2e", "3e"; never "2ème" or "2nd".
- Ellipsis: no space before it; mirror the source ("Chargement...").
- Times and dates: 24-hour clock ("14 h 30" or "14:30"), "8 novembre", lowercase months and days.
- Keyboard keys: E, R, T, Y, U, I, O, P, S, D, F, G, H, J, K, L, X, C, V, B, N sit in the same place on AZERTY: keep them ("Appuie sur E"). A, Q, W, Z and M do not. Roblox KeyCodes are QWERTY positions, so on a French or Belgian AZERTY keyboard KeyCode.Q is the key labeled A. Never write "Q", "W", "A", "Z", "M" or "WASD" as a literal: ask the developer for a {key} filled by UserInputService:GetStringForKeyCode, or write "touches de déplacement". Swiss keyboards are QWERTZ, so don't hard-code "ZQSD" either.
- Number keys: on AZERTY the top-row digits are shifted, and GetStringForKeyCode returns "&" and "é" for KeyCode.One and Two (Roblox staff, DevForum). Write the digit ("Appuie sur 1"); French players know the key.

## Do not translate / keep as is
- Roblox, Robux, Roblox Plus, Premium, Roblox Studio, and the game title ("Pet Hatch Tycoon") unless the developer supplies a French title.
- Usernames and display names, promo codes (FREEPETS: players type them exactly), keybind letters, {params}, rich text tags.
- Gamer words players keep: AFK, OP, VIP, XP, noob, obby, tycoon. They are masculine: "le boost", "le pass", "un obby".
- Do translate item, pet, pass and rarity names, and reuse each translation in every string ("Dragon" on the card = "Dragon" in the toast).

## Rendering on Roblox
- Latin script, no shaping, words separated by spaces, so wrapping works.
- French needs Latin-1 letters plus œ/Œ (U+0153/U+0152) and « ». Measured in Studio 2026-11-08 with TextService:GetTextBoundsAsync on 12 fonts (BuilderSans, BuilderSansBold, GothamBold, FredokaOne, LuckiestGuy, SourceSansBold, Arial, Cartoon, Bangers, Ubuntu, Michroma, Arcade): œ Œ « » É À Ê ç Ç ’ each get their own width, not the missing-glyph width, so they render (from the font or a fallback, unverified which). Arcade is monospace, so the test proves nothing there: look at pixel and decorative fonts.
- Accented capitals (É, À, Ê) are taller: in tight TextScaled boxes check they are not clipped at the top.
- string.upper and string.lower only handle ASCII: "échalote" becomes "éCHALOTE". If code uppercases titles, write the uppercase form in the translation or ask for UTF-8-aware conversion.
- Accented letters are 2 bytes: code that truncates with string.sub or counts with # can split a letter into a broken glyph; utf8.len and utf8.offset are safe.
- U+00A0 measured in Studio 2026-11-08 on the same 12 fonts: as wide as a normal space, and it holds when wrapping: "Super bravo !" in a box just wider than "Super bravo" breaks before "bravo !" instead of leaving "!" alone on line 2.

## Mistakes machine translation makes here
- Vous register: "Revenez dans {time} pour votre récompense" -> "Reviens dans {time} pour ta prochaine récompense !"
- tu and vous mixed across strings of one game -> tu everywhere.
- "Claim" as "Réclamer" (= complain, demand) -> "Récupérer".
- "Like the game" as "Aime le jeu" -> "Like le jeu" or "Mets un like au jeu".
- English Title Case: "Récompense Du Jour" -> "Récompense du jour".
- Missing no-break spaces: "Bravo!", "10%" -> "Bravo !", "10 %".
- English word order: "2x Pièces", "Légendaire Dragon" -> "Pièces x2", "Dragon légendaire".
- "éclore" used with an object: "Tu as éclos un dragon" -> "Tu as fait éclore un œuf" / "Tu as obtenu : Dragon".
- Gendered player text: "{player} est parti" -> "{player} a quitté la partie".
- "experience" as "expérience" for the game -> "jeu".
- Outdated Roblox terms: "Connexions" -> "Amis"; "groupe" -> "communauté".
- France-only slang or Quebec forms: "Cette épée est cheatée !", "magasiner" -> "Cette épée est trop OP !", "acheter".
- English durations kept: "3h 20m" -> "3 h 20 min".

## Reference translations
Lengths in notes count visible text without {params} or tags, as `i18n.py lint` does; where it matters, the length with a typical value filled in follows.

| key | translation | note |
|---|---|---|
| menu.play | Jouer | infinitive button |
| shop.title | Boutique | |
| shop.buy | Acheter | |
| reward.claim | Récupérer | not "Réclamer" |
| rebirth.button | Renaître | "Rebirth" acceptable only if the whole game keeps the English term |
| rebirth.confirm | Renaître maintenant ? Tu perdras tes pièces, mais tu gagneras un boost permanent x{multiplier}. | {multiplier} should arrive as "1,5", not "1.5" |
| coins.need_more | Oups ! Pièces manquantes : {amount} | noun before the number dodges "1 pièces"; "Oups" added for tone |
| coins.count | Pièces : {count} | label pattern, correct for 0, 1 and millions |
| egg.hatched | Tu as obtenu : {pet} ({rarity}) ! | no article before {pet}, rarity in its own slot to dodge agreement |
| rarity.legendary | Légendaire | epicene |
| pet.name.dragon | Dragon | same word in French; masculine |
| chat.player_joined | {player} a rejoint la partie | avoir-participle: no gender agreement |
| trade.request | {player} te propose un échange | |
| prompt.open_shop | E pour ouvrir | "Appuie sur E pour ouvrir" is 24 > 22; E is the same key on AZERTY |
| pass.buy_price | Payer {price} Robux | 17 at "1 000"; "Acheter pour {price} Robux" is more literal but fits only up to 3-digit prices (22 at 499, 24 at 1 000) |
| pass.coins2x | Pièces x2 | |
| pass.vip | VIP | kept |
| reward.daily_title | Récompense du jour | exactly 18 |
| reward.come_back | Reviens dans {time} pour ta prochaine récompense ! | {time} must read "3 h 20 min" |
| codes.placeholder | Entre un code | |
| codes.invalid | Ce code n'est pas valide ou a expiré. | |
| social.like_reward | Like le jeu : <b>Potion de chance</b> offerte ! | 40; French promo style ("1 mois offert"); "offerte" = free; "Mets un like au jeu : ..." (48) also fits |
| social.group_reward | Rejoins notre communauté et débloque un cadeau ! | Roblox calls groups communities; "cadeau" carries "free" |
| afk.warning | Tu es AFK. Bouge pour continuer à gagner ! | AFK kept |
| leaderboard.title | Classement | "Top joueurs" also fits |
| level.up | Niveau supérieur ! Tu es au niveau {level}. | |
| tutorial.sell | Entre dans le cercle lumineux pour vendre tes animaux. | |
| inventory.full | Sac plein ! Vends des animaux pour faire de la place. | "Ton sac est plein !..." is 61 > 60 |
| settings.music | Musique | |
| settings.on | Oui | "Activé" is 6 > 5; pair with "Non"; "ON"/"OFF" fit but read as English |
| loading | Chargement... | |
| event.ends_in | Événement : fin dans {time} | 21 + {time}: 28 with "2 j 5 h", 31 with "3 h 20 min"; if the banner overflows, "Fin dans {time}" |
| item.op | Cette épée est trop OP ! | OP kept; "cheatée" is France-only slang |
| friends.boost | +{percent} % de boost par ami sur ton serveur | no-break space before % |

## Sources
1. Microsoft French (France) localization style guide (PDF): https://aka.ms/french-france-styleguide
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox newsroom (FR), Connexions renamed to Amis: https://about.roblox.com/fr/newsroom/2026/04/expanding-trusted-friends
4. Roblox app listing in French (Roblox's own copy, tu register): https://apps.apple.com/fr/app/roblox/id431946152
5. Roblox Creator Hub FR, passes: https://create.roblox.com/docs/fr-fr/production/monetization/passes
6. Roblox Creator Hub FR, game passes: https://create.roblox.com/docs/fr-fr/production/monetization/game-passes
7. Roblox Creator Hub FR, private servers: https://create.roblox.com/docs/fr-fr/production/monetization/private-servers
8. Roblox automatic translation languages: https://create.roblox.com/docs/production/localization/automatic-translations
9. DevForum, Introducing Roblox Communities: https://devforum.roblox.com/t/introducing-roblox-communities/3268307
10. Roblox newsroom (FR), Roblox Plus launch and end of new Premium sign-ups: https://about.roblox.com/fr/newsroom/2026/04/introducing-roblox-plus-subscription
11. Gamewave, Pet Simulator X codes (FR player-facing wording): https://gamewave.fr/roblox/roblox-codes-pet-simulator-x/
12. Dexerto FR, Steal an Egg codes: https://www.dexerto.fr/roblox/codes-steal-an-egg-1656311/
13. MGG (millenium.org), Blade Ball codes: https://www.millenium.org/news/412299.html
14. DevForum, multilingual text manipulation (string.upper and accents): https://devforum.roblox.com/t/multilingual-text-manipulation/3892642
15. Roblox Creator Hub FR, groups (teams) vs the "Communautés" section: https://create.roblox.com/docs/fr-fr/projects/groups
16. DevForum, AZERTY keyboard binding issue (staff reply: KeyCodes are QWERTY positions): https://devforum.roblox.com/t/azerty-keyboard-binding-issue/4070475
