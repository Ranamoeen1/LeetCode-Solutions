from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # For each street type, define which directions it connects to
        # Directions: 0: left, 1: up, 2: right, 3: down
        connections = {
            1: [0, 2],  # left and right
            2: [1, 3],  # up and down
            3: [0, 3],  # left and down
            4: [2, 3],  # right and down
            5: [0, 1],  # left and up
            6: [2, 1]   # right and up
        }
        
        # For each direction, what's the opposite direction when moving to adjacent cell
        # And what's the delta in coordinates
        # Direction: 0: left, 1: up, 2: right, 3: down
        opposite = {0: 2, 2: 0, 1: 3, 3: 1}
        deltas = {0: (0, -1), 2: (0, 1), 1: (-1, 0), 3: (1, 0)}
        
        # BFS approach
        visited = [[False] * n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        
        while queue:
            x, y = queue.popleft()
            
            # If reached destination
            if x == m - 1 and y == n - 1:
                return True
            
            current_street = grid[x][y]
            
            # For each direction this street connects to
            for direction in connections[current_street]:
                dx, dy = deltas[direction]
                nx, ny = x + dx, y + dy
                
                # Check if neighbor is within bounds and not visited
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Check if neighbor's street connects back to this cell
                    neighbor_street = grid[nx][ny]
                    opposite_direction = opposite[direction]
                    
                    if opposite_direction in connections[neighbor_street]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        
        return False