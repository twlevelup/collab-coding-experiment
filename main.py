import words.word_bank as wb
import hangman.graphics as hg
import os
from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich.align import Align

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

def game_box(*text):
    os.system('clear')
    print(
        Panel(
            Padding(
                Align(
                    '\n'.join(text),
                    align='center',
                    vertical='middle'
                    ), 
                3), 
            title="Hangman LevelUp 2022",
            height=18)
        )

def is_valid_word_length(string):
    if not string.isdigit():
        return False
    if int(string) not in range(3,21):
        return False
    return True

def main():
    game_box(WELCOMETEXT)
    name = input()

    game_box(WORDLENGTHTEXT.format(name))
    word_length = input()

    while not is_valid_word_length(word_length):
        game_box(WORDLENGTHERROR)
        word_length = input()

    word_length = int(word_length)
    word_bank = wb.WordBank()
    word = word_bank.get_word(word_length)
    turn_counter = 0
    hangman_output = hg.GameDisplay()
    while turn_counter < 7:
        current_hangman = hangman_output.get_next_hangman()
        game_box(current_hangman, '____________', 'e,q,p')
        input()
        turn_counter += 1

    return

if __name__ == '__main__':
    main()