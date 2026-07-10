from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Get sorted unique values
        unique_vals = sorted(list(set(nums)))
        m = len(unique_vals)
        
        # Determine the max bits needed for binary lifting
        MAX_LOG = 17  # since n <= 10^5, 2^17 = 131072 > 10^5
        
        # up[i][j] stores the index reached from unique_vals[j] after 2^i optimal steps
        up = [[0] * m for _ in range(MAX_LOG)]
        
        # Step 2: Initialize the base cases for binary lifting (2^0 = 1 step)
        for i in range(m):
            limit = unique_vals[i] + maxDiff
            # Find the largest value <= unique_vals[i] + maxDiff
            idx = bisect_right(unique_vals, limit) - 1
            up[0][i] = idx
            
        # Step 3: Populate the binary lifting table
        for i in range(1, MAX_LOG):
            for j in range(m):
                up[i][j] = up[i-1][up[i-1][j]]
                
        # Step 4: Process each query
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u, val_v = nums[u], nums[v]
            if val_u == val_v:
                ans.append(1)
                continue
                
            # Find corresponding indices in the unique sorted array
            idx_u = bisect_left(unique_vals, val_u)
            idx_v = bisect_left(unique_vals, val_v)
            
            # Ensure we always move from left to right (smaller to larger value)
            if idx_u > idx_v:
                idx_u, idx_v = idx_v, idx_u
                
            steps = 0
            curr = idx_u
            
            # Lift greedily using binary powers
            for i in range(MAX_LOG - 1, -1, -1):
                if up[i][curr] < idx_v and up[i][curr] > curr:
                    curr = up[i][curr]
                    steps += (1 << i)
            
            # Final check to see if we can reach the target destination in one last step
            if curr < idx_v:
                if up[0][curr] >= idx_v:
                    steps += 1
                else:
                    steps = -1
                    
            ans.append(steps)
            
        return ans