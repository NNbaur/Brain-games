from random import randint, choice


def initial_game_data():
    number1 = randint(0, 101)
    number2 = randint(0, 101)
    operator = choice(['*', '+', '-'])
    expressions = {
        '*': number1 * number2,
        '+': number1 + number2,
        '-': number1 - number2
    }
    answer = str(expressions[operator])
    return (answer, f'What is the result of the expression?'
                    f'\nQuestion: {number1} {operator} {number2}')
