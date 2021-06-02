"""Tests of the application."""


from app.models.map_request import HereAPI


def test_request_returns_correct_values(monkeypatch):
    """Test if the function catch the position and the title."""

    class FakeResponse:
        def __init__(self, url, params=None):
            pass

        def json(self):
            """Return a fake json with the coordinates and the place title."""
            location = {"lat": 20, "lng": 30}
            items = [{"position": location}]
            return {"items": items}

    monkeypatch.setattr("app.models.map_request.requests.get", FakeResponse)
    result = HereAPI().get_coordinates("tour eiffel")
    assert result == {"lat": 20, "lng": 30}
