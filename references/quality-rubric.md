# Quality rubric

Used by translators to aim and by reviewers to judge. Categories follow the
usual translation-quality model (accuracy, fluency, terminology, style,
locale conventions), adapted to game UI.

## Categories
| Category | The string... |
|---|---|
| accuracy | says something different from the source: wrong meaning, missing or added information, wrong sense of an ambiguous word, mistranslated parameter role |
| fluency | is grammatically wrong, unnatural, or reads as translated (calque, English word order, textbook phrasing) |
| terminology | uses a different word than `terms.json`, the glossary or the guide's vocabulary table; translates a keep-term; inconsistent with other strings |
| register | uses the wrong address form, politeness or tone for a kids' game in this locale (too formal, too stiff, too slangy) |
| locale | breaks this locale's conventions: punctuation, quotes, number format, regional variant leakage (Spain words in es-mx, Simplified characters in zh-tw), wrong script |
| length | exceeds the budget so it will be cut off or shrunk |
| markup | broken or renamed `{param}`, lost or misplaced rich-text tag, stray whitespace |
| safety | harsher, ruder or more suggestive than the source; anything not kid-safe |

## Severity
| Severity | Meaning | Examples |
|---|---|---|
| critical | breaks the game or misleads the player | renamed `{param}`; "Sell" translated as "Buy"; offensive word |
| major | a native player notices it at once | wrong meaning of "Claim"; formal "vous" in a kids' game; Spain slang in es-mx; plural wrong for count = 1; text cut off |
| minor | a careful native reader notices | slightly unnatural word order; a better word exists; small punctuation slip |

## Pass bar
A locale ships when: zero critical, zero major, lint clean, and every
`keep: true` has a reason. Minor fixes are applied when the reviewer
proposes them. Anything still major after the resolve round is marked
`needs_native` in the report, not shipped silently.

## What is not an error
- A wording that differs from the reviewer's preference but is correct and
  natural.
- Dropping English filler ("Hey!", "Oops") when the language would not say it.
- Restructuring a sentence around a parameter.
- Keeping an English gaming word the locale guide says players use.
