import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

def greedy_best_first_search(start_state, goal_state, heuristic_func, get_neighbors):
    open_list = []
    heapq.heappush(open_list, Node(start_state, heuristic=heuristic_func(start_state)))
    closed_list = set()
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.state == goal_state:
            return reconstruct_path(current_node)
        
        closed_list.add(tuple(tuple(peg) for peg in current_node.state))
        
        for neighbor, cost in get_neighbors(current_node.state):
            neighbor_tuple = tuple(tuple(peg) for peg in neighbor)
            if neighbor_tuple in closed_list:
                continue
            
            neighbor_node = Node(neighbor, current_node, current_node.cost + cost, heuristic_func(neighbor))
            heapq.heappush(open_list, neighbor_node)
    
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def heuristic(state):
    goal_post = state[2]
    return len(goal_post) - sum(1 for i, disk in enumerate(goal_post) if disk == len(goal_post) - i)

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        if state[i]:
            disk = state[i][-1]
            for j in range(3):
                if i != j and (not state[j] or state[j][-1] > disk):
                    new_state = [peg[:] for peg in state]
                    new_state[i].pop()
                    new_state[j].append(disk)
                    neighbors.append((new_state, 1))
    return neighbors

start_state = [[5, 4, 3, 2, 1], [], []]
goal_state = [[], [], [5, 4, 3, 2, 1]]

path = greedy_best_first_search(start_state, goal_state, heuristic, get_neighbors)
for step in path:
    print(step)
