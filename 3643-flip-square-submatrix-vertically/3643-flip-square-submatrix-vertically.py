class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # Extract the rows of the submatrix
        submatrix_rows = [grid[x + i][y:y + k] for i in range(k)]
        
        # Reverse the order of rows
        submatrix_rows.reverse()
        
        # Place the reversed rows back into the grid
        for i in range(k):
            grid[x + i][y:y + k] = submatrix_rows[i]
        
        return grid