import random

def get_int_from_user():
    user_input = None

    while not isinstance(user_input, int):
        try:
            user_input = int(input('Guess a number between 0 and 100, inclusive: '))
        except:
            pass

    return user_input

def guessing_game():
    random_0to100 = random.randint(0,101)

    user_input = get_int_from_user()

    while user_input != random_0to100:
        if user_input > random_0to100:
            print('Your guess was too high.')
        else:
            print('Your guess was too low.')
        user_input = get_int_from_user()

    print('Just right.')

guessing_game()