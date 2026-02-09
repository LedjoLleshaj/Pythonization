# Testing Code: Mocking - Study Notes

Mocking is used to isolate the code being tested by replacing real objects with "test doubles" that simulate their behavior.

## The `Mock` Class
A `Mock` object can simulate any attribute or method, returning another mock object by default.

```python
from unittest.mock import Mock
m = Mock()
m.some_method() # Returns another Mock
```

## `MagicMock`
A subclass of `Mock` that has default implementations of many magic methods (like `__len__`, `__str__`, etc.).

## Configuring Mocks
- **`return_value`**: Defines what a mock returns when called.
  ```python
  m.return_value = 10
  m() # 10
  ```
- **`side_effect`**: Can raise an exception or return a different value on each call (if given a list).
  ```python
  m.side_effect = [1, 2, 3] # Returns 1, then 2, then 3
  ```

## Asserting Calls
- `assert_called()` / `assert_not_called()`
- `assert_called_with(*args, **kwargs)`
- `call_count`: Number of times the mock was called.

## The `patch` Function
Used to temporarily replace an object in a module with a mock.
- **As a decorator**: `@patch('module.object')`
- **As a context manager**: `with patch('module.object') as mock_obj:`

> [!IMPORTANT]
> When patching, specify the **target** as it is imported in the code under test, not where it is defined.

## Verifying with `spec`
Use the `spec` argument (e.g., `Mock(spec=MyClass)`) to ensure the mock only has attributes/methods that exist in the real class, preventing typos and "ghost" methods.
筋
