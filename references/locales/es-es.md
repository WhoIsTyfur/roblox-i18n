# Spanish (Spain) (es-es) -- translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `es-es` only. The bare `es` column carries Latin American Spanish (es-mx); never put Spain forms there |
| Script, direction | Latin, LTR; needs á é í ó ú ü ñ Ñ ¡ ¿ « » |
| Address the player as | informal "tú"; a group as "vosotros" (os, vuestro); never "usted", never "ustedes" |
| Text expansion vs English | about +20-30%, one-word buttons can more than double ("Buy" -> "Comprar") (unverified estimate) |
| Plural categories (CLDR) | one, many, other ("many" = exact millions: "1.000.000 de monedas") |
| Model confidence | high -- huge training data; the main risk is drifting into Latin American forms |
| Native review before shipping | recommended |

## Audience and register
- Players are Spanish kids and teens who play on móvil, tablet, ordenador or consola. Write like a friendly game, not a manual: short, warm, a little playful.
- One player is always "tú": "Pulsa", "Entra", "Vuelve", "tu mochila". Microsoft's es-ES guide also recommends "tú" and drops "please": "Prueba otra vez", not "Por favor, inténtelo de nuevo".
- A group (server announcements, event banners, the whole lobby) is "vosotros", the form Spain uses and Latin America does not: "¡Preparaos, el jefe llega en 10 s!", "¿Estáis listos?", "Os esperamos en el evento". Never "¡Prepárense!" or "Les damos...", which read as Mexican or as stiff "ustedes".
- Vosotros imperative + "os" drops the final -d: "preparaos", "uníos", "daos prisa". The infinitive form ("prepararos", "uniros") is a common spoken error; do not write it. Exception: "idos" (RAE tolerates "iros").
- Buttons and menu items: infinitive or a short noun ("Jugar", "Comprar", "Tienda", "Canjear código"). Instructions and toasts: tú imperative ("Pulsa E para abrir").
- Something that just happened takes the present perfect in Spain: "¡Has subido de nivel!", "{player} se ha unido a la partida". The simple past ("¡Subiste de nivel!") reads Latin American.
- Hype that sounds natural in Spain: "¡Genial!", "¡Increíble!", "¡Qué pasada!", "¡Toma ya!", "¡Mola!". Never use Mexican or Southern Cone hype ("¡Qué padre!", "chido", "chévere", "bacán").
- Swap formal verbs for everyday ones (Microsoft list): "desear" -> "querer", "solicitar" -> "pedir", "proporcionar" -> "dar", "sin embargo" -> "pero".
- Roblox's own Spanish menus are one neutral, Latin American-leaning variant: its `es` and `es-es` CoreScript columns are identical ("Agrega amigos", "Presiona la tecla", "se unió a la experiencia"). Take platform nouns from it, not its verbs or tenses; a game for Spain still writes Spain Spanish.
- Kid-safe: no "joder", "hostia", "coño" or "tío/tía" as a form of address, even though teens say them. "Flipar" and "mola" are fine.

