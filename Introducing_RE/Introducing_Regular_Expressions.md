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

# 04. Alternation, Groups, and Backreferences

# 05. Character Classes

# 06. Matching Unicode and Other Characters

# 07. Quantifiers

# 08. Lookarounds

# 09. Marking Up a Document with HTML

# 10. The end of the Beginning
