# URL c14n

[![Build Status](https://travis-ci.org/info-labs/python-url-c14n.svg?branch=master)](https://travis-ci.org/info-labs/python-url-c14n)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

URL Canonicalization utility

## See also

* <http://tools.ietf.org/html/rfc3986#section-6>
* <http://en.wikipedia.org/wiki/URL_normalization>
* <http://tools.ietf.org/html/rfc5849#section-3.4.1.3.2>

## Usage

```python
from url_c14n import url_c14n
url_c14n("HTTP://example.com:80/path/to/../../normalized//path/?c=x&b=y&a=z")
# http://example.com/normalized/path/?a=z&b=y&c=x
```
