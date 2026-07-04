from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build the adjacency list graph
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # BFS initialization
        queue = deque([1])
        visited = {1}
        min_score = float('inf')
        
        while queue:
            node = queue.popleft()
            
            for neighbor, weight in graph[node]:
                # Update the minimum score with every road we see in this component
                if weight < min_score:
                    min_score = weight
                    
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score