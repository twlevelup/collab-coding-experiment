from random import choice

DEFAULT_LENGTH = 100
DEFAULT_PATH = "./words/words.txt"

class WordBank:
    def __init__(self, word_length=DEFAULT_LENGTH, path=DEFAULT_PATH):
        self.word_list = self.generate_word_list(path)
        self.word_length = word_length
        self.word = self.set_word(word_length)
        self.incorrect_guess = []
        self.correct_guess = []
        self.guess_state = len(self.word)*'_'
        self.current_message = ''
        self.turn_counter = 0

    def generate_word_list(self, path):
        with open(path, "r") as file:
            words = [line.strip("\n").lower() for line in file.readlines()]
        return words

    def set_word(self, word_length):
        # TODO: create a list of words of the specified word_length
        # TODO: randomly select one of those words and return it
        return 'word'

    def get_word(self):
        return self.word

    def get_current_guess_state(self):
        return self.guess_state

    def get_incorrect_guesses(self):
        return ','.join(self.incorrect_guess)

    def get_current_message(self):
        return self.current_message

    def get_turn(self):
        return self.turn_counter

    def refresh_guess_state(self):
        return ''.join([letter if letter in self.correct_guess else '_' for letter in self.get_word()])

    def make_a_guess(self, guess):
        if len(guess) == 1:
            if not guess.isalpha():
                self.current_message = 'Please enter a letter!'
                return False
            elif guess in self.incorrect_guess or guess in self.correct_guess:
                self.current_message = 'You already guessed that! Try something else.'
                return False
            elif guess not in self.get_word():
                self.turn_counter += 1
                self.incorrect_guess.append(guess)
                self.current_message = 'Sorry, that letter isn\'t in the word, try again!'
                return False
            elif guess in self.get_word():
                self.turn_counter += 1
                self.correct_guess.append(guess)
                self.guess_state = self.refresh_guess_state()
                self.current_message = 'Nice, you guessed a letter!'
                if self.guess_state == self.get_word():
                    return True
                return False
        else:
            if guess == self.get_word():
                self.current_message = 'You guessed the word!'
                # TODO: Display the correct word on the screen
                return True
            else:
                self.current_message = 'Sorry that wasn\'t the word'
                self.turn_counter += 1
                self.incorrect_guess.append(guess)
                return False
