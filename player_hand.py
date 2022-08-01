import ui


class PlayerHand:
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    def __init__(self, shape: str):
        self.shape = shape

    def choose_opposite(self) -> None:
        if self.shape == self.ROCK:
            ui.print_result(self.PAPER)
        if self.shape == self.PAPER:
            ui.print_result(self.SCISSORS)
        if self.shape == self.SCISSORS:
            ui.print_result(self.ROCK)
