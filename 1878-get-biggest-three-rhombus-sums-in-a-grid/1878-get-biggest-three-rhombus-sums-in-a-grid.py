class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
        
        # Enumerate by top corner and size
        max_k = (min(m, n) + 1) // 2
        
        for k in range(1, max_k + 1):
            dk = 2 * k
            for i in range(m - dk):
                i2 = i + dk
                ik = i + k
                for j in range(k, n - k):
                    jk = j + k
                    jmk = j - k
                    
                    # Compute border sum
                    s = 0
                    
                    # Top edge to right
                    r, c = i, j
                    while r < ik:
                        s += grid[r][c]
                        r += 1
                        c += 1
                    
                    # Right edge to bottom
                    while r < i2:
                        s += grid[r][c]
                        r += 1
                        c -= 1
                    
                    # Bottom edge to left
                    while r > ik:
                        s += grid[r][c]
                        r -= 1
                        c -= 1
                    
                    # Left edge to top (exclusive)
                    while r > i:
                        s += grid[r][c]
                        r -= 1
                        c += 1
                    
                    sums.add(s)
        
        arr = sorted(sums, reverse=True)
        return arr[:3]



# class Solution:
#     def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
#         m, n = len(grid), len(grid[0])
#         sums = set()
        
#         # All size 0 rhombuses (single cells)
#         for i in range(m):
#             for j in range(n):
#                 sums.add(grid[i][j])
        
#         # Try all size k >= 1 rhombuses
#         max_k = min(m, n)
        
#         for k in range(1, max_k + 1):
#             for i in range(m - 2 * k):  # top row can go up to here
#                 for j in range(k, n - k):  # need k columns on each side
#                     total = 0
                    
#                     # Top to right (down-right, k cells, not including right corner)
#                     for d in range(k):
#                         total += grid[i + d][j + d]
                    
#                     # Right to bottom (down-left, k cells, not including bottom corner)
#                     for d in range(k):
#                         total += grid[i + k + d][j + k - d]
                    
#                     # Bottom to left (up-left, k cells, not including left corner)
#                     for d in range(k):
#                         total += grid[i + 2 * k - d][j - d]
                    
#                     # Left to top (up-right, k cells, not including top corner)
#                     for d in range(k):
#                         total += grid[i + k - d][j - k + d]
                    
#                     sums.add(total)
        
#         # Return top 3 distinct values in descending order
#         return sorted(sums, reverse=True)[:3]