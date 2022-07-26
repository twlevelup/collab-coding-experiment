import unittest
import hangman.startup as startup

class TestStartup(unittest.TestCase):
  def test_valid_word_length_should_not_allow_non_numbers(self):
    self.assertFalse(startup.is_valid_word_length("a"))

  def test_valid_word_length_should_not_allow_numbers_outside_range(self):
    """it should not allow numbers less than 4 or greater than 11"""
    self.assertFalse(startup.is_valid_word_length("3"), "it should not allow 3")
    self.assertFalse(startup.is_valid_word_length("12"), "it should not allow 12")

  def test_valid_word_length_should_only_allow_numbers_within_range(self):
    """it should allow numbers between 4 and 11"""
    self.assertTrue(startup.is_valid_word_length("4"), "it should allow 4")
    self.assertTrue(startup.is_valid_word_length("11"), "it should allow 11")