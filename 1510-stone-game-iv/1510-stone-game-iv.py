class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] will store whether the player whose turn it is can win with i stones left
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                # If removing k^2 stones leaves a losing state for the next player,
                # then the current player wins from state i.
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1
                
        return dp[n]