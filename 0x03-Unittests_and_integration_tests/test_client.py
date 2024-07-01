#!/usr/bin/env python3
"""Module containing unit tests for GithubOrgClient class"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test the _public_repos_url property"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url', new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos method"""
        mock_public_repos_url.return_value = (
            "https://api.github.com/orgs/google/repos"
        )
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get"""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return Mock(json=lambda: cls.org_payload)
            elif url == "https://api.github.com/orgs/google/repos":
                return Mock(json=lambda: cls.repos_payload)
            return None

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
