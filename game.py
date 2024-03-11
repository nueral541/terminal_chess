import chess
from variables import *
from functions import *

ask_for_name()

while True:
    player_turn(name1)
    player_turn(name2)
    if check_board():
        running = False