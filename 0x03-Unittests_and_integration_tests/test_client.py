#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""
        # Configure the mock to return a known payload for the org
        mock_get_json.return_value = {"payload": True}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Access the org property without calling it
        result = client.org

        # Assert that the result is not None
        self.assertIsNotNone(result)

        # Assert that get_json was called with the correct URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    @patch('client.get_json')
    def test_public_repos_url(self, org_name, expected_url, mock_get_json):
        """Test GithubOrgClient._public_repos_url property"""
        # Configure the mock to return a known payload for the org
        mock_get_json.return_value = {"repos_url": expected_url}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Access the _public_repos_url property
        result = client._public_repos_url

        # Assert that the result matches the expected URL
        self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
