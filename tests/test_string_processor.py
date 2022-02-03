""" Testing zombie game """
import unittest
from collections import Counter
from string_processor import count


class TestCreateFrequencyMap(unittest.TestCase):
    """ Testing function create_frequency_map """

    def test_create_frequency_map_single_characters(self):
        """ Testing create_frequency_map with string of length = 1 """
        self.assertEqual(count.create_frequency_map('a'), Counter())

    def test_create_frequency_map_two_characters(self):
        """ Testing create_frequency_map with string of length > 2 """
        self.assertEqual(count.create_frequency_map('ab'), Counter())
    
    def test_create_frequency_map_more_than_two_characters(self):
        """ Testing create_frequency_map with string of length = 2 """
        self.assertEqual(count.create_frequency_map('abcd'), Counter({'b': 1, 'c': 1}))
        self.assertEqual(count.create_frequency_map('abcbd'), Counter({'b': 2, 'c': 1}))


class TestCountSmallDatasets(unittest.TestCase):
    """ Testing function count_small_datasets """
    def setUp(self):
        self.dictionary = ['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd', 'tx', '', 't']

    def test_count_small_datasets_long_string(self):
        """ Testing count_small_datasets with a long string """
        self.assertEqual(count.count_small_datasets(self.dictionary, ['aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt']), [5])
    
    def test_count_small_datasets_multiple_long_string(self):
        """ Testing count_small_datasets with a single letter string and empty string """
        self.assertEqual(count.count_small_datasets(self.dictionary, ['t', '']), [1, 0])
    
    def test_count_small_datasets_two_characters_string(self):
        """ Testing count_small_datasets with a long string of size 2 """
        self.assertEqual(count.count_small_datasets(self.dictionary, ['tx']), [2])


class TestCountLargeDatasets(unittest.TestCase):
    """ Testing function count_large_datasets """
    def setUp(self):
        self.dictionary = ['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd', 'tx', '', 't']

    def test_count_large_datasets_long_string(self):
        """ Testing count_large_datasets with a long string """
        self.assertEqual(count.count_large_datasets(self.dictionary, ['aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt']), [5])
    
    def test_count_large_datasets_multiple_long_string(self):
        """ Testing count_large_datasets with a single letter string and empty string """
        self.assertEqual(count.count_large_datasets(self.dictionary, ['t', '']), [1, 0])
    
    def test_count_large_datasets_two_characters_string(self):
        """ Testing count_large_datasets with a long string of size 2 """
        self.assertEqual(count.count_large_datasets(self.dictionary, ['tx']), [2])
