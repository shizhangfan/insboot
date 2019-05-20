import logging


class Client():
    API_URL = 'https://i.instagram.com/api/{version!s}'

    def __init__(self, username, password, **kwargs):
        """

        :param username: Login username
        :param password: Login password
        :param kwargs: See below

        :Keyword Arguments:
            - **auto_patch**: Patch the api objects to match the public API. Default: False
            - **drop_incompat_key**: Remove api object keys that is not in the public API. Default: False
            - **timeout**: Timeout interval in seconds. Default: 15
            - **api_url**: Override the default url base
            - **cookie**: Saved cookie string from a previous session
            - **settings**: A dict of settings from a previous session
            - **on_login**: Callback after successful login
            - **proxy**: Specify a proxy ex: 'http://127.0.0.1:8888' (ALPHA)
            - **proxy_handler**: Specify your own proxy handler
        :return:

        """
        self.username = username
        self.password = password
        
