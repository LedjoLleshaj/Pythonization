# Regular Expressions - Study Notes

Regular expressions (regex) are patterns used to match character combinations in strings. In Python, the `re` module provides regex support.

## Raw Strings
Always use **raw strings** (`r"pattern"`) for regex to prevent Python from interpreting backslashes as escape characters.

## Core Functions (`re` module)
- **`re.search(pattern, string)`**: Returns a match object if the pattern is found anywhere in the string.
- **`re.match(pattern, string)`**: Returns a match object ONLY if the pattern is at the **beginning** of the string.
- **`re.findall(pattern, string)`**: Returns a list of all non-overlapping matches as strings.
- **`re.finditer(pattern, string)`**: Returns an iterator yielding match objects for all matches.
- **`re.compile(pattern)`**: Pre-compiles a regex for better performance if used multiple times.

## Match Objects
If a match is found, these methods are useful:
- `.group()`: Returns the actual string matched.
- `.start()` / `.end()`: Returns the start/end index of the match.
- `.span()`: Returns a tuple of `(start, end)`.

## Common Meta Characters
- `.`: Any character except newline.
- `\d`: Any digit (0-9). `\D`: Any non-digit.
- `\w`: Any word character (alphanumeric + underscore). `\W`: Non-word.
- `\s`: Any whitespace. `\S`: Non-whitespace.
- `\b`: Word boundary.
- `^`: Beginning of string.
- `$`: End of string.

## Quantifiers
- `{x}`: Exactly x occurrences.
- `{x,y}`: Between x and y occurrences.
- `+`: One or more.
- `*`: Zero or more.
- `?`: Zero or one.

## Character Sets and OR
- `[abc]`: Matches a, b, or c.
- `[a-z]`: Matches any lowercase letter.
- `[^abc]`: Matches anything EXCEPT a, b, or c.
- `A|B`: Matches either pattern A or pattern B.
筋
