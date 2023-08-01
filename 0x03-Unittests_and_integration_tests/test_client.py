#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class


@parameterized_class([
    ("google",),
    ("abc",),
])
class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""
        expected_result = {"repos_url": f"https://api.github.com/orgs/{org_name}/repos"}

        # Configure the mock_get_json to return the expected_result
        mock_get_json.return_value = expected_result

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org()

        # Assert that get_json was called once with the correct argument
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert that the result is the same as the expected_result
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
