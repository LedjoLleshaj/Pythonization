# Classes: Attributes and Methods - Study Notes

## Instance Methods
Methods defined inside a class that operate on a specific instance. They must take `self` as the first argument.

```python
class Pokemon:
    def roar(self):
        print("Roar!!!")

p = Pokemon()
p.roar()
```

## Class Attributes vs. Instance Attributes
- **Class Attributes**: Defined directly in the class body. Shared by all instances.
- **Instance Attributes**: Defined inside `__init__` or other methods using `self.`. Unique to each instance.

## Class Methods (`@classmethod`)
Methods bound to the class rather than the instance. They take `cls` as the first argument. Useful for "factory" methods.

```python
class Pizza:
    @classmethod
    def margherita(cls):
        return cls(ingredients=["tomato", "mozzarella"])
```

## Static Methods (`@staticmethod`)
Methods that don't need access to the class (`cls`) or instance (`self`). They behave like regular functions but are namespaced within a class.

## Encapsulation (Protected Attributes)
By convention, attributes starting with a single underscore `_` are considered **protected** and should not be accessed directly from outside the class.

## Properties (`@property`)
Allows a method to be accessed like an attribute. Often used with a **setter** to add validation.

```python
class Currency:
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, value):
        if value >= 0:
            self._cents = value * 100
```

## Built-in functions for Attributes
- `getattr(obj, name, default)`: Get an attribute value.
- `setattr(obj, name, value)`: Set an attribute value.
- `hasattr(obj, name)`: Returns `True` if attribute exists.
- `delattr(obj, name)`: Deletes an attribute.
