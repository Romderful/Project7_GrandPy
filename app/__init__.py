"""App entry point."""


import json
from pathlib import Path


words_path = Path().resolve() / "app" / "stopwords.json"
with open(words_path, encoding="utf-8") as data:
    stopwords = json.load(data)
