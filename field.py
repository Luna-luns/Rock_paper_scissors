from player_hand import PlayerHand


class Field:
    def __init__(self, player_option: str, opponent_option: str):
        self.player_option = player_option
        self.opponent_option = opponent_option

    def define_result(self, player: PlayerHand) -> str:
        if player.options:
            return self.play_multiple_game(player)
        else:
            return self.play_standard_game(player)

    def play_standard_game(self, player: PlayerHand) -> str:
        if self.player_option == PlayerHand.ROCK and self.opponent_option == PlayerHand.SCISSORS or \
                    (self.player_option == PlayerHand.PAPER and self.opponent_option == PlayerHand.ROCK) or \
                    (self.player_option == PlayerHand.SCISSORS and self.opponent_option == PlayerHand.PAPER):
            player.score += 100
            return PlayerHand.WIN
        elif self.player_option == self.opponent_option:
            player.score += 50
            return PlayerHand.DRAW
        else:
            return PlayerHand.LOSS

    def play_multiple_game(self, player: PlayerHand) -> str:
        player_index = player.options.index(self.player_option)
        precede_list = player.options[:player_index]
        following_list = player.options[player_index + 1:]
        new_list = following_list + precede_list
        half = len(new_list) // 2

        if self.opponent_option in new_list[half:]:
            player.score += 100
            return PlayerHand.WIN
        elif self.player_option == self.opponent_option:
            player.score += 50
            return PlayerHand.DRAW
        else:
            return PlayerHand.LOSS
