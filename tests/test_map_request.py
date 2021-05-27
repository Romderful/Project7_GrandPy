"""Tests of the application."""


from app.map_request import request_map


def test_request_returns_correct_values(monkeypatch):
    """Test if the function catch the position and the title."""

    def get_location():
        """Return a fake json with the coordinates and the place title."""
        location = {"lat": 20, "lng": 30}
        items = [{"position": location, "title": "Tour Eiffel"}]
        response = {"items": items}
        return response

    monkeypatch.setattr("app.map_request.requests", get_location)
    result = request_map("tour eiffel")

    assert result["position"] == {"lat": 20, "lng": 30}
    assert result["title"] == "Tour Eiffel"
