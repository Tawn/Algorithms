class Bellman_Ford():
    
    def __init__(self, V, E, W):
        self.V = V # Vertices
        self.E = E # Edges
        self.W = W # Weights
        self.iter = len(V)-1
        self.visited = {}
        self.prev = {}
        self.chart = {}
        self.setup()

    def bellman(self):
        # Number of iterations
        for i in range(self.iter):
            # For every vertices
            for v in self.V:
                # For every reachable vertices
                    for u in self.E[v]:
                        key = v + u # Edge weight
                        if (self.chart[v] + self.W[key]) < self.chart[u]:
                            self.chart[u] = (self.chart[v] + self.W[key])
                            self.prev[u] = v      

    def setup(self):
        count = 0
        for v in self.V:
            if count is 0:
                self.chart[v] = 0
                count += 1
            else:
                self.chart[v] = float("inf")
        self.bellman()
        print(self.chart)
        
        
        
            
