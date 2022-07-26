import unittest
import words.word_bank as wb

class TestWordBank(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.bank = wb.WordBank()

    def test_initializing_word_bank_creates_word_list(self):
        self.assertIsInstance(self.bank.word_list, list)

    def test_word_list_not_empty(self):
        self.assertGreater(len(self.bank.word_list), 0)
        
    def test_get_word_is_string(self):
        word = self.bank.get_word()
        self.assertIsInstance(word, str)

    def test_get_word_is_non_empty(self):
        word = self.bank.get_word()
        self.assertGreater(len(word), 0)


if __name__ == '__main__':
    unittest.main()