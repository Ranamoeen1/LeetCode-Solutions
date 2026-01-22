class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        operations = 0
        # Make a copy to work with
        arr = nums.copy()
        
        # Helper to check if array is non-decreasing
        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True
        
        while not is_non_decreasing(arr):
            # Find the adjacent pair with minimum sum
            min_sum = float('inf')
            min_index = -1
            
            for i in range(len(arr) - 1):
                current_sum = arr[i] + arr[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_index = i
            
            arr[min_index] = min_sum
            arr.pop(min_index + 1)
            
            operations += 1
        
        return operations