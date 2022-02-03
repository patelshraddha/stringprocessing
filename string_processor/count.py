""" Module to process a list of strings to count the substrings - scrambled or not """
import argparse
import logging
from typing import List
from collections import Counter
from itertools import groupby


def read_file(file_path: str) -> List[str]:
    """ Read file into a list of strings """
    with open(file_path) as f:
        return f.read().splitlines()
    return []


def create_frequency_map(string: str):
    """ Create a map of letter vs counts for letters between the first and last letters """
    if len(string) > 2:
        return Counter(string[1:len(string)-1])
    return Counter()
        

def count_small_datasets(scrambled_strings: List[str], long_strings: List[str]) -> List[int]:
    """ For every string in the dictionary """
    output = []
    for long_string in long_strings:
        counter = 0
        max_idx = len(long_string)
        for scrambled_string in scrambled_strings:
            len_substr = len(scrambled_string)
            if len_substr == 0:
                # continue matching the next substring
                continue
            scrambled_string_map = create_frequency_map(scrambled_string)
            for idx, letter in enumerate(long_string):
                if len_substr < 3:
                    if scrambled_string == long_string[idx:min(idx+len_substr, max_idx)]:
                        counter += 1
                        # stop matching if the substring is found 
                        break
                    else:
                        # continue matching with the next letter
                        continue
                if idx == 0:
                    long_string_map = Counter(long_string[idx + 1:min(len_substr - 1, max_idx)])
                else:
                    prev_value = long_string_map[letter]
                    if long_string_map[letter] == 1:
                        # Counter equality doesn't work if the count of an element is 0
                        del long_string_map[letter]
                    else:
                        long_string_map[letter] = prev_value - 1
                    last_idx = idx+len_substr-2
                    if last_idx < max_idx:
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


def count_large_datasets(scrambled_strings: List[str], long_strings: List[str]) -> List[int]:
    """ For every string in the dictionary """
    output = []
    dict_scrambled_strings = {length: list(set(items)) for length, items in groupby(scrambled_strings, key=len)}
    for long_string in long_strings:
        counter = set()
        max_idx = len(long_string)
        for len_substr, substrings in dict_scrambled_strings.items():
            if len_substr == 0:
                # continue matching the next set of substrings
                continue
            for idx, letter in enumerate(long_string):
                if len_substr < 3:
                    for substr in substrings:
                        if substr not in counter and substr == long_string[idx:min(idx + len_substr, max_idx)]:
                            counter.add(substr)
                else:
                    if idx == 0:
                        long_string_map = Counter(long_string[idx + 1:min(len_substr - 1, max_idx)])
                    else:
                        prev_value = long_string_map[letter]
                        if long_string_map[letter] == 1:
                            # Counter equality doesn't work if the count of an element is 0
                            del long_string_map[letter]
                        else:
                            long_string_map[letter] = prev_value - 1
                        last_idx = idx + len_substr - 2
                        if last_idx < max_idx:
                            long_string_map[long_string[last_idx]] += 1
                    for substr in substrings:
                        # check if the first and last character is the same 
                        # and the frequency of the middle letters is the same
                        if substr not in counter and (substr[0] == long_string[idx] and
                            idx + len_substr - 1 < max_idx and
                            substr[-1] == long_string[idx + len_substr - 1] and
                            create_frequency_map(substr) == long_string_map):
                            counter.add(substr)
        output.append(len(counter))     
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