from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Group indices by value
        indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            indices_map[num].append(i)
        
        min_distance = float('inf')
        
        # For each value that appears at least 3 times
        for indices in indices_map.values():
            if len(indices) < 3:
                continue
            
            # Try all consecutive triples to find minimum span
            # Distance for (i,j,k) where i<j<k is 2*(k-i)
            for i in range(len(indices) - 2):
                # Take indices[i], indices[i+1], indices[i+2]
                span = indices[i + 2] - indices[i]
                distance = 2 * span
                min_distance = min(min_distance, distance)
        
        return min_distance if min_distance != float('inf') else -1