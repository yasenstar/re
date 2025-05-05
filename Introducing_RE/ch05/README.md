# Chapter 5: Character Classes

## 05.03 POSIX Character Classes

- `[:alnum:]`: Alphanumeric characters, same as `[a-zA-Z0-9]`
- `[:alpha:]`: Alphabetic characters, same as `[a-zA-Z]`
- `[:blank:]`: Space or tab characters, same as `[ \t]`
- `[:cntrl:]`: Control characters
- `[:digit:]`: Numeric characters, same as `[0-9]`
- `[:graph:]`: Visible characters (i.e., not space, control, or delete)
- `[:lower:]`: Lowercase letters, same as `[a-z]`
- `[:xdigit:]`: Hexadecimal digits, same as `[0-9A-Fa-f]`- `[:space:]`: Whitespace characters, same as `[ \t\n\x0B\f\r]`
- `[:upper:]`: Uppercase letters, same as `[A-Z]`
- `[:punct:]`: Punctuation characters, same as `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`
- `[:print:]`: Visible characters and space, same as `[:graph:]` + `[ ]`
