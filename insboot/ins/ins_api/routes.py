from .constants import Constans


def url_format(url):
    return url


def get_url(key, data):
    return Constans.API_ENDPOINT + URLS[key](data)


URLS = [url_format(route) for route in Constans.ROUTES]
