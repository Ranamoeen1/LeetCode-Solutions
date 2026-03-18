class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # Create prefix sum matrix
        prefix = [[0] * n for _ in range(m)]
        
        # Fill prefix sums
        for i in range(m):
            for j in range(n):
                prefix[i][j] = grid[i][j]
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j-1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]
        
        # Count valid submatrices
        count = 0
        for i in range(m):
            for j in range(n):
                if prefix[i][j] <= k:
                    count += 1
                else:
                    break
        
        return count