from typing import List
import bisect

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Find the maximum possible coordinate across all queries
        max_x = max(q[1] for q in queries) + 1
        
        # Iterative Segment Tree size (power of 2 greater than max_x for safety)
        n = 1
        while n < max_x + 1:
            n *= 2
            
        tree = [0] * (2 * n)
        
        def update(i, val):
            i += n
            tree[i] = val
            i //= 2
            while i > 0:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i //= 2
                
        def query(l, r):
            res = 0
            l += n
            r += n
            while l <= r:
                if l % 2 == 1:
                    res = max(res, tree[l])
                    l += 1
                if r % 2 == 0:
                    res = max(res, tree[r])
                    r -= 1
                l //= 2
                r //= 2
            return res

        # Track active obstacles
        obstacles = [0, max_x]
        update(max_x, max_x)
        
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_left(obstacles, x)
                left = obstacles[idx - 1]
                right = obstacles[idx]
                
                # Using list.insert is perfectly fine here because N is very small 
                # and the iterative tree eliminates recursion overhead entirely.
                obstacles.insert(idx, x)
                
                update(x, x - left)
                update(right, right - x)
                
            elif q[0] == 2:
                x = q[1]
                sz = q[2]
                
                idx = bisect.bisect_left(obstacles, x)
                left = obstacles[idx - 1]
                
                # Check the gap between the last obstacle before x, and x itself
                max_gap = x - left
                
                # Query the maximum complete gap to the left of the 'left' obstacle
                if left > 0:
                    max_gap = max(max_gap, query(0, left))
                    
                results.append(max_gap >= sz)
                
        return results





# import bisect
# from typing import List

# class SegmentTree:
#     def __init__(self, size):
#         self.n = size
#         self.tree = [0] * (4 * size)

#     def update(self, node, start, end, idx, val):
#         if start == end:
#             self.tree[node] = val
#             return
#         mid = (start + end) // 2
#         if idx <= mid:
#             self.update(2 * node, start, mid, idx, val)
#         else:
#             self.update(2 * node + 1, mid + 1, end, idx, val)
#         self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

#     def query(self, node, start, end, l, r):
#         if l > end or r < start:
#             return 0
#         if l <= start and end <= r:
#             return self.tree[node]
#         mid = (start + end) // 2
#         p1 = self.query(2 * node, start, mid, l, r)
#         p2 = self.query(2 * node + 1, mid + 1, end, l, r)
#         return max(p1, p2)

# class Solution:
#     def getResults(self, queries: List[List[int]]) -> List[bool]:
#         # Determine the maximum coordinate boundary dynamically based on constraints
#         max_x = 0
#         for q in queries:
#             max_x = max(max_x, q[1])
        
#         # Add a small buffer to avoid out-of-bounds
#         max_x += 2
        
#         # Obstacles list initialized with boundaries 0 and a practical infinity
#         # using max_x as the rightmost boundary
#         obstacles = [0, max_x]
        
#         seg_tree = SegmentTree(max_x + 1)
#         # Initially, there is one giant gap from 0 to max_x
#         seg_tree.update(1, 0, max_x, max_x, max_x)
        
#         results = []
        
#         for q in queries:
#             if q[0] == 1:
#                 x = q[1]
#                 # Find where x fits among existing obstacles
#                 idx = bisect.bisect_left(obstacles, x)
#                 left = obstacles[idx - 1]
#                 right = obstacles[idx]
                
#                 # Insert x into our sorted obstacles
#                 obstacles.insert(idx, x)
                
#                 # Update segment tree gaps
#                 # The old gap was (right - left) stored at 'right'
#                 # The new gaps are (x - left) stored at 'x', and (right - x) stored at 'right'
#                 seg_tree.update(1, 0, max_x, x, x - left)
#                 seg_tree.update(1, 0, max_x, right, right - x)
                
#             elif q[0] == 2:
#                 x = q[1]
#                 sz = q[2]
                
#                 # Find the closest obstacle to the left of x
#                 idx = bisect.bisect_left(obstacles, x)
#                 left = obstacles[idx - 1]
                
#                 # Check the partial trailing block from the last obstacle up to x
#                 max_gap = x - left
                
#                 # Query the segment tree for the maximum complete gap in [0, left]
#                 if left > 0:
#                     max_gap = max(max_gap, seg_tree.query(1, 0, max_x, 0, left))
                
#                 results.append(max_gap >= sz)
                
#         return results