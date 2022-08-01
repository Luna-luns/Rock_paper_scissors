import ui
import random


class PlayerHand:
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    LOSS = '1'
    DRAW = '2'
    WIN = '3'

    def __init__(self):
        self.option = None
        self.score = 0

    def choose_option_opponent(self):
        self.option = random.choice([self.ROCK, self.PAPER, self.SCISSORS])
        return self.option

    def choose_option_player(self):
        self.option = ui.choose_option()
        return self.option
