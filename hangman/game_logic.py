import words.word_bank as wb


class GameLogic:
    def __init__(self):
        self.incorrect_guess = []
        self.correct_guess = []
        self.guess_state = ''
        self.current_message = ''
        self.turn_counter = 0
        self.correct_word = ''

    def set_correct_word(self, word):
        self.correct_word = word
        self.guess_state = len(word)*'_'

    def get_current_guess_state(self):
        return self.guess_state

    def get_incorrect_guesses(self):
        return ','.join(self.incorrect_guess)

    def get_current_message(self):
        return self.current_message

    def get_turn(self):
        return self.turn_counter

    def refresh_guess_state(self):
        return ''.join([letter if letter in self.correct_guess else '_' for letter in self.correct_word])

    def make_a_guess(self, guess):
        if len(guess) == 1:
            if not guess.isalpha():
                self.current_message = 'Please enter a letter!'
                return False
            elif guess in self.incorrect_guess or guess in self.correct_guess:
                self.current_message = 'You already guessed that! Try something else.'
                return False
            elif guess not in self.correct_word:
                self.turn_counter += 1
                self.incorrect_guess.append(guess)
                self.current_message = 'Sorry, that letter isn\'t in the word, try again!'
                return False
            elif guess in self.correct_word:
                self.turn_counter += 1
                self.correct_guess.append(guess)
                self.guess_state = self.refresh_guess_state()
                self.current_message = 'Nice, you guessed a letter!'
                if self.guess_state == self.correct_word:
                    return True
                return False
        else:
            if guess == self.correct_word:
                self.current_message = 'You guessed the word!'
                # TODO: Display the correct word on the screen
                return True
            else:
                self.current_message = 'Sorry that wasn\'t the word'
                self.turn_counter += 1
                self.incorrect_guess.append(guess)
                return False





def is_valid_word_length(string):
    if not string.isdigit():
        return False
    if int(string) not in range(4,12):
        return False
    return True