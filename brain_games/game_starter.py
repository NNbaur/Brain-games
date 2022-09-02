from brain_games.games import brain_calc, brain_even,\
    brain_gcd, brain_prime, brain_progression  # noqa
import prompt
import json
import os


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def choose_the_game():
    list_of_games = json.load(open(
        os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'list_of_games.json')))
    print("Let's play some games."
          "Please choose a game from the list and enter a title:")
    print('', *list_of_games.keys(), sep='\n  ')
    try:
        ans1 = input()
        print(list_of_games[ans1])
        ans2 = input('Do you sure you want to play this? Enter "yes" or "no"')
        if ans2 == 'yes' and ans1 in list_of_games:
            return f'{ans1}.initial_game_data()'
        else:
            print('Ok, goodbye!')
            return choose_the_game()
    except KeyError:
        print('Wrong title')
        return None


def check_answer(answer):
    uranswer = input()
    print(f'Your answer: {uranswer}')
    if answer == uranswer:
        return 'Correct!'
    else:
        return (f"'{uranswer}' is wrong answer ;(."
                f"Correct answer was '{answer}'")


def start_game(game, name):
    count = 0
    while count < 3:
        answer, question = eval(game)
        print(question)
        result = check_answer(answer)
        if result == 'Correct!':
            print(result)
            count += 1
        else:
            print(result)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def play_game():
    name = welcome_user()
    game = choose_the_game()
    if game:
        start_game(game, name)
    print('Do you want play again? Enter "yes" or "no"')
    answer = input()
    play_game() if answer == 'yes' else print('Goodbye!')
