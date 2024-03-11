import chess

from variables import *
from functions import *

# Main game loop
name1, name2 = ask_for_name()
board = chess.Board()
move_made = False

while not board.is_game_over():
    player_turn(name1, name2, board)
    if board.is_game_over():
        break
    move_made = False  # Reset for the next player's turn
    player_turn(name2, name1, board)
    move_made = False  # Reset for the next player's turn

# Check the game result
check_board()
exit()