# Strings: The Basics - Study Notes

## Immuteability
Strings in Python are **immutable**, meaning they cannot be changed after they are created. You cannot reassign a character at a specific index.

```python
name = "Ledjo"
# name[0] = "l" # This will raise a TypeError
```

## String Length
Use `len()` to get the number of characters in a string.
```python
len("Python") # 6
```

## Escaping Characters
Use the backslash `\` to include special characters in strings.
- `\n`: Newline
- `\t`: Tab
- `\"` or `\'`: Quotes
- `\\`: Backslash

## Indexing
Access individual characters using square brackets `[]`.
- **Positive Indexing**: Starts at `0` (left to right).
- **Negative Indexing**: Starts at `-1` (right to left).

```python
word = "Python"
word[0]  # 'P'
word[-1] # 'n'
```

## Slicing
Extract a portion of a string using `[start:stop:step]`.
- `start`: Inclusive.
- `stop`: Exclusive.
- `step`: Interval (can be negative for reverse).

```python
word = "Python"
word[0:2] # 'Py'
word[2:]  # 'thon'
word[::-1] # 'nohtyP' (Reverse)
```

## Membership Operators
- `in`: Returns `True` if a substring exists in the string.
- `not in`: Returns `True` if a substring does not exist.

```python
"Py" in "Python" # True
```
