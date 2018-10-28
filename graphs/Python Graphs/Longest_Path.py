class Longest_Path():   
    def __init__(self, V, Adj):
        self.V = V
        self.Adj = Adj
        self.L = {}
        self.stack = []

    def longest_path(self, s, v):
        # Base Case
        if s == v:
            return 0

        # Getting max val from out-neighbors
        max_val = 0
        c = None
        for u in self.Adj[s]:
            print(s, u, v)
            val = 1 + self.longest_path(u,v)
            if max_val < val:
                max_val = val
                
        return max_val
            
        
    
