#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.org method"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient.org method"""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch('client.get_json')  # Patch get_json method
    def test_org(self, org_name, expected_result, mock_get_json):
        """Test GithubOrgClient.org method"""
        # Configure the mock_get_json to return the expected result
        mock_get_json.return_value = expected_result

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Assert that get_json was called once with the correct argument
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        # Assert that the result is equal to the expected_result
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
