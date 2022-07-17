from random import choice

DEFAULT_LENGTH = 100
DEAULT_PATH = "./words/words.txt"

class WordBank:
    def __init__(self, word_length=DEFAULT_LENGTH, path=DEAULT_PATH):
        self.word_list = self.generate_word_list(path)
        self.word_length = word_length
        self.word = self.set_word(word_length)
        self.letters_guessed_incorrect = []
        self.letters_guessed_correct = []
        self.guess_state = len(self.word)*'_'
        self.current_message = ''
        self.turn_counter = 0

    def generate_word_list(self, path):
        with open(path, "r") as file:
            words = [line.strip("\n").lower() for line in file.readlines()]
        return words

    def set_word(self, word_length):
        return choice([word for word in self.word_list if len(word) == word_length])

    def get_word(self):
        return self.word

    def get_current_guess_state(self):
        return self.guess_state

    def get_letters_guessed_incorrect(self):
        return ','.join(self.letters_guessed_incorrect)

    def get_current_message(self):
        return self.get_current_message

    def refresh_guess_state(self):
        return [letter if letter in self.letters_guessed_correct else '_' for letter in self.get_word()]

    def make_a_guess(self, guess):
        if len(guess) == 1:
            if not guess.isalpha():
                self.current_message = 'Please enter a number!'
                return False
            elif guess in self.letters_guessed_incorrect or guess in self.letters_guessed_correct:
                self.current_message = 'You already guessed that! Try something else.'
                return False
            elif guess not in self.get_word():
                self.turn_counter += 1
                self.letters_guessed_incorrect.append(guess)
                self.current_message = 'Sorry, that letter isn\'t in the word, try again!'
                return False
            elif guess in self.get_word():
                self.turn_counter += 1
                self.letters_guessed_correct.append(guess)
                self.guess_state = self.refresh_guess_state()
                self.current_message = 'Nice, you guessed a letter!'
                return False
        else:
            if guess == self.get_word():
                self.current_message = 'You guessed the word!'
                return True
            else:
                self.current_message = 'Sorry that wasn\'t the word'
                return False


        return
