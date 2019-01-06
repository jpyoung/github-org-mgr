__author__ = 'john.young'
import requests
import os
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Requestable(object):

    def __init__(self, auth, baseAPI):
        self._baseAPI = baseAPI
        self._auth = auth

    def __get_url(self, api_route):
        """
        Return the full URL for API Call
        :param api_route:
        :return:
        """
        return self._baseAPI + api_route

    def __get_header(self):
        """
        Return the request header using the auth token provided to the constructor

        :return: dict - header
        """

        header = {
            'accept': "application/vnd.github.v3+json",
            'content-type': "application/json",
            'authorization': "Basic {}".format(str(self._auth['token'])),
        }
        return header

    def _request(self, method, path, data=None):
        """
        Generic function for making HTTP requests to the API

        :param method: [POST, GET, PATCH]
        :param path:
        :param data:
        :return:
        """

        full_url = self.__get_url(path)
        payload = data
        reponse = requests.request(method, full_url, headers=self.__get_header())
        return reponse


    def listLabels(self, repository):
        """
        List the labels for a given repository

        :param repository: org/repo
        :return:
        """
        return self._request("GET", "/repos/{}/labels".format(str(repository)))




	







