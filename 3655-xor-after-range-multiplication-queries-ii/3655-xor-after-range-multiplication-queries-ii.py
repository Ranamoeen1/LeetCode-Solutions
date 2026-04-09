import math
from typing import List
from collections import defaultdict

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = int(math.isqrt(n)) + 1
        
        multipliers = [1] * n
        
        # Separate queries by k value
        small_queries = [[] for _ in range(B + 1)]  # index by k
        large_queries = []
        
        for l, r, k, v in queries:
            if k <= B:
                small_queries[k].append((l, r, v))
            else:
                large_queries.append((l, r, k, v))
        
        # Process large k directly - each affects at most n/B elements
        for l, r, k, v in large_queries:
            idx = l
            while idx <= r:
                multipliers[idx] = (multipliers[idx] * v) % MOD
                idx += k
        
        # Process small k using sweep line with difference arrays
        for k in range(1, B + 1):
            if not small_queries[k]:
                continue
            
            # Group events by remainder
            events = defaultdict(list)  # rem -> list of (compressed_idx, mult_delta)
            
            for l, r, v in small_queries[k]:
                rem = l % k
                j_start = l // k
                j_end = (r - rem) // k
                
                # Range multiply by v: apply v at start, v^{-1} after end
                events[rem].append((j_start, v))
                events[rem].append((j_end + 1, pow(v, MOD - 2, MOD)))
            
            # Process each remainder group
            for rem, evt_list in events.items():
                if rem >= n:
                    continue
                    
                evt_list.sort()
                max_j = (n - 1 - rem) // k
                
                curr_mult = 1
                evt_idx = 0
                for j in range(max_j + 1):
                    # Apply all events at position j
                    while evt_idx < len(evt_list) and evt_list[evt_idx][0] == j:
                        curr_mult = (curr_mult * evt_list[evt_idx][1]) % MOD
                        evt_idx += 1
                    
                    i = rem + j * k
                    multipliers[i] = (multipliers[i] * curr_mult) % MOD
        
        # Compute final XOR
        ans = 0
        for i in range(n):
            ans ^= (nums[i] * multipliers[i]) % MOD
        
        return ans