class Dijkstra_Algorithm():
    def __init__(self, V, E, edge_weight):
        self.V = V
        self.E = E
        self.edge = edge_weight
        self.visited = []
        self.chart = {}
        self.prev = {}


    # 1. Shortest path tarting vertex s
    def dijkstra(self, s, v): 
        self.setup(s)
        self.shortest(s)

        cur = v
        path = []
        while cur:
            path.insert(0, cur)
            cur = self.prev[cur]
        print("Shortest Path is:", path)

    def shortest(self, s):
        self.visited.append(s)

        # Set shortest path for every outgoing from v
        for u in self.E[s]:
            if u not in self.visited:
                _set = self.chart[s] + self.edge[s + u]
                if _set < self.chart[u]:
                    self.chart[u] = _set
                    self.prev[u] = s
                    
        # Visit next shortest path that's not visited
        _next = None
        for v in self.chart:
            if v not in self.visited:
                if _next is None:
                    _next = v
                elif self.chart[_next] > self.chart[v]:
                    _next = v
        if _next is not None:
            self.shortest(_next)
        
    def setup(self, s):
        # 2. Set inf to all vertices, but 0 for s
        #    Set prev to None for all vertices
        for v in self.V:
            self.chart[v] = float("inf")
            self.prev[v] = None
        self.chart[s] = 0
