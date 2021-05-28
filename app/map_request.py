"""Requests the here map API."""


import requests


class HereAPI:
    """Class HereAPI."""

    def get_coordinates(self, place):
        """Return a dict."""
        response = requests.get("")
        data = response.json()
        return data
