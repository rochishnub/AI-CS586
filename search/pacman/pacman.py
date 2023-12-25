import sys
sys.path.append("..")

from base import Node, Problem
from math import dist
from uninformed import breadth_first_search, depth_first_search
from animate import run_animation
from informed import a_star_search
# import matplotlib.animation as anim
# import matplotlib.pyplot as plt

class State(Node):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(id)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.id = self.get_id()
    
    def get_id(self):
        return f"{self.x1}-{self.y1}-{self.x2}-{self.y2}"

class Maze(Problem):
    def __init__(self, size:int):
        super().__init__()
        self.size = size
    
    def successors(self, node:State):
        succ = []
        pacman = self.neighbours(node.x1, node.y1)
        mspacman = self.neighbours(node.x2, node.y2)
        for pmove in pacman:
            for mpmove in mspacman:
                x1, y1 = pmove
                x2, y2 = mpmove
                succ.append(State(x1, y1, x2, y2))
        return succ
        
    def neighbours(self, x, y):
        moves = [(x,y-1), (x,y+1), (x+1,y), (x-1,y), (x,y)]
        moves = [move for move in moves if self.boundary(move)]
        return moves
    
    def boundary(self, move):
        p, q = move
        if 0<=p<self.size and 0<=q<self.size:
            return True
        else: return False

    
    def goal_test(self, node:State):
        if node.x1==node.x2 and node.y1==node.y2:
            return True
        else: return False
    
    def heuristic(self, node:State):
        pacman = [node.x1, node.y1]
        mspacman = [node.x2, node.y2]
        distance = dist(pacman, mspacman)
        return distance
        
size = 8
q2 = Maze(size)
start = State(0,0,7,7)

path = breadth_first_search(q2, start)
print(path, len(path))

run_animation(size, path, 'BFS')

path = a_star_search(q2, start)
print(path, len(path))

run_animation(size, path, 'A*')

path = depth_first_search(q2, start)
print(path, len(path))

run_animation(size, path, 'DFS')