from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_name):
        """Reads file and prints number of words read"""
        self.file = self.call_file(file_name)
        print(f"{len(self.file)} words read")

    def __repr__(self):
        """"""
        return f"{self}"

    def call_file(self, file):
        """Opens file and returns list of words with lines stripped"""
        return [item.strip() for item in open(file)]

    def random(self):
        """Returns a random word from list of words"""
        # return [line for line in file]
        return choice(self.file)

class SpecialWordFinder(WordFinder):
    """subclass of WordFinder"""
    def __init__(self, file_name):
        super().__init__(file_name)

    def call_file(self, file):
        return [item.strip() for item in open(file) if not item.startswith('#') or item == '']

