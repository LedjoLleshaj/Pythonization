# testing functions that actually raise errors
import unittest


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


class DivideTestCase(unittest.TestCase):
    def test_divide(
        self,
    ):  # we don't actually invoke the function we pass it as an argument
        self.assertRaises(ZeroDivisionError, divide, 1, 0)
        self.assertEqual(divide(1, 1), 1)

    # a better way to test the function is to use the context manager "with"
    # which is a bit more readable and less error prone
    def test_divide_better(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
        self.assertEqual(divide(1, 1), 1)


if __name__ == "__main__":
    unittest.main()
