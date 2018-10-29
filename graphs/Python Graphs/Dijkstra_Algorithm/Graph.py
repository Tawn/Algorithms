class Graph():
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.adj = {}
        self.edge_weight = {}

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

    def add_weight(self, u, v, weight):
        key = u + v
        self.edge_weight[key] = weight

    def get_weight(self, u, v):
        key = u + v
        return self.edge_weight[key]
        
    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def get_adjacent(self):
        return self.adj
