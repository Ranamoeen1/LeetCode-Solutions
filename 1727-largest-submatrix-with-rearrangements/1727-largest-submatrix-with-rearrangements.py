class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # Track the height of consecutive 1's ending at each cell
        heights = [0] * n
        
        for i in range(m):
            # Update heights for current row
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Sort heights in non-increasing order
            sorted_heights = sorted(heights, reverse=True)
            
            # Calculate maximum area ending at this row
            for k in range(n):
                if sorted_heights[k] > 0:
                    # Width is k+1 (since we can take columns from 0 to k)
                    # Height is sorted_heights[k]
                    max_area = max(max_area, sorted_heights[k] * (k + 1))
        
        return max_area