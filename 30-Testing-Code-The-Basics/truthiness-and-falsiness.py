import unittest


class TruthinessAndFalsiness(unittest.TestCase):
    def test_truthiness(self):
        self.assertTrue(True)
        self.assertTrue(1)
        self.assertTrue("Hello")
        self.assertTrue([1, 2, 3])

    def test_falsiness(self):
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse([])
        self.assertFalse(None)


if __name__ == "__main__":
    unittest.main()
