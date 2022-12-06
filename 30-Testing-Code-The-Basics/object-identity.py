import unittest


class IdentityTest(unittest.TestCase):
    def test_identity(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertEqual(a, b)
        self.assertIs(a, b)
        # self.assertIs(a, c) # This will actually check if a and b are the same object so it will fail


if __name__ == "__main__":
    unittest.main()
