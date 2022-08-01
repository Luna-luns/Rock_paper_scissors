import ui
from player_hand import PlayerHand
from field import Field


player_name = ui.ask_name()
ui.greet_player(player_name)
options = ui.get_options().replace(',', ' ').split()
player = PlayerHand(options)
opponent = PlayerHand(options)

with open('rating.txt', 'r') as file:
    if player_name in file.read():
        player.score = 350
        file.close()
    else:
        player.score = 0

ui.print_game_start()

while True:
    player_option = player.choose_option_player()

    if player_option == '!exit':
        ui.print_exit()
        exit()

    if player_option == '!rating':
        ui.print_rating(player.score)
        continue

    opponent_option = opponent.choose_option_opponent()
    field = Field(player_option, opponent_option)
    result = field.define_result(player)
    ui.print_winner(result, opponent_option)
