from typing import List
from functools import lru_cache
import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        
        @lru_cache(None)
        def dp(i: int, gcd1: int, gcd2: int) -> int:
            # Base case: reached the end of the array
            if i == n:
                # Both subsequences must be non-empty (gcd > 0) and have equal GCD
                return 1 if (gcd1 > 0 and gcd1 == gcd2) else 0
            
            # Choice 1: Skip the current element
            res = dp(i + 1, gcd1, gcd2)
            
            # Choice 2: Add nums[i] to the first subsequence
            new_gcd1 = math.gcd(gcd1, nums[i]) if gcd1 > 0 else nums[i]
            res = (res + dp(i + 1, new_gcd1, gcd2)) % MOD
            
            # Choice 3: Add nums[i] to the second subsequence
            new_gcd2 = math.gcd(gcd2, nums[i]) if gcd2 > 0 else nums[i]
            res = (res + dp(i + 1, gcd1, new_gcd2)) % MOD
            
            return res
        
        # Start matching from index 0 with empty subsequences (GCD = 0)
        return dp(0, 0, 0)