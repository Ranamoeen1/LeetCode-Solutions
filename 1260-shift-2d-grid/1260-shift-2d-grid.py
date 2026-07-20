class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        
        # Optimize shift count
        k %= total
        if k == 0:
            return grid
        
        # Step 1: Flatten the grid into a 1D list
        flat = [val for row in grid for val in row]
        
        # Step 2: Rotate the 1D list using Python slicing
        # Moves the last k elements to the front
        shifted = flat[-k:] + flat[:-k]
        
        # Step 3: Reshape back into an m x n 2D grid
        return [shifted[i * n : (i + 1) * n] for i in range(m)]






# class Solution:
#     def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         m, n = len(grid), len(grid[0])
#         total = m * n
        
#         # Optimize shift amount to eliminate redundant full rotations
#         k = k % total
#         if k == 0:
#             return grid
            
#         # Create a blank grid for the shifted values
#         result = [[0] * n for _ in range(m)]
        
#         for r in range(m):
#             for c in range(n):
#                 # Convert 2D coordinates to 1D index
#                 old_1d = r * n + c
                
#                 # Calculate new 1D index after shifting
#                 new_1d = (old_1d + k) % total
                
#                 # Convert back to 2D coordinates
#                 new_r = new_1d // n
#                 new_c = new_1d % n
                
#                 result[new_r][new_c] = grid[r][c]
                
#         return result