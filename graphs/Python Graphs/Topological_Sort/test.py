from Graph import *
from Topological_Sort import *

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

    # Print Curent Vertices and Edges
    print("Vertices:", graph.get_vertices())
    print("Edges: ", graph.get_edges())

    # Print the Adjacency List
    print("Adjacency List:")
    for i in graph.get_vertices():
        print("{} -> {}".format(i, graph.get_adjacent()[i]))
        
    # Tests the Topological Sorts
    V = graph.get_vertices()
    Adj = graph.get_adjacent()
    edge_weight = graph.edge_weight
    
    sort = Topological_Sort()
    sort.t_sort(V, Adj)
main()
