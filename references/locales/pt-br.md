# Portuguese (Brazil) (pt-br) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `pt-br`, and always the same text in the bare `pt` column: every Portuguese-language player without a closer column gets it, including Portugal when the game ships no `pt-pt` |
| Script, direction | Latin, LTR |
| Address the player as | "você" with third-person verbs ("Você tem", "Volte amanhã"); never "tu", "o senhor" or "vós" |
| Text expansion vs English | about +15-35% on sentences (+17% over the reference set below; no published Roblox figure); short buttons can double ("Buy" -> "Comprar", "Claim" -> "Resgatar") |
| Plural categories (CLDR) | one (integer part 0 or 1: 0, 1, 1,5), many (exact millions, compact forms), other; ordinals: other only |
| Model confidence | high -- big, well-documented language; the real risks are Portugal-Portuguese leakage and stiff, textbook register |
| Native review before shipping | recommended |

## Audience and register
Brazil is one of Roblox's biggest player bases, and the `pt` fallback also reaches Angola, Mozambique and other Lusophone players. Write the way a polished Brazilian mobile game talks to a 12-year-old: short, warm, energetic, never corporate.
- Pronoun: "você" everywhere. "Tu" lives in speech in the South and parts of the North and Northeast, often with "você" verb forms ("tu vai"); in written UI it reads regional or Portuguese. Drop "você" when the sentence is clear without it: "Precisa de mais 250." is natural, "Você precisa de mais 250 para você comprar" is not.
- Buttons and labels take the infinitive, as in Roblox's own pt-BR UI ("Comprar", "Convidar", "Bloquear", "Denunciar"): "Jogar", "Resgatar", "Vender tudo".
- Instructions inside sentences take the você-imperative (subjunctive form): "Volte amanhã!", "Entre na comunidade", "Venda seus pets". The spoken tu-forms "Volta", "Entra", "Vende" look sloppy in writing; never mix both in one string ("Entra e ganhe" is wrong).
- Hype that sounds native: "Parabéns!", "Mandou bem!", "Incrível!", "Uau!", "Que sorte!", "Bora!" (kid-safe, casual). One exclamation mark, never "!!!".
- Reads stiff or adult: "Por favor, aguarde", "Deseja realizar...?", "Prezado jogador", "Caso queira", future tense ("você receberá") where the present works ("você ganha"). Use simple present and past; avoid gerundism ("vou estar enviando").
- Avoid heavy regional slang that the `pt` fallback audience may not share ("mano", "bagulho", "tipo assim"). Mild gamer slang is fine: "OP", "noob", "brabo", "top".

## Roblox and gaming vocabulary
| English | pt-BR | Note |
|---|---|---|
| Robux | Robux | Invariable, capital R: "150 Robux", never "Robuxes" |
| Premium | Premium / Roblox Premium | Roblox UI: "Apenas Premium" |
| game pass | passe | Roblox client: "Passe"; pt-BR Creator docs: "pass", "passes de jogo"; players say "gamepass" |
| developer product | produto | Creator docs: "Produtos do desenvolvedor"; in game UI just name the item |
| experience / game | jogo | Roblox UI says "experiência"; players and in-game text say "jogo" |
| obby, tycoon, simulator | obby, tycoon, simulator | Kept in game titles; in prose "jogo de obby", "simulador" |
| rebirth | Rebirth (o rebirth) | Players keep the English word, "fazer rebirth" (not confirmed from a Brazilian community source); "Renascer" is the translated option -- pick one per game |
| pet | pet (o pet, os pets) | Masculine; players never say "animal de estimação" in games |
| egg / hatch | ovo / chocar (abrir) | "Ovo Lendário"; players often say "abrir ovo"; never "eclodir" in UI |
| coins / gems | moedas / gemas | "Poção de moedas", "gemas"; avoid "joias" for gems |
| boost | bônus (o boost) | Roblox UI: "Bônus de 10%"; "boost" is understood but keep one term |
| multiplier | multiplicador | "Multiplicador 2x" |
| XP | XP (o XP) | Never "PE" or "pontos de experiência" on a HUD |
| level up | subir de nível | "Subiu de nível!"; players say "upar" -- fine in flavor text, not in system messages |
| quest | missão | "Missões diárias" |
| leaderboard | ranking / classificação | Roblox's player list: "Classificação"; in-game boards: "Ranking", "Top jogadores" |
| AFK, noob, OP, GG | AFK, noob, OP, GG | Kept in English, uppercase acronyms |
| VIP | VIP | "Servidor VIP" for private servers in games; Roblox UI: "servidor privado" |
| trade | trocar / troca | "Trocar", "Pedido de troca"; players also say "trade" |
| inventory / backpack | inventário / mochila | Roblox UI: "Inventário", "Mochila" |
| daily reward | recompensa diária | Button "Resgatar"; never "Reivindicar" |
| codes | códigos | "Resgatar código", "Digite o código" |
| group | comunidade | Roblox renamed Groups to Communities: pt-BR Creator docs name the section "Comunidades", the client shows "Emblema da comunidade"; players still say "grupo", also fine |
| like / favorite | dar like / favoritar | "Dê like no jogo", "Favoritar"; Roblox client: "Favorito", "Adicionar item aos favoritos"; the like control is a thumbs-up icon, its pt-BR label ("Curtir"/"Gostei") unverified |
| server | servidor | "Servidor cheio" |
| friends / connections | amigos | The 2026-11 client ships both "Conexões" strings and newer friends-wording ones ("amigos", neutral "amizade(s)"), so Roblox seems to be returning to "friends" (inferred from key names); in game text say "amigo(s)" |
| badge | emblema | Roblox UI: "Emblema" |

