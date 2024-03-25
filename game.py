# Importing chess library
import chess

# Importing variables from a separate file named "variables.py"
from variables import *

depth = 6

# Function to check the board for draw or checkmate
def check_board():
    if board.is_checkmate():
        if board.turn == chess.BLACK:
            print(name1 + " wins by checkmate")
        else:
            print(name2 + " wins by checkmate")
        return True
    elif board.is_stalemate():
        print("The game is a stalemate")
        return True
    elif board.is_insufficient_material():
        print("The game is a draw due to insufficient material")
        return True
    elif board.can_claim_draw():
        print("The game is a draw by threefold repetition or the fifty-move rule")
        return True

# Function to prompt for player names
def ask_for_name():
    name1 = input("What is player one's name?  ")
    name2 = input("What is player two's name?  ")
    print(name1 + ' is uppercase letters and ' + name2 + ' is lowercase letters.')
    print("Starting game...")
    return name1, name2

# Function for the minimax player's turn
def minimax_player_turn(player, opponent, board, maximizing_player):
    global move_made
    # Implement the minimax algorithm here to find the best move for the minimax player
    best_move_found = best_move(board, depth, maximizing_player)
    board.push(best_move_found)
    print(player + "'s move:", best_move_found)

def player_turn(player, opponent, board):
    global move_made
    while not move_made:
        print(player + "'s turn:")
        print(board)
        try:
            turn = input("What is your move? Type 'd' or 'r' to draw or resign:  ")
            if turn in ['d', 'r']:
                handle_resignation_or_draw(turn, player, opponent)
                move_made = True
            else:
                process_move(turn, board)
        except ValueError:
            print("Invalid move format. Please use UCI format (e.g., e2e4).")

def handle_resignation_or_draw(turn, player, opponent):
    if turn == 'r':
        print(f"{player} has resigned. {opponent} wins!")
    else:
        print(f"{player} has offered a draw. It's a draw!")
    print('Thank you for playing.')
    exit()

def process_move(turn, board):
    global move_made
    turn = chess.Move.from_uci(turn)
    if turn in board.legal_moves:
        board.push(turn)
        print("Move made successfully!")
        move_made = True
    else:
        print("Sorry, that is not a legal move. Please try again.")

# Main game loop
name1, name2 = ask_for_name()
board = chess.Board()
move_made = False

while not board.is_game_over():
    minimax_player_turn(name1, name2, board, True)  # Minimax player's turn
    if board.is_game_over():
        break
    move_made = False  # Reset for the next player's turn
    player_turn(name2, name1, board)  # Opponent's turn
    if board.is_game_over():
        break
    move_made = False  # Reset for the next player's turn

# Check the game result
check_board()
exit()