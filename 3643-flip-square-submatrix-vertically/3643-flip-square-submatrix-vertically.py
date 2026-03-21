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

# # # # # class Solution:
# # # # #     def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
# # # # #         # Two pointers: top and bottom rows of the submatrix
# # # # #         top = x
# # # # #         bottom = x + k - 1
        
# # # # #         while top < bottom:
# # # # #             # Swap the entire rows within the submatrix column range
# # # # #             for col in range(y, y + k):
# # # # #                 grid[top][col], grid[bottom][col] = grid[bottom][col], grid[top][col]
# # # # #             top += 1
# # # # #             bottom -= 1
        
# # # # #         return grid



# # # # class Solution:
# # # #     def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
# # # #         # Create a deep copy to avoid modifying the original (if needed)
# # # #         result = [row[:] for row in grid]
        
# # # #         # Extract the rows to reverse
# # # #         rows_to_reverse = [grid[x + i][y:y + k] for i in range(k)]
        
# # # #         # Reverse the rows
# # # #         rows_to_reverse.reverse()
        
# # # #         # Place them back in the result
# # # #         for i in range(k):
# # # #             result[x + i][y:y + k] = rows_to_reverse[i]
        
# # # #         return result


# # # from typing import List
# # # import numpy as np

# # # class Solution:
# # #     def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
# # #         # Convert to numpy array
# # #         arr = np.array(grid)
        
# # #         # Extract submatrix, reverse rows, and assign back
# # #         arr[x:x+k, y:y+k] = arr[x:x+k, y:y+k][::-1, :]
        
# # #         return arr.tolist()

# # from typing import List
# # from collections import deque

# # class Solution:
# #     def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
# #         # Extract the rows of the submatrix
# #         submatrix = deque([grid[x + i][y:y + k] for i in range(k)])
        
# #         # Reverse the deque
# #         submatrix.reverse()
        
# #         # Place back
# #         for i in range(k):
# #             grid[x + i][y:y + k] = submatrix[i]
        
# #         return grid


# class Solution:
#     def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
#         # Get the rows to reverse
#         rows = [grid[x + i][y:y + k] for i in range(k)]
        
#         # Reverse and assign using enumerate
#         for i, row in enumerate(reversed(rows)):
#             grid[x + i][y:y + k] = row
        
#         return grid