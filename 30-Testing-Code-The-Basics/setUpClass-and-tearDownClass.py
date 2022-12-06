import unittest

"""
    THese kind of test are used for heavy operation 
    Like database connection or API calls
    that need to be done only once
"""


class Testoperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("I am setUpClass and i am called only once before anything else")

    @classmethod
    def tearDownClass(cls):
        print("I am tearDownClass and i am called only once after everything else")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])


if __name__ == "__main__":
    unittest.main()
