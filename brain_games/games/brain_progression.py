from random import randint


def initial_game_data():
    progression = []
    while len(progression) <= 5:
        num1 = randint(1, 101)
        num2 = randint(1, 101)
        step = randint(1, 101)
        progression = [str(i) for i in
                       range(min(num1, num2), max(num1, num2), step)]
    a = randint(0, len(progression) - 1)
    answer = progression[a]
    progression[a] = '..'
    progression = ' '.join(progression)
    return (answer, f'What number is missing in'
                    f'the progression?\nQuestion: {progression}')
