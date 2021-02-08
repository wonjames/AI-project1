from dijkstra import Graph, DijkstraSPF
import time

# parses through the txt file and adds the nodes to the graph
def createGraph():
    graph = Graph()
    f = open("p1_graph.txt", "r")
    for line in f:
        line = line.strip()
        path_values = line.split(",")
        graph.add_edge(int(path_values[0]),int(path_values[1]),int(path_values[2]))
    return graph

# uses the Dijkstra Algorithm to find the path from the parameters: start and dest
def findPath(start, dest):
    graph = createGraph()
    start_time = time.time()
    dijkstra = DijkstraSPF(graph, start)
    try:
        path = dijkstra.get_path(dest)
        print(path)
    except KeyError:
        print("No path found")
    end_time = time.time()
    total_time = end_time-start_time
    print("Total Elasped: ", total_time)
    

if __name__ == '__main__':
    path = input("Enter two numbers (0,99) separated by a comma: ")
    path_array = path.split(',')
    findPath(int(path_array[0]),int(path_array[1]))

