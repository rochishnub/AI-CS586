import sys
sys.path.append("..")

from base import Problem, Node
from informed import a_star_search
import numpy as np

class Graph(Problem):
    def __init__(self):
        super().__init__()
        self.start = Node('S')
        self.adjacency = {
            'S': ['A','B','C'],
            'A': ['D','E'],
            'B': ['G'],
            'C': ['F'],
            'D': ['H'],
            'E': ['G'],
            'F': ['G']
        }

        self.cost_matrix = {
            'S': {'A':5, 'B':2, 'C':4},
            'A': {'D':9, 'E':4},
            'B': {'G':6},
            'C': {'F':2},
            'D': {'H':7},
            'E': {'G':6},
            'F': {'G':1}
        }

        self.heuristic = {
            'S':8, 'A':8, 'B':4, 'C':3, 'D':np.inf, 'E':np.inf, 'F':1, 'G':0
        }
    
    def successors(self, node:Node):
        id = node.id
        if id not in set(self.adjacency.keys()):
            return []
        return [Node(neighID) for neighID in self.adjacency[id]]
    
    def goal_test(self, node: Node):
        if node.id=='G':
            return True
        else: return False
    
    def path_cost(self, path):
        if len(path)==1:
            return 100
        cost = 0
        path_id = [node.id for node in path]
        for i in range(len(path_id)-1):
            start,end = path_id[i], path_id[i+1]
            cost += self.cost_matrix[start][end]
        return cost
    

tree = Graph()

a = a_star_search(tree, tree.start)
print(f"A*: {a}")