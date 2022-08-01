from player_hand import PlayerHand


class Field:
    def __init__(self, player_option: str, opponent_option: str):
        self.player_option = player_option
        self.opponent_option = opponent_option

    def define_result(self, player: PlayerHand) -> str:
        if self.player_option == PlayerHand.ROCK and self.opponent_option == PlayerHand.SCISSORS or\
                (self.player_option == PlayerHand.PAPER and self.opponent_option == PlayerHand.ROCK) or\
                (self.player_option == PlayerHand.SCISSORS and self.opponent_option == PlayerHand.PAPER):
            player.score += 100
            return PlayerHand.WIN
        elif self.player_option == PlayerHand.ROCK and self.opponent_option == PlayerHand.ROCK or\
                (self.player_option == PlayerHand.PAPER and self.opponent_option == PlayerHand.PAPER) or\
                (self.player_option == PlayerHand.SCISSORS and self.opponent_option == PlayerHand.SCISSORS):
            player.score += 50
            return PlayerHand.DRAW
        else:
            return PlayerHand.LOSS
