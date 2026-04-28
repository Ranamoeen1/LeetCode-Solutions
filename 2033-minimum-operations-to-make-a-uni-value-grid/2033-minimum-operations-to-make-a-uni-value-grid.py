# class Solution:
#     def minOperations(self, grid: List[List[int]], x: int) -> int:
#         # Step 1: Flatten the grid into a single list
#         nums = [val for row in grid for val in row]
        
#         # Step 2: Check if transformation is possible
#         # All elements must have the same remainder modulo x
#         remainder = nums[0] % x
#         for num in nums:
#             if num % x != remainder:
#                 return -1
        
#         # Step 3: Sort the array to find the median
#         nums.sort()
#         n = len(nums)
#         median = nums[n // 2]
        
#         # Step 4: Calculate operations needed
#         operations = 0
#         for num in nums:
#             operations += abs(num - median) // x
        
#         return operations





class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Step 1: Count frequencies of values
        # Since grid[i][j] <= 10^4, we can use counting sort approach
        MAX_VAL = 10**4
        
        # Check remainder consistency first (fast fail)
        remainder = grid[0][0] % x
        for row in grid:
            for val in row:
                if val % x != remainder:
                    return -1
        
        # Count frequency of each value
        freq = {}
        for row in grid:
            for val in row:
                freq[val] = freq.get(val, 0) + 1
        
        # Get all unique values
        unique_vals = sorted(freq.keys())
        
        # Step 2: Prefix sums for efficient median calculation
        # Instead of storing all values, work with frequencies
        total_elements = len(grid) * len(grid[0])
        
        # Find median value using cumulative frequency
        cumulative = 0
        median_val = None
        target = total_elements // 2
        
        for val in unique_vals:
            cumulative += freq[val]
            if cumulative > target:
                median_val = val
                break
        
        # Step 3: Calculate operations using median
        operations = 0
        for val in unique_vals:
            operations += abs(val - median_val) // x * freq[val]
        
        return operations