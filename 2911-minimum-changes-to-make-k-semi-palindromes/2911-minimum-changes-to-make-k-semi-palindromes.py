class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # cost[i][j] stores the minimum changes to make substring s[i...j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        def get_changes(i, j, d):
            changes = 0
            for offset in range(d):
                l = i + offset
                r = j - d + 1 + offset
                while l < r:
                    if s[l] != s[r]:
                        changes += 1
                    l += d
                    r -= d
            return changes

        # Precompute costs for all substrings of length >= 2
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                min_c = float('inf')
                for d in range(1, length):
                    if length % d == 0:
                        min_c = min(min_c, get_changes(i, j, d))
                cost[i][j] = min_c

        # DP table: dp[i][p] = min changes to partition prefix s[0...i] into p parts
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][1] = cost[0][i]
            
        for p in range(2, k + 1):
            for i in range(p - 1, n):
                for j in range(p - 2, i):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j + 1][i])
                    
        return dp[n - 1][k]