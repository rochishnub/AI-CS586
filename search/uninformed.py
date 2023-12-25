from base import Node, Problem

# BFS
def breadth_first_search(problem:Problem, start:Node):

    if problem.goal_test(start):
        return [start.id]
    
    frontier = []
    frontier.append([start])
    visited = {start.id}
    while frontier:
        curr_path = frontier.pop(0)
        node = curr_path[-1]
        children = problem.successors(node)
        for child in children:

            if problem.goal_test(child): 
                new_path = list(curr_path)
                new_path.append(child)
                return [n.id for n in new_path]
            
            if child.id not in visited:
                visited.add(child.id)
                new_path = list(curr_path)
                new_path.append(child)
                frontier.append(new_path)
    return []

# UCS
def uniform_cost_search(problem:Problem, start:Node):
    frontier = []
    frontier.append([start])
    while frontier:
        frontier = sorted(frontier, key=problem.path_cost)
        curr_path = frontier.pop(0)
        node = curr_path[-1]
        if problem.goal_test(node):
            return [n.id for n in curr_path]
        
        children = problem.successors(node)
        for child in children:
            new_path = list(curr_path)
            new_path.append(child)
            frontier.append(new_path)
        
    return []
    

# DFS
def depth_first_search(problem:Problem, start:Node, visited=set()):
    visited.add(start.id)
    if problem.goal_test(start):
        return [start.id]
        
    children = problem.successors(start)
    for child in children:
        if child.id not in visited:
            path = depth_first_search(problem, child, visited)
            if path:
                path.insert(0, start.id)
                return path
    return []

# DLS
def depth_limited_search(problem:Problem, start:Node, limit:int, visited=set()):
    visited.add(start.id)
    if limit==0:
        if problem.goal_test(start):
            return [start.id]
        return []
    
    if problem.goal_test(start):
        return [start.id]
        
    children = problem.successors(start)
    for child in children:
        if child.id not in visited:
            path = depth_limited_search(problem, child, limit-1, visited)
            if path:
                path.insert(0, start.id)
                return path
    return []

# IDS
def iterative_deepening_search(problem:Problem, start:Node):
    depth = 0
    while True:
        path = depth_limited_search(problem, start, depth, visited=set())
        if path:
            return path
        depth += 1

    



