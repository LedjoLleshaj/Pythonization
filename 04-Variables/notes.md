# Variables - Study Notes

## Variable Assignment
Variables are created by assigning a value to a name using the `=` operator.

```python
name = "Ledjo"
age = 22
```

## Naming Conventions
- Use `snake_case` (all lowercase with underscores).
- Names must start with a letter or underscore, not a number.
- Names are case-sensitive (`Age` != `age`).

## Augmented Assignment
Shortcuts for updating a variable's value.
- `+=`: Add and assign (`x += 1` is `x = x + 1`)
- `-=`: Subtract and assign
- `*=`: Multiply and assign
- `/=`: Divide and assign

## Multiple Assignment
Assigning multiple variables in one line.
```python
a = b = 10 # Both a and b are 10
x, y = 5, 10 # x is 5, y is 10
```

## User Input
The `input()` function pauses the program and takes input from the user.
- **Important**: `input()` always returns a **string**. You must convert it (e.g., `int()`, `float()`) if you need to perform math.

```python
age = int(input("Enter your age: "))
```

## Common Exceptions
- `NameError`: Using a variable name that hasn't been defined.
- `TypeError`: Performing an operation on incompatible types (e.g., `5 + "10"`).
- `ValueError`: Passing an argument with the right type but inappropriate value (e.g., `int("abc")`).
- `SyntaxError`: Incorrect Python syntax (e.g., missing reaching parenthesis).
