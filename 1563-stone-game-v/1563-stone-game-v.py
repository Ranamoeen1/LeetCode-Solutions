class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0

        # Compute prefix sums for O(1) range sum queries
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        # Base cases for single stone ranges
        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]

        # Fill DP table from bottom to top
        for i in range(n - 1, -1, -1):
            mid = i
            for j in range(i + 1, n):
                # If even the smallest left split is greater than right sum, no L(k) <= R(k) exists
                if pref[i + 1] - pref[i] > pref[j + 1] - pref[i + 1]:
                    dp[i][j] = maxR[i + 1][j]
                else:
                    # Advance mid to the largest index where L(mid) <= R(mid)
                    while (
                        mid + 1 < j
                        and pref[mid + 2] - pref[i]
                        <= pref[j + 1] - pref[mid + 2]
                    ):
                        mid += 1

                    L_mid = pref[mid + 1] - pref[i]
                    R_mid = pref[j + 1] - pref[mid + 1]

                    if L_mid == R_mid:
                        dp[i][j] = max(maxL[i][mid], maxR[mid + 1][j])
                    else:  # L_mid < R_mid
                        ans = maxL[i][mid]
                        if mid + 2 <= j:
                            ans = max(ans, maxR[mid + 2][j])
                        dp[i][j] = ans

                # Update maxL and maxR helper matrices
                maxL[i][j] = max(
                    maxL[i][j - 1], pref[j + 1] - pref[i] + dp[i][j]
                )
                maxR[i][j] = max(
                    maxR[i + 1][j], pref[j + 1] - pref[i] + dp[i][j]
                )

        return dp[0][n - 1]