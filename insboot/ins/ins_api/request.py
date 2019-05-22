from .helpers import Helpers
from .routes import get_url

class Request:

    def __init__(self, *args, **kwargs):
        self.url = None
        self.method = 'GET'
        self.data = {}
        self.body_type = 'formData'
        self.options = {
            "gzip": True
        }

    @staticmethod
    def set_proxy(proxyUrl):
        if not Helpers.isValidUrl(proxyUrl):
            raise Exception("proxyUrl 不合法")
        
    def set_method(self, method):
        method = method.upper()
        if ['POST', 'GET', 'PATCH', 'PUT', 'DELETE'].index(method) > 0:
            self.method = method
        else:
            raise Exception("Method 不合法")

    def merge_options(self, options):
        if options is None:
            self._request.options = {
                "method": self._request.method,
                "url": self.url,
                "resolveWithFullResponse": True,
                "headers": self._request.headers
            }
        else:
            self._request.options = options
        
        return self

    def send(self, options, attemps):
        if attemps is None:
            attemps = 0
        self.merge_options(options)

    @property
    def resource(self):
        return self.resource

    @resource.setter
    def resource(self, resource, data):
        self.resource = resource
        self.set_url(get_url(resource, data))
        return self

