# class Solution:
#     def largestSubmatrix(self, matrix: List[List[int]]) -> int:
#         if not matrix or not matrix[0]:
#             return 0
        
#         m, n = len(matrix), len(matrix[0])
#         max_area = 0
        
#         # Track the height of consecutive 1's ending at each cell
#         heights = [0] * n
        
#         for i in range(m):
#             # Update heights for current row
#             for j in range(n):
#                 if matrix[i][j] == 1:
#                     heights[j] += 1
#                 else:
#                     heights[j] = 0
            
#             # Sort heights in non-increasing order
#             sorted_heights = sorted(heights, reverse=True)
            
#             # Calculate maximum area ending at this row
#             for k in range(n):
#                 if sorted_heights[k] > 0:
#                     # Width is k+1 (since we can take columns from 0 to k)
#                     # Height is sorted_heights[k]
#                     max_area = max(max_area, sorted_heights[k] * (k + 1))
        
#         return max_area


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0] * n
        
        for i in range(m):
            # Update heights
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Create a frequency map of heights
            freq = {}
            for h in heights:
                if h > 0:  # Only consider heights > 0
                    freq[h] = freq.get(h, 0) + 1
            
            # Calculate area by considering each unique height
            # We need to know how many columns have height >= current height
            unique_heights = sorted(freq.keys(), reverse=True)
            
            cumulative_cols = 0
            for h in unique_heights:
                cumulative_cols += freq[h]  # Add columns with exactly this height
                # Now cumulative_cols represents columns with height >= current h
                area = h * cumulative_cols
                max_area = max(max_area, area)
        
        return max_area