"""Tests of the application."""


from app.models.wiki_request import WikiAPI


def test_request_returns_pageid(monkeypatch):
    """Test if the function catch the page id."""

    class FakeResponse:
        def __init__(self, url, params=None):
            pass

        def json(self):
            """Return a fake json request."""
            pageid = {"geosearch": [{"pageid": 5905004}]}
            return {"query": pageid}

    monkeypatch.setattr("app.models.wiki_request.requests.get", FakeResponse)
    result = WikiAPI().get_page_id(40, 50)
    assert result == 5905004
