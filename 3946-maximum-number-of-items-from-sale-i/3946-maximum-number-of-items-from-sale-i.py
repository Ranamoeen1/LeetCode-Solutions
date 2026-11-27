class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)

        # Count how many other items have a factor divisible by items[i]'s factor
        gains = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            gains[i] = cnt

        # 0/1 DP over budget: max copies from activating a subset of items
        dp = [0] * (budget + 1)
        for i in range(n):
            price = items[i][1]
            value = 1 + gains[i]
            for c in range(budget, price - 1, -1):
                if dp[c - price] + value > dp[c]:
                    dp[c] = dp[c - price] + value

        # Spend remaining budget on the cheapest item for extra copies
        ans = 0
        for c in range(budget + 1):
            extra = (budget - c) // min_price
            ans = max(ans, dp[c] + extra)

        return ans