## Grammar traps in UI strings
- **Plurals with {count}.** No plural selection in Roblox, and "{count} moedas" breaks at 1 ("1 moedas"); CLDR files 0 under "one", but Brazilians write "0 moedas", so only 1 breaks. Put the noun first as a label: "Moedas: {count}", "Dragão x{count}". Agreeing verbs break too: "Faltam {amount} moedas" -> "Faltam moedas! Precisa de mais {amount}."
- **Millions.** Spelled-out millions take "de": "1 milhão de moedas", "2 milhões de moedas". Keep digits ("1.000.000") or "1M" and the problem disappears.
- **Gender of {player}.** Display names can be any gender. Use verbs, not adjectives or participles: "{player} entrou no jogo" (good), "{player} foi eliminado" (bad) -> "{player} está fora!". "Bem-vindo, {player}!" -> "Boas-vindas, {player}!" or "Olá, {player}!". Avoid "inativo(a)"-style hedges, which Roblox itself uses; rephrase instead.
- **Gender of the reader.** "Você está pronto?" assumes a boy -> "Tudo pronto?". "Obrigado por jogar!" is fine: it agrees with the speaker, not the player.
- **Articles and contractions before {pet}/{item}.** Portuguese wants an article, and its gender depends on the noun ("o Dragão", "a Coruja"): "Você ganhou um {pet}" and "Bônus do {item}" break for feminine names. Use a colon: "Você ganhou: {pet}!", "Bônus: {item}".
- **Rarity agreement.** Adjectives follow and agree with their noun ("Coruja Lendária"). Translate rarity words in the masculine (Comum, Raro, Épico, Lendário, Mítico) and attach them to a masculine head noun: "pet {rarity}", "item {rarity}", "Ovo {rarity}".
- **Word order.** Adjective after noun, English compounds become noun + de + noun: "Lucky Potion" -> "Poção da Sorte", "Golden Dragon" -> "Dragão Dourado", "Coin Boost" -> "Bônus de moedas". Product names in the "2x Moedas" pattern keep the multiplier first.
- **Capitalization.** Sentence case for titles, buttons and messages, as in Roblox's pt-BR UI ("Adicionar item aos favoritos", "Emblema da comunidade"): "Recompensa diária", "Top jogadores". Item and pet names capitalize nouns and adjectives but not "de/da/do": "Poção da Sorte". Months and weekdays are lowercase ("sábado", "dezembro").
- **Tense parallelism.** Keep both clauses in the same tense: "Você perde suas moedas, mas ganha um bônus", not "vai perder ... mas ganha".
- **Possessives.** English stacks "your"; Portuguese drops them when obvious: "Equip your best pets" -> "Equipe os melhores pets".

## Typography and formatting
- No space before ! ? : ; (unlike French). No inverted marks.
- Quotation marks: double quotes "..." ("aspas"); never French-style guillemets, which read Portugal-Portuguese.
- Numbers: period for thousands, comma for decimals: "1.250 moedas", "1,5x". English-formatted "1,250" from game code reads as one-and-a-quarter in Brazil -- flag it to the developer rather than working around it in the string. The skill's audit lists such pre-formatted values; it does not reformat numbers in game code.
- Percent: no space: "10%", "+25% de bônus" (Roblox UI: "Bônus de 10%").
- Durations: "3h 20min", "2d 5h", "45s"; "min" not "m" (m is meters), no period, no plural s. {time} arrives as game code formats it ("3h 20m"); the fix is in code, not in the string.
- Ordinals: "1º lugar", "2ª temporada" (º masculine, ª feminine).
- Ellipsis: three periods, as Roblox does: "Carregando...". Gerund, not the Portugal form "A carregar...".
- Keys: the key letter stays. Roblox's client says "Pressione {tecla}"; "Aperte E" is the casual form, also natural -- one per game. "Shift", "Enter" stay; Space -> "Espaço" (as in Roblox's client). Mobile copy says "Toque", PC copy "Clique".
- Dates: dd/mm/aaaa ("25/12"). Real money uses "R$", but Roblox prices are always "Robux" after the number.

