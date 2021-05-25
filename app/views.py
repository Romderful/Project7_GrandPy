"""Views module."""


from . import app
from flask.templating import render_template


@app.route("/")
def index():
    """Return the index page of the application."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Return the about file."""
    return render_template("about.html")
