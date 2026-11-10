class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for k in range(1, 4):
                if i - k >= 0:
                    cost = dp[i - k] + costs[i - 1] + k * k
                    if cost < dp[i]:
                        dp[i] = cost
                        
        return dp[n]