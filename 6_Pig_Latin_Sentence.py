def pl_sentence():
    sentence = input('Enter a sentence: ')
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}nay')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)

print(pl_sentence())