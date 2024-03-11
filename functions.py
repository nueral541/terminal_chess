import chess
from variables import *

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

def ask_for_name():
    name1 = input("What is player one's name?  ")
    name2 = input("What is player two's name?  ")
    print(name1 + ' is uppercase letters and ' + name2 + ' is lowercase letters.')
    print("Starting game...")
    return name1, name2

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