from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Prefix sums for rows and columns
        rowPrefix = [[0] * (n + 1) for _ in range(m)]
        colPrefix = [[0] * (m + 1) for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j]
        
        for j in range(n):
            for i in range(m):
                colPrefix[j][i + 1] = colPrefix[j][i] + grid[i][j]
        
        # Try all possible sizes from largest to smallest
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if self.isMagicSquare(grid, i, j, k, rowPrefix, colPrefix):
                        return k
        
        return 1
    
    def isMagicSquare(self, grid, r, c, k, rowPrefix, colPrefix):
        # Calculate the sum of first row as reference
        target = rowPrefix[r][c + k] - rowPrefix[r][c]
        
        # Check all rows
        for i in range(r, r + k):
            if rowPrefix[i][c + k] - rowPrefix[i][c] != target:
                return False
        
        # Check all columns
        for j in range(c, c + k):
            if colPrefix[j][r + k] - colPrefix[j][r] != target:
                return False
        
        # Check main diagonal
        diag1 = 0
        for d in range(k):
            diag1 += grid[r + d][c + d]
        if diag1 != target:
            return False
        
        # Check anti-diagonal
        diag2 = 0
        for d in range(k):
            diag2 += grid[r + d][c + k - 1 - d]
        if diag2 != target:
            return False
        
        return True