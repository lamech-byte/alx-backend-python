#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient"""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url property"""
        # Create a mock for the GithubOrgClient.org property
        mock_org_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }
        mock_org.return_value = mock_org_payload

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("testorg")

        # Access the _public_repos_url property
        result = client._public_repos_url

        # Assert that the result is equal to the expected URL
        expected_url = "https://api.github.com/orgs/testorg/repos"
        self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
