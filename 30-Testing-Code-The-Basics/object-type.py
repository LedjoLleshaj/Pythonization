import unittest


class ObjectTypeTest(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(1.0, float)
        self.assertIsInstance("1", str)
        self.assertIsInstance([1], list)
        self.assertIsInstance((1,), tuple)
        self.assertIsInstance({1}, set)
        self.assertIsInstance({1: 1}, dict)
        self.assertIsInstance(None, type(None))

    def test_not_is_instance(self):
        self.assertNotIsInstance(1, float)
        self.assertNotIsInstance(1.0, int)
        self.assertNotIsInstance("1", int)
        self.assertNotIsInstance([1], tuple)
        self.assertNotIsInstance((1,), list)
        self.assertNotIsInstance({1}, dict)
        self.assertNotIsInstance({1: 1}, list)
        self.assertNotIsInstance(None, int)


if __name__ == "__main__":
    unittest.main()
