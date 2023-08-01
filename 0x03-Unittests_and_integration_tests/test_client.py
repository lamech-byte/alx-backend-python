#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.org method"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    # Existing test for the org method (same as before)

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch('client.get_json')  # Patch get_json method
    def test_org(self, org_name, expected_result, mock_get_json):
        # Same as before
        pass

    @parameterized.expand([
        (
            "google", "https://api.github.com/orgs/google/repos", {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
        ),
        (
            "abc", "https://api.github.com/orgs/abc/repos", {
                "repos_url": "https://api.github.com/orgs/abc/repos"
            }
        )
    ])
    @patch('client.get_json')  # Patch get_json method
    def test_public_repos_url(
        self, org_name, expected_url, expected_result, mock_get_json
    ):
        """Test GithubOrgClient._public_repos_url property"""
        # Configure the mock_get_json to return the expected result
        mock_get_json.return_value = expected_result

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Access the _public_repos_url property
        result = client._public_repos_url

        # Assert that get_json was called once with the correct argument
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        # Assert that the result is equal to the expected URL
        self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
