from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        # Check if two matrices are equal
        def is_equal(matrix1, matrix2):
            for i in range(n):
                for j in range(n):
                    if matrix1[i][j] != matrix2[i][j]:
                        return False
            return True
        
        # Check 0° rotation (original)
        if is_equal(mat, target):
            return True
        
        # Check 90° rotation
        rotated_90 = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated_90[j][n-1-i] = mat[i][j]
        if is_equal(rotated_90, target):
            return True
        
        # Check 180° rotation (apply 90° rotation twice)
        rotated_180 = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated_180[n-1-i][n-1-j] = mat[i][j]
        if is_equal(rotated_180, target):
            return True
        
        # Check 270° rotation (apply 90° rotation three times)
        rotated_270 = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated_270[n-1-j][i] = mat[i][j]
        if is_equal(rotated_270, target):
            return True
        
        return False