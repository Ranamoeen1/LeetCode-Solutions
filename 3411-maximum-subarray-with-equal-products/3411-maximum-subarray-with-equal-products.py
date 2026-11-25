import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # Max LCM of numbers in [1..10] is 2520; max GCD is 10
        max_rhs = 2520 * 10
        ans = 2  # Every subarray of length 2 satisfies prod == lcm * gcd

        for i in range(n):
            curr_prod = nums[i]
            curr_gcd = nums[i]
            curr_lcm = nums[i]

            for j in range(i + 1, n):
                val = nums[j]
                curr_prod *= val
                if curr_prod > max_rhs:
                    break

                curr_gcd = math.gcd(curr_gcd, val)
                curr_lcm = math.lcm(curr_lcm, val)

                if curr_prod == curr_lcm * curr_gcd:
                    ans = max(ans, j - i + 1)

        return ans