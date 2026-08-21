import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Helper function to count distinct multiples <= target using Inclusion-Exclusion
        def count_multiples(target: int) -> int:
            total_count = 0
            # Iterate through all non-empty subsets of coins
            for mask in range(1, 1 << n):
                lcm_val = 1
                bits_set = 0
                for i in range(n):
                    if (mask >> i) & 1:
                        bits_set += 1
                        lcm_val = math.lcm(lcm_val, coins[i])
                        # Early exit if LCM exceeds target
                        if lcm_val > target:
                            break
                
                if lcm_val <= target:
                    if bits_set % 2 == 1:
                        total_count += target // lcm_val
                    else:
                        total_count -= target // lcm_val
                        
            return total_count

        # Binary search range
        left = 1
        right = min(coins) * k
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if count_multiples(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans