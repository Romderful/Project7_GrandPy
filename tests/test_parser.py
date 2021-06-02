"""Tests of the application."""


import pytest
from app.models.parser import Parser


@pytest.mark.parametrize(
    "words",
    [
        ("bonjour"),
        ("Salut"),
        ("hey"),
        ("Hey papi tu peux me dire comment tu vas ?"),
        ("aujourd'hui"),
        ("idée"),
        ("situé"),
        ("avoir"),
        ("emplacement"),
    ],
)
def test_catch_stopwords(words):
    """Test if the function catch the stopwords."""
    assert Parser().parse(words) == ""


@pytest.mark.parametrize(
    "words",
    [("Paris"), ("Toulouse"), ("Bordeaux")],
)
def test_catch_locations(words):
    """Test if the function catch the places."""
    assert Parser().parse(words) == words.lower()


@pytest.mark.parametrize(
    "sentence,expected",
    [
        (
            "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier"
            + " soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se"
            + " trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?",
            "fribourg",
        ),
        (
            "Bonsoir Grandpy, j'espère que tu as passé une belle semaine."
            + " Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel?"
            + " Merci d'avance et salutations à Mamie.",
            "tour eiffel",
        ),
    ],
)
def test_parser_test_complete_sentences(sentence, expected):
    """Situationals tests."""
    assert Parser().parse(sentence) == expected
