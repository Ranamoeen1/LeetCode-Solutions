from heapq import heappop, heappush
from math import inf
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
        
        # dist[u][cur] stores the min weight to reach node u with 'cur' consecutive identical characters
        dist = [[inf] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        # Priority queue stores tuples of (distance, node, current_consecutive_count)
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, cur = heappop(pq)
            
            # If we reached the destination node, return the distance
            if u == n - 1:
                return d
            
            if d > dist[u][cur]:
                continue
                
            for v, w in g[u]:
                nxt = 1 if labels[v] != labels[u] else cur + 1
                nd = d + w
                
                if nxt <= k and nd < dist[v][nxt]:
                    dist[v][nxt] = nd
                    heappush(pq, (nd, v, nxt))
                    
        return -1