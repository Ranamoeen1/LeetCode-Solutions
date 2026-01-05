class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        min_abs_val = float('inf')
        negative_count = 0
        
        for row in matrix:
            for val in row:
                total_sum += abs(val)
                
                if val < 0:
                    negative_count += 1
                if abs(val) < min_abs_val:
                    min_abs_val = abs(val)
        if negative_count % 2 == 1:
            return total_sum - 2 * min_abs_val
        
        return total_sum