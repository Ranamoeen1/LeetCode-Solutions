# class Solution:
#     def maximumAmount(self, coins: List[List[int]]) -> int:
#         m, n = len(coins), len(coins[0])
        
#         # DP array: dp[i][j][k] = max coins at cell (i,j) with k neutralizations used
#         # Initialize with -inf since we want max
#         dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
#         # Starting position
#         for k in range(3):
#             if k == 0:
#                 dp[0][0][k] = coins[0][0]
#             else:
#                 # If we neutralize starting cell
#                 dp[0][0][k] = max(coins[0][0], 0)
        
#         # Fill the DP table
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     continue
                
#                 # For each possible number of neutralizations used so far
#                 for k in range(3):
#                     # Current cell value
#                     val = coins[i][j]
                    
#                     # Case 1: Don't neutralize current cell
#                     # Can only do this if we haven't used more than k neutralizations before
#                     # and we're not neutralizing this cell
#                     # We need to come from top or left with exactly k neutralizations
#                     if i > 0:
#                         dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
#                     if j > 0:
#                         dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
                    
#                     # Case 2: Neutralize current cell (if val < 0 and k > 0)
#                     if k > 0 and val < 0:
#                         if i > 0:
#                             dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + 0)
#                         if j > 0:
#                             dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1] + 0)
                    
#                     # Special case: If val >= 0 and we neutralize, it's worse than not neutralizing
#                     # So we don't need to consider that separately
        
#         # Return the maximum coins at bottom-right with 0, 1, or 2 neutralizations used
#         return max(dp[m-1][n-1][k] for k in range(3))


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # DP for current row: dp[k][j] = max coins at column j with k neutralizations used
        # Initialize with negative infinity
        prev = [[-float('inf')] * n for _ in range(3)]
        
        # Handle first row specially
        for j in range(n):
            for k in range(3):
                if j == 0:
                    # Starting cell (0,0)
                    if k == 0:
                        prev[k][j] = coins[0][0]
                    else:
                        prev[k][j] = max(coins[0][0], 0)
                else:
                    val = coins[0][j]
                    # Come from left
                    if k == 0:
                        prev[k][j] = prev[0][j-1] + val
                    else:
                        # Option 1: Don't neutralize current
                        prev[k][j] = prev[k][j-1] + val
                        # Option 2: Neutralize current (if val < 0)
                        if val < 0:
                            prev[k][j] = max(prev[k][j], prev[k-1][j-1] + 0)
        
        # Process remaining rows
        for i in range(1, m):
            # Current row DP
            curr = [[-float('inf')] * n for _ in range(3)]
            
            for j in range(n):
                val = coins[i][j]
                
                for k in range(3):
                    # Come from top (previous row, same column)
                    if k == 0:
                        curr[k][j] = max(curr[k][j], prev[k][j] + val)
                    else:
                        # Don't neutralize current
                        curr[k][j] = max(curr[k][j], prev[k][j] + val)
                        # Neutralize current
                        if val < 0:
                            curr[k][j] = max(curr[k][j], prev[k-1][j] + 0)
                    
                    # Come from left (same row, previous column)
                    if j > 0:
                        if k == 0:
                            curr[k][j] = max(curr[k][j], curr[k][j-1] + val)
                        else:
                            # Don't neutralize current
                            curr[k][j] = max(curr[k][j], curr[k][j-1] + val)
                            # Neutralize current
                            if val < 0:
                                curr[k][j] = max(curr[k][j], curr[k-1][j-1] + 0)
            
            prev = curr
        
        # Return maximum at bottom-right with 0, 1, or 2 neutralizations
        return max(prev[k][n-1] for k in range(3))