from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        # Dictionary to store indices for each value
        index_map = defaultdict(list)
        
        # Group indices by their values
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        # Process each group of indices
        for indices in index_map.values():
            m = len(indices)
            if m == 1:
                continue
            
            # Calculate prefix sums
            prefix_sum = [0] * m
            prefix_sum[0] = indices[0]
            for i in range(1, m):
                prefix_sum[i] = prefix_sum[i-1] + indices[i]
            
            # Calculate distances for each index in the group
            for i, idx in enumerate(indices):
                # Sum of distances to previous indices
                left_sum = indices[i] * i - (prefix_sum[i-1] if i > 0 else 0)
                # Sum of distances to next indices
                right_sum = (prefix_sum[m-1] - prefix_sum[i]) - indices[i] * (m - i - 1)
                result[idx] = left_sum + right_sum
        
        return result