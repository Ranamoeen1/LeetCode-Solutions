class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Step 1: Flatten the grid into a single list
        nums = [val for row in grid for val in row]
        
        # Step 2: Check if transformation is possible
        # All elements must have the same remainder modulo x
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        
        # Step 3: Sort the array to find the median
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        
        # Step 4: Calculate operations needed
        operations = 0
        for num in nums:
            operations += abs(num - median) // x
        
        return operations





# class Solution:
#     def minOperations(self, grid: List[List[int]], x: int) -> int:
#         # Step 1: Count frequencies of values
#         # Since grid[i][j] <= 10^4, we can use counting sort approach
#         MAX_VAL = 10**4
        
#         # Check remainder consistency first (fast fail)
#         remainder = grid[0][0] % x
#         for row in grid:
#             for val in row:
#                 if val % x != remainder:
#                     return -1
        
#         # Count frequency of each value
#         freq = {}
#         for row in grid:
#             for val in row:
#                 freq[val] = freq.get(val, 0) + 1
        
#         # Get all unique values
#         unique_vals = sorted(freq.keys())
        
#         # Step 2: Prefix sums for efficient median calculation
#         # Instead of storing all values, work with frequencies
#         total_elements = len(grid) * len(grid[0])
        
#         # Find median value using cumulative frequency
#         cumulative = 0
#         median_val = None
#         target = total_elements // 2
        
#         for val in unique_vals:
#             cumulative += freq[val]
#             if cumulative > target:
#                 median_val = val
#                 break
        
#         # Step 3: Calculate operations using median
#         operations = 0
#         for val in unique_vals:
#             operations += abs(val - median_val) // x * freq[val]
        
#         return operations


# from typing import List
# import statistics

# class Solution:
#     def minOperations(self, grid: List[List[int]], x: int) -> int:
#         # Step 1: Flatten the grid
#         nums = [val for row in grid for val in row]
        
#         # Step 2: Check if transformation is possible
#         remainder = nums[0] % x
#         for num in nums:
#             if num % x != remainder:
#                 return -1
        
#         # Step 3: Find median without sorting the entire array
#         n = len(nums)
#         median = self.quick_select(nums, 0, n - 1, n // 2)
        
#         # Step 4: Calculate operations
#         operations = 0
#         for num in nums:
#             operations += abs(num - median) // x
        
#         return operations
    
#     def quick_select(self, arr, left, right, k):
#         """Find k-th smallest element (0-indexed) using Quick Select algorithm"""
#         if left == right:
#             return arr[left]
        
#         # Choose pivot (using median-of-three for better performance)
#         pivot_index = self.partition(arr, left, right)
        
#         if k == pivot_index:
#             return arr[k]
#         elif k < pivot_index:
#             return self.quick_select(arr, left, pivot_index - 1, k)
#         else:
#             return self.quick_select(arr, pivot_index + 1, right, k)
    
#     def partition(self, arr, left, right):
#         """Partition array around a pivot (using median-of-three)"""
#         # Median-of-three pivot selection
#         mid = (left + right) // 2
#         pivot = self.median_of_three(arr[left], arr[mid], arr[right])
        
#         # Find and move pivot to the end
#         if arr[left] == pivot:
#             pivot_index = left
#         elif arr[mid] == pivot:
#             pivot_index = mid
#         else:
#             pivot_index = right
        
#         arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
#         pivot = arr[right]
        
#         # Partition
#         i = left
#         for j in range(left, right):
#             if arr[j] <= pivot:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 i += 1
        
#         # Place pivot in its correct position
#         arr[i], arr[right] = arr[right], arr[i]
#         return i
    
#     def median_of_three(self, a, b, c):
#         """Return the median of three numbers"""
#         if a > b:
#             a, b = b, a
#         if b > c:
#             b, c = c, b
#         if a > b:
#             a, b = b, a
#         return b