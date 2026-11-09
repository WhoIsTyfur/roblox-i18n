# French (Canada) (fr-ca) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `fr-ca` only. Never write Quebec text into the bare `fr` column: that column serves France and every unlisted French region, and a Quebec player falls back to it only when `fr-ca` is missing |
| Script, direction | Latin, LTR |
| Address the player as | informal "tu" everywhere; never "vous" (Microsoft fr-CA software uses "vous"; a kids' game does not) |
| Text expansion vs English | about +15-30% (the reference set below runs +22%); one-word buttons can nearly double ("Claim" -> "Récupérer") |
| Plural categories (CLDR) | one (0 and 1, also 1,5), many (exact millions: "1 000 000 de pièces"), other |
| Model confidence | medium -- the French is solid, but models drift to France norms: spacing before ! ?, France slang, "shopping", AZERTY keys |
| Native review before shipping | recommended, by a Quebec reviewer (not a France one) |

## Audience and register
- Players are francophone Canadians, mostly in Quebec, aged 9-16. Write standard Quebec French: the vocabulary the OQLF accepts, spelled and spaced the Quebec way. No joual or heavy street slang in UI ("pantoute", "toé", "char"), and no France-only slang ("c'est ouf", "kiffer", "grave cool", "mec").
- "tu" plus the imperative for instructions, toasts and tutorials: "Rejoins notre communauté", "Vends tes animaux", "Reviens demain". Short buttons use the infinitive or a noun, as in French software: "Jouer", "Acheter", "Boutique". Never mix "tu" and "vous" in one game.
- Hype sounds natural with short standard words: "Bravo!", "Génial!", "Super!", "Wow!". At most one "!" per string; Microsoft's fr-CA guide warns against copying every English exclamation mark.
- Prefer gender-neutral phrasing (Microsoft fr-CA inclusive-language rules): plural nouns, epicene adjectives, impersonal turns. House rule: no abbreviated doublets like "ami·e" or "prêt(e)" in UI.
- Avoid adjectives about the player, since "tu" has no visible gender: "Tu es prêt?" -> "C'est parti?"; "Tu es inactif" -> "Tu es AFK".

## Roblox and gaming vocabulary
| English | fr-ca | note |
|---|---|---|
| Robux | Robux | invariable, capitalized: "100 Robux"; Roblox French docs: "Acheter des Robux" |
| game pass | pass (m.), pl. passes | Roblox French docs: "un pass", "Créer un pass", "des passes"; in game, "Pass VIP" |
| developer product | produit | players never see the term; name the item itself |
| experience / game | jeu | Roblox's French pages also say "expérience"; inside a game, "jeu" is what kids say |
| obby | obby, parcours d'obstacles | keep "obby" in titles; "parcours" in tutorial text |
| tycoon / simulator | tycoon / simulateur | keep "Tycoon" when it is part of the game title |
| rebirth | renaissance (n.), Renaître (button) | "Renaissances : 3" for a counter |
| pet | animal (pl. animaux), familier | not "mascotte" (in Quebec that is a costumed team mascot) |
| egg / hatch | œuf / faire éclore, éclosion | keep the œ ligature; Builder Sans has it |
| coins | pièces | not "coins" (a "coin" is a corner) and not "monnaie" (that is change) |
| gems | gemmes | "diamants" only if the icon is a diamond |
| boost / multiplier | bonus / multiplicateur | "x2" goes after the noun: "Pièces x2" |
| XP / level up | XP / Niveau supérieur!, monter de niveau | "+50 XP" stays |
| quest | quête | |
| leaderboard | classement, tableau de classement | OQLF rejects the calque "tableau des meneurs" |
| AFK | AFK | keep; it also avoids the gendered "inactif/inactive" |
| noob | débutant | "noob" only in jokey flavor text; "néophyte" is too bookish for kids |
| OP | surpuissant, trop fort | "OP" is understood but keep it out of buttons |
| VIP / Premium | VIP / Premium | never translate |
| trade | échange (n.), échanger (v.) | "Demande d'échange" |
| inventory / backpack | inventaire / sac (à dos) | "sac" when space is short |
| daily reward | récompense du jour, récompense quotidienne | |
| codes | codes, code promo | |
| group | communauté (f.) | Roblox renamed player-facing Groups to Communities (Nov 2024); its French docs call that section "Communautés" and keep "groupe" only for creator teams: "Rejoins notre communauté" |
| like / favorite | aimer, un J'aime / favori, ajouter aux favoris | "Aime le jeu" follows Quebec social-media usage ("Aimez notre page"); Roblox's exact French labels unverified |
| server | serveur | "sur le serveur", not "dans le serveur" |
| friends | amis | Roblox French UI went back from "Connexions" to "Amis" (and "Amis de confiance") in April 2026 |
| chat | chat (m.), discuter (v.) | Roblox's French pages call the feature "chat"; OQLF discourages "chat"/"tchat" for "clavardage", which is correct but reads official to kids. Verb: "discuter" |
| shop / shopping | boutique / magasiner, magasinage | never "faire du shopping" |
| email / weekend | courriel / fin de semaine | never "e-mail", "mail", "week-end" |

No separate fr-CA Roblox app text was found (unverified): Quebec players likely see the same French platform
labels as France, so platform terms follow Roblox's French wording, with Quebec typography. Which English
words Quebec kids keep (pets, tycoon, noob, OP, boost) is unverified: no Quebec Roblox wiki or forum turned up.

## Grammar traps in UI strings
- **Plurals with {count}.** CLDR puts 0 and 1 in "one": "0 pièce", "1 pièce", "2 pièces"; exact millions take "de": "1 000 000 de pièces". With one string per key, never "pièce(s)". Safe patterns: label then colon ("Pièces : {count}"), or a pronoun that hides the noun ("Il en manque {amount}.").
- **{player} and gender.** "être" past participles and adjectives agree with the player, whose gender is unknown: "{player} est arrivé" is wrong half the time. Use "avoir" verbs: "{player} a rejoint la partie", "{player} a quitté la partie", "{player} a gagné!".
- **Inserted nouns and articles.** Items and pets have gender: "un Dragon", "une Licorne". With {pet} the article must go: "Nouvel animal {rarity} : {pet}!" not "Tu as eu un {pet}!".
- **Rarity agreement.** Rarity follows its noun and agrees with it: "Dragon légendaire", never "Légendaire Dragon". Put {rarity} after the fixed masculine noun "animal", then the pet: "Nouvel animal {rarity} : {pet}!". Then the usual masculine set fits every pet: Commun, Peu commun, Rare, Épique, Légendaire, Mythique. Never "{pet} {rarity}": "Licorne Commun" is wrong and one key cannot serve both genders.
- **Elision before names.** "de" and "que" elide before a vowel: "le sac de Max" but "le sac d'Alex". Never write "de {player}" or "que {player}"; put the name first: "{player} a gagné l'obby", not "Victoire de {player}".
- **Word order.** "{player} wants to trade with you" -> "{player} veut échanger avec toi" (object pronoun "toi" after "avec"); "Event ends in {time}" -> "Fin de l'événement : {time}".
- **Capitalization.** Sentence case for titles, buttons and item names: "Récompense du jour", "Potion de chance", never "Récompense Du Jour". Days and months are lowercase: "lundi", "novembre".
- **Accents on capitals.** Keep accents on capital letters: "ÉVÉNEMENT", "À BIENTÔT", never "EVENEMENT". The Académie française gives accents full spelling value on capitals too.
- **Spelling.** "événement" (traditional) and "évènement" (1990 reform) are both correct; this guide uses "événement". Never mix them in one game.

## Typography and formatting
Every space in this file before a French colon, percent or dollar sign, and inside French numbers and
durations, is a no-break space (U+00A0). Copy them as is.
- **No space before ! ? ;** -- unlike France: "Bravo!", "Prêt à jouer?". France style "Bravo !" is wrong here.
- **No-break space before the colon**, normal space after: "Pièces : 250".
- **Quotes:** « » with a no-break space inside: « Potion de chance ». No quotes around button names (Microsoft fr-CA): "Appuie sur Acheter", not « Acheter ».
- **Numbers:** no-break space between thousands, comma for decimals: "1 250", "1,5". English "1,250" reads as one and a quarter in French, so game code must format numbers, multipliers and timers for fr-ca before filling {params}; the skill's audit lists every value the code pre-formats in English. Roblox's `{name:int}` and `{name:fixed}` specifiers are not documented to localize separators (the docs' Spanish example prints "$500.00"), so format in code.
- **Percent and money:** "25 %", "+10 %", "4,99 $" -- no-break space before % and $, symbol after the number.
- **Time and durations:** 24-hour clock "14 h 30"; durations "3 h 20 min", "2 j 5 h", "45 s". No period after the symbols, never "3h20m". CLDR fr-CA short date: "2026-11-08"; long form "8 novembre 2026".
- **Ellipsis:** the single character "…", no space before: "Chargement…".
- **Multipliers:** "x2", "x1,5" with a plain x; same style throughout the game.
- **Keys:** keep key letters as printed: "Appuie sur E", "touche E". Canadian French keyboards are QWERTY: keep WASD, never France's ZQSD. Shift is "Maj", Ctrl stays "Ctrl" (Microsoft fr-CA).
- **Apostrophe:** straight ' or curly ’ both render; pick one per game. Codes and keys stay straight.

## Do not translate / keep as is
- Roblox, Robux, Premium, VIP, Roblox Studio, Creator Hub.
- The game title (Pet Hatch Tycoon) unless the developer supplies a French title.
- Promo codes exactly as typed (FREEPETS), usernames and display names, key letters (E, WASD).
- Gamer acronyms in flavor text: AFK, XP, GG, OP. Item names DO translate unless they are brand-like: "Lucky Potion" -> "Potion de chance".

## Rendering on Roblox
- Builder Sans, the default UI font, maps every French letter (àâçéèêëîïôœùûüÿ and their capitals) plus « » … ’ × and U+00A0 -- checked in the font files of the local Studio install, 2026-11-08.
- Builder Sans has no glyph for U+202F (narrow no-break space) or U+2009 (thin space), which France-style CLDR output and some MT tools insert. Use U+00A0 only; it is also what CLDR fr-CA uses.
- Fredoka One (FredokaOne-Regular.ttf) has no U+00A0 glyph; whether Roblox falls back to another font, leaves a gap or draws a box is unverified. Other common game fonts (Luckiest Guy, Bangers, Source Sans Pro, Montserrat, Press Start 2P, Arimo, Denk One, Creepster, Oswald) have the full French set. With Fredoka One, check "25 %" and "1 250" in Studio; if a box shows, use a plain space in that font.
- Verify in Studio: accented capitals (É, À) clipped at the top under TextScaled (unverified risk), and long words like "récompense" wrapping in narrow buttons.

## Mistakes machine translation makes here
- France spacing: "Super !" / "Prêt ?" -> "Super!" / "Prêt?".
- English number format: "1,250 pièces" -> "1 250 pièces"; "3h 20m" -> "3 h 20 min".
- Formal register: "Rejoignez notre communauté" -> "Rejoins notre communauté".
- France anglicisms: "faire du shopping", "week-end", "e-mail" -> "magasiner", "fin de semaine", "courriel".
- France slang: "Cette épée est ouf!" -> "Cette épée est surpuissante!".
- Calque of "claim": "Réclamer" (to demand or complain) -> "Récupérer".
- Calque of "leaderboard": "Tableau des meneurs" -> "Classement".
- Gendered participle: "{player} est arrivé" -> "{player} a rejoint la partie".
- English word order: "Légendaire Dragon" -> "Dragon légendaire".
- Plural hedge: "Il te manque {amount} pièce(s)" -> "Pas assez de pièces! Il en manque {amount}."
- Wrong pet word: "mascotte" -> "animal"; "coins" left as is -> "pièces".
- AZERTY remap: "Appuie sur Z pour avancer" -> "Appuie sur W pour avancer".

## Reference translations
Lengths in notes are rendered text with the sample value shown; the skill's linter counts text without {params} and <b> tags.

| key | translation | note |
|---|---|---|
| menu.play | Jouer | infinitive button |
| shop.title | Boutique | |
| shop.buy | Acheter | |
| reward.claim | Récupérer | not "Réclamer" (calque) |
| rebirth.button | Renaître | "Renaissance" is 11 chars, over max |
| rebirth.confirm | Renaître maintenant? Tu perdras tes pièces, mais tu gagneras un bonus permanent x{multiplier}. | code must send "1,5", not "1.5" |
| coins.need_more | Pas assez de pièces! Il en manque {amount}. | "en" dodges the plural; 40 at "1 250", 6+ digit amounts overflow; fallback "Pièces manquantes : {amount}" |
| coins.count | Pièces : {count} | label-colon dodges "0/1 pièce"; over 16 only at 7+ digit counts |
| egg.hatched | Nouvel animal {rarity} : {pet}! | "hatched" is clear from the egg; {rarity} agrees with "animal" (m.), so any rarity fits any pet; no article before {pet} |
| rarity.legendary | Légendaire | masculine tag form (here also epicene) |
| pet.name.dragon | Dragon | masculine |
| chat.player_joined | {player} a rejoint la partie | "avoir" avoids gender agreement |
| trade.request | {player} veut échanger avec toi | |
| prompt.open_shop | Touche E pour ouvrir | "Appuie sur E pour ouvrir" is 24 chars, over max |
| pass.buy_price | Acheter ({price} Robux) | "Acheter pour {price} Robux" runs over 22 |
| pass.coins2x | Pièces x2 | multiplier after the noun |
| pass.vip | VIP | kept: French uses the acronym as is |
| reward.daily_title | Récompense du jour | exactly 18; "quotidienne" is too long |
| reward.come_back | Reviens dans {time} pour ta prochaine récompense! | {time} formatted "3 h 20 min" |
| codes.placeholder | Entre un code | |
| codes.invalid | Ce code n'est pas valide ou a expiré. | "non valide" as in Microsoft fr-CA |
| social.like_reward | Aime le jeu pour une <b>Potion de chance</b> gratuite! | "aimer" = like, as in Quebec social media; Roblox's French like label unverified |
| social.group_reward | Rejoins notre communauté pour une récompense gratuite! | Roblox calls groups "communautés"; 54 chars |
| afk.warning | Tu es AFK. Bouge pour continuer à gagner! | AFK kept; avoids "inactif/inactive" |
| leaderboard.title | Classement | OQLF term; epicene, unlike "Meilleurs joueurs" |
| level.up | Niveau supérieur! Te voilà au niveau {level}. | |
| tutorial.sell | Entre dans le cercle lumineux pour vendre tes animaux. | |
| inventory.full | Ton sac est plein! Vends des animaux pour faire de la place. | exactly 60; "sac à dos" overflows |
| settings.music | Musique | |
| settings.on | Oui | "Activé" is 6 chars, over max; "ON" is an anglicism |
| loading | Chargement… | single ellipsis character |
| event.ends_in | Fin de l'événement : {time} | 28 at "2 j 5 h"; longer durations overflow |
| item.op | Cette épée est surpuissante! | |
| friends.boost | +{percent} % de bonus par ami sur ton serveur | no-break space before % |

## Sources
1. Microsoft French (Canada) Style Guide -- https://download.microsoft.com/download/5/6/8/568628ff-0646-4740-a052-d8bd97ecdcf8/fra-can-StyleGuide.pdf
2. CLDR language plural rules -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR 47 fr-CA vs fr-FR number, time, duration formats via ICU 77.1 (Node.js Intl), run 2026-11-08 -- https://cldr.unicode.org/
4. OQLF, spacing before and after punctuation -- https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles
5. OQLF GDT, clavardage -- https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8392463/clavardage
6. OQLF GDT, tableau de classement -- https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26529687/tableau-de-classement
7. Roblox Creator Docs (French), Groups -- https://create.roblox.com/docs/fr-fr/projects/groups
8. Roblox newsroom (French), Friends are back -- https://about.roblox.com/fr/newsroom/2026/04/expanding-trusted-friends
9. Roblox Creator Docs (French), Passes -- https://create.roblox.com/docs/fr-fr/production/monetization/game-passes
10. Roblox language codes -- https://create.roblox.com/docs/production/localization/language-codes
11. DevForum, Locale support for translations -- https://devforum.roblox.com/t/locale-support-for-translations/4095306
12. DevForum, Introducing Roblox Communities -- https://devforum.roblox.com/t/introducing-roblox-communities/3268307
13. DevForum, Introducing Builder Font -- https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222
14. Font cmaps read from the local Roblox Studio install (content/fonts: BuilderSans-*.otf and bundled game fonts), 2026-11-08
15. DevForum, Canadian French translations (magasinage vs shopping) -- https://devforum.roblox.com/t/canadian-french-translations-translation-service-open/442499
16. Roblox Creator Docs, Localize with scripting (format specifiers) -- https://create.roblox.com/docs/production/localization/localize-with-scripting
17. Wikipedia (French), Diacritiques utilisés en français (Académie française on accented capitals) -- https://fr.wikipedia.org/wiki/Diacritiques_utilisés_en_français
