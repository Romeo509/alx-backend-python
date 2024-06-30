import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import the function to be tested


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
    ])
    def test_access_nested_map_exception(
        self, nested_map, path, expected_message
    ):
        """Test access_nested_map function raises
         KeyError with expected message."""
        with self.assertRaises(KeyError) as context_manager:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context_manager.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
