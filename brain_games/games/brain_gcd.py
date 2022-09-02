from random import randint


def initial_game_data():
    number1 = randint(0, 101)
    number2 = randint(0, 101)
    answer = str(
        [i for i in range(1, min(number1, number2) + 1)
         if number1 % i == number2 % i == 0][-1])
    return (answer, f'Find the greatest common divisor'
                    f'of given numbers.\nQuestion: {number1} {number2}')
