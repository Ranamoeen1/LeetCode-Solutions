# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
        
#         # Step 1: Transpose the matrix
#         for i in range(n):
#             for j in range(i + 1, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
#         # Step 2: Reverse each row
#         for i in range(n):
#             matrix[i].reverse()


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Process each layer from outer to inner
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            for i in range(first, last):
                # Save top element
                top = matrix[first][i]
                
                # Move left to top
                matrix[first][i] = matrix[last - (i - first)][first]
                
                # Move bottom to left
                matrix[last - (i - first)][first] = matrix[last][last - (i - first)]
                
                # Move right to bottom
                matrix[last][last - (i - first)] = matrix[i][last]
                
                # Move top to right
                matrix[i][last] = top