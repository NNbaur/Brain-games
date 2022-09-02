from random import randint


def isPrime(number: int) -> bool:
    # check number, if it's even and != 2 return False, because it's not prime
    if number % 2 == 0:
        return number == 2
    # let's start from divisor = 3 (1,2 not in case) and only odd divisors
    d = 3
    # the divisor does not exceed the square root of the number (acc. to math)
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def initial_game_data():
    number = randint(0, 101)
    flag = isPrime(number)
    if flag:
        answer = 'yes'
    else:
        answer = 'no'
    return (answer, f'Answer "yes" if given number is prime.'
                    f'Otherwise answer "no".\nQuestion: {number}')
