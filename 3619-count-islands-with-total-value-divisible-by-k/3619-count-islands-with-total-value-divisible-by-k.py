from typing import List
from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    # BFS to explore the island and sum its values
                    island_sum = 0
                    queue = deque([(i, j)])
                    visited[i][j] = True
                    
                    while queue:
                        r, c = queue.popleft()
                        island_sum += grid[r][c]
                        
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                                
                    if island_sum % k == 0:
                        count += 1
                        
        return count