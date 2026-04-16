# from typing import List
# from collections import defaultdict
# import bisect

# class Solution:
#     def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         n = len(nums)
        
#         # Group indices by value
#         value_indices = defaultdict(list)
#         for i, num in enumerate(nums):
#             value_indices[num].append(i)
        
#         results = []
        
#         for query in queries:
#             val = nums[query]
#             indices = value_indices[val]
            
#             # If this value appears only once, answer is -1
#             if len(indices) == 1:
#                 results.append(-1)
#                 continue
            
#             # Find position of query index in the sorted list
#             pos = bisect.bisect_left(indices, query)
            
      
#             prev_idx = indices[(pos - 1) % len(indices)]
#             next_idx = indices[(pos + 1) % len(indices)]
            
#             # Calculate circular distances
#             dist_prev = min(abs(query - prev_idx), n - abs(query - prev_idx))
#             dist_next = min(abs(query - next_idx), n - abs(query - next_idx))
            
#             # Take the minimum distance
#             min_dist = min(dist_prev, dist_next)
#             results.append(min_dist)
        
#         return results


from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        # Group indices by value
        value_indices = defaultdict(list)
        for i, num in enumerate(nums):
            value_indices[num].append(i)
        
        # Precompute answer for all indices
        answer = [-1] * n
        
        # For each value that appears more than once
        for val, indices in value_indices.items():
            if len(indices) < 2:
                continue
            
            m = len(indices)
            
            # For each occurrence, find distances to previous and next
            for i in range(m):
                curr_idx = indices[i]
                
                # Previous index in circular list of occurrences
                prev_idx = indices[(i - 1) % m]
                # Next index in circular list of occurrences
                next_idx = indices[(i + 1) % m]
                
                # Calculate circular distances
                # Distance to previous: min(direct, wrapped)
                dist_prev = min(abs(curr_idx - prev_idx), n - abs(curr_idx - prev_idx))
                # Distance to next: min(direct, wrapped)
                dist_next = min(abs(curr_idx - next_idx), n - abs(curr_idx - next_idx))
                
                # Store the minimum distance
                answer[curr_idx] = min(dist_prev, dist_next)
        
        # Return answers only for queried indices
        return [answer[q] for q in queries]