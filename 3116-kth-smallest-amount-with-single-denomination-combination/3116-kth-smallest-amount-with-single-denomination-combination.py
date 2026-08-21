import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Optimization 1: Remove redundant coins that are multiples of smaller coins
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % prev == 0 for prev in filtered_coins):
                filtered_coins.append(c)
        
        coins = filtered_coins
        n = len(coins)

        # Optimization 2: Fast Inclusion-Exclusion with DFS and Early Pruning
        def count_multiples(target: int) -> int:
            total_count = 0

            def dfs(index: int, count: int, current_lcm: int):
                nonlocal total_count
                for i in range(index, n):
                    next_lcm = math.lcm(current_lcm, coins[i])
                    # Prune branch early if LCM exceeds target
                    if next_lcm > target:
                        continue
                    
                    # Add/Subtract contribution based on subset size parity
                    if count % 2 == 1:
                        total_count += target // next_lcm
                    else:
                        total_count -= target // next_lcm

                    dfs(i + 1, count + 1, next_lcm)

            dfs(0, 1, 1)
            return total_count

        # Binary search bounds
        left = 1
        right = coins[0] * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_multiples(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans




# import math
# from typing import List

# class Solution:
#     def findKthSmallest(self, coins: List[int], k: int) -> int:
#         n = len(coins)
        
#         # Helper function to count distinct multiples <= target using Inclusion-Exclusion
#         def count_multiples(target: int) -> int:
#             total_count = 0
#             # Iterate through all non-empty subsets of coins
#             for mask in range(1, 1 << n):
#                 lcm_val = 1
#                 bits_set = 0
#                 for i in range(n):
#                     if (mask >> i) & 1:
#                         bits_set += 1
#                         lcm_val = math.lcm(lcm_val, coins[i])
#                         # Early exit if LCM exceeds target
#                         if lcm_val > target:
#                             break
                
#                 if lcm_val <= target:
#                     if bits_set % 2 == 1:
#                         total_count += target // lcm_val
#                     else:
#                         total_count -= target // lcm_val
                        
#             return total_count

#         # Binary search range
#         left = 1
#         right = min(coins) * k
#         ans = right
        
#         while left <= right:
#             mid = (left + right) // 2
#             if count_multiples(mid) >= k:
#                 ans = mid
#                 right = mid - 1
#             else:
#                 left = mid + 1
                
#         return ans