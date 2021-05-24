"""Parser."""


import re
from app import stopwords


class Parser:
    """Class Parser."""

    @staticmethod
    def parse(sentence):
        """Parse the words."""
        lowered_sentence = sentence.lower()
        filtered_symbols = re.sub("[!@#$?,:;.~%§><&]", "", lowered_sentence)
        filtered_junctions = re.sub(r"((\s|^)\w{1}\')|\-", " ", filtered_symbols)

        word_list = filtered_junctions.split()
        filtered = [word for word in word_list if word not in stopwords]

        return " ".join(filtered)
