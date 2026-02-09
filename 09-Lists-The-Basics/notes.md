# Lists: The Basics - Study Notes

## Intro to Lists
A list is a mutable, ordered collection of objects. Lists can contain any data type, including other lists.

```python
# Empty list
items = []

# Multiple types
mixed = [1, "two", 3.0, True]

# Nested lists
nested = [[1, 2], [3, 4]]
```

## Indexing
Similar to strings, lists use zero-based indexing.
```python
users = ["Alice", "Bob", "Charlie"]
users[0]  # "Alice"
users[-1] # "Charlie"
```

## Slicing
Extract sub-lists using `[start:stop:step]`.
```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3]  # [2, 3]
numbers[::-1] # [5, 4, 3, 2, 1]
```

## Membership Operators
- `in`: Returns `True` if an element exists in the list.
- `not in`: Returns `True` if it does not.

```python
"Alice" in users # True
```
