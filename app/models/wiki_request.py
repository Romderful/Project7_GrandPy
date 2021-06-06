"""Requests the wikipedia API."""


import requests


class WikiAPI:
    """Class WikiAPI."""

    @staticmethod
    def get_page_id(lat, lng):
        """Return a dict with the place coordinates."""
        url = "http://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "geosearch",
            "gsradius": "10000",
            "gscoord": f"{lat}|{lng}",
            "format": "json",
        }
        response = requests.get(url, params=params)
        data = response.json()
        try:
            pageid = data["query"]["geosearch"][0]["pageid"]
        except (IndexError, KeyError):
            return None
        else:
            return pageid
