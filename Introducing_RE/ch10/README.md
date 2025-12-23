# Chapter 10. The End of the Beginning

- [Chapter 10. The End of the Beginning](#chapter-10-the-end-of-the-beginning)
  - [Matching a North American Phone Number](#matching-a-north-american-phone-number)
    - [Problem Description](#problem-description)
    - [Solution](#solution)
    - [Regular Expression](#regular-expression)
    - [JavaScript implementation example](#javascript-implementation-example)
    - [Discussion](#discussion)

## Matching a North American Phone Number

From book "Regular Expression Cookbook" (Section 4.2 in 2nd Edition) --

### Problem Description

You want to determine whether a user entered a North American phone number, including the local area code, in a common format.

These formats include `1234567890`, `123-456-7890`, `123.456.7890`, `123 456 7890`, `(123) 456 7890`, and all related combinations.

### Solution

A regular expression can easily check whether a user entered something that looks like a valid phone number.

By using capturing groups to remember each set of digits, the same regular expression can be used to replace the subject text with precisely the format your want.

### Regular Expression

```re
^\(?([0-9]{3})\)?[-.*]?([0-9]{3})[-.*]?([0-9]{4})$
```

Regular options: None

### JavaScript implementation example

```javascript
var phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
if (phoneRegex.test(subjectString)) {
    var formattedPhoneNumber = subjectString.replace(phoneRegex, "($1) $2-$3");
}
else {
    // Invalid phone number
}
```

### Discussion

This regular expression matches three groups of digits.

The first group can optionally be enclosed with parentheses, and the first two groups can optionally be followed with a choice of three seperators (a hyphen, dot, or space).

The following layout breaks the regular expression into its individual parts, omitting the redundant groups of digits for explanation:

| RE | Explanation |
| --- | --- |
| `^` | Assert position at the beginning of the string. |
| `\(` | Match a literal "(" |
| `?` | between zero and one time. |
| `(` | Capture the enclosed match to backreference 1: |
| `[0-9]` | Match a digit, can also use `\d` |
| `{3}` | exactly three times. |
| `)` | End capturing group 1. |
| `\)` | Match a literal ")" |
| `?` | between zero and one time. |
| `[-. ]` | Match one hyphen, dot, or space |
| `?` | between zero and one time. |
| ... | [Match the remaining digits and spearater.] |
| `$` | Assert position a the end of the string. |

---

Last updated at 2025-12-23