"""Views module."""


from . import app
from flask import render_template, jsonify, request
from .parser import Parser


@app.route("/")
def index():
    """Return the index page of the application."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Return the about page of the application."""
    return render_template("about.html")


@app.route("/process", methods=["POST"])
def process():
    """Ajax request."""
    user_text = request.form["data"]
    place = Parser().parse(user_text)
    """
    coordinates = HereAPI().get_coordinates(place)
    wikitext = WikiAPI().get_wiki_text(coordinates)
    """
    print(place)
    return jsonify("""coordinates, wikitext""")
