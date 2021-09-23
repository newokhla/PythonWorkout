def hex_output():
    decimal_number = 0
    hex_input = ''
    while not hex_input:
        hex_input = input('Enter a hexadecimal number to convert: ')
        for letter in hex_input:
            if not letter.isnumeric() and not letter in 'abcdef':
                print(f'Input was invalid.')
                hex_input = input('Enter a hexadecimal number to convert: ')
    for power, digit in enumerate(reversed(hex_input)):
        decimal_number += int(digit, 16) * (16 ** power)
    print(f'The decimal conversion is {decimal_number}.')
hex_output()