class Shortest_Path():   
    def __init__(self, V, Adj):
        self.V = V
        self.Adj = Adj
        self.L = {}
        self.stack = []

    def shortest_path(self, s, v):
        # Base Case
        if s == v:
            return 0

        # Getting max val from out-neighbors
        min_val = float("inf")
        c = None
        for u in self.Adj[s]:
            print(s, u, v)
            val = 1 + self.shortest_path(u,v)
            if min_val > val:
                min_val = val
                
        return min_val
