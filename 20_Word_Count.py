def wordcount():
    counts = {'characters': 0,
            'words': 0,
            'lines': 0,
            'unique_words': set()}
    with open('testfile.txt') as f:
        for line in f:
            counts['lines'] += 1
            counts['characters'] += len(line)
            counts['words'] += len(line.split())
            counts['unique_words'].update(line.split())
        counts['unique_words'] = len(counts['unique_words'])
    return print(counts)
wordcount()