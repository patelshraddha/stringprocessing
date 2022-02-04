""" Module to process a list of strings to count the substrings - scrambled or not """
import argparse
import logging
from typing import List, Dict
from collections import Counter

from string_processor import word


def read_file(file_path: str) -> List[str]:
    """ Read file into a list of strings """
    with open(file_path) as f:
        return f.read().splitlines()
    return []
        

def count_small_datasets(scrambled_strings: List[str], long_strings: List[str]) -> List[int]:
    """ Returns a count of words in a dictionary present in long strings in a scrambled format or not 
        This function implements the matching algorithm in a simpler way via looping
        through long strings, through dictionary words 
        and matching the frequency map at each position in the long string
    """
    output = []
    for long_string in long_strings:
        counter = 0
        max_idx = len(long_string)
        for scrambled_string in scrambled_strings:
            len_substr = len(scrambled_string)
            scrambled_string_map = Counter(scrambled_string[1:len(scrambled_string)-1])
            for idx, letter in enumerate(long_string):
                if idx == 0:
                    long_string_map = Counter(long_string[idx + 1:min(len_substr - 1, max_idx)])
                else:
                    long_string_map[letter]-=1
                    if long_string_map[letter] <= 0:
                        # Counter equality doesn't work if the count of an element is 0
                        del long_string_map[letter]
                    last_idx = idx + len_substr - 2
                    if last_idx < max_idx and len_substr > 2:
                        long_string_map[long_string[last_idx]] += 1
                # check if the first and last character is the same 
                # and the frequency of the middle letters is the same
                if (scrambled_string[0] == long_string[idx] and
                    idx + len_substr - 1 < max_idx and
                    scrambled_string[-1] == long_string[idx + len_substr - 1] and
                    scrambled_string_map == long_string_map):
                    counter += 1
                    # stop matching if the substring is found 
                    break
        output.append(counter)     
    return output


def get_scrambled_strings_map(scrambled_strings: List[str]) -> Dict[int, Dict[word.Word, int]]:
    """ Create map for strings in the format 
        {length of string: {word : count of word inc. other scrambled words in the dictionary }}
    """
    string_map = {}
    for string in scrambled_strings:
        created_word = word.Word(string)
        if len(string) not in string_map:
            string_map[len(string)] = {created_word: 1}
        else:
            if created_word in string_map[len(string)]:
                # word has been encountered in the dictionary before but in some other scrambled format
                string_map[len(string)][created_word]+= 1
            else:
                # a word of the same length has been encountered before
                string_map[len(string)][created_word] = 1
    return string_map



def count_large_datasets(scrambled_strings: List[str], long_strings: List[str]) -> List[int]:
    """ Returns a count of words in a dictionary present in long strings in a scrambled format or not 
        This function implements the matching algorithm in a complex way via looping
        through long strings and creating a map of length vs word from dictionary 
        while combining words which are scrambled E.g. ecoc vs eocc are treated the same
        This reduces the complexity of matching against substrings at each position of the long string
    """
    output = []
    dict_scrambled_strings = get_scrambled_strings_map(scrambled_strings)
    for long_string in long_strings:
        counter = set()
        output_counter = 0
        max_idx = len(long_string)
        for len_substr, substrings in dict_scrambled_strings.items():
            for idx, letter in enumerate(long_string):
                if idx == 0:
                    long_string_map = Counter(long_string[idx + 1:min(len_substr - 1, max_idx)])
                else:
                    long_string_map[letter]-=1
                    if long_string_map[letter] <= 0:
                        # Counter equality doesn't work if the count of an element is 0
                        del long_string_map[letter]
                        
                    last_idx = idx + len_substr - 2
                    if last_idx < max_idx and len_substr > 2:
                        long_string_map[long_string[last_idx]] += 1
                for substr, substr_count in substrings.items():
                    # check if the first and last character is the same 
                    # and the frequency of the middle letters is the same
                    if substr not in counter and (substr.first_letter == long_string[idx] and
                        idx + len_substr - 1 < max_idx and
                        substr.last_letter == long_string[idx + len_substr - 1] and
                        substr.frequency_map == long_string_map):
                        counter.add(substr)
                        output_counter += substr_count
        output.append(output_counter)     
    return output


def cli_run_counter():
    """ Run counter of strings - scrambled or not in long strings """
    arg_parser = argparse.ArgumentParser(description='CLI interface to run string counter')
    arg_parser.add_argument('--dictionary', dest='dict_file', type=str, required=True,
                            help='The file path of list of substrings')
    arg_parser.add_argument('--input', dest='input_file', type=str, required=True,
                            help='The file path of long strings')
    
    args = arg_parser.parse_args()
    scrambled_strings = read_file(args.dict_file)
    long_strings = read_file(args.input_file)

    logging.info("Running the string counter now: ")

    
    for idx, count in enumerate(count_large_datasets(scrambled_strings, long_strings)):
        print(f"Case #{str(idx)}: {str(count)}")