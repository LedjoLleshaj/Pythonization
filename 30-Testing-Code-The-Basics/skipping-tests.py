import unittest


class TestSkippingStuff(unittest.TestCase):
    def test_addition(self):
        self.assertTrue(True)

    def test_subtraction(self):
        self.assertTrue(True)

    @unittest.skip("To be implemented later")
    def test_multiplication(self):
        pass


if __name__ == "__main__":
    unittest.main()
