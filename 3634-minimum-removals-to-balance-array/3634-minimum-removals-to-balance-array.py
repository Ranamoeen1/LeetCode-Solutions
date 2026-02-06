class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        nums.sort()
        
        max_window = 1  
        j = 0
        
        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            max_window = max(max_window, j - i)
        
        return n - max_window