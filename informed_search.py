import time
import astar

# 2D array that holds the neighbors and distance of each node
nodes = [[] for x in range(100)]

# parses through the txt file and adds the nodes to the nodes 2D array
def createGraph():
    f = open("p1_graph.txt", "r")
    for line in f:
        line = line.strip()
        path_values = line.split(",")
        path = {'node2': int(path_values[1]), 'distance': int(path_values[2])}
        nodes[int(path_values[0])].append(path)

# sends all the neighbors back to the neighbor function
# n is the node that you want to get the neighbors for
def neighbors(n):
    for neighbor in nodes[n]:
        yield neighbor['node2']

# gets the distance between n1 and n2
def distance(n1, n2):
    for dst in nodes[n1]:
        if dst['node2'] == n2:
            return dst['distance']
            
# generic cost function
def cost(n, goal):
    return 1

if __name__ == '__main__':
    createGraph()
    path = input("Enter two numbers (0,99) separated by a comma: ")
    path_array = path.split(',')
    start = time.time()
    try:
        path = list(astar.find_path(int(path_array[0]), int(path_array[1]), neighbors_fnct=neighbors,
                    heuristic_cost_estimate_fnct=cost, distance_between_fnct=distance))
        print(path)
    except TypeError:
        print("No path found")
    end = time.time()
    total_time = end - start
    print("Time Elasped: ", total_time)
    