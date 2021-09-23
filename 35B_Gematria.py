import string
gematria_dict = {letter: index for index, letter in enumerate(string.ascii_lowercase, 1)}

def gematria_for(word):
    return sum(gematria_dict.get(letter,0) for letter in word)

print(gematria_for('ab'))