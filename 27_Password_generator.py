import random

def create_password_generator(a_string):
    password = ''
    for char in range(0,len(a_string)):
        password += random.choice(a_string)
    return password

print(create_password_generator('hello'))