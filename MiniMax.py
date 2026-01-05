from Evaluation import Evalualtion

MAX, MIN = 100000, -100000

# Returns optimal value for current player
# (Initially called for root and maximizer)
def minimax(depth, maximizingPlayer, alpha, beta, board, firstMove):
    """
depth: Number of moves ahead to evaluate.

maximizingPlayer: True for White, False for Black.

alpha: Best value that the maximizer (White) can achieve so far.

beta: Best value that the minimizer (Black) can achieve so far.

board: Current state of the chessboard.

firstMove: True if it's the root of the tree (AI's immediate move).
    """
    # Terminating condition. i.e
    # leaf node is reached
    if (depth == 0) or (board.is_game_over()):

        if maximizingPlayer:
            eval = Evalualtion(board, "W")
        else:
            eval = Evalualtion(board, "B")

        return eval.result()

    # All Code from here only runs if the tree has not yet reached the leaf node

    if maximizingPlayer:

        best = MIN#Initializes best to MIN (worst possible value).
        # Recur for left and right children
        for i in board.legal_moves:

            board.push(i)#Makes the move on the board.

            if checkmate(board) and firstMove:
                return i#If the move results in checkmate, return it immediately.

            val = minimax(depth - 1, False, alpha, beta, board, False)#Recursively calls minimax to evaluate the opponent’s best response.
            board.pop()#Undoes the move to restore the board.

            if val > best:#Updates the best move if this move has a better evaluation.
                best = val
                best_move_white = i

            alpha = max(alpha, best)#Updates alpha (best move so far for White).

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        if firstMove:#If it's the AI's first move, return the best move
            print(best_move_white)
            return best_move_white
        else:#Otherwise, return the evaluation score.
            return best

    else:#Black's turn

        best = MAX#Initializes best to MAX (worst possible value for Black).
        for i in board.legal_moves:

            board.push(i)

            if checkmate(board) and firstMove:
                return i

            val = minimax(depth - 1, True, alpha, beta, board, False)
            board.pop()

            if val < best:
                best = val
                best_move_black = i

            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        if firstMove:
            return best_move_black
        else:
            return best

def checkmate(board):#Simply checks if the game is in checkmate.
    if board.is_checkmate():
        return True
    else:
        return False




