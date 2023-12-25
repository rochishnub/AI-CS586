from base import Problem, Node

def a_star_search(problem:Problem, start:Node):
    frontier = []
    frontier.append([start])
    # turn=0
    while frontier:
        frontier = sorted(frontier, key=lambda path:estimated_cost(problem, path))

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

def estimated_cost(problem:Problem, path):
    end = path[-1]
    gn = problem.path_cost(path)
    hn = problem.heuristic(end)
    # print(end.id, 'hn',hn, 'gn', gn, 'fn', gn+hn)
    return gn + hn
