import unittest
from unittest import mock

from src.exceptions import (
    RedirectionException,
    NotFoundException,
    ForbiddenException,
    TooManyRequestsException,
    BadRequestException,
    InternalServerErrorException
)
from src.nanorequests import NanoRequests


def mock_requests_get(response_status_code, response_json=None, response_text=None):
    mock_response = mock.MagicMock()
    mock_response.status_code = response_status_code
    mock_response.headers.get.return_value = 'application/json'

    if response_json is not None:
        mock_response.json.return_value = response_json

    if response_text is not None:
        mock_response.json.side_effect = ValueError
        mock_response.text = response_text

    return mock_response


class NanoRequestsTests(unittest.TestCase):
    @staticmethod
    def mock_get(response_status_code, response_json=None, response_text=None):
        return mock.patch('nanorequests.requests.get',
                          side_effect=lambda url, **kwargs: mock_requests_get(response_status_code, response_json,
                                                                              response_text))

    def test_get_success_json(self):
        url = "https://api.example.com/users/1"
        expected_response = {'id': 1, 'name': 'John Doe'}

        with self.mock_get(200, response_json=expected_response):
            response = NanoRequests.get(url)
            self.assertEqual(response, expected_response)

    def test_get_success_plain_text(self):
        url = "https://api.example.com/users/2"
        expected_response = {'message': 'User not found'}

        with self.mock_get(200, response_json=expected_response, response_text="User not found"):
            response = NanoRequests.get(url)
            self.assertEqual(response, expected_response)

    def test_get_redirection(self):
        url = "https://api.example.com/users/3"

        with self.mock_get(302):
            with self.assertRaises(RedirectionException):
                NanoRequests.get(url)

    def test_get_not_found(self):
        url = "https://api.example.com/users/4"

        with self.mock_get(404):
            with self.assertRaises(NotFoundException):
                NanoRequests.get(url)

    def test_get_forbidden(self):
        url = "https://api.example.com/users/5"

        with self.mock_get(403):
            with self.assertRaises(ForbiddenException):
                NanoRequests.get(url)

    def test_get_too_many_requests(self):
        url = "https://api.example.com/users/6"

        with self.mock_get(429):
            with self.assertRaises(TooManyRequestsException):
                NanoRequests.get(url)

    def test_get_client_error(self):
        url = "https://api.example.com/users/7"

        with self.mock_get(400):
            with self.assertRaises(BadRequestException):
                NanoRequests.get(url)

    def test_get_server_error(self):
        url = "https://api.example.com/users/8"

        with self.mock_get(500):
            with self.assertRaises(InternalServerErrorException):
                NanoRequests.get(url)


if __name__ == '__main__':
    unittest.main()
