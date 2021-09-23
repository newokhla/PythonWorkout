import random

def get_int_from_user():
    user_input = None

    while not isinstance(user_input, int):
        try:
            user_input = int(input('Guess a number between 0 and 100, inclusive: '))
        except:
            pass

    return user_input

def guessing_game(number_of_guesses):
    random_0to100 = random.randint(0,101)
    print(f'You have {number_of_guesses} guesses.')
    user_input = None

    while True:
        user_input = get_int_from_user()
        number_of_guesses -= 1

        if user_input == random_0to100:
            print(f'Just right. You had {number_of_guesses} left.')
            break

        if number_of_guesses == 0:
            print(f'You ran out of guesses. The number was {random_0to100}.')
            break

        if user_input > random_0to100:
            print('Your guess was too high.')

        else:
            print('Your guess was too low.')
        print(f'You have {number_of_guesses} guesses remaining.')
        
guessing_game(number_of_guesses=5)