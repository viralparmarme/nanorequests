# nanorequests

[![PyPI version](https://badge.fury.io/py/nanorequests.svg)](https://badge.fury.io/py/nanorequests)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

The `nanorequests` package is your gateway to simplified REST requests for swift API integration. This lightweight wrapper around the `requests` library streamlines HTTP requests and exception handling, making API interactions a breeze.

## Requirements

Before diving into the world of `nanorequests`, ensure you have the following dependency installed:

- [`requests`](https://requests.readthedocs.io/en/master/)

## Installation

Installing `nanorequests` is as easy as running a pip command:

```bash
pip install nanorequests
```

## Usage

Begin using `nanorequests` by importing it and creating an instance of the `NanoRequests` class. This class offers static methods for performing various types of HTTP requests:

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

The `NanoRequests` class also handles different HTTP status codes and raises specific exceptions for each one. You can catch these exceptions and handle them gracefully:

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

The `nanorequests` package offers the following features:

- Simplified methods for GET, POST, PUT, DELETE, and PATCH requests.
- Exception handling for various HTTP status codes.
- Automatic parsing of JSON responses for 2XX responses.
- Seamless integration with the `requests` library.

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

For in-depth information on each class and method, consult the source code and docstrings within the `nanorequests` package.

## Author

The `nanorequests` package is developed and maintained by Viral Parmar.

- [Twitter](https://twitter.com/viralparmarme)
- [GitHub](https://github.com/viralparmarme)
- [PyPI](https://pypi.org/user/viralparmar)

## License

This project is licensed under the terms of the MIT license. To learn more, please refer to the [LICENSE.txt](https://github.com/viralparmarme/nanorequests/blob/main/LICENSE.txt) file. Feel free to raise an issue or submit a pull request to support this project. Your contributions are welcome!
