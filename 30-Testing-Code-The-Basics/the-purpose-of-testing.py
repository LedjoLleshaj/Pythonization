import unittest


def mutiply(a, b):
    # return a * b # we might change in the futture so having a test helps finding if we messed something up
    total = 0
    for _ in range(b):
        total += a
    return total


class MultiplyTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(mutiply(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
