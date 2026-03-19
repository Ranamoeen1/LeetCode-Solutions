class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Create prefix sum arrays for X and Y
        prefix_X = [[0] * (n + 1) for _ in range(m + 1)]
        prefix_Y = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill prefix sum arrays
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_X[i][j] = prefix_X[i-1][j] + prefix_X[i][j-1] - prefix_X[i-1][j-1] + (1 if grid[i-1][j-1] == 'X' else 0)
                prefix_Y[i][j] = prefix_Y[i-1][j] + prefix_Y[i][j-1] - prefix_Y[i-1][j-1] + (1 if grid[i-1][j-1] == 'Y' else 0)
        
        count = 0
        
        # Check each possible bottom-right corner (i, j)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Count X and Y in rectangle from (0,0) to (i-1, j-1)
                num_X = prefix_X[i][j]
                num_Y = prefix_Y[i][j]
                
                # Check conditions
                if num_X == num_Y and num_X >= 1:
                    count += 1
        
        return count