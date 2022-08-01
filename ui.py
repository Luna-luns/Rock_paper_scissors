def choose_option() -> str:
    return input().strip()


def print_winner(option: str, shape: str) -> None:
    if option == '1':
        print(f'Sorry, but the computer chose {shape}')
    elif option == '2':
        print(f'There is a draw ({shape})')
    else:
        print(f'Well done. The computer chose {shape} and failed')
