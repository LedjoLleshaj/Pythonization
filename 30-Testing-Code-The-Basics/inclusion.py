import unittest


class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
        # self.assertIn(1, [1, 2, 3])
        self.assertIn("l", "ledjo")
        self.assertIn(2, [1, 2, 3])
        self.assertIn(55, range(59))

    def test_exclusion(self):
        self.assertNotIn(5, [1, 2, 3])
        self.assertNotIn("l", "ledjo")
        self.assertNotIn(2, [1, 2, 3])
        self.assertNotIn(55, range(59))


if __name__ == "__main__":
    unittest.main()
