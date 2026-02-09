# Classes: Inheritance - Study Notes

Inheritance allows a class (subclass) to derive attributes and methods from another class (superclass), promoting code reuse.

## Base Subclassing
```python
class Store: # Superclass
    pass

class HardwareStore(Store): # Subclass
    pass
```

## Method Overriding
A subclass can provide its own implementation of a method that is already defined in its superclass.

## The `super()` Function
Used to call methods from the parent class. Common in `__init__` to ensure parent attributes are initialized.

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

## Multiple Inheritance
A class can inherit from multiple parent classes.
- **MRO (Method Resolution Order)**: The order Python uses to search for methods in complex hierarchies. Access with `ClassName.mro()`.

## Polymorphism and Duck Typing
- **Polymorphism**: Different classes can have methods with the same name.
- **Duck Typing**: "If it walks like a duck and quacks like a duck, it's a duck." Python focuses on whether an object has the required method rather than its specific class type.

## Name Mangling for "Privacy"
Prefixing an attribute with double underscores `__` (e.g., `__attr`) mangles its name to `_ClassName__attr`, making it harder (but not impossible) to access from outside.

## Composition
Instead of inheriting, a class can contain an instance of another class as an attribute ("Has-a" relationship vs. "Is-a" relationship).
