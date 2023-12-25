import sys
sys.path.append("..")

from base import Problem, Node
from informed import a_star_search

class Graph(Problem):
    def __init__(self):
        super().__init__()
        self.start = Node('S')
        self.adjacency = {
            'S': ['A','B','G'],
            'A': ['C','D'],
            'B': ['D','E'],
            'C': ['G'],
            'D': ['G'],
        }

        self.cost_matrix = {
            'S': {'A':2, 'B':1, 'G':9},
            'A': {'C':2, 'D':3},
            'B': {'D':2, 'E':4},
            'C': {'G':4},
            'D': {'G':4}
        }

        self.heuristic_fn = {
            'S':6, 'A':0, 'B':6, 'C':4, 'D':1, 'E':10, 'G':0
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
    
    def heuristic(self, node: Node):
        return self.heuristic_fn[node.id]

tree = Graph()

a = a_star_search(tree, tree.start)
print(f"A*: {a}")