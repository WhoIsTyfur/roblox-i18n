# Czech (cs-cz) translation guide

## At a glance
| | |
|---|---|
| Roblox locale / column | `cs-cz` (the only Czech locale; no bare `cs` column needed) |
| Script, direction | Latin with diacritics (á č ď é ě í ň ó ř š ť ú ů ý ž), LTR |
| Address the player as | informal singular "ty" (tykání) everywhere; never "vy" or capitalized "Vy" |
| Text expansion vs English | sentences about -20% to +25% (no articles; the reference set below is +3% overall); short buttons up to +100% ("Buy" -> "Koupit", "On" -> "Zap.") |
| Plural categories (CLDR) | one, few, many, other |
| Model confidence | medium: grammar is well covered and Minecraft's Czech text is a kids'-game model, but Roblox has no Czech UI to copy platform terms from, and Roblox kid slang is thinly documented |
| Native review before shipping | strongly recommended (seven cases plus gender agreement around placeholders) |

## Audience and register
- Players are in Czechia; Slovak kids also read Czech easily. Write standard Czech with no regional slang, and never let Slovak words slip in (see mistakes).
- Roblox's own website and app are not offered in Czech: the Roblox locale API (checked 2026-11-08) flags `cs_cz` as off for the full experience and for sign-up, but on for in-game content. Czech kids likely run Roblox in English and meet Czech only inside games.
- How a player gets `cs-cz`: the in-experience Settings menu has a language dropdown listing the languages the experience supports; picking one calls `SetExperienceSettingsLocaleId` and is remembered per experience (Roblox CoreScripts `ExperienceLanguageSwitcher`; its flag is on for PC and Android, checked 2026-11-08). Czech only shows there once the game ships a cs-cz column. Whether a Czech device language selects it automatically is unverified. Test with Studio's Player Emulator set to cs-cz.
- Use "ty" in every string. Microsoft's Czech guide prefers the neutral plural "vy" for software and allows "ty" only where the context fits; Minecraft's Czech text, which Czech kids know, uses "ty" throughout ("Zemřel jsi!", "Stiskni %s", "Pohybuj se"). "Zadejte kód" in a kids' game reads like a school form. House choice: "Zadej kód", "Vrať se zítra". Never mix both in one game.
- Buttons, tabs and toggles: infinitive or noun, the Czech UI norm: "Hrát", "Koupit", "Získat", "Obchod". Tips and tutorials: ty-imperative: "Vejdi do kruhu", "Prodej mazlíčky".
- Hype sounds natural as short exclamations: "Super!", "Paráda!", "Hurá!", "Nová úroveň!", "Nenech si to ujít!".
- Prefer everyday words over bookish ones (Microsoft's list): "už" not "již", "ale" not "avšak", "nedá se" not "nelze", "dál" not "nadále", "nejdřív" not "nejprve", "teď" not "nyní", "koupit" not "zakoupit", "který" not "jenž".
- Prefer verbs and clauses to verbal nouns and instrumental phrases: "Když klikneš znovu, ..." not "Opětovným kliknutím ...".
- Don't blame the player in errors: "Kód je neplatný" rather than "Zadal jsi špatný kód" (also gendered, see below).
- Kid-safe slang is fine in flavor text ("totálně OP", "noob" in a joke). No insults and no swearing.

## Roblox and gaming vocabulary
| English | Czech | note |
|---|---|---|
| Robux | Robux | Latin. Undeclined after a number in UI: "100 Robux", "za 50 Robux". Czech Wikipedia declines it in prose ("Robuxy"); players write "robuxy/robuxů". |
| Premium | Premium | brand; Czech Wikipedia paraphrases it as "prémiové členství". |
| game pass | game pass / gamepass | Czech Wikipedia writes both ("game passů", "gamepassu"); in the shop just show the pass name. |
| developer product | name the item itself | players never see the term (Wikipedia: "vývojářský produkt"). |
| experience / game | hra | never "zážitek" or "zkušenost" (= experience points). Czech Wikipedia says "hry", "minihry". |
| obby | obby | "opičí dráha" (Czech kids' obstacle course) in descriptions (unverified for Roblox players). |
| tycoon / simulator | tycoon / simulátor | Czech spelling with á for simulátor. |
| rebirth | rebirth (button); znovuzrození (formal) | "Znovuzrození" is 12 chars, too long for most buttons; Czech gamers keep "rebirth" (unverified). |
| pet | mazlíček, pl. mazlíčci | "pet" is chat slang (unverified); UI says mazlíček. |
| egg / hatch | vejce / vylíhnout se | "Z vejce se vylíhl drak"; button "Otevřít". |
| coins / gems | mince / drahokamy | "diamanty" if the art shows diamonds. |
| boost / multiplier | bonus / násobič, "2×" | "boost" is gamer talk (unverified); "bonus" is plain Czech. |
| XP / level up | XP, zkušenosti / nová úroveň | slang verb "levelovat" exists (Čeština 2.0); "level" also understood. Pick level or úroveň per game. |
| quest | úkol | gamers also say "quest" [kvest], pl. "questy" (Čeština 2.0); UI says "úkol". |
| leaderboard | žebříček; "Nejlepší hráči" | |
| AFK | AFK | Latin capitals; slang verb "afkovat" (Čeština 2.0). |
| noob | nováček (UI); noob, said "nůb" (jokes) | feminine "noobka". |
| OP | OP; "přehnaně silný" | gamer use of OP in Czech unverified; Čeština 2.0 lists "op" only as "mobile operator". |
| VIP | VIP | "VIP server", "VIP výhody". |
| trade | výměna; vyměnit si | "trade/tradovat" in chat only (unverified). |
| inventory / backpack | inventář / batoh | keep whichever the source means. |
| daily reward | denní odměna | |
| codes | kódy; "Zadej kód"; redeem = "uplatnit" | never "vykoupit". |
| group | skupina; "Vstup do skupiny" | |
| like / favorite | like, "Dej hře like" / oblíbené, "Přidej do oblíbených" | Czech Roblox labels don't exist to copy. |
| server | server; soukromý server | |
| friends | přátelé (list labels); kamarád in sentences | Roblox's UI is English here (Friends / Connections), so no Czech label to match. "přítel" alone often means "boyfriend": write "za každého kamaráda". |
| event | event; událost (formal) | "event" is common gamer Czech (unverified). |

## Grammar traps in UI strings
- Plurals (CLDR): one = 1 ("1 den"), few = 2-4 ("2 dny"), many = decimals ("1,5 dne"), other = 0 and 5+ ("5 dní"). Note that 22-24 use "other" in Czech ("22 dní"), unlike Polish or Russian. One string per key, so never put {count} right before a countable noun.
  - Bad: "{amount} mincí" -> "2 mincí". Good: "Mince: {count}", "Chybí ti {amount}."
  - Numbers also drive verb agreement: "2 hráči čekají" but "5 hráčů čeká". Use "Čekající hráči: {count}".
  - Undeclined units are safe after a number: "{price} Robux", "{percent} %", "{multiplier}×", "{n} XP", "3 h 20 min".
- Gender: past tense, the conditional and short participles agree with the subject. {player} can be any gender, so:
  - use present tense, as Microsoft recommends: "{player} přichází do hry", "{player} ti nabízí výměnu";
  - or put a fixed head noun before the name: "Hráč {player} se připojil do hry" (Minecraft's Czech wording; the verb agrees with "hráč");
  - Microsoft also accepts "{player} se připojil(a)", but it looks clunky in a game.
- The player as "ty" is gendered too: "Získal jsi", "abys vydělával", "Jsi připraven?" all need (a). Use present, future or imperative: "Získáš", "ať dál vyděláváš", "Připraveno!".
- Adjective agreement: hard adjectives change with the noun's gender (vzácný drak, vzácná kočka, vzácné vejce); soft "-í" adjectives don't (legendární drak / kočka / vejce). Translate rarity labels in the masculine, agreeing with "mazlíček" or "předmět", and write "{rarity} mazlíček: {pet}!", never "{rarity} {pet}".
- Case: Czech has seven cases and a translated {pet} arrives in the nominative. Keep placeholders as subjects, after a colon or in parentheses. "Získal jsi {pet}" would need the accusative "draka". Let a head noun carry the case: "Obchod s hráčem {player}"; never add endings to usernames.
- Durations after "za" are safe because abbreviations don't decline: "za 3 h 20 min".
- Ordinals take a period: "5. úroveň"; "úroveň {level}" avoids the question.
- No articles: drop "a/the". Drop most "your": "Batoh je plný!" not "Tvůj batoh je plný!". When a possessive refers back to the subject, use svůj: "Prodej své mazlíčky", never "tvoje".
- English noun stacks become adjective + noun or a genitive: "Egg Shop" -> "Obchod s vejci", "Pet Storage" -> "Úložiště mazlíčků". Number + adjective compounds are written solid: "10% sleva", "2násobný bonus".
- Capitalization: sentence case for titles, buttons and item names: "Denní odměna", "Nejlepší hráči", "Lektvar štěstí".

## Typography and formatting
- No space before ! ? : ; and one space after, as in English.
- Quotes: „takto“ (low-high), nested ‚takto‘. Microsoft drops most quotes around names; never use English "..." in Czech text.
- Dashes: Czech has no em dash. Use the en dash with spaces as a sentence dash ("Jsi AFK – hýbej se!"), the en dash without spaces in ranges ("3–7"), the hyphen without spaces in compounds.
- Numbers: decimal comma ("1,5"), thousands separated by a space ("1 250"; a no-break space in code). The canonical {count} arrives as "1,250", which a Czech player reads as 1.25; flag it to the developer; same for a multiplier "1.5".
- Percent (ÚJČ, CLDR): a space before % for a quantity ("Šance: 10 %"); no space when the number works as an adjective ("20%" = "dvacetiprocentní": "+10% bonus", "50% sleva").
- Multiplier: "2×" (U+00D7) after the number, no space, reads "dvakrát" (ÚJČ); players type a Latin "2x".
- Time: h, min, s without a period (Microsoft also allows "hod."); compact timers "3 h 20 min", "2 d 5 h" (d is the SI symbol for day; "2 dny 5 h" is plainer if it fits). Never "m" for minutes: m is meters. If code outputs "3h 20m", flag it.
- Ellipsis: only on loading and progress labels ("Načítání…"), no space before.
- Keys stay Latin capitals: "Otevři klávesou E", "Stiskni E". Space bar = "mezerník".
- Single-letter prepositions and conjunctions (k, s, v, z, o, u, a, i) must not end a line in Czech typography: in long wrapped text put the real U+00A0 character (not an escape) after them ("v obchodě"). Roblox wrapping honors it: TextService measured "Jdi v" + U+00A0 + "obchod" breaking before "v", in Source Sans and Builder Sans (2026-11-08). Optional in short labels.
- Microsoft spells out numbers below 11 in running text ("tři zprávy"); in HUD labels and toasts digits are fine.

## Do not translate / keep as is
- Robux, Roblox, Premium, VIP, Roblox Studio: Latin. Robux stays undeclined after numbers. Roblox declines in sentences like any masculine noun: "hrát na Robloxu".
- Game titles ("Pet Hatch Tycoon"): keep in English; players search the English title.
- Usernames and display names: never translate, decline or add endings.
- Promo codes ("FREEPETS"): exactly as given, ASCII, same case; translate only the text around them.
- Key names (E, Q, Shift) stay Latin.
- Descriptive item names translate ("Lucky Potion" -> "Lektvar štěstí"); no hybrids like "Lucky lektvar".
- Established gamer loanwords may stay: AFK, XP, VIP, obby, tycoon, event, rebirth. Don't invent new ones.
- Never strip diacritics. Kids often chat without háčky and čárky, but UI text without them ("Ziskej odmenu") looks broken.

## Rendering on Roblox
- Czech needs Latin-1 (á é í ó ú ý) plus Latin Extended-A (č ď ě ň ř š ť ů ž).
- Checked 2026-11-08 against the cmap of the font files in a local Roblox Studio install (build of 2026-11-05): Builder Sans/Extended/Mono, Luckiest Guy (Roblox's file, unlike Google's "latin"-only listing), Bangers, Source Sans Pro, Montserrat, Nunito, Roboto, Oswald, Arimo, Ubuntu, Press Start 2P, Titillium Web, Comic Neue Angular, Patrick Hand, Special Elite and Grenze Gotisch have every Czech letter, both cases, plus „ “ – … ×.
- Missing letters: **Fredoka One** lacks č ď ě ň ř ť ů and their capitals (it has á é í ó ú ý š ž). It is a simulator favorite, so the main Czech risk. Creepster, Permanent Marker, Highway Gothic, Accanthis ADF Std and Balthazar lack the same seven; Denk One also lacks š ž; Roman Antique also lacks ž. A Studio test with Polish letters (2026-11-08) showed no boxes: the client draws missing letters from a thin sans fallback, so "Hřiště" in Fredoka One would mix two fonts inside one word (not yet tested with Czech letters). Switch cs-cz labels to a covering font (Luckiest Guy, Bangers, Builder Sans).
- Capitals with háček, čárka or kroužek (Č Ř Š Ž Ě Ů Á) are taller; in tight TextScaled labels check they aren't clipped (unverified).
- Luau string.upper changes only ASCII: "získáš" -> "ZíSKáš" (checked in Studio). Write uppercase text directly in the table.
- Czech letters are 2 bytes in UTF-8 (#"ř" is 2): string.sub and # can split "ř" into a broken glyph; utf8.len and utf8.offset are safe.
- Verify in Studio: Player Emulator set to Czech; a TextLabel with "Příliš žluťoučký kůň úpěl ďábelské ódy" (uses every Czech diacritic) and its uppercase form in every font the game uses; the longest strings (rebirth confirm, inventory full) at phone size.

## Mistakes machine translation makes here
- Slovak bleed: "Kúpiť", "Hrať", "odmena" -> "Koupit", "Hrát", "odměna". Slovak-only letters ľ ä ô ĺ ŕ never appear in Czech.
- "experience" as zážitek: "Nejlepší zážitek na Robloxu" -> "Nejlepší hra na Robloxu".
- "Claim" as nárokovat: "Nárokovat" -> "Získat"; "redeem" as vykoupit: "Vykoupit kód" -> "Uplatnit kód".
- Register mixing: "Stiskněte E a získáš odměnu" -> "Stiskni E a získáš odměnu".
- Gendered past with a bare username: "{player} se připojil ke hře" -> "Hráč {player} se připojil do hry" (or present "{player} přichází do hry").
- Gendered past for the player plus wrong case: "Získal jsi {pet}!" -> "{rarity} mazlíček: {pet}!".
- Number + noun: "Máš {count} mincí" -> "Mince: {count}".
- Calque "pro + verbal noun": "Stiskni E pro otevření" -> "Otevři klávesou E".
- English Title Case: "Denní Odměna" -> "Denní odměna".
- Wrong possessive: "Prodej tvoje mazlíčky" -> "Prodej své mazlíčky" (or just "Prodej mazlíčky").
- Literal slang: "Tento meč je přemožený" (= defeated) -> "Tenhle meč je totálně OP!".
- Stripped diacritics or English number format: "Ziskej 1,250 minci" -> "Mince: 1 250".

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Hrát | infinitive on buttons |
| shop.title | Obchod | |
| shop.buy | Koupit | |
| reward.claim | Získat | "Vyzvednout" is 10/10 |
| rebirth.button | Rebirth | kept English: "Znovuzrození" is 12 > max 10 |
| rebirth.confirm | Udělat rebirth teď? Přijdeš o mince, ale získáš trvalý bonus {multiplier}×. | future tense avoids gender; "1.5" should arrive as "1,5" |
| coins.need_more | Nemáš dost mincí! Chybí ti {amount}. | restructured so no noun follows the number |
| coins.count | Mince: {count} | colon avoids plural forms; "1,250" should be "1 250" (code issue) |
| egg.hatched | {rarity} mazlíček: {pet}! | "Legendary pet: Dragon!"; rarity tags in the masculine agree with "mazlíček" and avoid a gendered verb. Masculine tags on a feminine pet card ("Vzácný" over "Kočka") need native review; if they read wrong, use "Nový mazlíček: {pet} ({rarity})!" |
| rarity.legendary | Legendární | soft adjective, same form for every gender |
| pet.name.dragon | Drak | |
| chat.player_joined | Hráč {player} se připojil do hry | Minecraft's Czech join message; the verb agrees with "Hráč", so any gender works |
| trade.request | {player} ti nabízí výměnu | present tense avoids gender |
| prompt.open_shop | Otevři klávesou E | 17/22; avoids the "pro otevření" calque |
| pass.buy_price | Koupit za {price} Robux | Robux undeclined |
| pass.coins2x | 2× víc mincí | 12/14; "×" is U+00D7 |
| pass.vip | VIP | |
| reward.daily_title | Denní odměna | |
| reward.come_back | Vrať se za {time} pro další odměnu! | time should be "3 h 20 min" |
| codes.placeholder | Zadej kód | |
| codes.invalid | Kód je neplatný nebo už vypršel. | |
| social.like_reward | Dej hře like a získáš zdarma <b>Lektvar štěstí</b>! | "lektvar" accusative = nominative, so the tag wraps the plain name |
| social.group_reward | Vstup do naší skupiny a získej odměnu zdarma! | "získej", not the calque "odemkni" |
| afk.warning | Jsi AFK! Hýbej se, ať dál vyděláváš! | "ať" + present avoids gendered "abys vydělával" |
| leaderboard.title | Nejlepší hráči | "Žebříček" also fine |
| level.up | Nová úroveň! Teď máš úroveň {level}. | "Level up! Teď máš level {level}." if the game says level |
| tutorial.sell | Vejdi do svítícího kruhu a prodáš mazlíčky. | "your" dropped; future "prodáš" avoids gender |
| inventory.full | Batoh je plný! Prodej mazlíčky a uvolni místo. | |
| settings.music | Hudba | |
| settings.on | Zap. | pair with "Vyp." (Microsoft's UI abbreviation rule: cut after a consonant, add a period); "Zapnuto" is 7 > max 5. Minecraft's toggles say "Ano"/"Ne", also fine |
| loading | Načítání… | single ellipsis character |
| event.ends_in | Event končí za {time} | 22/28 with "2 d 5 h"; formal "Událost končí za {time}" |
| item.op | Tenhle meč je totálně OP! | gamer OP unverified; fallback "Tenhle meč je neskutečně silný!" |
| friends.boost | +{percent}% bonus za každého kamaráda na serveru | adjectival percent, no space; "kamaráda" avoids the boyfriend reading of "přítele" |

## Sources
1. Microsoft Czech localization style guide (PDF, via https://aka.ms/czech-styleguide): https://download.microsoft.com/download/7/b/5/7b57e4a1-d299-4238-9997-f3ac51d6f763/ces-cze-StyleGuide.pdf
2. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
3. CLDR Czech number symbols and formats: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-numbers-full/main/cs/numbers.json
4. Roblox language codes (Czech = `cs` / `cs-cz`): https://create.roblox.com/docs/production/localization/language-codes
5. Roblox locale API (cs_cz flags; checked 2026-11-08): https://locale.roblox.com/v1/locales
6. Roblox localization overview (per-player translation setting): https://create.roblox.com/docs/production/localization
7. roblox.com with a /cs/ path still renders English (checked 2026-11-08): https://www.roblox.com/cs/charts
8. Czech Wikipedia, "Roblox" (Robuxy, hry, miniher, prémiové členství, game passů / gamepassu): https://cs.wikipedia.org/wiki/Roblox
9. Čeština 2.0, "afk" (and "afkovat"): https://cestina20.cz/slovnik/afk/
10. Čeština 2.0, "noob" (pronounced nůb, feminine noobka): https://cestina20.cz/slovnik/noob/
11. Čeština 2.0, "levelovat": https://cestina20.cz/slovnik/levelovat/
12. Čeština 2.0, "op" (only "mobile operator", no gamer sense): https://cestina20.cz/slovnik/op/
13. Čeština 2.0, "quest" (gamer slang, pl. questy): https://cestina20.cz/slovnik/quest/
14. Minecraft Czech language file (ty-form, "Hráč %s se připojil do hry", "ANO"/"NE", "Lektvar štěstí"): https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.21/assets/minecraft/lang/cs_cz.json
15. ÚJČ Internetová jazyková příručka, symbols and spacing ("14 %" vs "20%" = adjective, "20×"): https://prirucka.ujc.cas.cz/?id=785
16. ÚJČ, numbers in compound words ("12%" = "12procentní", "8násobný"): https://prirucka.ujc.cas.cz/?id=790
17. Roblox CoreScripts in the local Studio install, `Modules/Settings/Pages/GameSettingsRowInitializers/ExperienceLanguageSwitcherInitializer.lua`, and live flag `FFlagEnableLocalesForExperienceLanguageSwitcher4`: https://clientsettingscdn.roblox.com/v2/settings/application/PCDesktopClient
18. Roblox Studio install `content/fonts` (cmap check with fontTools, 2026-11-08) and TextService wrap measurements in Studio, 2026-11-08
