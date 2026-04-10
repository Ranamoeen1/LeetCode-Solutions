class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        min_dist = float('inf')
        
        for idx_list in indices.values():
            if len(idx_list) >= 3:
                # Sliding window of size 3 on the index list
                for i in range(len(idx_list) - 2):
                    window_span = idx_list[i + 2] - idx_list[i]
                    min_dist = min(min_dist, 2 * window_span)
        
        return -1 if min_dist == float('inf') else min_dist



# class Solution:
#     def minimumDistance(self, nums: List[int]) -> int:
#         # Group indices by value
#         indices = defaultdict(list)
#         for i, num in enumerate(nums):
#             indices[num].append(i)
        
#         min_dist = float('inf')
        
#         # For each value with 3+ occurrences
#         for idx_list in indices.values():
#             if len(idx_list) >= 3:
#                 # Check all consecutive triplets
#                 # Distance for (i,j,k) where i<j<k is 2*(k-i)
#                 for i in range(len(idx_list) - 2):
#                     # Use indices[i], indices[i+1], indices[i+2]
#                     dist = 2 * (idx_list[i + 2] - idx_list[i])
#                     min_dist = min(min_dist, dist)
        
#         return min_dist if min_dist != float('inf') else -1