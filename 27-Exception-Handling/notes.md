# Exception Handling - Study Notes

## The `try-except` Block
Used to handle errors gracefully without crashing the program.

```python
try:
    result = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Catching Multiple Exceptions
You can have multiple `except` blocks or catch multiple errors in a tuple.

```python
try:
    # some code
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```

## `else` and `finally`
- **`else`**: Runs ONLY if the `try` block succeeded (no exception raised).
- **`finally`**: ALWAYS runs, regardless of whether an exception occurred. Ideal for cleanup (e.g., closing files).

## Raising Exceptions
Use the `raise` keyword to manually trigger an exception.

```python
if price < 0:
    raise ValueError("Price cannot be negative")
```

## User-Defined Exceptions
You can create custom exceptions by inheriting from the built-in `Exception` class.

```python
class MyCustomError(Exception):
    pass

raise MyCustomError("Something went wrong!")
```

## Inheritance Hierarchy
Exception types are classes. Catching a parent class (like `Exception` or `ArithmeticError`) will also catch all of its subclasses.