## Do not translate / keep as is
- Roblox, Robux, Premium, Roblox UI names when quoted exactly.
- The game title ("Pet Hatch Tycoon"): Brazilian players search and talk about Roblox games by their English titles; Brazilian code and guide sites keep them.
- Promo codes (FREEPETS) exactly as typed, same case; usernames and display names.
- VIP, AFK, OP, XP, GG, noob, obby, tycoon, and the multiplier "x" ("2x").
- Translate pet, item, egg and area names consistently once you translate the game ("Dragão", "Poção da Sorte"); keep English only if the community already knows the item by its English name.
- Script: Latin only, with full accents (á à â ã ç é ê í ó ô õ ú). The 1990 spelling agreement applies: "ideia", "heroico", "linguiça" (no trema).

## Rendering on Roblox
- Portuguese needs only Latin-1 accented letters. No DevForum report found of Roblox's stock fonts (Builder Sans, Gotham, Source Sans) missing them; the font-gap reports concern Cyrillic, CJK and Arabic. Treat full coverage in every decorative font as (unverified).
- Test in Studio: "AÇÃO ÉPICA LENDÁRIO ÔNIBUS" in every custom font the game uses, at the smallest TextSize. Accented capitals (Ã, Ç, É, Ô) are taller and can clip at the top in tight labels with TextScaled (unverified).
- Expansion is the main risk: give labels AutomaticSize or slack. "Recompensa diária" and "Carregando..." sit near typical button widths.

## Mistakes machine translation makes here
1. Portugal leakage: "ecrã" -> "tela", "utilizador" -> "jogador", "telemóvel" -> "celular", "equipa" -> "equipe", "A carregar..." -> "Carregando...", "Prima E" -> "Aperte E", "fixe" -> "legal".
2. Words innocent in Portugal, rude in Brazil: "bicha" (queue) -> "fila"; "rapariga" (girl) -> "menina"; "puto" (kid) -> "garoto". Never ship these to children.
3. "tu" or mixed forms: "Tu tens um novo pet" -> "Você tem um novo pet"; "Volta amanhã e ganhe" -> "Volte amanhã e ganhe".
4. Claim as "Reivindicar": "Reivindicar recompensa" -> "Resgatar recompensa".
5. Play as music: "Tocar" -> "Jogar"; Exit as "Êxito" (success) -> "Sair".
6. Over-formal: "Deseja realizar o renascimento?" -> "Fazer rebirth agora?"; "Por gentileza, aguarde" -> "Só um instante...".
7. Literal level up: "Nível acima!" -> "Subiu de nível!".
8. Hatch as biology: "O ovo eclodiu" -> "Novo pet!" / "Você chocou um ovo!".
9. Dropped accents: "Voce", "bonus", "nivel", "codigo" -> "Você", "bônus", "nível", "código".
10. English adjective order: "Lendário Dragão" -> "Dragão Lendário"; "Sorte Poção" -> "Poção da Sorte".
11. Trade as commerce: "Comércio com {player}" -> "Trocar com {player}".
12. Over-applying the platform rename: "+10% por conexão" -> "+10% por amigo".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Jogar | |
| shop.title | Loja | |
| shop.buy | Comprar | |
| reward.claim | Resgatar | Never "Reivindicar"; "Coletar" also works |
| rebirth.button | Rebirth | Kept as players say it; "Renascer" if the game translates every term |
| rebirth.confirm | Fazer rebirth agora? Você perde suas moedas, mas ganha um bônus permanente de {multiplier}x. | Present tense in both clauses; code should send "1,5", not "1.5" |
| coins.need_more | Faltam moedas! Precisa de mais {amount}. | Rebuilt so {amount} = 1 stays correct |
| coins.count | Moedas: {count} | Label form avoids "1 moedas"; leaves 8 characters for {count}, so abbreviate millions ("1,2M"). Bare "{count}" only if the developer drops the word |
| egg.hatched | Novo pet {rarity}: {pet}! | Rarity agrees with masculine "pet", so feminine pet names stay correct; drops the verb because "Você chocou um pet {rarity}: {pet}!" reaches 48 at max lengths |
| rarity.legendary | Lendário | Masculine, to agree with "pet"/"item" |
| pet.name.dragon | Dragão | |
| chat.player_joined | {player} entrou no jogo | Past tense verb has no gender |
| trade.request | {player} quer trocar com você | |
| prompt.open_shop | Aperte E para abrir | "Pressione E para abrir" (20) matches Roblox's wording |
| pass.buy_price | Comprar por {price} Robux | Fits 22 up to 4-digit prices |
| pass.coins2x | 2x Moedas | |
| pass.vip | VIP | |
| reward.daily_title | Recompensa diária | Sentence case |
| reward.come_back | Volte em {time} para pegar a próxima recompensa! | |
| codes.placeholder | Digite o código | |
| codes.invalid | Código inválido ou expirado. | |
| social.like_reward | Dê like no jogo e ganhe uma <b>Poção da Sorte</b> grátis! | 50 visible characters |
| social.group_reward | Entre na nossa comunidade e ganhe um prêmio grátis! | "comunidade" matches Roblox's "Comunidades" page; "grupo" also fine; "unlock" folded into "ganhe" |
| afk.warning | Você está AFK! Ande para continuar ganhando! | |
| leaderboard.title | Top jogadores | "Melhores jogadores" is 18, over the limit |
| level.up | Subiu de nível! Agora você é nível {level}. | |
| tutorial.sell | Entre no círculo brilhante para vender seus pets. | |
| inventory.full | Sua mochila está cheia! Venda pets para liberar espaço. | |
| settings.music | Música | |
| settings.on | Sim | Pair with "Não", as Minecraft pt-BR toggles do; Roblox's "Ligado" is 6, over 5; "Ativo" clashes with feminine rows ("Música"); "ON" also fine |
| loading | Carregando... | Same as Roblox UI |
| event.ends_in | O evento acaba em {time} | |
| item.op | Essa espada é OP! | |
| friends.boost | +{percent}% de bônus para cada amigo no seu servidor | |