## Roblox and gaming vocabulary
| English | Use in es-es | Note |
|---|---|---|
| Robux | Robux | Invariable: "100 Robux", never "Robuxes" |
| game pass | pase | Roblox's Spanish Creator docs use "pase"; players and press also say "gamepass". Shop UI: "Pase VIP" |
| developer product | producto (de desarrollador) | Players never see the term; name the item itself ("Pack de 500 monedas") |
| experience / game | juego | Roblox's 2026 Spanish newsroom says "juegos"; its in-game menus still say "experiencia". Players say "juego" |
| obby | obby | Kept; "parkour" also understood |
| tycoon | tycoon | Kept as a genre word, also in titles |
| simulator | simulador | "Simulator" stays only inside a game's title |
| rebirth | renacer (button), renacimiento (noun) | Players also say "hacer rebirth"; UI uses "Renacer" |
| pet | mascota (fem.) | "tus mascotas", "mascota legendaria" |
| egg / hatch | huevo / abrir, eclosionar | Roblox's Spanish docs: "¡Tu huevo ha eclosionado!"; button: "Abrir" |
| coins / gems | monedas / gemas | |
| boost | potenciador | "boost" is spoken; in text "+25 % extra" is often smoother |
| multiplier | multiplicador | Write "x2", "x1,5" |
| XP | XP | Keep the abbreviation; spelling it out ("experiencia") clashes with Roblox's "experiencia" |
| level up | subir de nivel | "¡Has subido de nivel!" |
| quest | misión | "Misiones diarias" |
| leaderboard | clasificación, ranking | "Clasificación" is Roblox's own player-list label; lobby board title: "Los mejores" |
| AFK | AFK | Kept: "Estás AFK" |
| noob | noob, novato | "novato" in UI; "noob" only in jokey flavor text |
| OP | chetado / chetada | Spain gamer slang for overpowered: "¡Esta espada está chetada!" |
| VIP | VIP | Kept, all caps |
| trade | intercambiar / intercambio | "tradear" is spoken only |
| inventory / backpack | inventario / mochila | |
| daily reward | recompensa diaria | |
| codes | códigos; redeem = canjear | "Canjear" for the button |
| group | comunidad | Roblox renamed player-facing Groups to Communities (Nov 2024); its Spanish in-game UI says "Insignia de la comunidad". Creator Hub keeps "grupo" |
| like / favorite | Me gusta / favoritos | "Dale a Me gusta" (Roblox's own label unverified); "Añadir a favoritos" |
| server | servidor | |
| friends | amigos | Roblox switched "Conexiones" back to "Amigos" in April 2026 ("Amigos de confianza"); its avatar menu says "Añadir amistad", a few old strings still "conexiones" |
| Premium / Roblox Plus | Premium / Roblox Plus | Brand names, untranslated; Roblox Plus replaced new Premium sign-ups on 30 April 2026 |
| shop / update | tienda / actualización | |

## Grammar traps in UI strings
- Plurals: "1 moneda" / "2 monedas", and the verb agrees too ("falta 1" / "faltan 2"). With no plural selection, put the number where nothing agrees with it: a label ("Monedas: {count}") or after a verb with a fixed form ("Necesitas {amount} más"). Never "{count} monedas" when count can be 1. Zero takes the plural: "0 monedas".
- Millions need "de" before the noun ("1.000.000 de monedas", "2 millones de monedas"); the label form avoids this too.
- Gender: every noun is masculine or feminine and adjectives agree. "{rarity} {pet}" breaks when the pet is feminine ("Abeja Legendario"). Isolate it: "{pet} ({rarity})" or "Rareza: {rarity}". Standalone rarity tags use the masculine: "Común", "Poco común", "Raro", "Épico", "Legendario", "Mítico".
- {player} can be any gender. Avoid adjectives and participles that agree with the player: not "{player} está listo", but "{player} ya puede jugar"; not "¡Bienvenido, {player}!", but "¡Hola, {player}!". "Se ha unido" is safe because the participle after "haber" never changes.
- Articles before an inserted noun carry gender ("un Dragón" / "una Abeja"). Use a colon instead: "Has conseguido: {item}".
- "a" + "el" -> "al", "de" + "el" -> "del", but not before a name that starts with "El": "Ve a El Bosque Oscuro" (RAE keeps the article of proper names uncontracted).
- Word order: adjectives follow the noun ("Dragón legendario", "Monedas x2"); English noun stacks become "de" phrases ("Lucky Potion" -> "Poción de suerte", "pet storage" -> "almacén de mascotas").
- Capitalization: sentence case for titles, buttons and item names ("Recompensa diaria", not "Recompensa Diaria"). Days, months and languages are lowercase ("lunes", "inglés"). Capitals keep their accents: "ÚNETE", "MÁS".
- Group nouns: the generic masculine ("jugadores", "amigos") is standard. Where a neutral form costs nothing, prefer it: "¿Todo listo?" over "¿Listos?", "todo el mundo" over "todos".

## Typography and formatting
- Every question and exclamation opens with ¿ or ¡ where the question starts, not always at the string start: "Estás AFK. ¡Muévete para seguir ganando!". No space after ¡ ¿ or before ! ?
- Ellipsis: three periods with no space before: "Cargando...".
- Quotes: use « » for names quoted inside a sentence («Poción de suerte»), the RAE's first choice and fine in Latin-1 fonts; never mix with English curly quotes in one game.
- Numbers: decimal comma ("x1,5", "2,5 s"). Thousands: none in 4-digit numbers ("1250"), a point from 5 digits ("12.500", "1.250.000"). This is CLDR's es-ES format (what `Intl.NumberFormat("es-ES")` prints); RAE prefers a space ("12 500"), which can wrap in a TextLabel. Never "1,250": in Spain that reads as one point two five. Game code that pre-formats "1,250", "1.5" or "3h 20m" in English breaks every string it fills: flag it to the developer, the translation cannot fix it.
- Percent: a space before % ("+25 %"), the RAE 2010 rule and CLDR's es-ES format; use this by default. Roblox's own Spanish UI writes "10%", and a wrapping label can split "25" from "%", so "25%" is acceptable in tight labels. Never mix the two in one game.
- Durations use symbols with a space and no period: "3 h 20 min", "2 d 5 h", "45 s". If game code outputs "3h 20m", ask for "min", since "m" is meters.
- Clock: 24-hour, "18:30".
- Keys: "Pulsa E" (Spain), not "Presiona E" (Latin America, and Roblox's own neutral menus). Spanish key names: "Mayús" (Shift), "Intro" (Enter), "Espacio", "Retroceso" (Backspace), "Ctrl", "Esc".
- Avoid em dashes in UI text; use a comma, a colon or a new sentence.

## Do not translate / keep as is
- Roblox, Robux, Roblox Plus, Premium, VIP, AFK, XP and other brands (Discord, YouTube, TikTok).
- The game title ("Pet Hatch Tycoon") unless the developer ships a Spanish title.
- Promo codes exactly as typed ("FREEPETS"), usernames and display names, key letters (E, Q, F).
- Meme names and imported meme characters stay as players know them.
- Do translate item names, pet names and rarities ("Poción de suerte", "Dragón", "Legendario"); kids expect them in Spanish.

## Rendering on Roblox
- Spanish needs only Latin-1 characters. Roblox ships its own Spanish menus in Builder Sans, so that font covers them; Source Sans, Montserrat, Arimo and the other Google-derived families are expected to (unverified per font).
- A font lacking a glyph falls back to another typeface mid-word (DevForum reports this for Cyrillic in Source Sans). Decorative or pixel fonts are the risk: check that ñ, ¡ and ¿ appear in the game's display font.
- TextScaled: accented capitals (Á, É, Ñ) are taller; check that accents are not clipped in tight labels and all-caps titles.
- What to verify in Studio: a TextLabel with "¡¿ÁÉÍÓÚÜÑ áéíóúüñ «»" in every font the game uses, and the longest buttons ("Comprar", "Reclamar") at phone size.

## Mistakes machine translation makes here
- Latin American vocabulary: "Presiona E" -> "Pulsa E"; "Ingresa el código" -> "Introduce el código"; "celular", "computadora" -> "móvil", "ordenador"; "video" -> "vídeo"; "carro" -> "coche"; "hacer espacio" -> "hacer sitio"; "entrar al círculo" -> "entrar en el círculo".
- "ustedes" for a group: "¡Únanse a la comunidad!" -> "¡Uníos a la comunidad!"; "Les damos 100 monedas" -> "Os damos 100 monedas".
- Infinitive as imperative: "¡Prepararos!" -> "¡Preparaos!".
- Simple past for a fresh event: "{player} se unió al juego" -> "{player} se ha unido a la partida".
- Formal "usted": "Inténtelo de nuevo" -> "Prueba otra vez"; "¿Desea continuar?" -> "¿Quieres seguir?".
- Missing opening marks: "Nivel superado!" -> "¡Nivel superado!".
- English title case: "Recompensa Diaria" -> "Recompensa diaria".
- English number format: "1,250 monedas" -> "1250 monedas"; "1.5x" -> "x1,5"; "25%" -> "25 %".
- Broken agreement or order: "Legendario Dragón" -> "Dragón legendario"; "Abeja legendario" -> "Abeja legendaria".
- Literal gamer slang: "Esta espada es OP" -> "¡Esta espada está chetada!".
- Latin American terms Microsoft flags for Spain: "costo" -> "coste", "reporte" -> "informe", "checar" -> "comprobar".
- False friends: "ignorar" for "Ignore" -> "Pasar" or "Omitir"; "actualmente" for "actually" -> "en realidad"; "embarazado" for "embarrassed" -> "avergonzado".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Jugar | |
| shop.title | Tienda | |
| shop.buy | Comprar | |
| reward.claim | Reclamar | The usual reward verb in Spain-localized games, and correct Spanish (DLE: to ask for what you are owed); "Recoger" is an equally natural choice (game usage from memory, not re-checked) |
| rebirth.button | Renacer | |
| rebirth.confirm | ¿Renacer ahora? Perderás tus monedas, pero tendrás un multiplicador permanente de x{multiplier}. | {multiplier} must arrive as "1,5", not "1.5" |
| coins.need_more | ¡Faltan monedas! Necesitas {amount} más. | Number placed where nothing agrees with it, so 1 works |
| coins.count | Monedas: {count} | Label form avoids "1 monedas". {count} arrives pre-formatted in English ("1,250"): the code must format it Spanish. From 7 digits ("Monedas: 1.250.000", 18) it passes 16; abbreviate in code ("1,25 M") |
| egg.hatched | ¡Nueva mascota: {pet} ({rarity})! | Parentheses avoid gender agreement between pet and rarity. "¡Te ha tocado un {pet} {rarity}!" only if every pet name is masculine. A 14-char pet plus a 12-char rarity gives 46 (English worst case: 42) |
| rarity.legendary | Legendario | Masculine default for rarity tags |
| pet.name.dragon | Dragón | |
| chat.player_joined | {player} se ha unido a la partida | "partida" is Spain's word for a game session |
| trade.request | {player} quiere intercambiar contigo | |
| prompt.open_shop | Pulsa E para abrir | |
| pass.buy_price | Comprar por {price} Robux | Fits 22 up to a 4-digit price; at 5 digits use "{price} Robux" |
| pass.coins2x | Monedas x2 | |
| pass.vip | VIP | Kept |
| reward.daily_title | Recompensa diaria | |
| reward.come_back | ¡Vuelve dentro de {time} a por otra recompensa! | "a por" is everyday Spain Spanish; {time} as "3 h 20 min" |
| codes.placeholder | Introduce código | "Introduce el código" if the box allows 19 |
| codes.invalid | Ese código no es válido o ha caducado. | |
| social.like_reward | ¡Dale a Me gusta y llévate una <b>Poción de suerte</b> gratis! | Exactly 55 visible characters; "al juego" dropped to fit |
| social.group_reward | ¡Únete a nuestra comunidad y llévate un premio gratis! | "comunidad" follows Roblox's Groups -> Communities rename |
| afk.warning | Estás AFK. ¡Muévete para seguir ganando! | |
| leaderboard.title | Los mejores | "Mejores jugadores" is 17, one over the limit; "Clasificación" (Roblox's label) also fits. Avoid "Top jugadores" |
| level.up | ¡Has subido de nivel! Ya eres nivel {level}. | Present perfect, the Spain form |
| tutorial.sell | Entra en el círculo brillante para vender tus mascotas. | "entrar en", not "entrar a" |
| inventory.full | ¡Tu mochila está llena! Vende mascotas para hacer sitio. | |
| settings.music | Música | |
| settings.on | Sí | Roblox's own toggle says "Activado" (8), over the limit; "Sí"/"No" is a standard Spanish options-menu pair. "ON" also works if the game keeps English toggles |
| loading | Cargando... | |
| event.ends_in | El evento acaba en {time} | 26 with "2 d 5 h" |
| item.op | ¡Esta espada está chetada! | Spain gamer slang for OP |
| friends.boost | +{percent} % extra por cada amigo en tu servidor | "boost" rendered as "extra"; space before % |

## Sources
1. Microsoft Spanish (Spain) Localization Style Guide (via aka.ms/spanish-spain-styleguide) -- https://download.microsoft.com/download/9/a/1/9a19beca-597c-417b-a2c2-0f1ea5a1e6c3/spa-esp-StyleGuide.pdf
2. Microsoft Localization Style Guides index -- https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
3. Unicode CLDR language plural rules -- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
4. RAE Ortografía, how to write percentages (returned 403 on 2026-11-08; rule matches CLDR's "25 %") -- https://www.rae.es/ortografía/la-expresión-de-los-porcentajes
5. RAE note on the imperative "iros" / "idos" -- https://aplica.rae.es/clweb/«iros» imperativo.pdf
6. Roblox, "¿Qué es Roblox?" (Spanish) -- https://about.roblox.com/es/what-is-roblox
7. Roblox newsroom (Spanish), April 2026, "Conexiones" back to "Amigos" -- https://about.roblox.com/es/newsroom/2026/04/expanding-trusted-friends
8. Roblox Creator docs (es-es), game passes -- https://create.roblox.com/docs/es-es/production/monetization/game-passes
9. Roblox Creator docs (es-es), experience notifications -- https://create.roblox.com/docs/es-es/production/promotion/experience-notifications
10. DevForum, Introducing Roblox Communities -- https://devforum.roblox.com/t/introducing-roblox-communities/3268307
11. Roblox newsroom (Spanish), April 2026, introducing Roblox Plus -- https://about.roblox.com/es/newsroom/2026/04/introducing-roblox-plus-subscription
12. DevForum, Builder font and Gotham/Arial deprecation -- https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222
13. DevForum, Source Sans missing Cyrillic glyphs (fallback behavior) -- https://devforum.roblox.com/t/source-sans-cyrillic-characters-missing/483144
14. Hola.com (Spain), gamer slang guide for parents -- https://www.hola.com/padres/20231010351354/guia-jerga-gamer-para-padres-de-adolescentes/
15. VidaExtra (Spain), Roblox animal games -- https://www.vidaextra.com/guias-y-trucos/roblox-mejores-juegos-animales
16. EarlyGame ES, Rebirth Champions Ultimate codes guide -- https://earlygame.com/es/guides/codigos/rebirth-champions-ultimate-codigos
17. Roblox client CoreScript translations, `es` and `es-es` columns (ExtraContent/translations/CoreScriptLocalization.csv, Roblox build of 2026-11-05) -- local file from the Roblox install
18. ICU 77 / CLDR 47 es-ES number and percent formats, checked with Node `Intl.NumberFormat` -- https://cldr.unicode.org/
