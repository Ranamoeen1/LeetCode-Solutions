# class Solution:
#     def maxProductPath(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         MOD = 10**9 + 7
        
#         # dp[i][j][0] = maximum product to reach (i,j)
#         # dp[i][j][1] = minimum product to reach (i,j)
#         dp = [[[float('-inf'), float('inf')] for _ in range(n)] for _ in range(m)]
        
#         # Initialize starting cell
#         dp[0][0][0] = grid[0][0]
#         dp[0][0][1] = grid[0][0]
        
#         # Fill first row
#         for j in range(1, n):
#             dp[0][j][0] = dp[0][j-1][0] * grid[0][j]
#             dp[0][j][1] = dp[0][j-1][1] * grid[0][j]
        
#         # Fill first column
#         for i in range(1, m):
#             dp[i][0][0] = dp[i-1][0][0] * grid[i][0]
#             dp[i][0][1] = dp[i-1][0][1] * grid[i][0]
        
#         # Fill the rest of the grid
#         for i in range(1, m):
#             for j in range(1, n):
#                 if grid[i][j] >= 0:
#                     # If current cell is non-negative, maximum comes from larger previous maximum
#                     dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) * grid[i][j]
#                     dp[i][j][1] = min(dp[i-1][j][1], dp[i][j-1][1]) * grid[i][j]
#                 else:
#                     # If current cell is negative, maximum comes from smaller previous minimum
#                     dp[i][j][0] = min(dp[i-1][j][1], dp[i][j-1][1]) * grid[i][j]
#                     dp[i][j][1] = max(dp[i-1][j][0], dp[i][j-1][0]) * grid[i][j]
        
#         # Check if we can get a non-negative product
#         result = dp[m-1][n-1][0]
#         if result < 0:
#             return -1
        
#         return result % MOD



class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dfs(i, j):
            """
            Returns a tuple (max_product, min_product) for the path from (i,j) to (m-1,n-1)
            """
            # If we're at the bottom-right corner
            if i == m - 1 and j == n - 1:
                return (grid[i][j], grid[i][j])
            
            max_product = float('-inf')
            min_product = float('inf')
            
            current_val = grid[i][j]
            
            # Try moving right
            if j + 1 < n:
                right_max, right_min = dfs(i, j + 1)
                
                # Update based on current value
                if current_val >= 0:
                    max_product = max(max_product, current_val * right_max)
                    min_product = min(min_product, current_val * right_min)
                else:
                    max_product = max(max_product, current_val * right_min)
                    min_product = min(min_product, current_val * right_max)
            
            # Try moving down
            if i + 1 < m:
                down_max, down_min = dfs(i + 1, j)
                
                if current_val >= 0:
                    max_product = max(max_product, current_val * down_max)
                    min_product = min(min_product, current_val * down_min)
                else:
                    max_product = max(max_product, current_val * down_min)
                    min_product = min(min_product, current_val * down_max)
            
            return (max_product, min_product)
        
        result, _ = dfs(0, 0)
        
        if result < 0:
            return -1
        
        return result % MOD