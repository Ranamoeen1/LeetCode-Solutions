from collections import deque
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If the start or end cell contains a thief, the safeness factor is automatically 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-source BFS to calculate distance to the nearest thief for each cell
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        # Step 2: Use a Max-Heap (Dijkstra-like) to find the path maximizing the minimum safeness factor
        # Python's heapq is a min-heap by default, so we store negative safeness values (-safeness, r, c)
        max_heap = [(-dist[0][0], 0, 0)]
        
        # Track the maximum safeness found for each cell to prevent redundant processing
        max_safeness_to = [[-1] * n for _ in range(n)]
        max_safeness_to[0][0] = dist[0][0]
        
        while max_heap:
            current_safeness, r, c = heapq.heappop(max_heap)
            current_safeness = -current_safeness  # Convert back to positive
            
            # If we reached the bottom-right corner, return the accumulated result
            if r == n - 1 and c == n - 1:
                return current_safeness
                
            # If we already found a better path to this cell, skip it
            if current_safeness < max_safeness_to[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # The safeness factor of the new path is limited by the minimum along its way
                    next_safeness = min(current_safeness, dist[nr][nc])
                    
                    if next_safeness > max_safeness_to[nr][nc]:
                        max_safeness_to[nr][nc] = next_safeness
                        heapq.heappush(max_heap, (-next_safeness, nr, nc))
                        
        return 0