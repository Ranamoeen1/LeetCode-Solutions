class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Count trailing zeros for each row
        trailing_zeros = []
        for i in range(n):
            count = 0
            # Count zeros from the right
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        swaps = 0
        
        # Process each row from top to bottom
        for i in range(n):
            # Row i needs at least (n-i-1) trailing zeros
            required = n - i - 1
            
            # Find a row with enough trailing zeros starting from current position
            found = -1
            for j in range(i, n):
                if trailing_zeros[j] >= required:
                    found = j
                    break
            
            # If no row found with required zeros, impossible
            if found == -1:
                return -1
            
            # Bring the found row to position i by swapping upwards
            for k in range(found, i, -1):
                trailing_zeros[k], trailing_zeros[k-1] = trailing_zeros[k-1], trailing_zeros[k]
                swaps += 1
        
        return swaps