# Tuples - Study Notes

## Intro to Tuples
Tuples are **immutable** sequences of objects. Once created, their elements cannot be changed, added, or removed.

```python
# Creation with or without parentheses
fruits = ("Apple", "Banana")
colors = "Red", "Blue" # Also a tuple

# Single element tuple (requires a trailing comma)
one_item = (1,)
```

## Tuples vs. Lists
- **Lists**: Mutable, slower, used for collections of similar items.
- **Tuples**: Immutable, faster, used for grouped related data (like a coordinate `(x, y)`).

## Tuple Unpacking
Extracting tuple elements into variables.

```python
employee = ("John", 30, "IT")
name, age, dept = employee

# Using the * operator for remaining items
first, *middle, last = (1, 2, 3, 4, 5)
# first = 1, middle = [2, 3, 4], last = 5

# Swapping variables
a, b = b, a
```

## Functions with Variable Arguments (`*args`)
The `*` prefix allows a function to accept any number of positional arguments, which are gathered into a **tuple**.

```python
def my_sum(*numbers):
    return sum(numbers)

my_sum(1, 2, 3) # numbers is (1, 2, 3)
```

## Unpacking Arguments
You can also use `*` to "spread" a list or tuple into function arguments.
```python
vals = [2, 3]
def add(a, b): return a + b
add(*vals) # Equivalent to add(2, 3)
```
