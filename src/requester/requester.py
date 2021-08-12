import ast
import time
import requests

from src.requester.constants import *


class Requester(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.session_token = ""
        self.return_value = ""
        self.response_status = ""
        self.authenticated = False
        self.authenticate(api_key)

    def authenticate(self, api_key):
        """
        Obtains token needed for subsequent requests.

        :param api_key: string
        """

        api_response = ast.literal_eval(requests.post(
            API_BASE_URL + I_AUTHENTICATE,
            data={API_KEY: api_key}).text)

        if api_response[RESPONSE_STATUS] == OK:
            self.session_token = api_response[RETURN_VALUE]
            self.authenticated = True

    def request(self, interface, method, data=None):
        """
        Performs all API requests.

        :param interface: string
        :param method: string
        :param data: dict
        """

        api_response = {RESPONSE_STATUS: "", RETURN_VALUE: 0}

        for i in range(2):

            url = API_BASE_URL + interface + TOKEN_KEY + self.session_token

            if method == GET:
                api_response = ast.literal_eval(requests.get(
                    url,
                    params=data).text)
            elif method == POST:
                api_response = ast.literal_eval(requests.post(
                    url,
                    data=data).text)
            elif method == PUT:
                api_response = ast.literal_eval(requests.put(
                    url,
                    data=data).text)
            elif method == DELETE:
                api_response = ast.literal_eval(requests.delete(
                    url,
                    params=data).text)
            elif method == OPTIONS:
                api_response = ast.literal_eval(requests.options(
                    url,
                    data=data).text)
            else:
                api_response = {RESPONSE_STATUS: NOT_OK, RETURN_VALUE: 405}
                break

            if api_response[RESPONSE_STATUS] != OK:
                if api_response[RETURN_VALUE] == TOKEN_EXPIRED:
                    self.authenticate(self.api_key)
                    continue
                if api_response[RETURN_VALUE] == QUOTA_EXCEEDED:
                    time.sleep(60)
                    continue
            break

        self.response_status = api_response[RESPONSE_STATUS]
        self.return_value = api_response[RETURN_VALUE]
