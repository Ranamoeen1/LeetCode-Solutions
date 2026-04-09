class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = int(math.isqrt(n)) + 1
        
        multipliers = [1] * n
        
        # Group by k value
        by_k = {}
        for l, r, k, v in queries:
            if k not in by_k:
                by_k[k] = []
            by_k[k].append((l, r, v))
        
        # Process each k
        for k, qlist in by_k.items():
            if k > B:
                # Large k: direct processing, O(n/k) per query
                for l, r, v in qlist:
                    idx = l
                    while idx <= r:
                        multipliers[idx] = (multipliers[idx] * v) % MOD
                        idx += k
            else:
                # Small k: use diff array approach, O(n) total for this k
                max_j = (n - 1) // k + 2
                
                # Group by remainder
                from collections import defaultdict
                by_rem = defaultdict(lambda: [1] * max_j)
                
                for l, r, v in qlist:
                    rem = l % k
                    js, je = l // k, (r - rem) // k
                    v_inv = pow(v, MOD - 2, MOD)
                    by_rem[rem][js] = (by_rem[rem][js] * v) % MOD
                    if je + 1 < max_j:
                        by_rem[rem][je + 1] = (by_rem[rem][je + 1] * v_inv) % MOD
                
                # Apply prefix products
                for rem, diff in by_rem.items():
                    if rem >= n:
                        continue
                    cur, max_pos = 1, (n - 1 - rem) // k
                    for j in range(max_pos + 1):
                        cur = (cur * diff[j]) % MOD
                        multipliers[rem + j * k] = (multipliers[rem + j * k] * cur) % MOD
        
        # Final XOR
        ans = 0
        for i in range(n):
            ans ^= (nums[i] * multipliers[i]) % MOD
        
        return ans



# import math
# from typing import List
# from collections import defaultdict

# class Solution:
#     def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
#         MOD = 10**9 + 7
#         n = len(nums)
#         B = int(math.isqrt(n)) + 1
        
#         multipliers = [1] * n
        
#         # Separate queries by k value
#         small_queries = [[] for _ in range(B + 1)]  # index by k
#         large_queries = []
        
#         for l, r, k, v in queries:
#             if k <= B:
#                 small_queries[k].append((l, r, v))
#             else:
#                 large_queries.append((l, r, k, v))
        
#         # Process large k directly - each affects at most n/B elements
#         for l, r, k, v in large_queries:
#             idx = l
#             while idx <= r:
#                 multipliers[idx] = (multipliers[idx] * v) % MOD
#                 idx += k
        
#         # Process small k using sweep line with difference arrays
#         for k in range(1, B + 1):
#             if not small_queries[k]:
#                 continue
            
#             # Group events by remainder
#             events = defaultdict(list)  # rem -> list of (compressed_idx, mult_delta)
            
#             for l, r, v in small_queries[k]:
#                 rem = l % k
#                 j_start = l // k
#                 j_end = (r - rem) // k
                
#                 # Range multiply by v: apply v at start, v^{-1} after end
#                 events[rem].append((j_start, v))
#                 events[rem].append((j_end + 1, pow(v, MOD - 2, MOD)))
            
#             # Process each remainder group
#             for rem, evt_list in events.items():
#                 if rem >= n:
#                     continue
                    
#                 evt_list.sort()
#                 max_j = (n - 1 - rem) // k
                
#                 curr_mult = 1
#                 evt_idx = 0
#                 for j in range(max_j + 1):
#                     # Apply all events at position j
#                     while evt_idx < len(evt_list) and evt_list[evt_idx][0] == j:
#                         curr_mult = (curr_mult * evt_list[evt_idx][1]) % MOD
#                         evt_idx += 1
                    
#                     i = rem + j * k
#                     multipliers[i] = (multipliers[i] * curr_mult) % MOD
        
#         # Compute final XOR
#         ans = 0
#         for i in range(n):
#             ans ^= (nums[i] * multipliers[i]) % MOD
        
#         return ans