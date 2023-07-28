#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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
        # Configure the Mock object to return test_payload when json() is called
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        # Call the get_json function with the test URL
        result = get_json(test_url)

        # Assert that the mocked requests.get method was called exactly once with the test URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to the expected test_payload
        self.assertEqual(result, test_payload)
