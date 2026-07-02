from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # min_cost[r][c] will store the minimum health cost to reach cell (r, c)
        min_cost = [[float('inf')] * n for _ in range(m)]
        
        # Initialize starting point
        min_cost[0][0] = grid[0][0]
        
        # Deque for 0-1 BFS: stores tuples of (row, col)
        queue = deque([(0, 0)])
        
        # Directions for up, down, left, right movements
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reached the destination, we can stop early
            if r == m - 1 and c == n - 1:
                break
                
            current_cost = min_cost[r][c]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    next_cost = current_cost + grid[nr][nc]
                    
                    # If we found a strictly cheaper path to the neighbor
                    if next_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = next_cost
                        
                        # 0-1 BFS optimization
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
        
        # We need to reach the end with AT LEAST 1 health remaining.
        # This means the total cost incurred must be strictly less than our initial health.
        return min_cost[m - 1][n - 1] < health