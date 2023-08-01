#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.org method"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    # Existing test methods

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
        # Same as before
        pass

    @parameterized.expand([
        ("google", "license_key", ["repo1", "repo2"]),
        ("abc", None, ["repo3", "repo4", "repo5"]),
        ("xyz", "other_license", [])
    ])
    @patch('client.get_json')  # Patch get_json method
    def test_public_repos(
        self, org_name, license_key, expected_repos, mock_get_json
    ):
        """Test GithubOrgClient.public_repos method"""
        # Configure the mock_get_json to return the expected result
        mock_get_json.return_value = {
            "name": "repo1", "license": {
                "key": "license_key"
                                        }
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Mock the _public_repos_url property
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = f"https://api.github.com/orgs/{
                org_name
            }/repos"

            # Call the public_repos method
            result = client.public_repos(license=license_key)

            # Assert that get_json was called once with the correct argument
            mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}/repos"
            )

            # Assert that the result is equal to the expected repos list
            self.assertEqual(result, expected_repos)


if __name__ == '__main__':
    unittest.main()
