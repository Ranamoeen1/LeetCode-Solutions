from typing import List
import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        
        # dp[(g1, g2)] stores the number of ways to have disjoint subsequences
        # with GCDs g1 and g2. An empty subsequence is represented by GCD 0.
        dp = {(0, 0): 1}
        
        for num in nums:
            # We must iterate over a copy of the current states 
            # to avoid modifying the dictionary while looping.
            next_dp = dp.copy()
            
            for (g1, g2), count in dp.items():
                # Choice 1: Add num to seq1
                new_g1 = math.gcd(g1, num) if g1 > 0 else num
                next_dp[(new_g1, g2)] = (next_dp.get((new_g1, g2), 0) + count) % MOD
                
                # Choice 2: Add num to seq2
                new_g2 = math.gcd(g2, num) if g2 > 0 else num
                next_dp[(g1, new_g2)] = (next_dp.get((g1, new_g2), 0) + count) % MOD
                
            dp = next_dp
            
        # Sum up combinations where both subsequences are non-empty (g > 0)
        # and they share the exact same GCD (g1 == g2).
        ans = sum(count for (g1, g2), count in dp.items() if g1 == g2 and g1 > 0)
        return ans % MOD




# from typing import List
# from functools import lru_cache
# import math

# class Solution:
#     def subsequencePairCount(self, nums: List[int]) -> int:
#         MOD = 1_000_000_007
#         n = len(nums)
        
#         @lru_cache(None)
#         def dp(i: int, gcd1: int, gcd2: int) -> int:
#             # Base case: reached the end of the array
#             if i == n:
#                 # Both subsequences must be non-empty (gcd > 0) and have equal GCD
#                 return 1 if (gcd1 > 0 and gcd1 == gcd2) else 0
            
#             # Choice 1: Skip the current element
#             res = dp(i + 1, gcd1, gcd2)
            
#             # Choice 2: Add nums[i] to the first subsequence
#             new_gcd1 = math.gcd(gcd1, nums[i]) if gcd1 > 0 else nums[i]
#             res = (res + dp(i + 1, new_gcd1, gcd2)) % MOD
            
#             # Choice 3: Add nums[i] to the second subsequence
#             new_gcd2 = math.gcd(gcd2, nums[i]) if gcd2 > 0 else nums[i]
#             res = (res + dp(i + 1, gcd1, new_gcd2)) % MOD
            
#             return res
        
#         # Start matching from index 0 with empty subsequences (GCD = 0)
#         return dp(0, 0, 0)