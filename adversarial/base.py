class Node():
    def __init__(self):
        self.id = 0
        self.state = []

class Game():
    def __init__(self):
        pass

    def turn(self, node:Node):
        return 0
    
    def terminate(self, node:Node):
        return False
    
    def utility(self, node:Node, player:bool):
        return 0
    
    def actions(self, node:Node, player:bool):
        return []
    
    def play(self, node:Node, action, player:bool, apply:bool):
        return 0
    
    def opponent(self, player:bool):
        return False