# Dictionaries: The Basics - Study Notes

## Intro to Dictionaries
A dictionary is an unordered collection of **key-value pairs**. Keys must be immutable (strings, numbers, tuples), while values can be anything.

```python
# Creation
user = {"name": "Ledjo", "age": 22}
empty = {}

# Also using dict() on list of pairs
pairs = [["a", 1], ["b", 2]]
d = dict(pairs) # {'a': 1, 'b': 2}
```

## Accessing and Modifying
- `d[key]`: Access value by key. (Raises `KeyError` if not found).
- `get(key, default)`: Safely access value. Returns `default` (or `None`) if key is missing.
- `d[key] = value`: Adds a new pair or updates an existing one.

## Membership Operators
- `in` / `not in`: Checks if a **key** exists in the dictionary.

```python
"name" in user # True
"Ledjo" in user # False (checks keys only)
```

## Manipulation Methods
- `update(other_dict)`: Merges another dictionary into the current one (overwrites existing keys).
- `pop(key)`: Removes and returns the value for a key.
- `setdefault(key, value)`: Returns value if key exists; otherwise, sets key to value and returns it.
- `clear()`: Removes all items.
- `del d[key]`: Deletes a key-value pair.

## Nested Dictionaries
Dictionaries can contain other dictionaries (useful for structured data).
```python
users = {
    "ledjo": {"role": "admin", "id": 1}
}
users["ledjo"]["role"] # "admin"
```
