from player_hand import PlayerHand


class Field:
    def __init__(self, player_shape: str, opponent_shape: str):
        self.player_shape = player_shape
        self.opponent_shape = opponent_shape

    def define_result(self) -> str:
        if self.player_shape == PlayerHand.ROCK and self.opponent_shape == PlayerHand.SCISSORS or\
                (self.player_shape == PlayerHand.PAPER and self.opponent_shape == PlayerHand.ROCK) or\
                (self.player_shape == PlayerHand.SCISSORS and self.opponent_shape == PlayerHand.PAPER):
            return PlayerHand.WIN
        elif self.player_shape == PlayerHand.ROCK and self.opponent_shape == PlayerHand.ROCK or\
                (self.player_shape == PlayerHand.PAPER and self.opponent_shape == PlayerHand.PAPER) or\
                (self.player_shape == PlayerHand.SCISSORS and self.opponent_shape == PlayerHand.SCISSORS):
            return PlayerHand.DRAW
        else:
            return PlayerHand.LOSS
