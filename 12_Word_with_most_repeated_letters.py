from collections import Counter
import operator

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(wordlist):
    return max(wordlist, key=most_repeating_letter_count)

words = ['this', 'is', 'an', 'elementary', 'test', 'example']

print(most_repeating_word(words))
