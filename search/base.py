class Node():
    def __init__(self, id):
        self.id = id
    


class Problem():
    def __init__(self):
        self.start = 0
        self.goals = []
    
    def successors(self, node:Node):
        pass

    def goal_test(self, node:Node):
        return False
    
    def path_cost(self, path):
        return 0
    
    def heuristic(self, node:Node):
        return 0




