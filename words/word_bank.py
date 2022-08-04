from random import choice

DEFAULT_LENGTH = 100
DEFAULT_PATH = "./words/words.txt"

class WordBank:
    def __init__(self, word_length=DEFAULT_LENGTH, path=DEFAULT_PATH):
        self.word_list = self.generate_word_list(path)
        self.word_length = word_length
        self.word = self.set_word(word_length)


    def generate_word_list(self, path):
        with open(path, "r") as file:
            words = [line.strip("\n").lower() for line in file.readlines()]
        return words

    def set_word(self, word_length):
        # TODO: create a list of words of the specified word_length
        # randomly select one of those words and return it
        return choice(self.word_list)

    def get_word(self):
        return self.word
