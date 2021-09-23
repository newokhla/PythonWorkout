import operator

def alphabetizer(dicts):
    return sorted(dicts, key=operator.itemgetter('last', 'first'))

people = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'r@co.il'}, {'first': 'Donald', 'last': 'Trump', 'email': 'dtrump@trump.com'}, {'first': 'Vladimir', 'last': 'Putin', 'email': 'chief@russia.com'}]

print(alphabetizer(people))