from Graph import *
from BellmanFord import *

def main():
    graph = Graph()

    # Vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    # Edges
    graph.add_edge("A", "B")
    graph.add_edge("A", "C") 
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "D")
    graph.add_edge("E", "D")

    # Edge weights
    graph.add_weight("A", "B", 2)
    graph.add_weight("A", "C", 2) 
    graph.add_weight("B", "D", 0)
    graph.add_weight("B", "E", -1)
    graph.add_weight("C", "D", -1)
    graph.add_weight("E", "D",-2)

    # Print Curent Vertices and Edges
    print("Vertices:", graph.get_vertices())
    print("Edges: ", graph.get_edges())

    # Print the Adjacency List
    print("Adjacency List:")
    for i in graph.get_vertices():
        print("{} -> {}".format(i, graph.get_adjacent()[i]))

    V = graph.get_vertices()
    E = graph.get_adjacent()
    W = graph.edge_weight

    # Bellman-Ford Algorithm: Shortest path from u to v w/neg
    ford = Bellman_Ford(V, E, W) # From A to all nodes
    

main()
