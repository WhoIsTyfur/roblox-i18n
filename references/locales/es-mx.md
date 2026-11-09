# Spanish (Mexico) (es-mx) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `es-mx`, and the same text in the bare `es` column: every Spanish player outside Spain (Argentina, Colombia, Chile, Peru, US...) gets `es`. Always fill `es` too; without it a non-Mexican player may land on `es-es`. |
| Script, direction | Latin, LTR |
| Address the player as | informal "tú" (`Vende`, `Vuelve`); "ustedes" for a group (`¡Únanse!`). Never "usted", "vos" or "vosotros". |
| Text expansion vs English | about +20-30%: this guide's reference set measures +22% after trimming; one-word buttons far more: Buy -> Comprar (+133%) |
| Plural categories (CLDR) | one, many, other (`many` = exact and compact millions: "1 millón de monedas", "1 M de monedas"; 0 is `other`) |
| Model confidence | high -- huge corpus; the real risks are Spain forms leaking in and country slang |
| Native review before shipping | recommended, ideally by a reviewer from outside Mexico to catch Mexicanisms |

## Audience and register
- Readers are 9-16 year olds from Mexico to Argentina plus Spanish-speaking kids in the US, many bilingual and used to English gaming words. Write neutral Latin American Spanish: words every country shares, no national slang.
- Instructions, toasts and tutorials use the tú imperative: `Vende mascotas para liberar espacio.` Buttons use the infinitive, as Roblox's own Spanish UI does (`Comprar`, `Canjear`, `Jugar`, `Quitar de favoritos`).
- Finished actions take the simple past, as Latin America speaks: `¡Subiste de nivel!`, `{player} se unió al juego`. The present perfect (`¡Has subido de nivel!`) sounds like Spain.
- Plain everyday words beat formal ones: `pedir` not `solicitar`, `dar` not `proporcionar`, `volver a intentarlo` not `inténtelo de nuevo`, `pero` not `sin embargo`.
- Hype is short and neutral: `¡Genial!`, `¡Increíble!`, `¡Lo lograste!`. Avoid Mexican `chido`, `padre`, `chamba`, `güey`, `órale`; Argentine `che`, `copado`; Colombian `bacano`, `parce`; Chilean `bacán`; Spain `mola`, `guay`, `tío`.
- Stiff or adult: usted forms (`Ingrese`), `Por favor` on every line, `realizar`, `efectuar`, `dicho`, passive `ha sido otorgado`.
- Kid-safe: never `coger` (vulgar in much of Latin America) -> `agarrar`, `tomar`, `recoger`; never `bicho` for creatures (vulgar in Puerto Rico); `huevo` is fine for eggs but use no idioms with it (`a huevo`, `huevón`).

## Roblox and gaming vocabulary
| English | Use in es (Latin America) | Note |
|---|---|---|
| Robux | Robux | Never translated or inflected: `500 Robux`, `Comprar por 99 Robux`. |
| Roblox Premium / Plus | Premium, Roblox Plus | Stay English. New Premium sign-ups ended when Roblox Plus launched (2026-04-30); old members keep Premium. |
| game pass | pase | Roblox store tab `Pases`; Creator docs (es): `pases de juego`. |
| developer product | producto | Players never see the term; name the product itself. Creator docs (es): `producto de desarrollador`. |
| experience / game | juego | Roblox's Spanish store copy says `juegos` almost everywhere; `experiencia` reads corporate in player text. |
| obby | obby | Kept; plural `obbys`. `parkour` also understood. |
| tycoon | tycoon | Kept in titles and genre tags; `magnate` is rare among kids. |
| simulator | simulador | `Simulador de mascotas`. |
| rebirth | Renacer (button), renacimiento (noun) | Players also say `rebirth` and `hacer rebirth`. |
| pet | mascota (feminine) | Adjectives after it agree (`mascota legendaria`); standalone rarity tags stay masculine. |
| egg / hatch | huevo / abrir | `Abre huevos`; `eclosionar` appears in Roblox listings. Never `incubar` (to brood) or `escotilla` (a hatch door). |
| coins / gems | monedas / gemas | |
| boost | potenciador (item), bonificación (%) | `+10% de bonificación`; kids also say `boost`. |
| multiplier | multiplicador, `x2` | `x` before the number: `Monedas x2`. |
| XP / level up | XP / subir de nivel | `¡Subiste de nivel!`; spelled out: `puntos de experiencia`. |
| quest | misión | `Misiones diarias`. |
| leaderboard | tabla de clasificación, `Top` | Roblox help uses `tablas de clasificación`; board title `Top jugadores`. |
| AFK / noob / OP | AFK / noob / OP | Kept; `está OP`. `novato` in polite text. |
| VIP | VIP | Roblox UI: `Servidores VIP`. |
| trade | intercambiar, intercambio | Roblox UI wording. Not `comerciar`, `negociar`. |
| inventory / backpack | inventario / mochila | `Inventario` is Roblox's label. |
| daily reward | recompensa diaria | |
| codes / redeem | códigos / canjear | Roblox button: `Canjear`. |
| group | comunidad | Roblox renamed groups; the page players join shows `Ver la comunidad`, `Unirse`. Use `comunidad`; `grupo` (kids' word, still in Roblox's store copy) only to match older game text. |
| like / favorite | Me gusta / favoritos | `Dale Me gusta`; Roblox: `Añadir a favoritos`, a favorited game is `Favorita`. |
| server | servidor | `servidor privado`, `servidor VIP`. |
| friends | amigos | Roblox renamed Conexiones back to Amigos in April 2026 (`Amigos de confianza`); a few old strings still say `conexiones`. |
| badge | insignia | Roblox UI mixes `insignia` and `emblema`; pick `insignia`. |

