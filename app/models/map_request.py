"""Requests the here map API."""


import requests
import os
from dotenv import load_dotenv


class HereAPI:
    """Class HereAPI."""

    def __init__(self):
        """Initialise."""
        load_dotenv()
        self.api_key = os.getenv("HERE_REST_API_KEY")

    def get_coordinates(self, place):
        """Return a dict with the place coordinates."""
        url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {"q": place, "apiKey": self.api_key}
        response = requests.get(url, params=params)
        data = response.json()
        try:
            coordinates = data["items"][0]["position"]
        except (IndexError, KeyError):
            return None
        else:
            return coordinates
