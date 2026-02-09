# Classes: The Basics - Study Notes

## Defining a Class
Classes are blueprints for creating objects. Use the `class` keyword and `PascalCase` naming convention.

```python
class Superhero:
    pass
```

## Instantiation
Creating an object (instance) from a class.

```python
batman = Superhero()
```

## The `__init__` Method
This is a special method (constructor) that runs automatically when an object is created. It is used to initialize the object's attributes.

- **`self`**: The first parameter of any instance method. It refers to the specific instance of the object being created/modified.

```python
class Book:
    def __init__(self, title, author, price=14.99):
        self.title = title
        self.author = author
        self.price = price

gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", 19.99)
```

## Attributes
- **Instance Attributes**: Variables that belong to a specific object (defined with `self.`).
- **Default Values**: You can provide default values for attributes in the `__init__` method.

```python
class Zombie:
    def __init__(self, health=100):
        self.health = health
```
