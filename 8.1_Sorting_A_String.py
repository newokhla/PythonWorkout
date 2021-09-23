def longest_word(sentence):
    words = sentence.split(' ')
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(f'The longest word in the sentence "{sentence}" is {longest_word}')

longest_word('four one five seven nineteen twenty')