import pandas as pd

# The function initializes and returns open
def init_open():
    raise NotImplementedError

# The function inserts s into open
def insert_to_open(open_list, s):  # Should be implemented according to the open list data structure
    raise NotImplementedError

# The function returns the best node in open (according to the search algorithm)
def get_best(open_list):
    raise NotImplementedError

# The function returns neighboring locations of s_location
def get_neighbors(grid, s_location):
    # neighbors = []
    raise NotImplementedError
    # return neighbors

# The function returns whether or not s_location is the goal location
def is_goal(s_location, goal_location):
    raise NotImplementedError

# Locations are tuples of (x, y)
def bfs(grid, start_location, goal_location):
    # State = (x, y, s_prev)
    # Start_state = (x_0, y_0, False)
    open_list = init_open()
    closed_list = set()

    # Mark the source node as
    # visited and enqueue it
    start = (start_location[0], start_location[1], None)
    insert_to_open(open_list, start)

    while not open_list.empty():
        # Dequeue a vertex from
        # queue and print it
        s = get_best(open_list)
        # print(s, end=" ")
        s_location = (s[0], s[1])
        if s_location in closed_list:
            continue
        if is_goal(s_location, goal_location):
            print("The number of states visited by BFS:", len(closed_list))
            return s
        neighbors = get_neighbors(grid, s_location)
        for n_location in neighbors:
            if n_location in closed_list:
                continue
            n = (n_location[0], n_location[1], s)
            insert_to_open(open_list, n)
        closed_list.add(s_location)

def print_route(s):
    while s:
        print(s[0], s[1])
        s = s[3]

def get_route(s):
    route = []
    while s:
        s_location = (s[0], s[1])
        route.append(s_location)
        s = s[2]
    route.reverse()
    return route

def print_grid_route(route, grid):
    for location in route:
        grid[location] = 'x'
    print(pd.DataFrame(grid))
