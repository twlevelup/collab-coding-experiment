import unittest
import hangman.game_logic as gl


class TestStartup(unittest.TestCase):
    def test_valid_word_length_should_not_allow_non_numbers(self):
        self.assertFalse(gl.is_valid_word_length("a"))

    def test_valid_word_length_should_not_allow_numbers_outside_range(self):
        """it should not allow numbers less than 4 or greater than 11"""
        self.assertFalse(gl.is_valid_word_length("3"), "it should not allow 3")
        self.assertFalse(gl.is_valid_word_length("12"), "it should not allow 12")

    def test_valid_word_length_should_only_allow_numbers_within_range(self):
        """it should allow numbers between 4 and 11"""
        self.assertTrue(gl.is_valid_word_length("4"), "it should allow 4")
        self.assertTrue(gl.is_valid_word_length("11"), "it should allow 11")


class TestGameLogic(unittest.TestCase):
    def test_initial_game_message(self):
        game_logic = gl.GameLogic()
        self.assertEquals("Please guess a character or a word", game_logic.current_message)
