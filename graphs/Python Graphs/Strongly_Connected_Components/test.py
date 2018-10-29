from Graph import *
from SCC import *

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

    # Include Cycle
    graph.add_edge("D", "A")

    # Print Curent Vertices and Edges
    print("Vertices:", graph.get_vertices())
    print("Edges: ", graph.get_edges())

    # Print the Adjacency List
    print("Adjacency List:")
    for i in graph.get_vertices():
        print("{} -> {}".format(i, graph.get_adjacent()[i]))

    # Strongly Connected Components
    scc = Strongly_Connected(V, Adj)
    scc.scc()

main()
