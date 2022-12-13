# patches are useful to mock deep hearchy of objects

import urllib.request
import unittest
from unittest.mock import patch


class WebRequest:
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        print(response.status)
        if response.status != 200:
            return "Error"
        else:
            return "Success"


class TestWebRequest(unittest.TestCase):
    def test_execute_with_success_response(self):
        # package.module.attribute
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.return_value.status = 200
            wr = WebRequest("http://www.google.com")
            self.assertEqual(wr.execute(), "Success")

    def test_execute_with_bad_response(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.return_value.status = 404
            wr = WebRequest("http://www.google.com")
            self.assertEqual(wr.execute(), "Error")


# wr = WebRequest('http://www.google.com')
# wr.execute()

if __name__ == "__main__":
    unittest.main()
