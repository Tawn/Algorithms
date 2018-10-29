from Graph import *
from Dijkstra import *

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
    graph.add_edge("C", "E")
    graph.add_edge("D", "C")

    # Edge weights
    graph.add_weight("A", "B", 5)
    graph.add_weight("A", "C", 10)
    graph.add_weight("B", "D", 1)
    graph.add_weight("C", "E", 1)
    graph.add_weight("D", "C", 1)

    # Print Curent Vertices and Edges
    print("Vertices:", graph.get_vertices())
    print("Edges: ", graph.get_edges())

    # Print the Adjacency List
    print("Adjacency List:")
    for i in graph.get_vertices():
        print("{} -> {}".format(i, graph.get_adjacent()[i]))

    # Dijkstra's Aglorithm: Shortest path from u to v
    path = Dijkstra_Algorithm(V, Adj, edge_weight)
    path.dijkstra("A", "E")
    print(path.chart)
    

main()
