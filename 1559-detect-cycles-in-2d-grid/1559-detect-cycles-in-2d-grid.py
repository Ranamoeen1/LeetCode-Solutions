# class Solution:
#     def containsCycle(self, grid: List[List[str]]) -> bool:
#         if not grid or not grid[0]:
#             return False
        
#         m, n = len(grid), len(grid[0])
#         visited = [[False] * n for _ in range(m)]
        
#         def dfs(row: int, col: int, parent_row: int, parent_col: int, value: str) -> bool:
#             visited[row][col] = True
            
#             # Four directions: up, down, left, right
#             directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
#             for dr, dc in directions:
#                 new_row, new_col = row + dr, col + dc
                
#                 # Check bounds and if the cell has the same value
#                 if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == value:
#                     # If not visited, continue DFS
#                     if not visited[new_row][new_col]:
#                         if dfs(new_row, new_col, row, col, value):
#                             return True
#                     # If visited and it's not the parent cell, we found a cycle
#                     elif (new_row, new_col) != (parent_row, parent_col):
#                         return True
            
#             return False
        
#         # Try to find a cycle starting from each unvisited cell
#         for i in range(m):
#             for j in range(n):
#                 if not visited[i][j]:
#                     if dfs(i, j, -1, -1, grid[i][j]):
#                         return True
        
#         return False


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid or not grid[0]:
            return False
        
        m, n = len(grid), len(grid[0])
        
        # Union-Find with path compression and union by rank
        parent = list(range(m * n))
        rank = [1] * (m * n)
        
        def find(x: int) -> int:
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> bool:
            # Returns False if x and y are already connected (cycle detected)
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False  # Cycle detected
            
            # Union by rank
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            
            return True
        
        # Process each cell and connect it to cells below and to the right
        # This ensures we only check each edge once
        for i in range(m):
            for j in range(n):
                current_val = grid[i][j]
                current_index = i * n + j
                
                # Check right neighbor (same row, next column)
                if j + 1 < n and grid[i][j + 1] == current_val:
                    if not union(current_index, i * n + (j + 1)):
                        return True
                
                # Check down neighbor (next row, same column)
                if i + 1 < m and grid[i + 1][j] == current_val:
                    if not union(current_index, (i + 1) * n + j):
                        return True
        
        return False