# # # from typing import List
# # # from collections import defaultdict
# # # import bisect

# # # class Solution:
# # #     def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
# # #         n = len(nums)
        
# # #         # Group indices by value
# # #         value_indices = defaultdict(list)
# # #         for i, num in enumerate(nums):
# # #             value_indices[num].append(i)
        
# # #         results = []
        
# # #         for query in queries:
# # #             val = nums[query]
# # #             indices = value_indices[val]
            
# # #             # If this value appears only once, answer is -1
# # #             if len(indices) == 1:
# # #                 results.append(-1)
# # #                 continue
            
# # #             # Find position of query index in the sorted list
# # #             pos = bisect.bisect_left(indices, query)
            
      
# # #             prev_idx = indices[(pos - 1) % len(indices)]
# # #             next_idx = indices[(pos + 1) % len(indices)]
            
# # #             # Calculate circular distances
# # #             dist_prev = min(abs(query - prev_idx), n - abs(query - prev_idx))
# # #             dist_next = min(abs(query - next_idx), n - abs(query - next_idx))
            
# # #             # Take the minimum distance
# # #             min_dist = min(dist_prev, dist_next)
# # #             results.append(min_dist)
        
# # #         return results


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

# from typing import List
# from collections import defaultdict

# class Solution:
#     def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         n = len(nums)
        
#         # Track next occurrence to the right
#         next_occurrence = [-1] * n
#         last_seen = {}
        
#         # First pass: find next occurrence to the right
#         for i in range(n):
#             val = nums[i]
#             if val in last_seen:
#                 prev_idx = last_seen[val]
#                 next_occurrence[prev_idx] = i
#             last_seen[val] = i
        
#         # Second pass: handle circular wrap by checking from start
#         # For indices that didn't find a next occurrence to the right,
#         # look from the beginning
#         for val, last_idx in last_seen.items():
#             # Find first occurrence of this value
#             first_idx = -1
#             for i in range(n):
#                 if nums[i] == val:
#                     first_idx = i
#                     break
            
#             if first_idx != -1 and next_occurrence[last_idx] == -1:
#                 # Last occurrence connects to first occurrence circularly
#                 next_occurrence[last_idx] = first_idx
        
#         # Track previous occurrence to the left (for circular distance)
#         prev_occurrence = [-1] * n
#         last_seen = {}
        
#         for i in range(n - 1, -1, -1):
#             val = nums[i]
#             if val in last_seen:
#                 next_idx = last_seen[val]
#                 prev_occurrence[next_idx] = i
#             last_seen[val] = i
        
#         # Handle circular wrap for previous occurrences
#         for val, first_idx in last_seen.items():
#             # Find last occurrence of this value
#             last_idx = -1
#             for i in range(n - 1, -1, -1):
#                 if nums[i] == val:
#                     last_idx = i
#                     break
            
#             if last_idx != -1 and prev_occurrence[first_idx] == -1:
#                 # First occurrence connects to last occurrence circularly
#                 prev_occurrence[first_idx] = last_idx
        
#         # Calculate answers
#         result = [-1] * n
        
#         for i in range(n):
#             min_dist = float('inf')
            
#             if next_occurrence[i] != -1:
#                 # Distance to next occurrence (going right)
#                 dist_right = next_occurrence[i] - i
#                 # Also consider wrapping around from i to next_occurrence[i]
#                 dist_wrap = n - dist_right
#                 min_dist = min(min_dist, dist_right, dist_wrap)
            
#             if prev_occurrence[i] != -1:
#                 # Distance to previous occurrence (going left)
#                 dist_left = i - prev_occurrence[i]
#                 dist_wrap = n - dist_left
#                 min_dist = min(min_dist, dist_left, dist_wrap)
            
#             if min_dist != float('inf'):
#                 result[i] = min_dist
        
#         return [result[q] for q in queries]