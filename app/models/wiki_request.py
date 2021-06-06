"""Requests the wikipedia API."""


import requests


class WikiAPI:
    """Class WikiAPI."""

    def __init__(self):
        """Initialise."""
        self.title_url = "http://fr.wikipedia.org/w/api.php"
        self.description_url = "https://fr.wikipedia.org/api/rest_v1/page/summary/"

    def get_page_title(self, lat, lng):
        """Return the place title."""
        params = {
            "action": "query",
            "list": "geosearch",
            "gsradius": "10000",
            "gscoord": f"{lat}|{lng}",
            "format": "json",
        }
        response = requests.get(self.title_url, params=params)
        data = response.json()
        try:
            page_title = data["query"]["geosearch"][0]["title"]
        except (IndexError, KeyError):
            return None
        else:
            return page_title

    def get_page_description(self, title):
        """Return the place title."""
        url = self.description_url + title
        response = requests.get(url)
        data = response.json()
        try:
            page_description = data["extract"]
        except (IndexError, KeyError):
            return None
        else:
            return page_description
