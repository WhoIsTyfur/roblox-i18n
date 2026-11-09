# Bosnian (bs-ba) -- translation guide

**Script decision: write Latin (latinica), never Cyrillic.** Roblox's language codes page labels Bosnian "босански" (its locale API: "Босански"), but that is only a display label: Microsoft publishes its Bosnian guide for Latin only, CLDR expands `bs` (and `und-BA`) to `bs-Latn-BA`, Minecraft's Bosnian (`bs_ba`) is Latin, and Latin is the everyday script of the Federation of BiH, where the Bosnian-speaking kids live. Cyrillic in BiH belongs mostly to Republika Srpska and Serbian.

## At a glance
| | |
|---|---|
| Roblox locale / column | `bs-ba` (Roblox lists one Bosnian locale only, so a bare `bs` column adds nothing) |
| Script, direction | Latin (Gaj's alphabet with č ć đ š ž), LTR; ijekavian standard |
| Address the player as | informal singular "ti" ("Pritisni", "Kupi"); never "vi"/"Vi" |
| Text expansion vs English | about +10% over this guide's reference set (sentences -15% to +40%); one-word labels up to +150% ("Shop" -> "Prodavnica") |
| Plural categories (CLDR) | one, few, other |
| Model confidence | medium -- low-resource language; models drift into Croatian or Serbian forms and mix them, and kid gaming slang could not be confirmed |
| Native review before shipping | strongly recommended |

## Audience and register
- Readers: Bosniak kids in the Federation of BiH and the diaspora. Bosnian Croats and Serbs mostly set Croatian or Serbian. Everyone also understands Croatian and Serbian, but a polished game stays consistently Bosnian.
- Roblox has no Bosnian app UI: its locale service enables `bs_ba` for in-experience content only, not for the full app. Players see Roblox's own menus in English (or another language), so they know platform terms in English. How a player ends up with `LocaleId` = `bs-ba` is unverified -- test with Studio's Player Emulator.
- Use "ti" in every string. Microsoft addresses adults with "vi"; for 9-16 year olds that reads like a bank or a school notice. Minecraft's Bosnian uses ti ("Pritisni %s", "Otvori svoj inventar", "Umro si!"). Never mix: "Pritisni E i pokupi nagradu", not "Pritisnite E i pokupi nagradu".
- Buttons: 2nd-person singular imperative, the BCS software norm (Microsoft's own button label "Otkaži"): "Igraj", "Kupi", "Pokupi", "Otvori". Titles and tabs: nouns ("Prodavnica", "Dnevna nagrada").
- Sentences: short ti-imperatives: "Prodaj ljubimce", "Vrati se sutra". Prefer an infinitive after modal verbs, as Microsoft prescribes for Bosnian: "Trebaš prodati ljubimce", not the Serbian "Treba da prodaš ljubimce".
- Hype that sounds natural: "Super!", "Bravo!", "Ludilo!", "Novi nivo!", "Car si!". Stiff or adult: "Izvršite kupovinu", "Ostvarili ste", "Ovim putem", "Uspješno ste...". Microsoft's plain-word list applies: "pronaći" not "locirati", "uraditi" not "ostvariti", "treba" not "iziskuje".
- Drop possessives English needs and Bosnian doesn't (Microsoft rule): "Prodaj ljubimce", not "Prodaj tvoje ljubimce". When one is needed, use reflexive "svoj": "Pokaži svoje ljubimce".
- Write the Bosnian standard: ijekavian ("vrijeme", "mjesto", "sljedeći", "svijet"), future "kupit ćeš" (not Serbian "kupićeš"), Bosnian words ("muzika", "hiljada", "sedmica", "nivo", "ranac").
- Kid-safe: light slang is fine ("ludilo", "car si", "nub" in a joke); no insults ("budala", "glup si") and no swearing.

## Roblox and gaming vocabulary
| English | Bosnian | note |
|---|---|---|
| Robux | Robux | Latin, capital R. After a number keep it undeclined like a unit: "{price} Robux". In text without a number, decline: "Nemaš dovoljno Robuxa". Chat forms "robuxi/robuxa" (unverified). |
| Premium | Premium | Roblox brand; "Roblox Premium članstvo" in prose (as hr.wikipedia writes it). |
| game pass | propusnica; in the shop just the pass name | players say "gamepass" in chat (unverified). |
| developer product | (name the item) | players never see the term. |
| experience / game | igra | never "iskustvo" (= XP, know-how), although hr.wikipedia calls Roblox experiences "iskustva". |
| obby | obby; "parkur" in descriptions | (unverified which kids prefer) |
| tycoon | tycoon | no native genre word (unverified); keep in titles. |
| simulator | simulator | |
| rebirth | preporod; verb "preporoditi se" | 8 letters, fits buttons; chat "rebirth" (unverified). |
| pet | ljubimac, pl. ljubimci, acc. pl. ljubimce | "pet" in chat (unverified). |
| egg / hatch | jaje / izleći se; button "Otvori jaje" | past "izlegao se" agrees with "ljubimac" (masculine). |
| coins | novčići (sg. novčić) | "kovanice" sounds like real money. |
| gems | dragulji | "dijamanti" if the art shows diamonds. |
| boost | pojačanje | "boost" in chat (unverified); "bonus" fine for % bonuses. |
| multiplier | "2x" before a noun ("2x novčići"), "x{multiplier}" after one ("pojačanje x2") | write the sign, not a noun ("množitelj" is Croatian-leaning). |
| XP | XP, iskustvo | "+50 XP"; pick one per game. |
| level / level up | nivo / "Novi nivo!" | not "razina" (Croatian) or "level" (chat). |
| quest | zadatak, misija | |
| leaderboard | Najbolji igrači; rang-lista | hyphenated "rang-lista". |
| AFK | AFK | Latin capitals; "AFK si". |
| noob | početnik (UI); "nub" (jokes, unverified) | |
| OP | prejak | "OP" understood by gamers (unverified). |
| VIP | VIP | "VIP server", gen. "VIP-a". |
| trade | razmjena; "mijenjati se" | ijekavian; not "trgovina" (= commerce). |
| inventory / backpack | inventar / ranac | "ruksak" is the Croatian-leaning word. |
| daily reward | dnevna nagrada | |
| codes | kodovi; "Unesi kod"; redeem = "Iskoristi" | |
| group | grupa | "Pridruži se grupi". |
| like / favorite | lajk, "Lajkaj igru" / "Dodaj u omiljene" | "lajkati"; Serbian "lajkovati" (unverified which BiH kids prefer). |
| server | server; privatni server | "na serveru", not "u serveru". |
| friends | prijatelji | Roblox renamed Connections back to Friends in April 2026; there is no Bosnian Roblox label. Never "konekcije" or "veze". |

## Grammar traps in UI strings
- Plurals: one (1, 21, 31; not 11), few (2-4, 22-24; not 12-14), other (0, 5-20, 25...). One string per key, so never put {count} straight before a countable noun.
  - Bad: "{count} novčića" -> "1 novčića". Good: "Novčići: {count}", "Fali još {amount}" (number without a noun).
  - Safe after a number: undeclined units "{price} Robux", "{percent}%", "x{multiplier}", "{n} kom.".
- Past tense carries gender: "pridružio se" (m) / "pridružila se" (f). {player} can be anyone, so:
  - use a state or present tense: "{player} je sada u igri", "{player} ti nudi razmjenu";
  - or a fixed head noun: "Igrač {player} je napustio igru" (agrees with "igrač");
  - or a colon: "Pobjednik: {player}".
- The player as "you" has gender too: "Dobio si" / "Dobila si". Use future, present or a noun: "Dobit ćeš...", "Sada si na nivou 5", "Tvoja nagrada: ...". "Dobio/la si" is ugly; never use it.
- Adjectives agree with the noun: legendarni zmaj, legendarna mačka, legendarno jaje. Translate rarity tags in the masculine (agreeing with an implied "ljubimac") and never write "{rarity} {pet}"; use "Novi ljubimac: {pet} ({rarity})!".
- Seven cases. An inserted {pet} or item arrives in the nominative; keep it as subject or after a colon. "Kupio si {item}" would need the accusative ("Mačku") -> "Kupljeno: {item}". Usernames are never declined: carry the case on a noun: "Igraj s igračem {player}", "Poklon od igrača {player}".
- Future spelling: "izgubit ćeš", "dobit ćeš" (infinitive loses -i, separate "ćeš"); -ći verbs stay whole: "doći ćeš". Questions: "Želiš li nastaviti?"
- No articles: drop a/the ("a Rare Dragon" -> "rijedak zmaj"). Indefinite adjective for new things: "dobij besplatan napitak", not "besplatni".
- English noun stacks become genitive phrases or adjective + noun: "Coin Boost" -> "pojačanje novčića", "Pet Storage" -> "spremište za ljubimce". Microsoft: hyphen for some noun pairs ("web-stranica").
- Capitalization: sentence case for titles, buttons and item names ("Dnevna nagrada", "Napitak sreće"); days and months lowercase ("subota", "maj").

## Typography and formatting
- No space before ! ? : ; and one space after (Microsoft). "Bravo! Novi nivo!"
- Dashes: no em dash in Bosnian (Microsoft). En dash with spaces for asides and ranges: "Sarajevo – Zenica", "10 – 20". Hyphen for compounds and suffixes on abbreviations: "VIP-a", "XP-a".
- Quotes: CLDR gives „...” (U+201E, U+201D); Minecraft's Bosnian closes with “ (U+201C) instead, and Microsoft quotes UI names in straight "...". Use „...” or straight "...", one style per game, never English “...”. The period goes after the closing quote: Klikni „Kupi”. The pravopis 2018 rule is unverified.
- Ellipsis: three dots, no space before: "Učitavanje...".
- Numbers: decimal comma, period for thousands: "1,5", "1.250" (CLDR; Microsoft: "100.000 km"). Game code that outputs "1,250" reads to a Bosnian kid as one point twenty-five, so the developer must format {count}, {amount}, {price} and {multiplier} per locale for bs-ba; do not "fix" numbers inside the string.
- Percent: no space, as in CLDR's Bosnian pattern and Minecraft's Bosnian ("100%"): "+{percent}%". Microsoft wants a no-break space ("50 %"); if you follow it, use U+00A0, never a plain space that can wrap, and not in Fredoka One, which lacks U+00A0.
- Ordinals take a period: "5. nivo", "1. mjesto" (Microsoft: "200. godišnjica").
- Durations: unit abbreviations avoid plural forms: "3 h 20 min", "2 d. 5 h", "30 s" (CLDR's narrow Bosnian units: d., h, m, s). Clock: 24-hour, "14:30".
- Keys: keep the key letter, "Pritisni E". Microsoft key names: Enter, Shift, Esc stay English; Space = "razmak"; arrows "strelica gore/dolje".

## Do not translate / keep as is
- Keep: Roblox, Robux, Premium, VIP, AFK, XP, usernames and display names, promo codes ("FREEPETS"), keybinds, the game title "Pet Hatch Tycoon" unless the developer ships a localized title.
- Foreign Latin-script names keep their spelling; never phonetic respelling ("Roblox", not "Robloks"). In prose they decline without a hyphen: "u Robloxu", "Robloxa"; acronyms take one: "VIP-a".
- Translate in-game item, pet and rarity names ("Napitak sreće", "Zmaj", "Legendarni").
- Script: Latin only, every string. Never Cyrillic, never a mix of scripts in one game, and never ASCII without diacritics ("Ucitavanje" is chat typing, not UI).

## Rendering on Roblox
- Bosnian needs č ć đ š ž and Č Ć Đ Š Ž (Latin Extended-A). dž, lj, nj are two ordinary letters; never the single-codepoint digraphs ǆ ǉ ǌ (U+01C4-U+01CC).
- Checked 2026-11-08 by reading the character maps of the fonts bundled with the installed Roblox client: Builder Sans, Builder Extended, Builder Mono, Source Sans Pro, Montserrat, Arimo, Roboto, Nunito, Oswald, Bangers, Luckiest Guy, Press Start 2P, Titillium Web, Ubuntu, Kalam, Patrick Hand and Comic Neue Angular have all ten letters.
- Missing č ć đ Č Ć Đ (š ž present): Fredoka One, Creepster, Permanent Marker, Highway Gothic, Accanthis ADF, Balthazar. Denk One has none of the ten. Fredoka One is common in simulators: "Novčići", "Učitavanje", "Uđi" break there, so set Bosnian labels in Builder Sans, Luckiest Guy or Bangers. Whether Roblox draws a fallback glyph or a box is unverified.
- Luau `string.upper` changes ASCII only: "novčići" -> "NOVčIćI". Write capitals directly in the table ("NOVČIĆI").
- Accented capitals are taller; check Č Ć Š Ž in tight TextScaled labels (unverified clipping).
- Verify in Studio: Player Emulator locale `bs-ba`; paste "ČĆĐŠŽ čćđšž DŽEMPER, ljubičasti šešir, žuti đak" into every FontFace the game uses; open the longest strings (rebirth.confirm, social.group_reward at 54/55) and the fullest button (shop.title at 10/10).

## Mistakes machine translation makes here
| Mistake | Bad | Good |
|---|---|---|
| Cyrillic because Roblox's label is Cyrillic | Играј | Igraj |
| Ekavian (Serbian) forms | Sledeća nagrada za vreme... | Sljedeća nagrada za... |
| Croatian vocabulary mixed in | Glazba, razina, ruksak, tisuća | Muzika, nivo, ranac, hiljada |
| Serbian "da" and future forms | Treba da prodaš ljubimce; kupićeš | Trebaš prodati ljubimce; kupit ćeš |
| Adult "vi" register | Pritisnite E da otvorite | Pritisni E da otvoriš |
| experience as "iskustvo" | Pridruži se iskustvu | Uđi u igru |
| claim as "zatraži" (= request) or "preuzmi" (= download) | Zatraži | Pokupi |
| Gendered past for you/{player} | Izlegao si legendarnog zmaja | Novi ljubimac: Zmaj (Legendarni)! |
| Count before a noun | {count} novčića -> "1 novčića" | Novčići: {count} |
| Wrong letters: Icelandic ð/Ð (U+00F0/U+00D0), "dj", stripped marks | Ðak, djak, Ucitavanje | Đak, Učitavanje (đ U+0111, Đ U+0110) |
| English Title Case | Dnevna Nagrada | Dnevna nagrada |
| Literal calque of slang | Ovaj mač je nadjačan | Ovaj mač je prejak! |

## Reference translations
| key | translation | note |
|---|---|---|
| menu.play | Igraj | |
| shop.title | Prodavnica | 10/10; "Trgovina" (8) is also accepted in BiH if space is tight |
| shop.buy | Kupi | |
| reward.claim | Pokupi | not "Zatraži"; "Preuzmi" reads as Download |
| rebirth.button | Preporod | |
| rebirth.confirm | Preporod sada? Izgubit ćeš novčiće, ali dobit ćeš trajno pojačanje x{multiplier}. | future tense avoids gender; "x2" after the noun; game code must print 1.5 as "1,5" |
| coins.need_more | Nedovoljno novčića! Fali još {amount}. | number without a noun avoids plural forms; everyday "fali" suits the tone; formal "Nedostaje" can pass 40 with big numbers |
| coins.count | Novčići: {count} | label pattern; 14/16 with "1.250" |
| egg.hatched | Novi ljubimac: {pet} ({rarity})! | no past tense, no {rarity} before {pet} |
| rarity.legendary | Legendarni | masculine, agrees with "ljubimac" |
| pet.name.dragon | Zmaj | |
| chat.player_joined | {player} je sada u igri | gender-neutral state; "se pridružuje" would read as still joining, "se pridružio" is masculine |
| trade.request | {player} ti nudi razmjenu | |
| prompt.open_shop | Pritisni E da otvoriš | 21/22 |
| pass.buy_price | Kupi za {price} Robux | Robux undeclined after a number |
| pass.coins2x | 2x novčići | "Dupli novčići" (13) also natural |
| pass.vip | VIP | kept: the acronym is the everyday BiH word ("VIP loža") |
| reward.daily_title | Dnevna nagrada | |
| reward.come_back | Vrati se za {time} po sljedeću nagradu! | |
| codes.placeholder | Unesi kod | |
| codes.invalid | Kod nije ispravan ili je istekao. | |
| social.like_reward | Lajkaj igru i dobij besplatan <b>Napitak sreće</b>! | 44 without tags |
| social.group_reward | Pridruži se našoj grupi i otključaj besplatnu nagradu! | 54/55, keeps "unlock"; only if the banner overflows: "Pridruži se našoj grupi za besplatnu nagradu!" (46) |
| afk.warning | AFK si! Pomjeri se i nastavi zarađivati. | |
| leaderboard.title | Najbolji igrači | masculine generic, as Microsoft allows |
| level.up | Novi nivo! Sada si na nivou {level}. | gender-neutral |
| tutorial.sell | Uđi u svijetleći krug i prodaj ljubimce. | no possessive (Microsoft rule) |
| inventory.full | Ranac je pun! Prodaj ljubimce i oslobodi mjesto. | |
| settings.music | Muzika | |
| settings.on | Da | Off = "Ne"; "Uklj." (5) fits but its Off "Isklj." (6) does not, and Minecraft's "UKLJUČENO" is far too long |
| loading | Učitavanje... | |
| event.ends_in | Događaj traje još {time} | "ističe" (expires) fits offers, not events |
| item.op | Ovaj mač je prejak! | "OP" kept would also be understood (unverified) |
| friends.boost | +{percent}% pojačanja za svakog prijatelja na serveru | genitive after %, like "20% popusta"; no space before % (CLDR) |

## Sources
1. Roblox language codes (Bosnian shown as "Bosnian (босански)", `bs-ba`): https://create.roblox.com/docs/production/localization/language-codes
2. Roblox locale service (`bs_ba`: in-game content only, not full app; 18 full-app locales): https://locale.roblox.com/v1/locales?displayValueLocale=en_us
3. Roblox localization overview (automatic translations setting): https://create.roblox.com/docs/production/localization
4. Microsoft localization style guides index (Bosnian offered in Latin only): https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
5. Microsoft Bosnian (Latin) style guide PDF, 2023: https://download.microsoft.com/download/4/4/c/44cd9e84-9003-4200-ab89-c31b038e9795/bos-bih-StyleGuide.pdf
6. CLDR language plural rules: https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
7. CLDR likely subtags (`bs` -> `bs-Latn-BA`): https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-core/supplemental/likelySubtags.json
8. Wikipedia, Bosnian language (scripts by entity, "kupit ću" spelling): https://en.wikipedia.org/wiki/Bosnian_language
9. DevForum, "Friends Are Back!" (Connections -> Friends, April 2026): https://devforum.roblox.com/t/friends-are-back-expanding-trusted-friends-for-a-new-way-to-chat-and-play/4554217
10. Character maps of the font files in the installed Roblox client (`content/fonts`, version-f0ea5da9412f4e35), read locally with fontTools 2026-11-08.
11. Croatian Wikipedia, Roblox (neighbor usage: "iskustva", "avatar", "Roblox Premium članstvo"): https://hr.wikipedia.org/wiki/Roblox
12. Bosnian Wikipedia, Videoigra (Latin script; "igrač", "računarska igra", "igraća konzola"): https://bs.wikipedia.org/wiki/Videoigra
13. CLDR JSON for `bs`: quotes „” (misc delimiters), number symbols and "#,##0%" (numbers), duration units (units): https://github.com/unicode-org/cldr-json/tree/main/cldr-json
14. Minecraft Java Bosnian language file `minecraft/lang/bs_ba.json` (community translation: ti, "Muzika", "Inventar", "Razmjene", „%s“, "100%"), read from the game's assets 2026-11-08; language list: https://minecraft.wiki/w/Language
