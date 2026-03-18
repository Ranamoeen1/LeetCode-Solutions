class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Build cumulative sums row by row
        cumulative = [[0] * n for _ in range(m)]
        
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                # Cumulative sum from (0,0) to (i,j)
                if i == 0:
                    cumulative[i][j] = row_sum
                else:
                    cumulative[i][j] = cumulative[i-1][j] + row_sum
                
                if cumulative[i][j] <= k:
                    count += 1
                else:
                    # Since all values are non-negative, further columns in this row
                    # will only increase the sum, but we need to continue to next row
                    # because previous columns might still be valid when extended downward
                    # So we don't break here
                    pass
        
        return count


# class Solution:
#     def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
#         m, n = len(grid), len(grid[0])
#         count = 0
        
#         # Create row-wise prefix sums
#         row_prefix = [[0] * (n + 1) for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
        
#         # For each possible ending column
#         for end_col in range(n):
#             # For each possible ending row, calculate sum of submatrix
#             total = 0
#             for end_row in range(m):
#                 # Add the sum of current row from col 0 to end_col
#                 total += row_prefix[end_row][end_col + 1]
#                 if total <= k:
#                     count += 1
#                 else:
#                     # Since all values are non-negative, we can break for remaining rows
#                     # because adding more rows will only increase the sum
#                     break
        
#         return count


# # class Solution:
# #     def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
# #         m, n = len(grid), len(grid[0])
        
# #         # Create prefix sum matrix
# #         prefix = [[0] * n for _ in range(m)]
        
# #         # Fill prefix sums
# #         for i in range(m):
# #             for j in range(n):
# #                 prefix[i][j] = grid[i][j]
# #                 if i > 0:
# #                     prefix[i][j] += prefix[i-1][j]
# #                 if j > 0:
# #                     prefix[i][j] += prefix[i][j-1]
# #                 if i > 0 and j > 0:
# #                     prefix[i][j] -= prefix[i-1][j-1]
        
# #         # Count valid submatrices
# #         count = 0
# #         for i in range(m):
# #             for j in range(n):
# #                 if prefix[i][j] <= k:
# #                     count += 1
# #                 else:
# #                     break
        
# #         return count