"""Views module."""


import os
from dotenv import load_dotenv
from . import app
from flask import render_template, jsonify, request
from .models.parser import Parser
from .models.map_request import HereAPI


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
    load_dotenv()
    HERE_JS_API_KEY = os.getenv("HERE_JS_API_KEY")
    user_text = request.form["data"]
    position = Parser().parse(user_text)
    coordinates = HereAPI().get_coordinates(position)
    # wikitext = WikiAPI().get_wiki_text(coordinates)
    return jsonify(
        {"here_js_api_key": HERE_JS_API_KEY, "coordinates": coordinates}
    )  # Add coordinates / wikitext
