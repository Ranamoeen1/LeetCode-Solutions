class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        row_count = [0] * m
        col_count = [0] * n
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        special_count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_count += 1
        
        return special_count


# from typing import List

# class Solution:
#     def numSpecial(self, mat: List[List[int]]) -> int:
#         m, n = len(mat), len(mat[0])
        
#         # Find rows that have exactly one 1
#         rows_with_one = []
#         for i in range(m):
#             ones_positions = [j for j in range(n) if mat[i][j] == 1]
#             if len(ones_positions) == 1:
#                 rows_with_one.append((i, ones_positions[0]))
        
#         # Find columns that have exactly one 1
#         cols_with_one = []
#         for j in range(n):
#             ones_positions = [i for i in range(m) if mat[i][j] == 1]
#             if len(ones_positions) == 1:
#                 cols_with_one.append((ones_positions[0], j))
        
#         # Find intersection
#         special_count = 0
#         for r, c in rows_with_one:
#             if (r, c) in cols_with_one:
#                 special_count += 1
        
#         return special_count


# from typing import List

# class Solution:
#     def numSpecial(self, mat: List[List[int]]) -> int:
#         m, n = len(mat), len(mat[0])
        
#         # Track rows and columns that have more than one 1
#         invalid_rows = set()
#         invalid_cols = set()
        
#         # First pass: mark invalid rows and columns
#         for i in range(m):
#             count = 0
#             for j in range(n):
#                 if mat[i][j] == 1:
#                     count += 1
#                     if count > 1:
#                         invalid_rows.add(i)
#                         break
        
#         for j in range(n):
#             count = 0
#             for i in range(m):
#                 if mat[i][j] == 1:
#                     count += 1
#                     if count > 1:
#                         invalid_cols.add(j)
#                         break
        
#         # Second pass: count special positions
#         special_count = 0
#         for i in range(m):
#             if i in invalid_rows:
#                 continue
#             for j in range(n):
#                 if j in invalid_cols:
#                     continue
#                 if mat[i][j] == 1:
#                     special_count += 1
        
#         return special_count


# from typing import List
# from collections import defaultdict

# class Solution:
#     def numSpecial(self, mat: List[List[int]]) -> int:
#         m, n = len(mat), len(mat[0])
        
#         # Store positions of all 1s
#         row_positions = defaultdict(list)
#         col_positions = defaultdict(list)
        
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] == 1:
#                     row_positions[i].append(j)
#                     col_positions[j].append(i)
        
#         # Check each 1's position
#         special_count = 0
#         for i in range(m):
#             if len(row_positions[i]) == 1:
#                 j = row_positions[i][0]
#                 if len(col_positions[j]) == 1:
#                     special_count += 1
        
#         return special_count



