# class Solution:
#     def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])
        
#         # Create prefix sum arrays for X and Y
#         prefix_X = [[0] * (n + 1) for _ in range(m + 1)]
#         prefix_Y = [[0] * (n + 1) for _ in range(m + 1)]
        
#         # Fill prefix sum arrays
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 prefix_X[i][j] = prefix_X[i-1][j] + prefix_X[i][j-1] - prefix_X[i-1][j-1] + (1 if grid[i-1][j-1] == 'X' else 0)
#                 prefix_Y[i][j] = prefix_Y[i-1][j] + prefix_Y[i][j-1] - prefix_Y[i-1][j-1] + (1 if grid[i-1][j-1] == 'Y' else 0)
        
#         count = 0
        
#         # Check each possible bottom-right corner (i, j)
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 # Count X and Y in rectangle from (0,0) to (i-1, j-1)
#                 num_X = prefix_X[i][j]
#                 num_Y = prefix_Y[i][j]
                
#                 # Check conditions
#                 if num_X == num_Y and num_X >= 1:
#                     count += 1
        
#         return count


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dpX[i][j] = count of 'X' in submatrix from (0,0) to (i,j)
        # dpY[i][j] = count of 'Y' in submatrix from (0,0) to (i,j)
        dpX = [[0] * n for _ in range(m)]
        dpY = [[0] * n for _ in range(m)]
        
        # Initialize first cell
        if grid[0][0] == 'X':
            dpX[0][0] = 1
        elif grid[0][0] == 'Y':
            dpY[0][0] = 1
        
        # Fill first row
        for j in range(1, n):
            dpX[0][j] = dpX[0][j-1] + (1 if grid[0][j] == 'X' else 0)
            dpY[0][j] = dpY[0][j-1] + (1 if grid[0][j] == 'Y' else 0)
        
        # Fill first column
        for i in range(1, m):
            dpX[i][0] = dpX[i-1][0] + (1 if grid[i][0] == 'X' else 0)
            dpY[i][0] = dpY[i-1][0] + (1 if grid[i][0] == 'Y' else 0)
        
        # Fill the rest using DP
        for i in range(1, m):
            for j in range(1, n):
                dpX[i][j] = dpX[i-1][j] + dpX[i][j-1] - dpX[i-1][j-1] + (1 if grid[i][j] == 'X' else 0)
                dpY[i][j] = dpY[i-1][j] + dpY[i][j-1] - dpY[i-1][j-1] + (1 if grid[i][j] == 'Y' else 0)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if dpX[i][j] == dpY[i][j] and dpX[i][j] >= 1:
                    count += 1
        
        return count