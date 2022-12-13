import unittest
from unittest.mock import MagicMock, Mock


class TestMockCalls(unittest.TestCase):
    def test_mock_calls(self):
        mock = MagicMock()
        mock()
        mock.assert_called()  # asserts if it was run at least once

    def test_not_called(self):
        mock = MagicMock()
        mock.assert_not_called()

    def test_called_with(self):
        mock = MagicMock()
        mock(1, 2, 3)
        mock.assert_called_with(1, 2, 3)

    def test_mock_attributes(self):
        mock = MagicMock()
        mock()
        mock(1, 2)
        print(mock.called)
        print(mock.call_count)
        print(mock.call_args)
        print(mock.call_args_list)


if __name__ == "__main__":
    unittest.main()
