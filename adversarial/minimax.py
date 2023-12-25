from base import Node, Game
import numpy as np

# MiniMax

def best_minimax(game:Game, state:Node):
    alpha = -np.inf
    beta = np.inf
    _, move = minimax(game, state, True, alpha, beta, 0)
    return move

def minimax(game:Game, state:Node, is_AI, alpha, beta, depth):

    if game.terminate(state):
        return game.utility(state, depth), 0
    
    # Maximizer
    if is_AI:
        max_score = -np.inf
        for action in game.actions(state):
            next_state = game.play(state, action, 1)
            score, _ = minimax(game, next_state, not is_AI, alpha, beta, depth+1)

            if score > max_score:
                max_score, move = score, action
                alpha = max(alpha, max_score)
            
            if max_score>=beta:
                return max_score, move
        return max_score, move
    
    if not is_AI:
        min_score = np.inf
        for action in game.actions(state):
            next_state = game.play(state, action, -1)
            score, _ = minimax(game, next_state, not is_AI, alpha, beta, depth+1)

            if score < min_score:
                min_score, move = score, action
                beta = min(beta, min_score)
            
            if min_score<=alpha:
                return min_score, move
        return min_score, move