# Chapter 2: Simple Pattern Matching

## Source Text

[rime-intro.txt](ch02/rime-intro.txt)

## Character Shorthands in Regular Expression

| Character Shorthand | Regular-Expression Meaning |
| --- | --- |
| \a | Match the bell character, pop up an Alert |
| \b | Match a word boundary |
| [\b] | Match a backspace character |
| \B | Match a non-word boundary |
| \c x | Match the control character x |
| \d | Match all Arabic digits (Digit Character), like [0-9] |
| \D | One character that is not a digit as defined by \d, Non-digit character |
| \d xxx | Match the character xxx in the current locale, decimal value for a character |
| \f | Match a form feed character |
| \h | Match a horizontal whitespace character |
| \H | Match a character that is not a horizontal whitespace character |
| \n | Match a newline character |
| \r | Match a carriage return character |
| \s | Whitespace character (space, tab, newline, carriage return, vertical tab), same as `[\t\n\x0B\f\r]`|
| \S | One character that is not a whitespace character as defined by \s |
| \t | Match a horizontal tab character |
| \v | Match a vertical tab character |
| \V | Match a character that is not a vertical whitespace character |
| \w | Word character (ASCII letter, digit or underscore), in English, same as `[a-zA-Z0-9_]` |
| \W | One character that is not a word character as defined by \w, same as `[^a-zA-Z0-9_]` |
| \0 | Match a NUL character |
| \xhh | Match the character with hex value hh |
| \x{h..h} | Match the character with hex value hh..hh |
| \uhhhh | Match the character with hex value hhhh |
| \uhhhhhhhh | Match the character with hex value hhhhhhhh |

## Difference between `\w` and `\D`

- `\w` matches any word character, including letters, digits (numbers) and underscore
- `\D` matches any non-digit character, including letters, underscore, whitespace, punctuation, quotation marks, forward slashes, and other similar characters

---

Date: 2025/04/29