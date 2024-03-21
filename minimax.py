import chess

def evaluate_board(board):
    values = {'pawn': 1, 'knight': 3, 'bishop': 3, 'rook': 5, 'queen': 9, 'king': 100000}
    white_value = 0
    black_value = 0

    piece_map = board.piece_map()
    for square, piece in piece_map.items():
        piece_type = piece.symbol().lower()
        piece_value = values.get(piece_type, 0)  # Get the value of the piece from the values dictionary
        if piece.color == chess.WHITE:
            white_value += piece_value
        else:
            black_value += piece_value

    return white_value - black_value  # Return the material advantage for white


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board, depth, maximizing_player):
    legal_moves = list(board.legal_moves)
    best_score = float('-inf') if maximizing_player else float('inf')
    best_move = None

    for move in legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, float('-inf'), float('inf'), not maximizing_player)
        board.pop()
        
        if maximizing_player and score > best_score:
            best_score = score
            best_move = move
        elif not maximizing_player and score < best_score:
            best_score = score
            best_move = move

    return best_move