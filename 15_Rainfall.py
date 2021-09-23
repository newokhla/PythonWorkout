def get_rainfall():
    data = {}
    while True:
        dict_key = input("Enter a city name: ")
        if not dict_key:
            break
        dict_value = input("Enter the amount of rainfall: ")
        data[dict_key] = data.get(dict_key, 0) + int(dict_value)
    for key in data:
        print(f'{key}: {data.get(key)}')
get_rainfall()