from random import choice

class WordBank:
    def __init__(self):
        self.word_list = self.generate_word_list()

    def generate_word_list(self, path="./words/words.txt"):
        with open(path, "r") as file:
            words = [line.strip("\n").lower() for line in file.readlines()]
        return words

    def get_word(self, word_length=100):
        return choice([word for word in self.word_list if len(word) <= word_length])