import ui
import random


class PlayerHand:
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    LOSS = '1'
    DRAW = '2'
    WIN = '3'

    def __init__(self, options: list):
        self.options = options
        self.score = 0
        self.option = None

    def choose_option_opponent(self):
        if self.options:
            self.option = random.choice(self.options)
            return self.option
        else:
            self.option = random.choice([self.ROCK, self.PAPER, self.SCISSORS])
            return self.option

    def choose_option_player(self):
        self.option = ui.choose_option(self.options)
        return self.option
