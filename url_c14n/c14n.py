import os
import re
import urllib

try:
    from urllib.parse import urlsplit, urlunsplit
except ImportError:
    from urlparse import urlsplit, urlunsplit


def url_c14n(s):
    # URL C14N
    #   see also:
    #    + <http://tools.ietf.org/html/rfc3986#section-6>
    #    + <http://en.wikipedia.org/wiki/URL_normalization>
    scheme, netloc, path, qs, anchor = urlsplit(s)
    # converting the scheme and host to lower case.
    scheme = scheme.lower()
    netloc = netloc.lower()
    # capitalizing letters in escape sequences
    path = _capitalize_escape_sequence(path)
    qs = _capitalize_escape_sequence(qs)
    # decoding percent-encoded octets of unreserved characters
    path = _decode_unreserved_escape(path)
    qs = _decode_unreserved_escape(qs)
    # removing the default port
    if scheme == 'http' and netloc.endswith(':80'):
        netloc = netloc[:-3]
    # adding trailing / (root path only)
    if not path:
        path = '/'
    # removing dot-segments
    path_last = ''
    if path and path[-1] == '/':
        path_last = '/'
    path = os.path.normpath(path)
    if path and path[-1] != '/':
        path += path_last
    # removing duplicate slashes
    path = re.sub('//+', '/', path)
    # sorting the query parameters
    #   see also (informational):
    #    + <http://tools.ietf.org/html/rfc5849#section-3.4.1.3.2>
    if qs:
        params = {}
        for param in qs.split('&'):
            tmp = param.split('=', 1)
            if len(tmp) == 1:
                # `a=1&b&c=2` to `a=1&b=&c=2`
                tmp.append('')
            key = tmp[0]
            value = tmp[1]
            if key not in params:
                params[key] = []
            params[key].append(value)
        queries = []
        # sort by key
        for key in sorted(params.keys()):
            # sort by value, if same key exists
            for value in sorted(params[key]):
                queries.append('='.join([key, value]))
        qs = '&'.join(queries)
    return urlunsplit((scheme, netloc, path, qs, anchor))

def _capitalize_escape_sequence(s):
    return re.sub(r'%[a-f0-9]{2}', lambda x: x.group(0).upper(), s)

def _decode_unreserved_escape(s):
    return RE_UNRESERVED.sub(lambda x: chr(int(x.group(1), 16)), s)

ALPHA = list(range(0x41, 0x5a+1))+list(range(0x61, 0x7a+1))
DIGIT = list(range(0x30, 0x39+1))

UNRESERVED = ALPHA + DIGIT + [0x2d, 0x2e, 0x5f, 0x7e]
RE_UNRESERVED = re.compile('(?i)%({0})'.format(
    '|'.join(['{0:02X}'.format(x) for x in UNRESERVED])
))
