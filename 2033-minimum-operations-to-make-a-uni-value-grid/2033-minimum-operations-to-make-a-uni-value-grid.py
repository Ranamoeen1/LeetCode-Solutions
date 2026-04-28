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