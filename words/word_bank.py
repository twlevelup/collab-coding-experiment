from random import choice

DEFAULT_LENGTH = 100
DEAULT_PATH = "./words/words.txt"

class WordBank:
    def __init__(self, word_length=DEFAULT_LENGTH, path=DEAULT_PATH):
        self.word_list = self.generate_word_list(path)
        self.word_length = word_length
        self.word = self.set_word(word_length)
        self.letters_guessed = []
        self.guess_state = len(self.word)*'_'

    def generate_word_list(self, path):
        with open(path, "r") as file:
            words = [line.strip("\n").lower() for line in file.readlines()]
        return words

    def set_word(self, word_length):
        return choice([word for word in self.word_list if len(word) <= word_length])

    def get_word(self):
        return self.word

    def make_a_guess(self, guess):
        return

    def get_current_guess_state(self):
        return self.guess_state

    def get_letters_guessed(self):
        return ','.join(self.letters_guessed)