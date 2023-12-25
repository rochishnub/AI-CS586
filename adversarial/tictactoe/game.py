import sys
sys.path.append("..")

from base import Node, Game
from minimax import best_minimax
import numpy as np

class State(Node):
    def __init__(self, state):
        super().__init__()
        self.board = state

class TicTacToe(Game):
    def __init__(self, with_depth=True):        
        self.check_rows = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        self.with_depth = with_depth
    
    def check_winner(self, state:State):
        scores = set([sum(state.board[row]) for row in self.check_rows])
        if 3 in scores:
            return 'ai'
        if -3 in scores:
            return 'human'
        if 0 in state.board:
            return 'none'
        else: return 'draw'
    
    def terminate(self, state:State):
        winner = self.check_winner(state)
        if winner=='none':
            return False
        else: return True
    
    def utility(self, state:State, depth:int):
        winner = self.check_winner(state)
        if self.with_depth:
            if winner=='ai':
                return 10 - depth
            elif winner=='human':
                return -10 + depth
            else: return 0
        
        else:
            if winner=='ai':
                return 10
            elif winner=='human':
                return -10
            else: return 0

    def actions(self, state:State):
        moves = [i for i in range(9) if state.board[i]==0]
        return moves
    
    def play(self, state:State, a:int, player:int):
        board = np.copy(state.board)
        board[a] = player
        return State(board)
    
    def opponent(self, player:int):
        return -1 * player


# start = np.zeros(9, dtype=int)
# start = np.array([1, -1, -1, 1, 0, 0, 0, 0, 0])
# print(start)

# S = State(start)
# T = TicTacToe()
# T_ = TicTacToe(with_depth=False)

# k = best_minimax(T, S)
# print(k)

# k = best_minimax(T_, S)
# print(k)