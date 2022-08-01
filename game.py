from player_hand import PlayerHand
import ui


player_1_shape = ui.choose_option()
player_1 = PlayerHand(player_1_shape)
player_1.choose_opposite()
