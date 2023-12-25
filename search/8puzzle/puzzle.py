import sys
sys.path.append("..")

from base import Problem, Node
from informed import a_star_search
from uninformed import breadth_first_search
from animate import run_animation
import numpy as np

class State(Node):
    def __init__(self, state):
        super().__init__(id)
        self.id = self.get_id(state)
        self.state = state

    def get_id(self, state):
        fl = list(state.flatten())
        ids = map(str, fl)
        id = "".join(ids)
        return id

class Puzzle(Problem):
    def __init__(self):
        super().__init__()
        self.goals = {'012345678', '123456780'}
        self.goal1 = np.asarray([[1,2,3], [4,5,6], [7,8,0]], dtype=int)
        self.goal2 = np.asarray([[0,1,2], [3,4,5], [6,7,8]], dtype=int)
        self.goal_coords = self.get_goal_coord()
    
    def successors(self, node:State):
        x,y = np.where(node.state==0)
        x,y = x[0], y[0]
        moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        moves = [move for move in moves if self.boundary(move)]

        # print(moves)

        succ = []
        for move in moves:
            neigh = np.copy(node.state)
            neigh[x,y], neigh[move] = neigh[move], neigh[x,y]
            # print(neigh, move)
            succ.append(State(neigh))

        # for node in succ:
        #     print(node.id)
        return succ
    
    def boundary(self, move):
        p, q = move
        if 0<=p<3 and 0<=q<3:
            return True
        else: return False
    
    def goal_test(self, node: Node):
        if node.id in self.goals:
            return True
        return False
    
    def path_cost(self, path):
        return len(path) - 1
    
    def heuristic(self, node: Node):
        h1, h2 = 0, 0
        for i in range(1,9):
            x,y = np.where(node.state==i)
            x,y = x[0], y[0]
            x1,y1 = self.goal_coords[i][0]
            x2,y2 = self.goal_coords[i][1]
            
            h1 += abs(x-x1) + abs(y-y1)
            h2 += abs(x-x2) + abs(y-y2)
        return min(h1, h2)
    
    def get_goal_coord(self):
        coords = {}
        for i in range(1,9):
            x1, y1 = np.where(self.goal1==i)
            x1, y1 = x1[0], y1[0]
            x2, y2 = np.where(self.goal2==i)
            x2, y2 = x2[0], y2[0]

            coords[i] = [(x1,y1), (x2,y2)]
        return coords

def get_state(id):
    xn = np.asarray(list(id))
    xn = xn.reshape((3,3))
    xn = xn.astype(int)
    return xn

P = Puzzle()

id1 = '287361045'
start1 = get_state(id1)
S1 = State(start1)

# id2 = '287061345'
# start2 = get_state(id2)
# S2 = State(start2)

path1 = a_star_search(problem=P, start=S1)
print(path1, len(path1))

# path2 = a_star_search(problem=P, start=S2)
# print(path2, len(path2))

# path = breadth_first_search(problem=P, start=S)
# print(path, len(path))

# goal = [path[-1]]
# path.extend(goal*3)

# run_animation(path)




