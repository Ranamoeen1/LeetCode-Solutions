# class Solution:
#     def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         m, n = len(grid), len(grid[0])
#         result = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
#         # Iterate over all possible top-left corners of k×k submatrices
#         for i in range(m - k + 1):
#             for j in range(n - k + 1):
#                 # Collect all values in this k×k submatrix
#                 values = []
#                 for x in range(i, i + k):
#                     for y in range(j, j + k):
#                         values.append(grid[x][y])
                
#                 distinct_values = sorted(set(values))
                
#                 if len(distinct_values) == 1:
#                     result[i][j] = 0
#                     continue
                
#                 min_diff = float('inf')
#                 for idx in range(1, len(distinct_values)):
#                     diff = distinct_values[idx] - distinct_values[idx - 1]
#                     min_diff = min(min_diff, diff)
                
#                 result[i][j] = min_diff
        
#         return result


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        # For each possible top row of the k×k window
        for i in range(m - k + 1):
            # Maintain a min-heap and max-heap to track min difference
            # This approach is more complex but can be optimized further
            window_values = []
            
            # Initialize the first window
            for x in range(i, i + k):
                for y in range(k):
                    window_values.append(grid[x][y])
            
            # Compute for first window
            result[i][0] = self._optimized_min_diff(sorted(set(window_values)))
            
            # Slide window across columns
            for j in range(1, n - k + 1):
                # Remove left column, add right column
                removed = [grid[x][j - 1] for x in range(i, i + k)]
                added = [grid[x][j + k - 1] for x in range(i, i + k)]
                
                # Update window values
                for val in removed:
                    window_values.remove(val)
                for val in added:
                    window_values.append(val)
                
                # Compute min diff for current window
                result[i][j] = self._optimized_min_diff(sorted(set(window_values)))
        
        return result
    
    def _optimized_min_diff(self, sorted_values: List[int]) -> int:
        """Optimized min diff calculation"""
        if len(sorted_values) <= 1:
            return 0
        
        min_diff = float('inf')
        for i in range(1, len(sorted_values)):
            diff = sorted_values[i] - sorted_values[i - 1]
            if diff < min_diff:
                min_diff = diff
                if min_diff == 1:  # Early termination if we find minimum possible difference
                    return 1
        
        return min_diff