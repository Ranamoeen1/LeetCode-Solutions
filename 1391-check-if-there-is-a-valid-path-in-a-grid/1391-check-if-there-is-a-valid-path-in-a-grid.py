# from typing import List
# from collections import deque

# class Solution:
#     def hasValidPath(self, grid: List[List[int]]) -> bool:
#         m, n = len(grid), len(grid[0])
        
#         # For each street type, define which directions it connects to
#         # Directions: 0: left, 1: up, 2: right, 3: down
#         connections = {
#             1: [0, 2],  # left and right
#             2: [1, 3],  # up and down
#             3: [0, 3],  # left and down
#             4: [2, 3],  # right and down
#             5: [0, 1],  # left and up
#             6: [2, 1]   # right and up
#         }
        
#         # For each direction, what's the opposite direction when moving to adjacent cell
#         # And what's the delta in coordinates
#         # Direction: 0: left, 1: up, 2: right, 3: down
#         opposite = {0: 2, 2: 0, 1: 3, 3: 1}
#         deltas = {0: (0, -1), 2: (0, 1), 1: (-1, 0), 3: (1, 0)}
        
#         # BFS approach
#         visited = [[False] * n for _ in range(m)]
#         queue = deque([(0, 0)])
#         visited[0][0] = True
        
#         while queue:
#             x, y = queue.popleft()
            
#             # If reached destination
#             if x == m - 1 and y == n - 1:
#                 return True
            
#             current_street = grid[x][y]
            
#             # For each direction this street connects to
#             for direction in connections[current_street]:
#                 dx, dy = deltas[direction]
#                 nx, ny = x + dx, y + dy
                
#                 # Check if neighbor is within bounds and not visited
#                 if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
#                     # Check if neighbor's street connects back to this cell
#                     neighbor_street = grid[nx][ny]
#                     opposite_direction = opposite[direction]
                    
#                     if opposite_direction in connections[neighbor_street]:
#                         visited[nx][ny] = True
#                         queue.append((nx, ny))
        
#         return False



class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Union-Find with path compression and union by rank
        parent = list(range(m * n))
        rank = [1] * (m * n)
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        
        # Direction mapping: (dx, dy, current_required, neighbor_required)
        # For each cell, connect to right and down neighbors only to avoid duplicates
        connections = {
            1: {  # left-right
                'right': ('right', 'left'),    # current goes right, neighbor connects from left
                'left': ('left', 'right')       # current goes left, neighbor connects from right
            },
            2: {  # up-down
                'down': ('down', 'up'),
                'up': ('up', 'down')
            },
            3: {  # left-down
                'down': ('down', 'up'),
                'left': ('left', 'right')
            },
            4: {  # right-down
                'down': ('down', 'up'),
                'right': ('right', 'left')
            },
            5: {  # left-up
                'up': ('up', 'down'),
                'left': ('left', 'right')
            },
            6: {  # right-up
                'up': ('up', 'down'),
                'right': ('right', 'left')
            }
        }
        
        # Function to get index in parent array
        def idx(i, j):
            return i * n + j
        
        # Connect cells
        for i in range(m):
            for j in range(n):
                street = grid[i][j]
                current_idx = idx(i, j)
                
                # Check right neighbor
                if j + 1 < n:
                    right_street = grid[i][j + 1]
                    # Can current go right and right come from left?
                    if ('right' in connections[street] and 
                        'left' in connections[right_street] and
                        connections[street]['right'][1] == 'left'):
                        union(current_idx, idx(i, j + 1))
                
                # Check down neighbor
                if i + 1 < m:
                    down_street = grid[i + 1][j]
                    # Can current go down and down come from up?
                    if ('down' in connections[street] and 
                        'up' in connections[down_street] and
                        connections[street]['down'][1] == 'up'):
                        union(current_idx, idx(i + 1, j))
        
        # Check if start and end are connected
        return find(0) == find(idx(m - 1, n - 1))