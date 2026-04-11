class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # For each value, store (first_idx, second_idx) of last two occurrences
        # Using two variables per value in a dict
        last = {}  # value -> last_index
        second_last = {}  # value -> second_last_index
        
        min_distance = float('inf')
        
        for i, num in enumerate(nums):
            if num in last:
                # We have at least one previous occurrence
                if num in second_last:
                    # Have two previous, can form triple!
                    distance = 2 * (i - second_last[num])
                    min_distance = min(min_distance, distance)
                    # Update: shift
                    second_last[num] = last[num]
                else:
                    # Only one previous, now we have two
                    second_last[num] = last[num]
                last[num] = i
            else:
                # First occurrence
                last[num] = i
        
        return min_distance if min_distance != float('inf') else -1





# class Solution:
#     def minimumDistance(self, nums: List[int]) -> int:
#         # Track occurrences count and last two indices
#         # state[v] = (count, prev2, prev1) where prev2 is second last, prev1 is last
#         # or simpler: just track last two, use None if not enough
#         last_two = {}  # value -> (second_last_idx, last_idx) or just track differently
        
#         # Actually cleaner: track list of up to 2 most recent indices
#         recent = {}  # value -> [list of up to 2 most recent indices]
        
#         min_distance = float('inf')
        
#         for i, num in enumerate(nums):
#             if num not in recent:
#                 recent[num] = [i]
#             elif len(recent[num]) == 1:
#                 recent[num].append(i)
#             else:  # have 2 already, now have 3rd+
#                 # Can form triple with (oldest, middle, current)
#                 distance = 2 * (i - recent[num][0])
#                 min_distance = min(min_distance, distance)
#                 # Slide window: drop oldest, add current
#                 recent[num][0] = recent[num][1]
#                 recent[num][1] = i
        
#         return min_distance if min_distance != float('inf') else -1




# # from typing import List
# # from collections import defaultdict

# # class Solution:
# #     def minimumDistance(self, nums: List[int]) -> int:
# #         # Group indices by value
# #         indices_map = defaultdict(list)
# #         for i, num in enumerate(nums):
# #             indices_map[num].append(i)
        
# #         min_distance = float('inf')
        
# #         # For each value that appears at least 3 times
# #         for indices in indices_map.values():
# #             if len(indices) < 3:
# #                 continue
            
# #             # Try all consecutive triples to find minimum span
# #             # Distance for (i,j,k) where i<j<k is 2*(k-i)
# #             for i in range(len(indices) - 2):
# #                 # Take indices[i], indices[i+1], indices[i+2]
# #                 span = indices[i + 2] - indices[i]
# #                 distance = 2 * span
# #                 min_distance = min(min_distance, distance)
        
# #         return min_distance if min_distance != float('inf') else -1