# Objects and References - Study Notes

## Variables as Pointers
Variables in Python are names that point to objects in memory.
- **Immutable Types** (int, str, tuple): When you "change" them, the variable points to a *new* object.
- **Mutable Types** (list, dict): Multiple variables can point to the same object (**aliasing**). Changes to the object affect all variables pointing to it.

## Equality (`==`) vs. Identity (`is`)
- `==`: Checks if the **values** are the same.
- `is`: Checks if the **objects** are the same (identical memory address).

```python
a = [1, 2]
b = [1, 2]
a == b # True
a is b # False
```

## Shallow vs. Deep Copies
- **Shallow Copy** (`list.copy()`, `list()`, `[:]`): Creates a new outer list, but the elements inside still point to the same objects as the original list.
- **Deep Copy** (`copy.deepcopy()`): Creates a new outer list AND recursively copies all nested objects. Use this for complex nested data structures.

## Garbage Collection
Python automatically reclaims memory of objects that are no longer referenced by any variables. You can manually hint at this by setting a variable to `None` or using the `del` keyword on a variable name.

## Interning
Python sometimes reuses objects for small integers and strings to save memory. This is why `a is b` might be `True` for two separate assignments of the same small number.
