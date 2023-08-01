#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    def test_org(self):
        """Test GithubOrgClient.org method"""
        org_names = ["google", "abc"]
        expected_urls = [
            "https://api.github.com/orgs/google/repos",
            "https://api.github.com/orgs/abc/repos",
        ]

        for i in range(len(org_names)):
            org_name = org_names[i]
            expected_url = expected_urls[i]

            # Patch get_json and return the expected URL
            with patch('client.get_json') as mock_get_json:
                mock_get_json.return_value = {"repos_url": expected_url}

                # Create an instance of GithubOrgClient
                client = GithubOrgClient(org_name)

                # Call the org method
                result = client.org()

                # Assert that get_json was called once
                mock_get_json.assert_called_once_with(
                    f"https://api.github.com/orgs/{org_name}"
                )

                # Assert that the result is the same as the expected URL
                self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
