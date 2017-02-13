import unittest
import pytest


from url_c14n import url_c14n


class URLC14NTests(unittest.TestCase):
    def check(self, source, c14ned):
        self.assertEqual(url_c14n(source), c14ned)

    def test_upper_scheme(self):
        self.check('HTTP://example.com/', 'http://example.com/')

    def test_upper_host(self):
        self.check('http://EXAMPLE.COM/HOGE', 'http://example.com/HOGE')

    def test_capitalize_escape_sequence(self):
        source = 'http://example.com/%e3%81%a6%e3%81%99%e3%81%a8'
        c14ned = 'http://example.com/%E3%81%A6%E3%81%99%E3%81%A8'
        self.check(source, c14ned)

    def test_unreserved_escape(self):
        source = 'http://example.com/%61%62%63'
        c14ned = 'http://example.com/abc'
        self.check(source, c14ned)

    def test_remove_default_port(self):
        self.check('http://example.com:80/', 'http://example.com/')
        self.check('https://example.com:443/', 'https://example.com/')

    def test_root_url(self):
        self.check('http://example.com', 'http://example.com/')

    def test_normalize_path(self):
        self.check('http://example.com/a/./b/../c', 'http://example.com/a/c')

    def test_duplicate_slash(self):
        self.check('http://example.com/a//b/////c', 'http://example.com/a/b/c')

    def test_normalize_path_last_slash(self):
        self.check('http://example.com/a/./b/../c/', 'http://example.com/a/c/')

    def test_query_order(self):
        source = 'http://example.com/?a=x&c=y&b=z'
        c14ned = 'http://example.com/?a=x&b=z&c=y'
        self.check(source, c14ned)

    def test_empty_parameter(self):
        source = 'http://example.com/?a&b=&c=z'
        c14ned = 'http://example.com/?a=&b=&c=z'
        self.check(source, c14ned)

    def test_empty_parameter(self):
        source = 'http://example.com/?a&b=&c=z'
        c14ned = 'http://example.com/?a=&b=&c=z'
        self.check(source, c14ned)
