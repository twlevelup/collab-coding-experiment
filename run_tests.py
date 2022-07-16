import unittest
import words.word_bank as wb

class TestWordBank(unittest.TestCase):
    def test_initializing_word_bank_creates_word_list(self):
        bank = wb.WordBank()
        self.assertIsInstance(bank.word_list, list)

    def test_word_list_not_empty(self):
        bank = wb.WordBank()
        self.assertGreater(len(bank.word_list), 0)
        
    def test_get_word_is_string(self):
        bank = wb.WordBank()
        word = bank.get_word()
        self.assertIsInstance(word, str)

    def test_get_word_is_non_empty(self):
        bank = wb.WordBank()
        word = bank.get_word()
        self.assertGreater(len(word), 0)

    def test_get_word_returns_correct_word_size(self):
        bank = wb.WordBank()
        word = bank.get_word(5)
        self.assertLessEqual(len(word), 5)

if __name__ == '__main__':
    unittest.main()