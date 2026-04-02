class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # DP array: dp[i][j][k] = max coins at cell (i,j) with k neutralizations used
        # Initialize with -inf since we want max
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Starting position
        for k in range(3):
            if k == 0:
                dp[0][0][k] = coins[0][0]
            else:
                # If we neutralize starting cell
                dp[0][0][k] = max(coins[0][0], 0)
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                # For each possible number of neutralizations used so far
                for k in range(3):
                    # Current cell value
                    val = coins[i][j]
                    
                    # Case 1: Don't neutralize current cell
                    # Can only do this if we haven't used more than k neutralizations before
                    # and we're not neutralizing this cell
                    # We need to come from top or left with exactly k neutralizations
                    if i > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
                    if j > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
                    
                    # Case 2: Neutralize current cell (if val < 0 and k > 0)
                    if k > 0 and val < 0:
                        if i > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + 0)
                        if j > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1] + 0)
                    
                    # Special case: If val >= 0 and we neutralize, it's worse than not neutralizing
                    # So we don't need to consider that separately
        
        # Return the maximum coins at bottom-right with 0, 1, or 2 neutralizations used
        return max(dp[m-1][n-1][k] for k in range(3))