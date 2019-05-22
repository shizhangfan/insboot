try:
    import urllib.request as compat_urllib_request
except ImportError:
    import urllib2 as compat_urllib_request

try:
    import urllib.error as compat_urllib_error
except ImportError:
    import urllib2 as compat_urllib_error

try:
    import urllib.parse as compat_urllib_parse
except ImportError:
    import urllib as compat_urllib_parse

try:
    from urllib.parse import urlparse as compat_urllib_parse_urlparse
except ImportError:
    from urlparse import urlparse as compat_urllib_parse_urlparse

try:
    import http.cookiejar as compat_cookiejar
except ImportError:
    import cookielib as compat_cookiejar

try:
    import http.cookies as compat_cookies
except ImportError:
    import Cookie as compat_cookies

try:
    import cPickle as compat_pickle
except ImportError:
    import pickle as compat_pickle

try:
    import http.client as compat_http_client
except ImportError:
    import httplib as compat_http_client
