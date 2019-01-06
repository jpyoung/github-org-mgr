__author__ = 'john.young'
import requests


class Requestable(object):

    def __init__(self, auth, baseAPI):
        self._baseAPI = baseAPI
        self._auth = auth


    def _getURL(self, api_route):
        """
        Return the full URL for API Call
        :param api_route:
        :return:
        """
        return self._baseAPI + api_route

    def __getHeader(self):
        header = {
            'accept': "application/vnd.github.v3+json",
            'content-type': "application/json",
            'authorization': "token {}".format(str(self._auth.token)),
        }
        return header

    def _request(self, method, path, data=None):

        full_url = self._getURL(path)
        payload = data
        response = requests.request(method, full_url, payload)
        return reponse


	







