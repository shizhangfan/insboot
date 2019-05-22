import logging


class Client():
    API_URL = 'https://i.instagram.com/api/{version!s}'

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password

    def _call_api(self):
