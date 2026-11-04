from typing import List
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        costs = [0] * (n - x + 1)
        
        left = SortedList()
        right = SortedList()
        left_sum = 0
        right_sum = 0
        
        def balance():
            nonlocal left_sum, right_sum
            target_left = (x + 1) // 2
            while len(left) > target_left:
                v = left[-1]
                left.remove(v)
                left_sum -= v
                right.add(v)
                right_sum += v
            while len(left) < target_left and right:
                v = right[0]
                right.remove(v)
                right_sum -= v
                left.add(v)
                left_sum += v

        for i in range(n):
            v = nums[i]
            if not left or v <= left[-1]:
                left.add(v)
                left_sum += v
            else:
                right.add(v)
                right_sum += v
            
            if i >= x:
                rem = nums[i - x]
                if rem in left:
                    left.remove(rem)
                    left_sum -= rem
                else:
                    right.remove(rem)
                    right_sum -= rem
            
            if i >= x - 1:
                balance()
                median = left[-1]
                cost = len(left) * median - left_sum + right_sum - len(right) * median
                costs[i - x + 1] = cost

        # DP to select k non-overlapping subarrays of size x with minimum total cost
        dp = [0] * (n + 1)
        
        for _ in range(k):
            next_dp = [float('inf')] * (n + 1)
            min_prev = float('inf')
            for i in range(x, n + 1):
                p = i - x
                if dp[p] != float('inf'):
                    min_prev = min(min_prev, dp[p] + costs[p])
                next_dp[i] = min_prev
            dp = next_dp
            
        return dp[n]