#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    def setUp(self):
        self.get_json_patch = unittest.mock.patch('client.get_json')
        self.mock_get_json = self.get_json_patch.start()
        self.mock_get_json.return_value = {"payload": True}

    def tearDown(self):
        self.get_json_patch.stop()

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_org(self, org_name):
        """Test GithubOrgClient.org method"""
        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Access the org property without calling it
        result = client.org

        # Assert that the result is not None
        self.assertIsNotNone(result)

        # Assert that get_json was called with the correct URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        self.mock_get_json.assert_called_once_with(expected_url)

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    def test_public_repos_url(self, org_name, expected_url):
        """Test GithubOrgClient._public_repos_url property"""
        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Access the _public_repos_url property
        result = client._public_repos_url

        # Assert that the result matches the expected URL
        self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
