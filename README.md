# nanorequests

[![PyPI version](https://badge.fury.io/py/nanorequests.svg)](https://badge.fury.io/py/nanorequests)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

The simplest REST requests package for quick API integration.

The `nanorequests` package is a lightweight wrapper around the `requests` library, providing simplified HTTP request methods and exception handling.

## Requirements

The `nanorequests` package requires the following dependencies:

- `requests`

## Installation

You can install the `nanorequests` package using pip:

```bash
pip install nanorequests
```

## Usage

To use the `nanorequests` package, you can import it and create an instance of the `NanoRequests` class. This class provides static methods for making different types of HTTP requests.

```python
from nanorequests import NanoRequests

# Create an instance of NanoRequests
nr = NanoRequests()

# Make a GET request
response = nr.get('https://dummyjson.com/products')

# Make a POST request
payload = {'title': 'Nano Requests Python'}
response = nr.post('https://dummyjson.com/products/add', json=payload)
```

The `NanoRequests` class also handles different types of HTTP status codes and raises specific exceptions for each status code. You can catch these exceptions and handle them accordingly.

```python
from nanorequests import NanoRequests, NotFoundException

nr = NanoRequests()

try:
    response = nr.get('https://dummyjson.com/products/99999')
except NotFoundException as e:
    print(f"Product not found. Status code: {e.status_code}, Message: {e.message}")
```

## Examples

### GET Request

```python
response = nr.get('https://dummyjson.com/products/1')
print(response)
```

### POST Request

```python
payload = {'title': 'Viral Parmar'}
response = nr.post('https://dummyjson.com/products/add', json=payload)
print(response)
```

### PUT Request

```python
payload = {'title': 'Python Requests PIP'}
response = nr.put('https://dummyjson.com/products/1', json=payload)
print(response)
```

### DELETE Request

```python
response = nr.delete('https://dummyjson.com/products/1')
print(response)
```

### PATCH Request

```python
payload = {'title': 'Open Source Python'}
response = nr.patch('https://dummyjson.com/products/1', json=payload)
print(response)
```

## Features

The `nanorequests` package provides the following features:

- Simplified methods for making GET, POST, PUT, DELETE, and PATCH requests.
- Exception handling for different types of HTTP status codes.
- Support for JSON responses which are automatically parsed in case of 2XX response.
- Easy integration with the `requests` library.

### Handling Custom Exceptions

```python
from nanorequests import NanoRequests, NotFoundException, UnauthorizedException

try:
    response = NanoRequests.get('https://dummyjson.com/products/1')
    print(response)
except NotFoundException as e:
    print(f'Resource not found: {e}')
except UnauthorizedException as e:
    print(f'Unauthorized access: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
```

## Reference

For detailed information on each class and method, please refer to the source code and docstrings of the `nanorequests` package.

## Author

The `nanorequests` package is developed and maintained by Viral Parmar.

- https://twitter.com/viralparmarme
- https://github.com/viralparmarme
- https://pypi.org/user/viralparmar

## License

This project is licensed under the terms of the MIT license. Please see the [LICENSE.txt](https://github.com/viralparmarme/nanorequests/blob/main/LICENSE.txt) file for more information.
Feel free to raise an issue or pull request to support this project.
