# Lists: Methods & Advanced - Study Notes

## Advanced Search and Counting
- `count(value)`: Returns number of occurrences in the list.
- `index(value)`: Returns the index of the first occurrence. Raises `ValueError` if not found.

## Combining and Splitting
- `"separator".join(list)`: Joins a list of strings into a single string with the separator.
- `"string".split("delimiter")`: Splits a string into a list based on the delimiter.

```python
words = ["Python", "is", "fun"]
s = " ".join(words)     # "Python is fun"
s.split(" ")            # ["Python", "is", "fun"]
```

## List Comprehension
A concise way to create lists.
**Syntax**: `[expression for item in iterable if condition]`

```python
nums = [1, 2, 3, 4]
squares = [n**2 for n in nums]          # [1, 4, 9, 16]
evens = [n for n in nums if n % 2 == 0] # [2, 4]
```

## The `zip()` Function
Combines multiple iterables into a single iterable of tuples.
```python
names = ["Alice", "Bob"]
scores = [85, 90]
list(zip(names, scores)) # [("Alice", 85), ("Bob", 90)]
```

## Copying Lists
- `list.copy()`: Returns a **shallow copy** of the list.
- Alternatively, use slicing: `new_list = old_list[:]`.
