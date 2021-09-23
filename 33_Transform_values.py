d = {'a': 1, 'b': 2, 'c': 3}

def _transform_values(func, a_dict):
    return {key: func(value) for key, value in a_dict.items()}

print(_transform_values(lambda x: x*x, d))