## Sources
1. Microsoft Portuguese (Brazil) Localization Style Guide -- https://download.microsoft.com/download/8/e/3/8e349e32-9eb9-4b63-9909-7586b94a24dd/por-bra-StyleGuide.pdf
2. Unicode CLDR language plural rules chart -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. Roblox client CoreScript translations, pt-br column (ExtraContent/translations/CoreScriptLocalization.csv, Roblox build of 2026-11-05) -- local file from the Roblox install
4. Roblox newsroom (pt-BR), age-based communication and "Amigos" -> "Conexões" -- https://about.roblox.com/pt-br/newsroom/2025/07/advancing-safety-on-roblox-with-age-based-communication
5. Roblox Creator docs (pt-BR), passes -- https://create.roblox.com/docs/pt-br/production/monetization/game-passes
6. DevForum, Introducing Roblox Communities (Groups renamed) -- https://devforum.roblox.com/t/introducing-roblox-communities/3268307
7. Critical Hits, Tap Simulator Reborn codes (Brazilian code-guide wording) -- https://criticalhits.com.br/dicas/tap-simulator-reborn-codigos-outubro-2026/
8. Critical Hits, Adopt Me rarest eggs (pets, rarity words, English egg names) -- https://criticalhits.com.br/games/roblox-adopt-me-ovos-mais-raros/
9. Esports.net Brasil, gamer slang (OP, AFK, nerfar, dropar, noob) -- https://www.esports.net/br/guias/girias-gamers/
10. ExitLag blog, "Como dar like no jogo do Roblox" -- https://www.exitlag.com/blog/pt/como-dar-like-no-jogo-do-roblox-em-qualquer-plataforma/
11. NoPing blog, "Como favoritar jogos no Roblox" -- https://noping.com/pt/blog/como-favoritar-jogos-no-roblox
12. creation.dev Portuguese glossary, "Rebirth" kept as the term -- https://www.creation.dev/pt/glossary/rebirth
13. DevForum, font coverage complaints (non-Latin scripts) -- https://devforum.roblox.com/t/theres-no-font-which-can-fullfill-all-my-use-cases-and-fit-game-style/3051353
14. Roblox Creator docs, size modifiers (AutomaticSize for localized text) -- https://create.roblox.com/docs/en-us/ui/size-modifiers
15. Roblox Creator docs (pt-BR), groups page pointing to "Comunidades" -- https://create.roblox.com/docs/pt-br/projects/groups
16. Minecraft Java pt_br.json (options.on "Sim", options.off "Não") -- https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21.4/assets/minecraft/lang/pt_br.json
