"""Parser."""


import re
import json
from pathlib import Path


class Parser:
    """Class Parser."""

    def __init__(self):
        """Initialize."""
        words_path = Path().resolve() / "app" / "stopwords.json"
        with open(words_path, encoding="utf-8") as data:
            self.stopwords = json.load(data)

    def parse(self, sentence):
        """Parse the sentence using regex lib."""
        lowered_sentence = sentence.lower()
        filtered_symbols = re.sub("[!@#$?,:;.~%§><&]", "", lowered_sentence)
        filtered_junctions = re.sub(r"((\s|^)\w{1}\')|\-", " ", filtered_symbols)

        word_list = filtered_junctions.split()
        filtered = [word for word in word_list if word not in self.stopwords]

        return " ".join(filtered)
