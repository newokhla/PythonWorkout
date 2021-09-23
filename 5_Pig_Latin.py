def pig_latin():
    english_word = input('Enter a word: ')
    for letter in english_word:
        if not letter.isalpha():
            english_word = input('Enter a word: ')
    if english_word[0].lower() in 'aeiou':
        pig_latin_translation = english_word + "way"
    else:
        pig_latin_translation = english_word[1:] + english_word[0] + "ay"
    print(f'The pig latin translation is {pig_latin_translation}.')

pig_latin()