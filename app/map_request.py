"""Requests the here map API."""


import requests


def get_coordinates(place):
    """Return a dict."""
    response = requests.get("")
    data = response.json()
    return data