## Grammar traps in UI strings
- Plurals: Roblox picks no plural form, and `1 monedas` and `0 moneda` are both wrong. Use a label (`Monedas: {count}`) or make the noun fixed and the number free (`¡Faltan monedas! Necesitas {amount} más.`). Never `moneda(s)`.
- Millions take `de`: `1 millón de monedas`, `2 M de monedas`. Label form (`Monedas: 1.5M`) sidesteps it.
- {player} can be any gender. Use verbs, not participles or adjectives: `{player} quedó fuera`, not `{player} fue eliminado`; `{player} ya puede jugar`, not `{player} está listo`.
- No article before an inserted noun of unknown gender (`un {pet}` fails for `Gata`). Make a known noun the head: `¡Nueva mascota: {pet}!`.
- Adjectives follow the noun and agree: `Dragón legendario`, `Gata legendaria`. Standalone rarity tags take the masculine, Spanish's unmarked default and how players say them (`me salió un legendario`): `Raro`, `Épico`, `Legendario`, `Secreto`; `Común` never changes. They match most pet names (`Dragón`, `Perro`, `Unicornio`), so never glue a tag to a noun (`{rarity} {pet}`, `mascota {rarity}`): put it in parentheses, `{pet} ({rarity})`.
- Word order flips: `2x Coins` -> `Monedas x2`; `Pet Shop` -> `Tienda de mascotas`; `Player's Base` -> `Base de {player}`.
- Sentence case for titles, buttons and item names: `Recompensa diaria`, `Poción de suerte`, never `Recompensa Diaria`. Weekdays and months are lowercase.
- `lo`, not `le`, for a masculine direct object (no leísmo): `Lo ayudas a escapar`.
- `estar` for states, `ser` for identity: `¡Esta espada está OP!`, `Ahora eres nivel 10`.

## Typography and formatting
- Opening `¡` and `¿` are mandatory and open where the exclamation starts: `Estás AFK. ¡Muévete!`. No space before `! ? : ;`.
- Accents stay on capitals: `ÉPICO`, `¡MÁS MONEDAS!`, never `EPICO`.
- Quotes: double quotes around typed text: `Escribe "FREEPETS"`. `« »` is the normative form, but Microsoft es-MX uses English double quotes and so do Latin American UIs.
- Numbers: Mexico, Peru, most of Central America and the US write `1,250.5`; Argentina, Colombia, Chile and Costa Rica use a decimal comma (`1.250,5`), and the `es` column serves all of them. Game code formats numbers; never type a separated figure into the text. Tell the developer: format by the player's country if the game can, else use Mexico's `1,250.5` (largest audience) or abbreviate (`1.2K`).
- Percent: no space (`+10%`): CLDR es-MX, es-419 and es-AR all write it so. RAE norms and Spain prefer `10 %`; don't copy it from Spain-leaning sources (Roblox's Spanish help reportedly spaces it).
- Durations: `h`, `min`, `s`, `d` with no period or plural: `3 h 20 min`, `2 d 5 h`. `3h 20m` from code is still understood.
- Ellipsis: no space before it: `Cargando...`.
- Keys: keep the key letter and say `Presiona`: `Presiona E para abrir`. Touch: `Toca`; mouse: `Haz clic`. `Pulsa` is understood (Microsoft es-MX uses it for taps) but `Presiona` is the Latin American norm for keys; Spain's `pincha` (click) reads foreign.

