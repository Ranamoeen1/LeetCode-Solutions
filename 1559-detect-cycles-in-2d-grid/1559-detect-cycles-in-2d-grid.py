class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid or not grid[0]:
            return False
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(row: int, col: int, parent_row: int, parent_col: int, value: str) -> bool:
            visited[row][col] = True
            
            # Four directions: up, down, left, right
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and if the cell has the same value
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == value:
                    # If not visited, continue DFS
                    if not visited[new_row][new_col]:
                        if dfs(new_row, new_col, row, col, value):
                            return True
                    # If visited and it's not the parent cell, we found a cycle
                    elif (new_row, new_col) != (parent_row, parent_col):
                        return True
            
            return False
        
        # Try to find a cycle starting from each unvisited cell
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        
        return False