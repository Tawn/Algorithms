from Graph import *

def main():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")

    print("Vertices:", graph.get_vertices())
    print("Edges: ", graph.get_edges())

    for i in graph.get_vertices():
        print("Adjacent {}: {}".format(i, graph.get_adjacent(i)))
    
main()
