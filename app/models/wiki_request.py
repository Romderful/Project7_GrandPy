"""Request the wikipedia API."""


import requests
import random


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
            "gsradius": "1000",
            "gscoord": f"{lat}|{lng}",
            "format": "json",
        }
        response = requests.get(self.title_url, params=params)
        data = response.json()
        try:
            title_index = random.randrange(len(data["query"]["geosearch"]))
            page_title = data["query"]["geosearch"][title_index]["title"]
        except (IndexError, KeyError):
            return None
        else:
            return page_title

    def get_page_description(self, title):
        """Return the place description."""
        url = self.description_url + title
        response = requests.get(url)
        data = response.json()
        page_description = data["extract"]
        return page_description
