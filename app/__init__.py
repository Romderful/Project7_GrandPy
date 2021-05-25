"""App entry point."""


import json
from pathlib import Path

from flask import Flask


app = Flask(__name__)

words_path = Path().resolve() / "app" / "stopwords.json"
with open(words_path, encoding="utf-8") as data:
    stopwords = json.load(data)

from . import views
