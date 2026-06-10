from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Precompute a Sparse Table or use a Segment Tree for O(1) or O(log n) range max/min queries.
        # Since we just want to expand/shrink boundaries, we can compute max/min of a range dynamically, 
        # but to keep it fast, a simple RMQ (Range Minimum/Maximum Query) via Sparse Table is perfect.
        
        # 1. Build Sparse Tables for Range Maximum and Range Minimum
        K = n.bit_length()
        st_max = [[0] * K for _ in range(n)]
        st_min = [[0] * K for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, K):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
                
        def get_val(l, r):
            if l > r:
                return -1
            j = (r - l + 1).bit_length() - 1
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            return mx - mn

        # 2. Max-Heap to greedily pick the largest distinct subarrays
        # Start with the full array [0, n-1]
        # Store as (-value, l, r) because Python's heapq is a min-heap by default
        max_heap = [(-get_val(0, n - 1), 0, n - 1)]
        visited = {(0, n - 1)}
        
        total_value = 0
        count = 0
        
        while max_heap and count < k:
            neg_val, l, r = heapq.heappop(max_heap)
            total_value += -neg_val
            count += 1
            
            # Generate next best candidates by shrinking boundaries
            if l < r:
                if (l + 1, r) not in visited:
                    visited.add((l + 1, r))
                    heapq.heappush(max_heap, (-get_val(l + 1, r), l + 1, r))
                if (l, r - 1) not in visited:
                    visited.add((l, r - 1))
                    heapq.heappush(max_heap, (-get_val(l, r - 1), l, r - 1))
                    
        return total_value