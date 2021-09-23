d = {'a': 1, 'b': 2, 'c': 3}

def flipdict(a_dict):
    return {value: key for key, value in a_dict.items()}

print(flipdict(d))

# Only returns keys
for a in d:
    print(a)

# Returns each key-pair in the dictionary
for a in d.items():
    print(a)