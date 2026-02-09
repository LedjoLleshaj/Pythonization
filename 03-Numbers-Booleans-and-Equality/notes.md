# Numbers, Booleans, and Equality - Study Notes

## Data Types
- `int`: Integers (e.g., `5`, `-10`)
- `float`: Floating-point numbers (e.g., `5.0`, `3.14`)
- `bool`: Booleans (`True`, `False`)
- `str`: Strings (e.g., `"Hello"`)

## Arithmetic Operators
- `/`: Floating-point division (always returns a float).
- `//`: Floor division (truncates decimal part).
- `%`: Modulo (returns the remainder).
- `**`: Exponentiation (power).

## Comparison Operators
Returns a boolean value (`True` or `False`).
- `==`: Equal to
- `!=`: Not equal to
- `>` : Greater than
- `<` : Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

## Logical Operators
- `and`: True if both conditions are true.
- `or`: True if at least one condition is true.
- `not`: Reverses the boolean state.

## Type Function
The `type()` function identifies the data type of an object.
```python
type(5) # <class 'int'>
type(5.0) # <class 'float'>
```

## Type Conversion
Functions to convert between types:
- `int()`: Convert to integer.
- `float()`: Convert to float.
- `str()`: Convert to string.
- `bool()`: Convert to boolean.

> [!NOTE]
> `int()` on a float truncates toward zero (doesn't round).
> `bool()` on empty values (like `0`, `0.0`, `""`) returns `False`, others return `True`.
