#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map, utils.get_json, and utils.memoize"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
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

        # Assert that the mocked requests.get method was called exactly once
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to the expected
        self.assertEqual(result, test_payload)


class TestClass:
    def a_method(self):
        return 42

    @property
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """Test the memoize decorator"""
        # Create an instance of TestClass
        instance = TestClass()

        # Patch the a_method in the TestClass
        with patch.object(TestClass, 'a_method') as mock_a_method:
            # Configure the mock_a_method to return a specific value when called
            mock_a_method.return_value = 42

            # Call the a_property method twice
            result1 = instance.a_property
            result2 = instance.a_property

            # Assert that the mock_a_method was called exactly once
            mock_a_method.assert_called_once()

            # Assert that the results of both calls are the same (memoized result)
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
