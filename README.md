# URL c14n

[![Build Status](https://travis-ci.org/info-labs/python-url-c14n.svg?branch=master)](https://travis-ci.org/info-labs/python-url-c14n)

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
