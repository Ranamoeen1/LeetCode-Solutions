from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        # Group indices by value
        value_indices = defaultdict(list)
        for i, num in enumerate(nums):
            value_indices[num].append(i)
        
        results = []
        
        for query in queries:
            val = nums[query]
            indices = value_indices[val]
            
            # If this value appears only once, answer is -1
            if len(indices) == 1:
                results.append(-1)
                continue
            
            # Find position of query index in the sorted list
            pos = bisect.bisect_left(indices, query)
            
      
            prev_idx = indices[(pos - 1) % len(indices)]
            next_idx = indices[(pos + 1) % len(indices)]
            
            # Calculate circular distances
            dist_prev = min(abs(query - prev_idx), n - abs(query - prev_idx))
            dist_next = min(abs(query - next_idx), n - abs(query - next_idx))
            
            # Take the minimum distance
            min_dist = min(dist_prev, dist_next)
            results.append(min_dist)
        
        return results