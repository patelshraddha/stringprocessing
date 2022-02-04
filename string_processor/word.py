""" Module to implement the behaviour of a word. """
from collections import Counter

class Word:

    def __init__(
        self,
        word: str
    ):
        self.first_letter = word[0]
        self.last_letter = word[-1]
        self.frequency_map = Counter(word[1:len(word) - 1])
        # frozenset sorts the counter so that ecoc and eocc are equivalent
        self.frequency_map_hash = hash(frozenset(self.frequency_map.items()))

    
    def __eq__(self, other):
        """ Check equality between two words ignoring the scramble """
        return (isinstance(other, self.__class__) and
                (self.first_letter, self.last_letter, self.frequency_map) == (other.first_letter, other.last_letter, other.frequency_map))

    def __hash__(self):
        """ For the class to be used as a dictionary key """
        return hash((self.first_letter, self.last_letter, self.frequency_map_hash))