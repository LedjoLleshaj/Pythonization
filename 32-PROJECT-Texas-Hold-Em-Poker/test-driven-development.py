# a process in which you write tests before you write any code
# the purpose of the tests is to specify and validate what the code should do
# the tests are specifications of the code's behavior
# red-green-refactor
# red: write a test that fails
# green: write the simplest code that makes the test pass
# refactor: improve the design of the code and tests
# test-driven development is a design technique
# it is a way to think about the problem before you write any code

# benefits of test-driven development
# 1. it leads to better code
# 2. it leads to better tests (if your tests are hard to write, your code is hard to use)
# better test coverage
# Every new error is a sign of improvement

import unittest


def multiply(a, b):
    total = 0
    for i in range(b):
        total += a
    return total


class TestProduct(unittest.TestCase):
    def test_multiplies_two_numbers_together(self):
        self.assertEqual(multiply(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
