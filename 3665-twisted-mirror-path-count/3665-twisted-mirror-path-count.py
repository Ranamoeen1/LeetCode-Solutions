class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(grid[0])
        
        # dp[c+1] stores [paths_from_above, paths_from_left] for column c
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1] = [1, 1]
        
        for r in range(len(grid)):
            for c in range(n):
                if grid[r][c] == 1:
                    # Mirrors swap the path counts
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    # Empty cells add and distribute path counts
                    val = (dp[c + 1][1] + dp[c][0]) % MOD
                    dp[c + 1] = [val, val]
                    
        return dp[n][0]