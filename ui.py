from player_hand import PlayerHand
from input_error import InputError


def ask_name() -> str:
    return input('Enter your name: ').strip()


def greet_player(name: str) -> None:
    print(f'Hello, {name}')


def choose_option() -> str:
    while True:
        try:
            option = input().strip()
            if option not in (PlayerHand.ROCK, PlayerHand.PAPER, PlayerHand.SCISSORS, '!exit', '!rating'):
                raise InputError
            break
        except InputError as error:
            print(error)

    return option


def print_winner(option: str, shape: str) -> None:
    if option == '1':
        print(f'Sorry, but the computer chose {shape}')
    elif option == '2':
        print(f'There is a draw ({shape})')
    else:
        print(f'Well done. The computer chose {shape} and failed')


def print_exit() -> None:
    print('Bye!')


def print_rating(score: int) -> None:
    print(f'Your rating: {score}')
