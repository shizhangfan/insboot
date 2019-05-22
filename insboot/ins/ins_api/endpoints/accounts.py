import json


class AccountsEndpointMixin(object):

    def login(self):
        """Login."""

        prelogin_params = self._call_api(
            'si/fetch_headers',
            params
        )
