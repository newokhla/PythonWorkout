vowels = {'a', 'e', 'i', 'o', 'u'}
word = 'aeou'

if set(word).issuperset(vowels) or set(word) == vowels:
    print(f'{word} is supervocalic.')
else:
    print(f'{word} is not supervocalic.')