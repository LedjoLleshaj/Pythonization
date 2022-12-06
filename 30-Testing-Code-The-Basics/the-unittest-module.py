import unittest

# unittest.TestCase # this is the class that we will inherit from to create our test cases


# Python gods suggest that we name our test cases with the word Test in the name
# and use only one assert per test case so that we can pinpoint the exact problem


class TestStringMethods(unittest.TestCase):
    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        self.assertEqual(s.split("o"), ["hell", " w", "rld"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_count(self):
        self.assertEqual("motherfucker".count("e"), 2)


if __name__ == "__main__":
    unittest.main()
