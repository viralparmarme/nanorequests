# nanorequests: Simplified REST Requests for Swift API Integration

[![PyPI version](https://badge.fury.io/py/nanorequests.svg)](https://badge.fury.io/py/nanorequests)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

Welcome to `nanorequests`, your gateway to simplified REST requests for seamless API integration. This high-performance Python package is designed to streamline HTTP requests and provide robust exception handling, making API interactions a breeze.

## Requirements

Before diving into the world of `nanorequests`, make sure you have the following dependency installed:

- [`requests`](https://requests.readthedocs.io/en/master/): The fundamental HTTP library for Python.

## Installation

Getting started with `nanorequests` is as easy as running a single pip command:

```bash
pip install nanorequests
```

## Usage

Begin your journey with `nanorequests` by importing it and creating an instance of the `NanoRequests` class. This class offers static methods for performing various types of HTTP requests, simplifying your code and enhancing readability:

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

Don't worry about handling HTTP status codes; `NanoRequests` automatically raises specific exceptions for each one, allowing you to catch and handle them gracefully:

```python
from nanorequests import NanoRequests, NotFoundException

nr = NanoRequests()

try:
    response = nr.get('https://dummyjson.com/products/99999')
except NotFoundException as e:
    print(f"Product not found. Status code: {e.status_code}, Message: {e.message}")
```

## Examples

Explore some common use cases with `nanorequests`:

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

Discover the powerful features of the `nanorequests` package:

- Simplified methods for GET, POST, PUT, DELETE, and PATCH requests.
- Exception handling for various HTTP status codes, ensuring robustness.
- Automatic parsing of JSON responses for 2XX responses.
- Seamless integration with the widely-used `requests` library.

### Handling Custom Exceptions

Leverage custom exception handling for a more controlled development experience:

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

For comprehensive information on each class and method, consult the source code and docstrings within the `nanorequests` package.

## Author

The `nanorequests` package is proudly developed and actively maintained by Viral Parmar.

- [Twitter](https://twitter.com/viralparmarme)
- [GitHub](https://github.com/viralparmarme)
- [PyPI](https://pypi.org/user/viralparmar)

## License

This project is licensed under the terms of the MIT license. To learn more, please refer to the [LICENSE.txt](https://github.com/viralparmarme/nanorequests/blob/main/LICENSE.txt) file. Feel free to raise an issue or submit a pull request to support this project; your contributions are greatly appreciated!
