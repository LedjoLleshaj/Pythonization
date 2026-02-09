# Testing Code: The Basics - Study Notes

Testing ensures that your code behaves as expected and helps prevent regressions.

## The `assert` Statement
The simplest form of testing. If the expression is `False`, it raises an `AssertionError`.
```python
assert 1 + 1 == 2, "Math is broken!"
```

## The `unittest` Module
A built-in framework for creating and running tests.

### Creating a Test Case
Inherit from `unittest.TestCase` and name methods starting with `test_`.

```python
import unittest

class MyTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()
```

### Common Assertion Methods
- `assertEqual(a, b)` / `assertNotEqual(a, b)`
- `assertTrue(x)` / `assertFalse(x)`
- `assertIs(a, b)` (Checks object identity)
- `assertIn(item, container)`
- `assertIsInstance(obj, cls)`
- `assertRaises(Error, func, *args)`

## Lifecycle Methods (Setup and Teardown)
- `setUp()`: Runs **before each** test method. Use it to create fresh objects.
- `tearDown()`: Runs **after each** test method.
- `setUpClass()`: Runs **once** before all tests in the class (must be `@classmethod`).
- `tearDownClass()`: Runs **once** after all tests in the class.

## `doctest`
Allows you to write tests inside your docstrings. Great for documentation that stays up-to-date.
```python
def add(a, b):
    """
    >>> add(1, 2)
    3
    """
    return a + b
```

## Skipping Tests
Use the `@unittest.skip("Reason")` decorator to bypass specific tests.
