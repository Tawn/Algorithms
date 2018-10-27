class Graph():
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.adj = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []
            self.vertices.append(vertex)
        else:
            print("vertex already exists")

    def add_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            print("need to add vertex first")
        else:
            self.adj[u].append(v)
            self.edges.append("({}, {})".format(u, v))
        
    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def get_adjacent(self, vertex):
        return self.adj[vertex]
