# Topological Sorting of a Graph is an in-order
# Sorting algorithm for all paths {(u, v) | u, v in V}
# u is always before v
# Using a Depth-First search method with stack of array

class Topological_Sort():
    def __init__(self):
        # For Keeping Track of DFS
        self.visited = []
        self.sort = []

    def t_sort(self, V, Adj):
        for s in V:
            if s not in self.visited:
                self.visited.append(s)
                self.dfs(V, Adj, s)

        print("Topological Sort: ", self.sort)

    def dfs(self, V, Adj, s):
        for u in Adj[s]:
            if u not in self.visited:
                self.visited.append(u)
                self.dfs(V, Adj, u)
        self.sort.insert(0, s)
