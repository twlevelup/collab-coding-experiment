import os
from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich.align import Align

# Source
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class GameDisplay:
    def __init__(self):
        self.hangman = iter(HANGMANPICS)

    def get_next_hangman(self):
        return self.hangman.__next__()

    def game_box(self, *text):
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