from sre_constants import SUCCESS
import words.word_bank as wb
import hangman.graphics as hg

TURNLIMIT = 9

WELCOMETEXT = """
[white]Welcome to [red]LevelUp 2022[white]!
Lets play a game of Hangman!
Start by entering your name.
"""

WORDLENGTHTEXT = """
[white]Hi [red]{}[white], now choose how long you want your word to be[4-11].
"""

WORDLENGTHERROR = """
[white]Please enter an [red]integer [white]from 4 to 11 
"""

SUCCESS = """
You got it! Congratulations!
"""

FAILURE = """
Better luck next time, the word was: {}
"""

def is_valid_word_length(string):
    if not string.isdigit():
        return False
    if int(string) not in range(4,12):
        return False
    return True

def main():
    game_display = hg.GameDisplay()

    # game_box is the output the player sees
    game_display.display_game_box(WELCOMETEXT)
    name = input()

    game_display.display_game_box(WORDLENGTHTEXT.format(name))
    word_length = input()

    # if input isnt a number, will keep asking for input
    while not is_valid_word_length(word_length):
        game_display.display_game_box(WORDLENGTHERROR)
        word_length = input()

    word_length = int(word_length)

    # The wordbank generates a list of words and selects one
    # Also handles the guess logic
    word_bank = wb.WordBank(word_length)

    # TODO: Instruct them to add a word or letter

    while word_bank.turn_counter < TURNLIMIT:
        # Shows the hangman, letters correctly and incorrectly guessed
        # as well as any game messages 
        game_display.display_game_box(
            game_display.get_current_hangman(word_bank.get_turn()), 
            word_bank.get_current_guess_state(), 
            word_bank.get_incorrect_guesses(),
            word_bank.get_current_message()
        )
        guess = input().lower()
        if word_bank.make_a_guess(guess):
            # Player guesses correctly and gets a success message
            game_display.display_game_box(
                game_display.get_current_hangman(word_bank.get_turn()), 
                word_bank.get_current_guess_state(), 
                word_bank.get_incorrect_guesses(),
                SUCCESS
            )
            return
    # Player fails to guess in time
    game_display.display_game_box(
        game_display.get_current_hangman(word_bank.get_turn()), 
        word_bank.get_current_guess_state(), 
        word_bank.get_incorrect_guesses(),
        FAILURE.format(word_bank.get_word())
    )
    return

if __name__ == '__main__':
    main()