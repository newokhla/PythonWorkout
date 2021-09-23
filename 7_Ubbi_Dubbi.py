def ubbi_dubbi(word):
    translated_word = ''
    for letter in word:
        if letter.isalpha():
            if letter in 'aeiou':
                translated_word += 'ub'
            translated_word += letter
    print(translated_word)

ubbi_dubbi('hello')