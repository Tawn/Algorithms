# Dijkstra Algorithm

Given a graph with edge weights G = (V, E, W):
- Finding the shortest path from any starting vertex s in V to all other vertices

Procedure: 
1. bookkeep {all vertices v | distance[v] = infinite, but s to 0}
2. mark s as visited
3. From vertices u reachable from s: 
    - update distance[u] = distance[s] + edge weight (if distance[u] is greater)
    - set previous vertex prev[u] to [s]
4. repeat from step 2 by recursively calling with s as the next unvisited and smallest val
