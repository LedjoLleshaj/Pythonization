import unittest


def explicit_return_sum(a, b):
    return a + b


def implicit_return_sum(a, b):
    print(a + b)


class TestNone(unittest.TestCase):
    def test_explicit_return(self):
        self.assertEqual(explicit_return_sum(1, 2), 3)
        self.assertNotEqual(explicit_return_sum(1, 2), None)

    def test_implicit_return(self):
        self.assertEqual(implicit_return_sum(1, 2), None)
        self.assertNotEqual(implicit_return_sum(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
