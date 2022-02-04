""" Testing zombie game """
import unittest
from string_processor import word


class TestWord(unittest.TestCase):
    """ Testing class Word """

    def test_word_scrambled(self):
        """ Testing equality between two scrambled words """
        self.assertEqual(word.Word('abcde'), word.Word('adbce'))

    def test_word_diff_frequeny(self):
        """ Testing equality between two scrambled words with different frequencies """
        self.assertNotEqual(word.Word('abcde'), word.Word('abbbe'))
    
    def test_word_diff_length(self):
        """ Testing equality between two scrambled words with same letters but different lengths """
        self.assertNotEqual(word.Word('abcde'), word.Word('abcdde'))