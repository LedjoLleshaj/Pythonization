# String Methods - Study Notes

## Case Methods
- `capitalize()`: Capitalizes first letter of the string.
- `title()`: Capitalizes first letter of every word.
- `upper()`: All characters to uppercase.
- `lower()`: All characters to lowercase.
- `swapcase()`: Swaps upper to lower and vice versa.

## Search and Count
- `count(substring)`: Returns number of occurrences.
- `find(substring)`: Returns index of first occurrence (returns `-1` if not found).
- `index(substring)`: Similar to `find()`, but raises `ValueError` if not found.

## Modification (Returns new string)
- `replace(old, new)`: Replaces all occurrences of `old` with `new`.
- `strip()`: Removes leading and trailing whitespace.
- `lstrip()` / `rstrip()`: Removes leading or trailing whitespace.
- `strip(chars)`: Removes specified characters from ends.

## Boolean (Checks)
- `startswith(prefix)` / `endswith(suffix)`: Returns boolean.
- `islower()` / `isupper()`: Checks case.
- `isalpha()`: True if all characters are letters.
- `isdecimal()`: True if all characters are numbers.
- `isalnum()`: True if characters are alphanumeric.
- `isspace()`: True if string contains only whitespace.

## String Formatting
- **f-strings** (Recommended): `f"Hello {name}"`
- `.format()`: `"{} laughed at the {}".format(name, noun)`
