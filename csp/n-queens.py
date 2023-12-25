import sys
sys.path.append("..")

import numpy as np
from animate import run_animation

def init_board(N, random=True):
    if random:
        board = np.random.permutation(N)
        return board
    else:
        board = np.zeros(N, dtype=int)
        return board

def print_board(board, N):
    b = np.zeros((N,N), dtype=int)
    for i in range(N):
        b[board[i]][i] = 1
    print(b)

def get_conflicts(board, N):
    conflict_queens = []
    for i in range(N):
        n = num_attacks(board, i, board[i], N)
        if n>0:
            conflict_queens.append(i)
    return conflict_queens

def num_attacks(board, j, pos_j, N):
    num = 0
    for i in range(N):
        pos_i = board[i]
        if i==j:
            continue
        if pos_i==pos_j:
            num += 1
            continue
        if np.abs(i-j)==np.abs(pos_i-pos_j):
            num += 1
    return num

def min_conflicts(board, N, log=False):
    conflicts = get_conflicts(board, N)
    last_choice = -1
    turns = 0       # counts number of turns
    path = [np.copy(board)]
    while conflicts:
        if log:
            print_board(board, N)

        i = np.random.choice(conflicts)
        while last_choice==i:               # ensure new queen is chosen
            i = np.random.choice(conflicts)

        pos = board[i]
        if log:
            print(f"selected queen {i}, current position {pos}")

        # calculate number of attacks in each position
        attacks = np.zeros(N, dtype=int)
        for pos_i in range(N):
            if pos_i==pos:
                attacks[pos_i] = N+1        # ensure queen moves to new position
                continue
            attacks[pos_i] = num_attacks(board, i, pos_i, N)

        # move queen to new position with minimum conflict
        min_attacks = np.where(attacks==attacks.min())
        new_pos = np.random.choice(min_attacks[0])
        board[i] = new_pos

        # reset variables
        last_choice = i
        conflicts = get_conflicts(board, N)
        turns += 1

        if log:
            print(f"turn {turns}: move queen {i} to position {new_pos}")
        
        path.append(np.copy(board))
    return path, turns

N = 4
b1 = init_board(N, random=False)

path, turns = min_conflicts(b1, N)
# run_animation(N, path)

N = 8
b2 = init_board(N, random=True)

path, turns = min_conflicts(b2, N)
run_animation(N, path)

    