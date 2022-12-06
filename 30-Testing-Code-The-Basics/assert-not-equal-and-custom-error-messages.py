import unittest


def copy_and_add_element(values, element):
    copy = values.copy()
    copy.append(element)
    return copy


class TestInequality(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(1, 2)
        # self.assertNotEqual(1, 1, "One is equal to one")

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertNotEqual(values, result, "The original list should not be modified")


if __name__ == "__main__":
    unittest.main()
