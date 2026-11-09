# Localizability audit -- Lantern Lake Fishing

No game source in this example; audit is from the table alone.

## Dynamic text in the table
None. All 40 entries are static UI text with `{params}` for the dynamic parts.

## Concatenation
None found in the table. (With source available, also search scripts for
`..` next to quoted English.)

## Ambiguous short strings (covered by the Example column)
`hud.cast`, `hud.reel`, `shop.free`, `settings.back`, `shop.equip` /
`shop.equipped`, `quest.claim`, `shop.rods`. Translators must use the
Example text, not the dictionary sense.

## Counts and agreement
- `hud.bait_left` "{count} Bait", `sell.done` "{count} fish ... {coins}
  coins", `quest.catch_n` "{n} fish": count can be 1; use plural-neutral
  wording per the locale guide.
- `catch.success` "You caught a {rarity} {fish}!": two translated words are
  inserted, so gendered languages cannot agree the adjective with the noun.
  Suggest the game change it to one parameter per fish+rarity, or to
  "{fish} ({rarity})". Translators should phrase around it meanwhile.
- `trade.sent`, `trade.accept`: `{player}` of unknown gender.

## Text in images
Not checked (no assets in this example).

## Added by the context analyst
- `sell.prompt` "Press E to sell" is wrong on phone, console and VR; the
  ProximityPrompt already shows the right key, so "Sell" alone would do.
- `catch.success` "a {rarity}" is wrong English for tiers starting with a
  vowel (Epic, Uncommon).
- `event.ends` `{time}` ("2d 4h") and `catch.new_record` `{weight}` ("12.4")
  arrive pre-formatted in English; translators cannot change the unit
  letters or the decimal mark.
