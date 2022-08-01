import ui
from player_hand import PlayerHand
from field import Field


player = PlayerHand()
player_shape = player.choose_option_player()
opponent = PlayerHand()
opponent_shape = opponent.choose_option_opponent()
field = Field(player_shape, opponent_shape)
result = field.define_result()
ui.print_winner(result, opponent_shape)
