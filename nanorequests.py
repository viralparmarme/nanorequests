import requests

from .exceptions import *


class NanoRequests:
    @staticmethod
    def _make_request(method, url, headers=None, json=None, timeout=None, **kwargs):
        try:
            response = method(url, headers=headers, json=json, timeout=timeout, **kwargs)
            return NanoRequests._handle_response(response)
        except requests.Timeout:
            raise TimeoutException('Request timed out.')
        except requests.ConnectionError:
            raise ConnectionErrorException('Connection error.')
        except requests.exceptions.RequestException:
            raise NoInternetException('No internet connection.')

    @staticmethod
    def get(url, headers=None, params=None, timeout=None, **kwargs):
        return NanoRequests._make_request(requests.get, url, headers=headers, params=params, timeout=timeout, **kwargs)

    @staticmethod
    def post(url, headers=None, json=None, timeout=None, **kwargs):
        return NanoRequests._make_request(requests.post, url, headers=headers, json=json, timeout=timeout, **kwargs)

    @staticmethod
    def put(url, headers=None, json=None, timeout=None, **kwargs):
        return NanoRequests._make_request(requests.put, url, headers=headers, json=json, timeout=timeout, **kwargs)

    @staticmethod
    def delete(url, headers=None, timeout=None, **kwargs):
        return NanoRequests._make_request(requests.delete, url, headers=headers, timeout=timeout, **kwargs)

    @staticmethod
    def patch(url, headers=None, json=None, timeout=None, **kwargs):
        return NanoRequests._make_request(requests.patch, url, headers=headers, json=json, timeout=timeout, **kwargs)

    @staticmethod
    def _handle_response(response):
        if response.status_code // 100 == 2:  # 2XX status codes
            if 'application/json' in response.headers.get('content-type', ''):
                try:
                    return response.json()
                except ValueError:
                    return {'message': response.text}
            else:
                return {'message': response.text}
        elif response.status_code // 100 == 3:  # 3XX status codes
            raise RedirectionException(response.status_code, response.text)
        elif response.status_code == 400:  # 400 Bad Request
            raise BadRequestException(response.status_code, response.text)
        elif response.status_code == 401:  # 401 Unauthorized
            raise UnauthorizedException(response.status_code, response.text)
        elif response.status_code == 403:  # 403 Forbidden
            raise ForbiddenException(response.status_code, response.text)
        elif response.status_code == 404:  # 404 Not Found
            raise NotFoundException(response.status_code, response.text)
        elif response.status_code == 409:  # 409 Conflict
            raise ConflictException(response.status_code, response.text)
        elif response.status_code == 429:  # 429 Too Many Requests
            raise TooManyRequestsException(response.status_code, response.text)
        elif response.status_code // 100 == 4:  # 4XX status codes
            raise ClientErrorException(response.status_code, response.text)
        elif response.status_code == 500:  # 500 Internal Server Error
            raise InternalServerErrorException(response.status_code, response.text)
        elif response.status_code == 502:  # 502 Bad Gateway
            raise BadGatewayException(response.status_code, response.text)
        elif response.status_code == 503:  # 503 Service Unavailable
            raise ServiceUnavailableException(response.status_code, response.text)
        elif response.status_code == 504:  # 504 Gateway Timeout
            raise GatewayTimeoutException(response.status_code, response.text)
        else:
            raise UnknownException(response.status_code, response.text)
