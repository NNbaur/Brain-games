from random import randint


def initial_game_data():
    number = randint(0, 101)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return (answer, f'Answer "yes" if the number is even,'
                    f'otherwise answer "no"\nQuestion: {number}')
