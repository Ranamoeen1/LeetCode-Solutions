class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # For each row, find how many trailing zeros it has
        # A row can go to position i if it has at least n-i-1 trailing zeros
        
        # First, find which positions each row can occupy
        row_capabilities = []
        for i in range(n):
            # Count trailing zeros
            zeros = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    zeros += 1
                else:
                    break
            
            # This row can go to positions where required zeros <= zeros
            # Required zeros for position p is n-p-1
            # So zeros >= n-p-1 => p >= n-zeros-1
            min_position = n - zeros - 1
            row_capabilities.append(min_position)
        
        # Now we need to assign rows to positions [0..n-1]
        # Each row i can only go to positions >= row_capabilities[i]
        # We want to minimize swaps
        
        available_rows = list(range(n))
        swaps = 0
        
        for position in range(n):
            # Find a row that can go to this position
            found = -1
            for idx, row in enumerate(available_rows):
                if row_capabilities[row] <= position:
                    found = idx
                    break
            
            if found == -1:
                return -1
            
            # Number of swaps needed = found (since we need to bring this row to front)
            swaps += found
            
            # Remove the found row from available rows
            available_rows.pop(found)
        
        return swaps

# class Solution:
#     def minSwaps(self, grid: List[List[int]]) -> int:
#         n = len(grid)
        
#         # Create a list of rows with their trailing zero counts
#         rows = []
#         for i in range(n):
#             zeros = 0
#             for j in range(n-1, -1, -1):
#                 if grid[i][j] == 0:
#                     zeros += 1
#                 else:
#                     break
#             rows.append((zeros, i))
        
#         # Sort rows by trailing zeros in descending order initially
#         rows.sort(reverse=True)
        
#         # Use a deque for efficient pops from both ends
#         dq = deque(rows)
#         swaps = 0
        
#         for i in range(n):
#             required = n - i - 1
            
#             # Find a row with enough trailing zeros
#             found = None
#             temp = []
            
#             while dq and dq[0][0] < required:
#                 temp.append(dq.popleft())
            
#             if not dq:
#                 return -1
            
#             # Found a suitable row
#             found = dq.popleft()
            
#             # Add back the rows we temporarily removed
#             while temp:
#                 dq.appendleft(temp.pop())
            
#             # Count swaps needed (this is tricky with deque approach)
#             # For counting swaps accurately, we need to know original positions
#             # So let's use the original indices approach
#             pass
        
#         # Better approach with original indices
#         trailing_zeros = []
#         for i in range(n):
#             zeros = 0
#             for j in range(n-1, -1, -1):
#                 if grid[i][j] == 0:
#                     zeros += 1
#                 else:
#                     break
#             trailing_zeros.append(zeros)
        
#         swaps = 0
#         for i in range(n):
#             required = n - i - 1
            
#             # Find the closest row below with enough zeros
#             for j in range(i, n):
#                 if trailing_zeros[j] >= required:
#                     # Bubble it up
#                     for k in range(j, i, -1):
#                         trailing_zeros[k], trailing_zeros[k-1] = trailing_zeros[k-1], trailing_zeros[k]
#                         swaps += 1
#                     break
#             else:
#                 return -1
        
#         return swaps



# # class Solution:
# #     def minSwaps(self, grid: List[List[int]]) -> int:
# #         n = len(grid)
        
# #         # Count trailing zeros for each row
# #         trailing_zeros = []
# #         for i in range(n):
# #             count = 0
# #             # Count zeros from the right
# #             for j in range(n-1, -1, -1):
# #                 if grid[i][j] == 0:
# #                     count += 1
# #                 else:
# #                     break
# #             trailing_zeros.append(count)
        
# #         swaps = 0
        
# #         # Process each row from top to bottom
# #         for i in range(n):
# #             # Row i needs at least (n-i-1) trailing zeros
# #             required = n - i - 1
            
# #             # Find a row with enough trailing zeros starting from current position
# #             found = -1
# #             for j in range(i, n):
# #                 if trailing_zeros[j] >= required:
# #                     found = j
# #                     break
            
# #             # If no row found with required zeros, impossible
# #             if found == -1:
# #                 return -1
            
# #             # Bring the found row to position i by swapping upwards
# #             for k in range(found, i, -1):
# #                 trailing_zeros[k], trailing_zeros[k-1] = trailing_zeros[k-1], trailing_zeros[k]
# #                 swaps += 1
        
# #         return swaps