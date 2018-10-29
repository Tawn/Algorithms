from Graph import *
from Topological_Sort import *
from Longest_Path import *
from Shortest_Path import *
from Cycles import *
from SCC import *

def main():
    graph = Graph()

    # Vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("X")
    graph.add_vertex("Y")
    graph.add_vertex("Z")

    # Edges
    graph.add_edge("A", "B") 
    graph.add_edge("B", "C")
    graph.add_edge("C", "X")
    graph.add_edge("C", "E")
    graph.add_edge("D", "B")
    graph.add_edge("E", "D")
    graph.add_edge("X", "Y")
    graph.add_edge("Y", "Z")
    graph.add_edge("Z", "X")
    
    # Cycle
    #graph.add_edge("X", "A")


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
    #sort = Topological_Sort()
    #sort.t_sort(V, Adj)

    # Strongly Connected Components
    scc = Strongly_Connected(V, Adj)
    scc.scc()

    # Test Longest Path
    #long = Longest_Path(V, Adj)
    #print("Longest Path (A,E):", long.longest_path("A","E"))

    # Test Shortest Path
    #short = Shortest_Path(V, Adj)
    #print("Shortest Path (A,E):", short.shortest_path("A", "E"))

    # Test Cycles
#    cycle = Strongly_Connected(V, Adj)
#    cycle.find_cycles()
main()
