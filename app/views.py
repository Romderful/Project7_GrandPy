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
    """Return the about file."""
    return render_template("about.html")


@app.route("/process", methods=["POST"])
def process():
    """Ajax request."""
    user_text = request.form["data"]
    response = Parser.parse(user_text)
    print(response)
    return jsonify(["pas de reponse"])
