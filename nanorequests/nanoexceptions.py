class BadRequestException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'BadRequestException: {self.status_code} - {self.message}'


class UnauthorizedException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'UnauthorizedException: {self.status_code} - {self.message}'


class ConflictException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'ConflictException: {self.status_code} - {self.message}'


class InternalServerErrorException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'InternalServerErrorException: {self.status_code} - {self.message}'


class BadGatewayException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'BadGatewayException: {self.status_code} - {self.message}'


class RedirectionException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'RedirectionException: {self.status_code} - {self.message}'


class NotFoundException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'NotFoundException: {self.status_code} - {self.message}'


class ForbiddenException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'ForbiddenException: {self.status_code} - {self.message}'


class TooManyRequestsException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'TooManyRequestsException: {self.status_code} - {self.message}'


class ClientErrorException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'ClientErrorException: {self.status_code} - {self.message}'


class ServerErrorException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'ServerErrorException: {self.status_code} - {self.message}'


class UnknownException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'UnknownException: {self.status_code} - {self.message}'


class TimeoutException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'TimeoutException: {self.message}'


class ConnectionErrorException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'ConnectionErrorException: {self.message}'


class NoInternetException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'NoInternetException: {self.message}'


class ServiceUnavailableException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'ServiceUnavailableException: {self.status_code} - {self.message}'


class GatewayTimeoutException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'GatewayTimeoutException: {self.status_code} - {self.message}'
