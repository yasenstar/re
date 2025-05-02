 Introducing RE

# 00. Opening and Preface

## "A regular expression is a pattern which specifies a set of strings of characters; it is said to match certain strings." -- Ken Thompson

# 01. What is a Regular Expression?

## 01.01 Getting Started with Regexpal

### https://www.regexpal.com/

## 01.02 Matching a North American Phone Number

### O'Reilly Media: +1 707-827-7019

### String Literal: a literal representation of a string

## 01.03 Match Digits with a Character Class

### [0-9]: Match any digit you find in the range 0 through 9
 
[]: metacharacters: has special meaning in regular expressions and isreserved.


### Character Class / Character Set

## 01.04 Using a Character Shorthand

### Character Shorthand / Character Escape

### \d: match all Arabic digits, like [0-9]

### \w: word character (ASCII letter, digit or underscore)

### \s: whitespace character (space, tab, newline, carriage return, vertical tab)

### \D: one character that is not a digit as defined by \d

### \W: one character that is not a word character as defined by \w

### \S: one character that is not a whitespace character as defined by \s

## 01.05 Matching Any Character

### .: Any character, including whitespace or numeric

### ?: Zero or one of the preceding character

### *: Zero or more of the preceding character

### +: One or more of the preceding character

### ^: Negation or complement

## 01.06 Capturing Groups and Back References

## 01.07 Using Quantifiers

## 01.08 Quoting Literals

## 01.09 A Sample of Applications

### TextMate (Mac Only)

### Notepad++

### Oxygen XML Editor

### regexr.com

#### VS Code Extension

### Regex Match (VS Code Extension)

#### create file with .rgx extension.

RE, e.g. /[0-9]+a+/gm
---
test string
---

### Regex Workbench (VS Code Extension)

# 02. Simple Pattern Matching

## 02.01 Matching String Literals

## 02.02 Matching Digits

## 02.03 Matching Non-Digits

## 02.04 Matching Word and Non-Word Characters

## 02.05 Matching Whitespace

## 02.06 Matching Any Character, Once Again

## 02.07 Matching Up the Text

### 02.07.01 Using sed to Mark Up Text

### 02.07.02 Using Perl to Mark Up Text

# 03. Boundaries

## 03.01 The Beginning and End of a Line

## 03.02 Word and Non-word Boundaries

## 03.03 Other Anchors

## 03.04 Quoting a Group of Characters as Literals

## 03.05 Adding Tags

# 04. Alternation, Groups, and Backreferences

## 04.01 Alternation

## 04.02 Subpatterns

## 04.03 Capturing Groups and Backreferences

### 04.03.01 Named Groups

## 04.04 Non-Capturing Groups

### 04.04.01 Atomic Groups

# 05. Character Classes

## 05.01 Negated Character Classes

## 05.02 Union and Difference

## 05.03 POSIX Character Classes

# 06. Matching Unicode and Other Characters

## 06.01 Matching a Unicode Character

### 06.01.01 Using vim

## 06.02 Matching Characters with Octal Numbers

## 06.03 Matching Unicode Character Properties

## 06.04 Matching Control Characters

# 07. Quantifiers

## 07.01 Greedy, Lazy, and Possessive

## 07.02 Matching with *, +, and ?

## 07.03 Matching a Specific Number of Times

## 07.04 Lazy Quantifiers

## 07.05 Possessive Quantifiers

# 08. Lookarounds

## 08.01 Positive Lookaheads

## 08.02 Negative Lookaheads

## 08.03 Positive Lookbehinds

## 08.04 Negative Lookbehinds

# 09. Marking Up a Document with HTML

## 09.01 Matching Tags

## 09.02 Transforming Plain Text with sed

### 09.02.01 Substitution with sed

### 09.02.02 Handling Roman Numerals with sed

### 09.02.03 Handling a Specific Paragraph with sed

### 09.02.04 Handling the Lines of the Poem with sed

## 09.03 Appending Tags

### 09.03.01 Using a Command File with sed

## 09.04 Transforming Plain Text with Perl

### 09.04.01 Handling Roman Numerals with Perl

### 09.04.02 Handling a Specific Paragraph with Perl

### 09.04.03 Handling the Lines of the Poem with Perl

### 09.04.04 Using a File of Commands with Perl

# 10. The end of the Beginning

## 10.01 Learning More

## 10.02 Notable Tools, Implementations, and Libraries

### 10.02.01 Perl

### 10.02.02 PCRE

### 10.02.03 Ruby (Oniguruma)

### 10.02.04 Python

### 10.02.05 RE2

## 10.03 Matching a North American Phone Number

## 10.04 Matching an Email Address
