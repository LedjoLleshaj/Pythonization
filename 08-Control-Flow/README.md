# Control Flow - Study Notes

## Conditional Statements
Use `if`, `elif`, and `else` to execute code based on conditions.

```python
if condition:
    # code
elif other_condition:
    # code
else:
    # code
```

## Truthiness and Falsiness
In Python, values have an inherent boolean meaning.
- **Falsy values**: `0`, `0.0`, `""` (empty string), `None`, `[]` (empty list), `False`.
- **Truthy values**: Almost everything else.

## Logical Operators
- `and`: True if both are true.
- `or`: True if at least one is true.
- `not`: Reverses the truth value.

## Conditional Expressions (Ternary Operator)
A one-liner for simple if-else logic.
```python
result = "Yes" if condition else "No"
```

## While Loops
Executes code as long as a condition is `True`.
```python
while condition:
    # code
    # update condition to avoid infinite loop
```

## Recursion
A function that calls itself. It must have a **base case** to prevent infinite recursion.
```python
def factorial(n):
    if n == 1: # Base Case
        return 1
    return n * factorial(n - 1)
```
