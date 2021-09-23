import os
import pprint as pp

def find_longest_word(filename):
    longest_word = ''
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word

def find_all_longest_words(directory):
    data = {}
    for file in os.listdir(directory):
        data[file] = find_longest_word(file)
    pp.pprint(data)

find_all_longest_words('.')