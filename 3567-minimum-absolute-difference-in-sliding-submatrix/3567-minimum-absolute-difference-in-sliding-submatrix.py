class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        # Iterate over all possible top-left corners of k×k submatrices
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Collect all values in this k×k submatrix
                values = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.append(grid[x][y])
                
                distinct_values = sorted(set(values))
                
                if len(distinct_values) == 1:
                    result[i][j] = 0
                    continue
                
                min_diff = float('inf')
                for idx in range(1, len(distinct_values)):
                    diff = distinct_values[idx] - distinct_values[idx - 1]
                    min_diff = min(min_diff, diff)
                
                result[i][j] = min_diff
        
        return result