## Do not translate / keep as is
- Robux, Roblox, Roblox Plus, Premium, VIP, AFK, OP, noob, obby, tycoon.
- Usernames, display names, {params} and promo codes (`FREEPETS` is typed exactly).
- The game title, unless the developer ships a Spanish title. Translate item, pet and rarity names: `Lucky Potion` -> `Poción de suerte`, `Dragon` -> `Dragón`.
- Roblox UI names as Roblox shows them: `Me gusta`, `Favoritos`, `Pases`, `Canjear`.
- Brand names: Discord, YouTube, TikTok.

## Rendering on Roblox
- Spanish needs only Latin-1 letters (á é í ó ú ü ñ, their capitals, ¡ ¿) and no shaping. Roblox's built-in fonts are expected to cover them: Roblox auto-translates every game into Spanish and shows it in those fonts (unverified per font: no Roblox doc lists coverage).
- Imported or pixel fonts may lack `ñ`, accented capitals or `¡ ¿`. Preview every custom font with `¡ÑANDÚ ÉPICO!`.
- Luau `string.upper` is byte-based: `string.upper("Dragón ñandú")` gives `DRAGóN ñANDú` (tested in Studio 2026-11-08). Write caps into the translation instead of upper-casing in code.
- Longer strings plus TextScaled shrink Spanish text below the English size; check that `Reclamar` and `Comprar` stay readable on phones. Check `Á É ¡` tops in tight single-line labels with ClipsDescendants.

## Mistakes machine translation makes here
- Spain forms: `ordenador`, `móvil` -> `computadora`, `celular` (or neutral `dispositivo`); `¡Uníos!` -> `¡Únanse!`.
- Present perfect: `¡Has ganado!` -> `¡Ganaste!`.
- Formal usted: `Ingrese el código` -> `Ingresar código`; `Vuelva mañana` -> `Vuelve mañana`.
- "Claim" as `Afirmar` or `Reivindicar` -> `Reclamar`.
- "Like the game" read as a comparison (`Como el juego`) -> `Dale Me gusta al juego`.
- "Hatch" as `escotilla` or `incubar` -> `abrir` (`¡Abre un huevo!`).
- "Rebirth" button as the noun `Renacimiento` -> `Renacer`.
- "Trade" as `Comerciar` or `Negociar` -> `Intercambiar`.
- Counted nouns: `1 Monedas` -> `Monedas: 1`.
- English title case: `Mejores Jugadores` -> `Mejores jugadores`.
- Calques: `hacer cuarto` (make room) -> `liberar espacio`; `Camina en el círculo` (walk around inside it) -> `Entra al círculo`.
- English word order kept: `¡Eclosionaste un {rarity} {pet}!` (`un Legendario Abeja`) -> `¡Nueva mascota: {pet} ({rarity})!`.
- Mexican slang from an `es-mx` prompt: `¡Qué padre!` -> `¡Genial!`; `chamba` -> `trabajo`.
- `coger` in any sense: `Coge las monedas` -> `Recoge las monedas`.

