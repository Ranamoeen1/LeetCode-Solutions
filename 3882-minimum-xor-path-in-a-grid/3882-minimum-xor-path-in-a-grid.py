class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] stores a bitmask of all possible XOR values reachable at cell (i, j)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 << grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                prev_mask = 0
                if i > 0:
                    prev_mask |= dp[i - 1][j]
                if j > 0:
                    prev_mask |= dp[i][j - 1]
                
                v = grid[i][j]
                curr_mask = 0
                
                # Optimized bit iteration: only loop through actually set bits
                mask = prev_mask
                while mask:
                    low_bit = mask & -mask
                    x = low_bit.bit_length() - 1
                    curr_mask |= (1 << (x ^ v))
                    mask &= mask - 1  # Clear the lowest set bit
                    
                dp[i][j] = curr_mask
                
        # Find the minimum XOR value instantly using the lowest set bit
        final_mask = dp[m - 1][n - 1]
        return (final_mask & -final_mask).bit_length() - 1




# class Solution:
#     def minCost(self, grid: list[list[int]]) -> int:
#         m, n = len(grid), len(grid[0])
        
#         # dp[i][j] will store a bitmask of all possible XOR values at cell (i, j)
#         dp = [[0] * n for _ in range(m)]
#         dp[0][0] = 1 << grid[0][0]
        
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     continue
                
#                 prev_mask = 0
#                 if i > 0:
#                     prev_mask |= dp[i - 1][j]
#                 if j > 0:
#                     prev_mask |= dp[i][j - 1]
                
#                 v = grid[i][j]
#                 curr_mask = 0
                
#                 # Iterate through all possible XOR values (0 to 1023)
#                 for x in range(1024):
#                     if (prev_mask & (1 << x)):
#                         curr_mask |= (1 << (x ^ v))
                        
#                 dp[i][j] = curr_mask
                
#         # Find the minimum XOR value present in the bottom-right cell's mask
#         final_mask = dp[m - 1][n - 1]
#         for x in range(1024):
#             if (final_mask & (1 << x)):
#                 return x
                
#         return 0