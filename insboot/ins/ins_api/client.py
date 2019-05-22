import logging
import hashlib
import uuid
import json
import re
import time
import random
from datetime import datetime
import gzip
from io import BytesIO
import warnings
from socket import timeout, error as SocketError
from ssl import SSLError
from .compat import (
    compat_urllib_request, compat_urllib_parse,
    compat_urllib_error, compat_urllib_parse_urlparse,
    compat_http_client
)
from .errors import (
    ErrorHandler, ClientError,
    ClientLoginRequiredError, ClientCookieExpiredError,
    ClientConnectionError
)

from .http import ClientCookieJar

from .constants import Constants
logger = logging.getLogger(__name__)


class Client:
    API_URL = 'https://i.instagram.com/api/{version!s}'

    USER_AGENT = Constants.USER_AGENT
    IG_SIG_KEY = Constants.IG_SIG_KEY
    IG_CAPABILITIES = Constants.IG_CAPABILITIES
    SIG_KEY_VERSION = Constants.SIG_KEY_VERSION
    APPLICATION_ID = Constants.APPLICATION_ID

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
        self.auto_patch = kwargs.pop('auto_patch', False)
        self.drop_incompat_keys = kwargs.pop('drop_incompat_keys', False)
        self.api_url = kwargs.pop('api_url', None) or self.API_URL
        self.timeout = kwargs.pop('timeout', 15)
        self.logger = logger

        user_settings = kwargs.pop('settings', None) or {}
        self.uuid = (
            kwargs.pop('guid', None) or kwargs.pop('uuid', None) or
            user_settings.get('uuid') or self.generate_uuid(False)
        )
        self.device_id = (
            kwargs.pop('device_id', None) or user_settings.get('device_id') or
            self.generate_deviceid()
        )

        # application session ID
        self.session_id = (
            kwargs.pop('session_id', None) or user_settings.get('session_id') or
            self.generate_uuid(False)
        )
        self.signature_key = (
            kwargs.pop('signature_key', None) or user_settings.get('signature_key') or
            self.IG_SIG_KEY
        )
        self.key_version = (
            kwargs.pop('key_version', None) or user_settings.get('key_version') or
            self.SIG_KEY_VERSION
        )
        self.ig_capabilities = (
                kwargs.pop('ig_capabilities', None) or user_settings.get('ig_capabilities') or
                self.IG_CAPABILITIES)
        self.application_id = (
                kwargs.pop('application_id', None) or user_settings.get('application_id') or
                self.APPLICATION_ID)

        # to maintain backward compat for user_agent kwarg
        custom_ua = kwargs.pop('user_agent', None) or user_settings.get('user_agent')

        if custom_ua:
            self.user_agent = custom_ua
        else:
            self.app_version = (
                    kwargs.pop('app_version', None) or user_settings.get('app_version') or
                    Constants.APP_VERSION)
            self.android_release = (
                    kwargs.pop('android_release', None) or user_settings.get('android_release') or
                    Constants.ANDROID_RELEASE)
            self.android_version = int(
                kwargs.pop('android_version', None) or user_settings.get('android_version') or
                Constants.ANDROID_VERSION)
            self.phone_manufacturer = (
                    kwargs.pop('phone_manufacturer', None) or user_settings.get('phone_manufacturer') or
                    Constants.PHONE_MANUFACTURER)
            self.phone_device = (
                    kwargs.pop('phone_device', None) or user_settings.get('phone_device') or
                    Constants.PHONE_DEVICE)
            self.phone_model = (
                    kwargs.pop('phone_model', None) or user_settings.get('phone_model') or
                    Constants.PHONE_MODEL)
            self.phone_dpi = (
                    kwargs.pop('phone_dpi', None) or user_settings.get('phone_dpi') or
                    Constants.PHONE_DPI)
            self.phone_resolution = (
                    kwargs.pop('phone_resolution', None) or user_settings.get('phone_resolution') or
                    Constants.PHONE_RESOLUTION)
            self.phone_chipset = (
                    kwargs.pop('phone_chipset', None) or user_settings.get('phone_chipset') or
                    Constants.PHONE_CHIPSET)
            self.version_code = (
                    kwargs.pop('version_code', None) or user_settings.get('version_code') or
                    Constants.VERSION_CODE)

            cookie_string = kwargs.pop('cookie', None) or user_settings.get('cookie')
            cookie_jar = ClientCookieJar(cookie_string=cookie_string)
            if cookie_string and cookie_jar.auth_expires and int(time.time()) >= cookie_jar.auth_expires:
                raise ClientCookieExpiredError('Cookie expired at {0!s}'.format(cookie_jar.auth_expires))
            cookie_handler = compat_urllib_request.HTTPCookieProcessor(cookie_jar)

            proxy_handler = kwargs.pop('proxy_handler', None)
            if not proxy_handler:
                proxy = kwargs.pop('proxy', None)
                if proxy:
                    warnings.warn('Proxy support is alpha.', UserWarning)
                    parsed_url = compat_urllib_parse_urlparse(proxy)
                    if parsed_url.netloc and parsed_url.scheme:
                        proxy_address = '{0!s}://{1!s}'.format(parsed_url.scheme, parsed_url.netloc)
                        proxy_handler = compat_urllib_request.ProxyHandler({'https': proxy_address})
                    else:
                        raise ValueError('Invalid proxy argument: {0!s}'.format(proxy))
            handlers = []
            if proxy_handler:
                handlers.append(proxy_handler)

            # Allow user to override custom ssl context where possible
            custom_ssl_context = kwargs.pop('custom_ssl_context', None)
            try:
                https_handler = compat_urllib_request.HTTPSHandler(context=custom_ssl_context)
            except TypeError:
                # py version < 2.7.9
                https_handler = compat_urllib_request.HTTPSHandler()

            handlers.extend([
                compat_urllib_request.HTTPHandler(),
                https_handler,
                cookie_handler])
            opener = compat_urllib_request.build_opener(*handlers)
            opener.cookie_jar = cookie_jar
            self.opener = opener

            # ad_id must be initialised after cookie_jar/opener because
            # it relies on self.authenticated_user_name
            self.ad_id = (
                    kwargs.pop('ad_id', None) or user_settings.get('ad_id') or
                    self.generate_adid())

            if not cookie_string:  # [TODO] There's probably a better way than to depend on cookie_string
                if not self.username or not self.password:
                    raise ClientLoginRequiredError('login_required', code=400)
                self.login()

            self.logger.debug('USERAGENT: {0!s}'.format(self.user_agent))
            super(Client, self).__init__()

    @property
    def settings(self):
        """
        Helper property that extracts the settings that you should cache in addition to username and password.
        :return:
        """

        return {
            'uuid': self.uuid,
            'device_id': self.device_id
        }

    @classmethod
    def generate_uuid(cls, return_hex=False, seed=None):
        """
        Generate uuid
        :param return_hex: Return in hex format
        :param seed: Save value to generate a consistent uuid
        :return:
        """
        if seed:
            m = hashlib.md5()
            m.update(seed.encode('utf-8'))
            new_uuid = uuid.UUID(m.hexdigest())
        else:
            new_uuid = uuid.uuid1()
        if return_hex:
            return new_uuid.hex
        return str(new_uuid)

    @classmethod
    def generate_deviceid(cls, seed=None):
        """
        Generate an android device ID

        :param seed: Seed value to generate a consistent device ID
        :return:
        """
        return 'android-{0!s}'.format(cls.generate_uuid(True, seed)[:16])

    def _call_api(self, endpoint, params=None, query=None, return_response=False, unsigned=False, version='v1'):
        """
        Calls the private api

        :param endpoint: endpoint path that should end with '/', example 'discover/explore/'
        :param params: POST parameters
        :param query: GET url query parameters
        :param return_response: return the response instead of the parsed json object
        :param unsigned: use post params as-is without signing
        :param version: for the versioned api base url. Default 'v1'.
        :return:
        """
        url = '{0}{1}'.format(self.api_url.format(version=version), endpoint)
        if query:
            url += ('?' if '?' not in endpoint else '&') + compat_urllib_parse.urlencode(query)

