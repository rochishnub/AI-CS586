import sys
sys.path.append("..")

from base import Node, Problem
from uninformed import breadth_first_search, uniform_cost_search, depth_first_search

class Graph(Problem):
    def __init__(self):
        super().__init__()
        self.start = Node('S')
        self.adjacency = {
            'S': ['A','B'],
            'A': ['C','D'],
            'B': ['D','G'],
            'C': ['G'],
            'D': ['G'],
        }

        self.cost_matrix = {
            'S': {'A':1, 'B':2},
            'A': {'C':1, 'D':1},
            'B': {'D':2, 'G':5},
            'C': {'G':5},
            'D': {'G':2},
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
            return 0
        cost = 0
        path_id = [node.id for node in path]
        for i in range(len(path_id)-1):
            start,end = path_id[i], path_id[i+1]
            cost += self.cost_matrix[start][end]
        return cost

tree = Graph()

bfs = breadth_first_search(tree, tree.start)
print(f"BFS: {bfs}")

ucs = uniform_cost_search(tree, tree.start)
print(f"UCS: {ucs}")

dfs = depth_first_search(tree, tree.start)
print(f"DFS: {dfs}")




