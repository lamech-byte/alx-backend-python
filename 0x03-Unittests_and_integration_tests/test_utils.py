#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map and utils.get_json"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
        self, nested_map, path, expected_exception
    ):
        """Test access_nested_map function for KeyError"""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertIsInstance(context.exception, expected_exception)


class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function"""
        # Configure the Mock object to return test_payload when json()
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        # Call the get_json function with the test URL
        result = get_json(test_url)

        # Assert that the mocked requests.get method was called exactly
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to the expected
        self.assertEqual(result, test_payload)


class TestClass:
    def a_method(self):
        return 42

    _a_property = None

    @property
    def a_property(self):
        if self._a_property is None:
            self._a_property = self.a_method()
        return self._a_property


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator"""

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """Test the memoize decorator"""
        # Configure the mock_a_method to return a specific value
        mock_a_method.return_value = 42

        # Create an instance of TestClass
        instance = TestClass()

        # Call the a_property method twice
        result1 = instance.a_property
        result2 = instance.a_property

        # Assert that the mock_a_method was called exactly once
        mock_a_method.assert_called_once()

        # Assert that the results of both calls are the same
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
