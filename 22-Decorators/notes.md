# Decorators and Scope - Study Notes

## Variable Scope (LEGB Rule)
Python resolves variable names in a specific order:
1. **Local**: Inside the current function.
2. **Enclosing**: Inside any enclosing functions (for nested functions).
3. **Global**: At the top level of the module.
4. **Built-in**: Names pre-defined in Python (like `len`, `range`).

### Keywords
- `global`: Allows modifying a global variable inside a function.
- `nonlocal`: Allows modifying a variable in the enclosing (outer) function's scope.

## High-Order Functions
A function that either:
- Takes one or more functions as arguments.
- Returns a function as its result.

## Decorators
A decorator is a function that "wraps" another function to extend its behavior without permanently modifying it.

```python
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = fn(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello {name}"
```

### `functools.wraps`
Use `@functools.wraps(fn)` inside your decorator's wrapper to preserve the original function's metadata (like its name and docstring).

## Closures
A closure is a nested function that "remembers" the variables from its enclosing scope even after the outer function has finished executing.
