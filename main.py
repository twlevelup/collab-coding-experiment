import words.word_bank as wb
import hangman.graphics as hg

TURNLIMIT = 7

WELCOMETEXT = """
[white]Welcome to [red]LevelUp 2022[white]!
Lets play a game of Hangman!
Start by entering your name.
"""

WORDLENGTHTEXT = """
[white]Hi [red]{}[white], now choose how long you want your word to be[3-20].
"""

WORDLENGTHERROR = """
[white]Please enter an [red]integer [white]from 3 to 20 
"""

def is_valid_word_length(string):
    if not string.isdigit():
        return False
    if int(string) not in range(3,21):
        return False
    return True

def main():
    game_display = hg.GameDisplay()

    # game_box is the output the player sees
    game_display.game_box(WELCOMETEXT)
    name = input()

    game_display.game_box(WORDLENGTHTEXT.format(name))
    word_length = input()

    # if input isnt a number, will keep asking for input
    while not is_valid_word_length(word_length):
        game_display.game_box(WORDLENGTHERROR)
        word_length = input()

    word_length = int(word_length)

    # The wordbank generates a list of words and selects one
    # Also handles the guess logic
    word_bank = wb.WordBank(word_length)

    while word_bank.turn_counter < TURNLIMIT:
        game_display.game_box(
            game_display.get_next_hangman(), 
            word_bank.get_current_guess_state(), 
            word_bank.get_letters_guessed_incorrect(),
            word_bank.get_current_message()
        )
        guess = input().lower()
        if word_bank.make_a_guess(guess):
            break

    return

if __name__ == '__main__':
    main()