# Sets - Study Notes

## Intro to Sets
A set is an unordered collection of **unique**, immutable elements. Sets are useful for removing duplicates and performing mathematical set operations.

```python
# Creation
s = {1, 2, 3, 3} # Result: {1, 2, 3}
empty = set() # {} creates an empty dictionary, not a set

# Converting to set (removes duplicates)
nums = [1, 2, 2, 3]
unique_nums = set(nums) # {1, 2, 3}
```

## Adding and Removing
- `add(value)`: Adds a single element.
- `update(iterable)`: Adds multiple elements from another collection.
- `remove(value)`: Removes an element (Raises `KeyError` if missing).
- `discard(value)`: Removes an element (Does nothing if missing).

## Set Operations
- **Union** (`|`): Elements in either set. `s1 | s2`
- **Intersection** (`&`): Elements in both sets. `s1 & s2`
- **Difference** (`-`): Elements in the first but not the second. `s1 - s2`
- **Symmetric Difference** (`^`): Elements in either set but NOT both. `s1 ^ s2`

## Relationships
- `issubset()` or `<`: Is every element of A in B?
- `issuperset()` or `>`: Does B contain every element of A?

## Frozenset
A **frozenset** is an immutable version of a set. Because it is immutable, it is **hashable** and can be used as a dictionary key or an element of another set.
```python
fs = frozenset([1, 2, 3])
```
