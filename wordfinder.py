class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_list):
        self.file_list = self.call_file()


    def __repr__(self):
        return ""

    def call_file(self, file):
        self.file = open(file,"r")
        return

        # return [line for line in file]



