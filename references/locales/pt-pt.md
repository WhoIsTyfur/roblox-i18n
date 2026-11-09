# Portuguese, Portugal (pt-pt) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `pt-pt` (not the bare `pt` column: that belongs to the default variant, Brazilian `pt-br`). Small reach: Roblox has no European Portuguese account language, so players in Portugal are `pt-br` by default (see Audience) |
| Script, direction | Latin, LTR |
| Address the player as | informal "tu" with 2nd-person verbs (tens, prime, a tua); never "você"; a group is "vocês" |
| Text expansion vs English | +15-30% for sentences (this guide's reference set: +18%); short buttons can double (Buy -> Comprar) |
| Plural categories (CLDR) | one, many, other: "one" is exactly 1; 0 is "other" (0 moedas), unlike pt-BR; "many" is only exact millions ("1 milhão de moedas") |
| Model confidence | medium: grammar is easy, but models drift into Brazilian forms (você, gerund, tela, bônus) |
| Native review before shipping | recommended: mainly to catch Brazilian words and spellings |

## Audience and register
- Who sees this column: Roblox's locale API (checked 2026-11-08) offers Portuguese accounts only as `pt_br`; `pt_pt` is enabled for creator tables but not for sign-up or the app, and the client's own strings ship only `pt` and `pt-br`. A player in Portugal reading Roblox in Portuguese is therefore `pt-br`, and the exact `pt-br` column wins. `pt-pt` reaches them only if they pick it in the in-game "Idioma da experiência" menu (whether that menu lists `pt-pt`: unverified) or the game's scripts choose it (`GetCountryRegionForPlayerAsync` returns "PT" -> `GetTranslatorForLocaleAsync("pt-pt")`); automatic GUI translation still follows the player's own locale. Ship `pt-br` first. A game with only a `pt-pt` column may serve it to Brazilians as the sibling fallback.
- Players are mostly 9-16. Roblox's own Portuguese (app, store page, help) is Brazilian: its store copy says "bate-papo", "celular", "galera", "seu avatar". Portuguese kids understand it, but a `pt-pt` column exists to sound local. Reuse Roblox's Portuguese wording only where Portugal says it the same way (Robux, passe, comunidade).
- Address one player as "tu", with tu verbs and article + possessive: "Tens 3 ovos na tua mochila." Minecraft's pt-PT file and Portuguese tech sites address readers this way ("Prime %s para abrires o teu inventário"; "Mantém-te atualizado").
- "Você" reads as distant or even rude in Portugal; the impersonal 3rd person ("Prima", "Tem de") is for adult software, as in Microsoft's guide. Do not use it for kids.
- Buttons and menu commands use the infinitive: Jogar, Comprar, Receber, Renascer, Cancelar (Microsoft rule for user-to-machine commands; Minecraft pt-PT does the same).
- Instructions to the player use the tu imperative: "Prime E", "Vende pets", "Volta amanhã". Negative imperative takes the subjunctive: "Não saias!", not "Não sai!".
- Progressive is "estar a + infinitive", never the gerund: "Estás a ganhar moedas!", "A carregar...".
- Hype that sounds natural: "Boa!", "Fixe!", "Brutal!", "Incrível!", "Parabéns!", "Vamos lá!". Microsoft notes slang like "bué fixe" fits only kid and young-teen audiences: allowed in flavor text, sparingly, never in purchase or error text.
- Brazilian hype words to avoid: "Legal!", "Massa!", "Show!", "Valeu!", "galera" (use "malta").
- Stiff or textbook: "Pretende continuar?", "Efetue a compra", "Por favor". Microsoft drops please/sorry in UI text; so should a game.

## Roblox and gaming vocabulary
| English | use in pt-pt | note |
|---|---|---|
| Robux | Robux | never translated, invariable: "100 Robux", "1 Robux" |
| Premium / Roblox Plus | Premium / Roblox Plus | brand names; Roblox Plus replaced new Premium sign-ups on 2026-04-30 |
| game pass | passe | "Passe VIP", "Comprar passe"; Roblox's machine-translated pt-BR docs say "pass"; avoid |
| developer product | (name the item) | players never see this term; say "Poção da Sorte", not "produto" |
| experience / game | jogo | "experiência" only for Roblox-platform wording; Portuguese press says "jogos e experiências" |
| obby | obby | genre word kept; describe as "percurso de obstáculos" if needed (unverified how often PT kids say it) |
| tycoon / simulator | tycoon / simulador | keep English in game titles |
| rebirth | Renascer (button), renascimento (noun) | Minecraft pt-PT uses "Renascer" for respawn: fine in a game without respawn; if the game also respawns players, keep "Rebirth" for the reset. Players also say "rebirth" (unverified for PT) |
| pet | pet (o pet, os pets) | kept from English in pet games (unverified for PT; "mascote" is the native fallback, feminine) |
| egg / hatch | ovo / chocar, abrir | "Abre ovos", "Chocaste 3 ovos" |
| coins / gems | moedas / gemas | "diamantes" if the icon is a diamond |
| boost | bónus | pt-PT accent: bónus, never bônus; players also say "boost" |
| multiplier | multiplicador | "x2" or "2x", both seen |
| XP / level up | XP / subir de nível | masculine (o XP, "+50 XP"); "Subiste de nível!" |
| quest | missão | feminine: "Missão concluída!" |
| leaderboard | classificação, Top | "Top jogadores"; "ranking" also common |
| AFK / noob / OP | AFK / noob / OP | gamer slang kept; never call the player "noob" in UI |
| VIP | VIP | kept |
| trade | troca (noun), trocar (verb) | Minecraft pt-PT: "Trocas" |
| inventory / backpack | inventário / mochila | Minecraft pt-PT: "Inventário" |
| daily reward | recompensa diária | or "prémio diário"; prémio, never prêmio |
| codes / redeem | códigos / resgatar | "Resgatar código"; the code itself stays as typed |
| group | comunidade (grupo) | Roblox renamed Groups to Communities; its UI says "comunidade" ("Emblema da comunidade"), which is also pt-PT: "Junta-te à nossa comunidade"; kids still say "grupo", also fine |
| like / favorite | like, gosto / favoritos | "Dá like"; "Adiciona aos favoritos"; "favoritar" is Brazilian |
| server | servidor | |
| friends | amigos | Roblox renamed friends to "Conexões" in 2025; its 2026-11 client mixes that with newer friends wording ("Amizades", "Novo amigo"); in game text say "amigo(s)"; never "ligações" |
| chat | chat | Minecraft pt-PT ("Definições do chat") and ZAP keep "chat"; "bate-papo" is Brazilian |

## Grammar traps in UI strings
- Plurals with {count}: pt-PT has one form for exactly 1 and another for everything else, including 0. One string cannot cover both, so put the number after a label: "Moedas: {count}", "Ovos: {count}". "{count} moedas" breaks at 1 ("1 moedas").
- Same for "need N more": keep the noun away from the number. "Faltam moedas! Precisas de mais {amount}." works for 1 and 1250; "Faltam-te {amount} moedas!" breaks at 1 ("Falta-te 1 moeda").
- {player} gender is unknown: avoid adjectives and participles about the player. "{player} entrou no jogo", "{player} ganhou a ronda!" are safe; "{player} foi eliminado" is not. Greet with "Olá, {player}!" or "Boas-vindas!", not "Bem-vindo".
- Item and pet gender: o Dragão, a Raposa, o Coelho. A rarity word inserted next to a pet cannot agree (um Dragão Lendário / uma Raposa Lendária). Translate rarities in the masculine and attach them to masculine "pet" or "item": "Novo pet {rarity}: {pet}!" -> "Novo pet Lendário: Raposa!". No per-pet gendered rarity strings needed.
- No article or contraction right before a parameter: "do {item}" / "da {item}" guesses the gender. Write "Compraste: {item}" or "Item comprado: {item}". No article before display names either: "{player} quer fazer uma troca contigo", not "O {player}...".
- Clitic pronouns go after the verb with a hyphen in plain sentences: "Junta-te", "Mexe-te", "Faltam-te". They go before the verb after "não", "já", "que": "Não te esqueças de voltar!". Never start a sentence with "Te" or "Se" (Brazilian): "Te vejo amanhã" -> "Até amanhã!".
- Personal infinitive after "para" when the doer should be clear: "para abrires o teu inventário", "para venderes os teus pets". Short prompts may keep the plain infinitive, as Minecraft does: "Prime E para abrir".
- "Precisar de" before a noun: "Precisas de mais gemas". "Contigo", not "com você".
- English noun stacks invert: "Lucky Potion" -> "Poção da Sorte", "Coin Boost" -> "Bónus de moedas", "Pet Shop" -> "Loja de pets". Adjectives follow the noun: "Dragão Lendário".
- Capitalization: house rule is sentence case for titles, buttons and labels, as Minecraft pt-PT does ("Menu principal", "Escolher mundo", "Definições do chat"): "Recompensa diária", "Top jogadores". Do not copy Microsoft's rule of keeping the source's Title Case; Portuguese prose does not title-case. Item names capitalize nouns and adjectives, not "da/de/do": "Poção da Sorte". Lowercase after a colon; months and weekdays are lowercase.
- Spelling follows the 1990 Orthographic Agreement (Acordo Ortográfico), as Microsoft does: ação, atual, ótimo, direção, receção. Portugal keeps consonants it pronounces: facto, contacto.

## Typography and formatting
- No space before ! ? : ; and no inverted marks: "Subiste de nível!".
- Quotes: double “ ” (Microsoft pt-PT) or traditional « »; straight "..." is fine in Roblox strings. Never single quotes as primary quotes.
- Numbers (CLDR pt-PT): decimal comma "1,5"; thousands separator is a no-break space (U+00A0), and 4-digit numbers are not grouped: 1250, 12 500, 1 250 000. "1,250" from game code reads as one and a quarter. Numbers inside {params} are the developer's job: flag English formatting in the report, do not work around it in the string.
- Multipliers: "1,5x" or "x1,5"; "1.5x" looks foreign.
- Percent: no space, "+10%" (CLDR pattern). Short forms: "12 mil", "1,2 M".
- Durations: "3 h 20 min", "2 d 5 h", "45 s" ("3h 20min" is the compact form). "m" means meters, so "3h 20m" from code reads wrong; flag it like numbers. Clock times "14:30" (24-hour).
- Ellipsis: three periods, as in the source: "A carregar...".
- Keys: letter keys stay as printed: "Prime E para abrir". Microsoft key names: Shift, Enter, Esc, Ctrl stay; Spacebar is "Barra de espaço". Mouse: "Clica"; touch: "Toca".

## Do not translate / keep as is
- Roblox, Robux, Premium, Roblox Plus, VIP, AFK, OP, XP, noob.
- The game title ("Pet Hatch Tycoon") unless the developer supplies a Portuguese one; many pt games on Roblox keep English titles.
- Promo codes exactly as typed (FREEPETS), keybind letters, usernames and display names.
- Third-party brands: Discord, YouTube, TikTok.
- Translate in-game item and pet names ("Poção da Sorte", "Dragão") unless they are trademarks or deliberate English flavor.

## Rendering on Roblox
- Portuguese uses only Latin-1 accented letters: á à â ã ç é ê í ó ô õ ú, plus ª º. Roblox's default Builder Sans and its legacy fonts serve Roblox's own Portuguese UI, so these render.
- Gotham and Arial were replaced in place by Montserrat and Arimo in 2024; both cover Latin-1 (unverified per weight).
- Risk 1: custom pixel or decorative fonts may lack ã, õ or ç (unverified; check each custom FontFace).
- Risk 2: TextScaled shrinks a whole label when the longer Portuguese text does not fit, so "Comprar por 1250 Robux" can look smaller than its English button. Give buttons room or use TextWrapped.
- Risk 3: accents on capitals (É, Ã, Ç) may clip in tight boxes with small line height (unverified).
- Verify in Studio: set the test locale to `pt-pt`, then view "AÇÃO ÉPICA", the longest reference strings, and a toast at phone size.

## Mistakes machine translation makes here
- Brazilian address: "Você precisa de mais moedas" -> "Precisas de mais moedas"; "seu inventário" -> "o teu inventário".
- Gerund: "Carregando..." -> "A carregar..."; "Você está ganhando" -> "Estás a ganhar".
- Brazilian pronoun placement: "Se junte ao grupo!" -> "Junta-te ao grupo!".
- Brazilian imperatives: "Pressione E" / "Clique" -> "Prime E" / "Clica".
- Brazilian vocabulary: tela -> ecrã, celular -> telemóvel, usuário -> utilizador or jogador, time/equipe -> equipa, salvar -> guardar, configurações -> definições, baixar -> transferir, liberar -> libertar, rodada -> ronda, registro -> registo, contato -> contacto.
- Brazilian accents: bônus -> bónus, prêmio -> prémio, gênio -> génio, econômico -> económico.
- Pre-1990 spelling: "acção", "óptimo", "actualizar" -> "ação", "ótimo", "atualizar".
- False friend for Claim: "Reclamar" (= complain) or "Reivindicar" (legal) -> "Receber".
- Register mix in one game: "Prime E" next to "A sua mochila está cheia" -> "A tua mochila está cheia".
- Plural with a count: "1 moedas" -> "Moedas: 1".
- Words fine in Portugal but offensive in Brazil: "puto", "rapariga", "bicha" (queue). Keep them out of UI; use "miúdo", "jogadora", "fila".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Jogar | infinitive button |
| shop.title | Loja | |
| shop.buy | Comprar | |
| reward.claim | Receber | not "Reclamar" (= complain) |
| rebirth.button | Renascer | |
| rebirth.confirm | Renascer agora? Perdes as tuas moedas, mas ganhas um bónus permanente de {multiplier}x. | bónus with the pt-PT accent; code should send "1,5", not "1.5" |
| coins.need_more | Faltam moedas! Precisas de mais {amount}. | no noun after {amount}, so 1 stays correct; 33 + digits |
| coins.count | Moedas: {count} | "{count} moedas" breaks at 1; code should send 1250, not 1,250 |
| egg.hatched | Novo pet {rarity}: {pet}! | rarity agrees with masculine "pet", so feminine pets stay correct; 38 at max lengths. Drops "hatched": "Chocaste um pet {rarity}: {pet}!" reaches 45 |
| rarity.legendary | Lendário | masculine, to agree with "pet"/"item" |
| pet.name.dragon | Dragão | masculine |
| chat.player_joined | {player} entrou no jogo | Minecraft pt-PT wording; no gender |
| trade.request | {player} quer fazer uma troca contigo | contigo, not "com você" |
| prompt.open_shop | Prime E para abrir | tu imperative of premir |
| pass.buy_price | Comprar por {price} Robux | 22 with a 4-digit price: no slack; a 5-digit price ("12 500") needs a wider button |
| pass.coins2x | Moedas x2 | |
| pass.vip | VIP | kept |
| reward.daily_title | Recompensa diária | "Prémio diário" also fine |
| reward.come_back | Volta daqui a {time} para a próxima recompensa! | "daqui a" for "in X time"; "recompensa" matches the panel title; 51 with "3 h 20 min" |
| codes.placeholder | Inserir código | infinitive field label; "Introduz o código" is 17, over max |
| codes.invalid | Esse código é inválido ou já expirou. | |
| social.like_reward | Dá like ao jogo e ganha uma <b>Poção da Sorte</b> grátis! | 50 visible; "dar like" is everyday pt-PT for social-media likes (unverified for Roblox kids); never Brazilian "curtir" |
| social.group_reward | Junta-te à nossa comunidade e ganha um prémio grátis! | Roblox's word for groups; 53; "unlock" folded into "ganha"; "recompensa" would be 57 |
| afk.warning | Estás AFK! Mexe-te para continuar a ganhar! | a + infinitive, not "continuar ganhando" |
| leaderboard.title | Top jogadores | "Melhores jogadores" is 18, over max |
| level.up | Subiste de nível! Estás no nível {level}. | |
| tutorial.sell | Entra no círculo brilhante para venderes os teus pets. | |
| inventory.full | A tua mochila está cheia! Vende pets para libertar espaço. | libertar, not Brazilian "liberar" |
| settings.music | Música | |
| settings.on | Sim | Minecraft pt-PT toggles use Sim/Não; "Ligado" (6) is over max |
| loading | A carregar... | never "Carregando..." |
| event.ends_in | O evento acaba em {time} | 25 with "2 d 5 h", 28 with "3 h 20 min": no slack for longer durations |
| item.op | Esta espada é OP! | gamer slang kept |
| friends.boost | +{percent}% de bónus por cada amigo no teu servidor | |

## Sources
1. Microsoft Portuguese (Portugal) localization style guide: https://aka.ms/portuguese-portugal-styleguide (PDF: https://download.microsoft.com/download/9/9/5/995a8ca6-383c-439d-9db0-cd457c9c2724/por-prt-StyleGuide.pdf)
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR pt-PT number data: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/pt-PT/numbers.json
4. Roblox language codes: https://create.roblox.com/docs/production/localization/language-codes
5. Roblox Creator Hub, Passes page in pt-BR (machine-translated): https://create.roblox.com/docs/pt-br/production/monetization/game-passes
6. Roblox on the Portugal App Store (pt-BR developer copy): https://apps.apple.com/pt/app/roblox/id431946152
7. DevForum, "Portuguese ... too ambiguous": https://devforum.roblox.com/t/portuguese-on-the-new-game-name-and-description-translations-page-is-too-ambiguous/206088
8. Minecraft Java pt_pt language file (mirror): https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21.4/assets/minecraft/lang/pt_pt.json
9. 4gnews.pt, Roblox parental controls article (pt-PT usage): https://4gnews.pt/roblox-anuncia-recurso-esperado-de-controlo-parental-e-recompensas-por-anuncios/
10. ZAP, "O que é o Roblox" (pt-PT usage): https://zap.aeiou.pt/o-que-e-roblox-734832
11. Priberam dictionary, prémio / prêmio: https://dicionario.priberam.org/prémio
12. Wikipedia, Brazilian Portuguese (grammar differences): https://en.wikipedia.org/wiki/Brazilian_Portuguese
13. DevForum, Builder font and Gotham/Arial replacement: https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222
14. Roblox newsroom (pt-BR), "Amigos" renamed "Conexões": https://about.roblox.com/pt-br/newsroom/2025/07/advancing-safety-on-roblox-with-age-based-communication
15. Roblox Plus launch coverage: https://allthings.how/roblox-plus-launches-april-30-pricing-perks-and-how-it-differs-from-premium/
16. Roblox locale API, account vs creator locales (`pt_pt` not enabled for sign-up or the full app): https://locale.roblox.com/v1/locales and https://locale.roblox.com/v1/locales/supported-locales
17. Roblox client CoreScript translations (ExtraContent/translations/CoreScriptLocalization.csv, install of 2026-11-08): only `pt` and `pt-br` columns; "Idioma da experiência", "Amizades", "Emblema da comunidade": local file from the Roblox install
