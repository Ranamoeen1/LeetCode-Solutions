class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 1:
                return
            # Mark the current land cell as visited by turning it into water (1)
            grid[r][c] = 1
            # Recursively visit all 4 neighboring directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Flood-fill (sink) all 0s connected to the boundary
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 0:
                    dfs(i, j)
                    
        # Step 2: Count the remaining closed islands
        closed_islands_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    closed_islands_count += 1
                    dfs(i, j)  # Sink this entire closed island
                    
        return closed_islands_count