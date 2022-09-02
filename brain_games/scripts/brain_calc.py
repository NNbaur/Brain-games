from brain_games import game_starter


def main():
    name = game_starter.welcome_user()
    game = 'brain_calc.initial_game_data()'
    game_starter.start_game(game, name)


if __name__ == '__main__':
    main()
