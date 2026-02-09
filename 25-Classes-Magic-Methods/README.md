# Classes: Magic Methods - Study Notes

Magic methods (dunder methods) are special methods with double underscores that allow you to hook into Python's built-in behaviors.

## String Representation
- `__str__`: Targeted at end-users (informal). Called by `print()` and `str()`.
- `__repr__`: Targeted at developers (formal). Used for debugging. Ideally, it should look like the code needed to recreate the object.

## Length and Indexing
- `__len__`: Called by `len(obj)`.
- `__getitem__(self, key)`: Called when using `obj[key]`.
- `__setitem__(self, key, value)`: Called when assigning `obj[key] = value`.

## Comparison Operators
Define how objects are compared:
- `__eq__` (==), `__ne__` (!=)
- `__lt__` (<), `__le__` (<=)
- `__gt__` (>), `__ge__` (>=)

## Arithmetic Operators
- `__add__` (+), `__sub__` (-)
- `__mul__` (*), `__truediv__` (/)
- `__pow__` (**)

## Truthiness
- `__bool__`: Determines what `bool(obj)` returns (used in `if` statements).

## Other Magic Methods
- `__init__`: Constructor.
- `__del__`: Destructor (called when object is garbage collected).

## Docstrings
Use triple quotes `"""Docstring"""` at the top of modules, classes, or functions to document them. Help can be accessed via `help(obj)`.

## Named Tuples
A quick way to create simple classes with only attributes.
```python
from collections import namedtuple
Book = namedtuple("Book", ["title", "author"])
```
