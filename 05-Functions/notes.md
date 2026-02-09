# Functions - Study Notes

## Defining Functions
Functions are defined using the `def` keyword. Code inside a function must be indented.

```python
def my_function():
    print("Hello from a function")

my_function() # Calling the function
```

## Parameters and Arguments
- **Parameters**: Modifiers defined in the function signature (e.g., `a`, `b`).
- **Arguments**: Actual values passed to the function when calling it.

```python
def greet(name):
    print("Hello", name)

greet("Ledjo") # "Ledjo" is the argument
```

## Return Values
The `return` keyword sends a result back to the caller and exits the function.
```python
def add(a, b):
    return a + b

result = add(5, 10)
```

## Positional vs. Keyword Arguments
- **Positional**: Arguments assigned based on their order.
- **Keyword**: Arguments assigned by explicitly naming the parameter.

```python
def display(a, b):
    print(a, b)

display(1, 2) # Positional
display(b=2, a=1) # Keyword
```

## Default Arguments
Parameters can have default values if no argument is provided.
```python
def add(a=0, b=0):
    return a + b
```

## Function Annotations (Type Hints)
Helps document the expected types of parameters and return values.
```python
def power(base: int, exp: int) -> int:
    return base ** exp
```

## The `None` Type
A special type representing the absence of a value. Functions that don't explicitly `return` anything return `None` by default.
```python
type(None) # <class 'NoneType'>
```