## Reference translations
| key | translation | note |
|---|---|---|
| `menu.play` | Jugar | Roblox's own verb (`Jugar como invitado`). |
| `shop.title` | Tienda | |
| `shop.buy` | Comprar | Infinitive, as in Roblox's buttons. |
| `reward.claim` | Reclamar | Standard Latin American game verb for taking a reward (game usage; not seen in Roblox's own UI). Not `Cobrar` (money owed). |
| `rebirth.button` | Renacer | Verb, not `Renacimiento`. |
| `rebirth.confirm` | ¿Renacer ahora? Perderás tus monedas, pero ganarás un multiplicador permanente de x{multiplier}. | "boost" made concrete as `multiplicador`; `x` before the number. |
| `coins.need_more` | ¡Faltan monedas! Necesitas {amount} más. | Fixed noun, invariable `más`: right for 1 and 1,250. |
| `coins.count` | Monedas: {count} | Label form avoids `1 monedas`. Passes 16 from `1,000,000` (18); abbreviate big counts in code (`1.2M`). |
| `egg.hatched` | ¡Nueva mascota: {pet} ({rarity})! | `mascota` as head avoids un/una; parentheses free the tag from agreeing (`Abeja (Legendario)`). "You hatched" dropped so no verb needs `un`/`una` before {pet}. |
| `rarity.legendary` | Legendario | Masculine, the unmarked label form; never `mascota {rarity}`. |
| `pet.name.dragon` | Dragón | |
| `chat.player_joined` | {player} se unió al juego | Simple past; no gender. |
| `trade.request` | {player} quiere intercambiar contigo | |
| `prompt.open_shop` | Presiona E para abrir | 21/22. |
| `pass.buy_price` | Comprar por {price} Robux | Matches Roblox's `por {robux} Robux` pattern. Fits 22 up to a 4-digit price; past that use `{price} Robux`. |
| `pass.coins2x` | Monedas x2 | |
| `pass.vip` | VIP | |
| `reward.daily_title` | Recompensa diaria | Sentence case. |
| `reward.come_back` | ¡Vuelve en {time} para reclamar tu próxima recompensa! | |
| `codes.placeholder` | Ingresar código | `Ingresa el código` is 17 > 16. `Introducir` is Spain. |
| `codes.invalid` | Ese código no es válido o ya expiró. | `venció` also fine. |
| `social.like_reward` | ¡Dale Me gusta y gana una <b>Poción de suerte</b> gratis! | 50 visible chars; "al juego" cut to fit. `Me gusta` is Roblox's Like label. |
| `social.group_reward` | ¡Únete a nuestra comunidad y gana un premio gratis! | `comunidad` matches the Roblox page the player lands on; "unlock" folded into `gana` to fit. |
| `afk.warning` | Estás AFK. ¡Muévete para seguir ganando! | |
| `leaderboard.title` | Top jugadores | `Mejores jugadores` is 17 > 16; `top` is everyday Latin American gamer Spanish. `Los mejores` also fits. |
| `level.up` | ¡Subiste de nivel! Ahora eres nivel {level}. | |
| `tutorial.sell` | Entra al círculo brillante para vender tus mascotas. | |
| `inventory.full` | ¡Mochila llena! Vende mascotas para liberar espacio. | Shortened opener keeps a margin under 60. |
| `settings.music` | Música | |
| `settings.on` | Sí | Pair with `No`. `Activado` (8) is too long and would need `Activada` beside `Música`; `ON`/`OFF` is also understood. |
| `loading` | Cargando... | |
| `event.ends_in` | El evento termina en {time} | |
| `item.op` | ¡Esta espada está OP! | |
| `friends.boost` | +{percent}% de bonificación por cada amigo en tu servidor | No space before `%`; Roblox says `amigos` again. |

## Sources
1. Microsoft Spanish (Neutral) Localization Style Guide -- https://aka.ms/spanish-neutral-styleguide
2. Microsoft Spanish (Mexico) Localization Style Guide -- https://aka.ms/spanish-mexico-styleguide
3. CLDR plural rules -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. CLDR number data for es-MX, es-419, es-AR, es-PE, es-CR, es-CO, es-US -- https://github.com/unicode-org/cldr-json/tree/main/cldr-json/cldr-numbers-full/main
5. Roblox language codes -- https://create.roblox.com/docs/production/localization/language-codes
6. Roblox Spanish web UI strings (localization bundles loaded by roblox.com/es game pages, read 2026-11-08) -- https://www.roblox.com/es/games/11901437921/Tapping-Fantasy-Simulator
7. Roblox Help (es), Experiencias en Roblox -- https://en.help.roblox.com/hc/es/articles/115004734603
8. Roblox Help (es), Pases de Experiencias -- https://en.help.roblox.com/hc/es/articles/203314040
9. Roblox Help (es), Intercambio en Roblox -- https://en.help.roblox.com/hc/es/articles/203313310
10. Roblox Help (es), marking an experience as a favorite -- https://en.help.roblox.com/hc/es/articles/203313670
11. Roblox Help (es), Suscripción a Roblox Premium -- https://en.help.roblox.com/hc/es/articles/360024256251
12. Roblox Help (es), adding trusted friends -- https://en.help.roblox.com/hc/es/articles/46158344285204
13. Roblox Newsroom (es), Conexiones renamed back to Amigos -- https://about.roblox.com/es/newsroom/2026/04/expanding-trusted-friends
14. XboxPlay (es), rebirth guide for Pet Simulator 99 -- https://xboxplay.games/es/news/como-renacer-en-roblox-pet-simulator-99-48017
15. El Comercio (Ecuador), gamer slang glossary -- https://www.elcomercio.com/games/farmear-campear-npc-y-afk-guia-de-lenguaje-para-entender-a-los-gamers/
16. Red Bull (Spain), gaming glossary, used for the Spain contrast -- https://www.redbull.com/es-es/gaming-diccionario-terminos-jerga
17. Roblox Creator Docs (es), Productos de desarrollador -- https://create.roblox.com/docs/es-es/production/monetization/developer-products
18. Roblox Newsroom, Roblox Plus launch and end of new Premium sign-ups -- https://about.roblox.com/newsroom/2026/04/introducing-roblox-plus-subscription
19. Roblox on the Mexican App Store (Spanish copy: juegos, amigos, grupo, tú) -- https://apps.apple.com/mx/app/roblox/id431946152?l=es-MX
