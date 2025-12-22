class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 0:
            return 0
        m = len(strs[0])
        dp = [1] * m
        for i in range(m):
            for j in range(i):
                can_precede = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        can_precede = False
                        break
                if can_precede:
                    dp[i] = max(dp[i], dp[j] + 1)
        return m - max(dp)
