import unittest
import hangman.graphics as graphics

class TestWordBank(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.game = graphics.GameDisplay()

    def test_initialise_game_shoud_create_hangman(self):
        self.assertTrue(self.game.hangman)

    def test_current_hangman_should_return_game_within_valid_turns(self):
        self.assertTrue(self.game.get_current_hangman(0))
        self.assertTrue(self.game.get_current_hangman(1))
        self.assertTrue(self.game.get_current_hangman(9))

    def test_current_hangman_should_return_error_outside_turns(self):
        with self.assertRaises(IndexError):
            self.game.get_current_hangman(10)


if __name__ == '__main__':
    unittest.main()