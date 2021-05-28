"""Tests of the application."""


from app.map_request import get_coordinates


def test_request_returns_correct_values(monkeypatch):
    """Test if the function catch the position and the title."""

    class FakeResponse:
        def __init__(self, url, params=None):
            pass

        def json(self):
            """Return a fake json with the coordinates and the place title."""
            location = {"lat": 20, "lng": 30}
            items = [{"position": location, "title": "Tour Eiffel"}]
            return items[0]

    monkeypatch.setattr("app.map_request.requests.get", FakeResponse)
    result = get_coordinates("tour eiffel")

    assert result["position"] == {"lat": 20, "lng": 30}
    assert result["title"] == "Tour Eiffel"
