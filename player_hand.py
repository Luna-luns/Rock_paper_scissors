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
        self.shape = None

    def choose_option_opponent(self):
        self.shape = random.choice([self.ROCK, self.PAPER, self.SCISSORS])
        return self.shape

    def choose_option_player(self):
        self.shape = ui.choose_option()
        return self.shape
