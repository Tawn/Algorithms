class Strongly_Connected():
    def __init__(self, V, Adj):
        self.V = V
        self.Adj = Adj
        self.stack = []
        self.visited = []
        self.reverse = {}
        self.components = []

    def scc(self):
        for u in self.V:
            if u not in self.visited:
                self.dfs(u)

        self.rev_adj()
        self.unstack()

    def unstack(self):
        self.visited = []
        for v in self.stack:
            if v not in self.visited:
                self.dfs2(v)
                self.components.append("_")

        print("Strongly-Connected Components: ", self.components)

    def dfs2(self, u):
        if u not in self.visited:
            self.visited.append(u)
            for s in self.reverse[u]:
                self.dfs2(s)
            self.components.append(u)
            

    def dfs(self, u):
        if u not in self.visited:
            self.visited.append(u)
            for s in self.Adj[u]:
                self.dfs(s)
            self.stack.insert(0, u)

    def rev_adj(self):
        # Initialize rev adj
        rev = {}
        for v in self.V:
            rev[v] = []

        # Reverse
        for v in self.V:
            for u in self.Adj[v]:
                rev[u].append(v)

        # Add to new Adj
        for v in self.V:
            self.reverse[v] = rev[v]
