"""Views module."""

from flask import Flask
from flask.templating import render_template


app = Flask(__name__)


@app.route("/")
def index():
    """Return the index page of the application."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Return the about file."""
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
