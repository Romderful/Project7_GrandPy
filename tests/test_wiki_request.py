"""Tests of the application."""


from app.models.wiki_request import WikiAPI


def test_request_returns_title(monkeypatch):
    """Test if the function catch the page title."""

    class FakeResponse:
        def __init__(self, url, params=None):
            pass

        def json(self):
            """Return a fake json request."""
            page_title = {"geosearch": [{"title": "bordeaux"}]}
            return {"query": page_title}

    monkeypatch.setattr("app.models.wiki_request.requests.get", FakeResponse)
    result = WikiAPI().get_page_title(40, 50)
    assert result == "bordeaux"


def test_request_returns_description(monkeypatch):
    """Test if the function catch the page description."""

    class FakeResponse:
        def __init__(self, url, params=None):
            pass

        def json(self):
            """Return a fake json request."""
            description = "Atur est une ancienne commune française située..."
            return {"extract": description}

    monkeypatch.setattr("app.models.wiki_request.requests.get", FakeResponse)
    monkeypatch.setattr(
        "app.models.wiki_request.random.choice",
        lambda introduction: "Tiens, ça me rappel... ",
    )
    result = WikiAPI().get_page_description("atur")
    assert (
        result
        == "Tiens, ça me rappel... Atur est une ancienne commune française située..."
    )
