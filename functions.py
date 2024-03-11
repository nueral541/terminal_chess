import chess
from variables import *

def ask_for_name():
    name1 = input("What is player one's name?  ")
    name2 = input("What is player two's name?  ")
    print(name1 + ' is uppercase letters and ' + name2 + ' is lowercase letters.')
    print("starting game...")

def player_turn(player):
    while move_made == False:
        print(player + "'s turn:")
        print(board)
        try:
            turn = input("What is your move? type a 'd' or an 'r' to draw or resign:  ")
            if turn == 'd' or turn == 'r':
                if turn == 'r':
                    print(player + ' has resigned')
                    print(player + ' is a bad sport')
                    if player == name1:
                        print(name2 + ' is the best chess player!!')
                        print('thank u for playing')
                    else:
                        print(name1 + ' is the best chess player!!')
                        print('thank u for playing')
                else:
                    print(player + ' has decided to have a draw; I hope he asked his opponent first...')
                    print('thank u for playing')
            else:
                move = chess.Move.from_uci(move)
                if turn in board.legal_moves():
                    board.push(turn)
                    print("move made succesfully!")
                    move_made == True
                else:
                    print("sorry that is not a legal move, please try again.")
        except ValueError:
            print("Invalid move format. Please use UCI format (e.g., e2e4).")

def check_board():
    if board.is_checkmate():
        if board.turn == chess.BLACK:
            print(name1 + " wins by checkmate")
        else:
            print(name2 + " wins by checkmate")
    elif board.is_stalemate():
        print("The game is a stalemate")
    elif board.is_insufficient_material():
        print("The game is a draw due to insufficient material")
    elif board.can_claim_draw():
        print("The game is a draw by threefold repetition or the fifty-move rule")