# Built-in Functions - Study Notes

## Functional Programming Tools
- **`lambda`**: An anonymous, one-line function.
  ```python
  (lambda x, y: x + y)(3, 4) # Returns 7
  ```
- **`map(func, iterable)`**: Applies a function to all items in an iterable.
  ```python
  list(map(str.upper, ["cat", "dog"])) # ["CAT", "DOG"]
  ```
- **`filter(func, iterable)`**: Filters elements based on a condition.
  ```python
  list(filter(lambda x: x > 5, [1, 10, 2])) # [10]
  ```

## Mathematical Functions
- `sum(list)`: Returns the total sum.
- `max(list)` / `min(list)`: Returns the largest/smallest element. Supports a `key` argument (e.g., `key=abs`).

## Boolean Checks
- `all(iterable)`: Returns `True` if **all** elements are truthy.
- `any(iterable)`: Returns `True` if **at least one** element is truthy.

## Documentation and Inspection
- `help(func)`: Displays the documentation (docstring) for a function or object.
- `dir(obj)`: Lists all attributes and methods of an object.

## Formatting
- `format(value, spec)`: Formats a value (e.g., `format(0.5, ".2%")` results in `"50.00%"`).
