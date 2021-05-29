"""Requests the here map API."""


import requests
from dotenv import load_dotenv
import os


class HereAPI:
    """Class HereAPI."""

    def __init__(self):
        """Initialise."""
        load_dotenv()
        self.api_key = os.getenv("HERE_MAP_API_KEY")

    def get_coordinates(self, place):
        """Return a dict with the place coordinates."""
        url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {"q": place, "apiKey": self.api_key}
        response = requests.get(url, params=params)
        data = response.json()
        return data["items"][0]["position"]
