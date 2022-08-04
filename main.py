from sre_constants import SUCCESS
import words.word_bank as wb
import hangman.graphics as hg
import hangman.game_logic as gl


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

def main():
    game_display = hg.GameDisplay()

    # game_box is the output the player sees
    game_display.display_game_box(WELCOMETEXT)
    name = input()

    game_display.display_game_box(WORDLENGTHTEXT.format(name))
    word_length = input()

    # if input isnt a number, will keep asking for input
    while not gl.is_valid_word_length(word_length):
        game_display.display_game_box(WORDLENGTHERROR)
        word_length = input()

    word_length = int(word_length)

    # The wordbank generates a list of words and selects one
    # Also handles the guess logic
    word_bank = wb.WordBank(word_length)
    game_logic = gl.GameLogic()
    game_logic.set_correct_word(word_bank.get_word())

    # TODO: Instruct them to add a word or letter

    while game_logic.turn_counter < TURNLIMIT:
        # Shows the hangman, letters correctly and incorrectly guessed
        # as well as any game messages 
        game_display.display_game_box(
            game_display.get_current_hangman(game_logic.get_turn()), 
            game_logic.get_current_guess_state(), 
            game_logic.get_incorrect_guesses(),
            game_logic.get_current_message()
        )
        guess = input().lower()
        if game_logic.make_a_guess(guess):
            # Player guesses correctly and gets a success message
            game_display.display_game_box(
                game_display.get_current_hangman(game_logic.get_turn()), 
                game_logic.get_current_guess_state(), 
                game_logic.get_incorrect_guesses(),
                SUCCESS
            )
            return
    # Player fails to guess in time
    game_display.display_game_box(
        game_display.get_current_hangman(game_logic.get_turn()), 
        game_logic.get_current_guess_state(), 
        game_logic.get_incorrect_guesses(),
        FAILURE.format(word_bank.get_word())
    )
    return

if __name__ == '__main__':
    main()