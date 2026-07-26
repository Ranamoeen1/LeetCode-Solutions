class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        # The maximum product can come from either:
        # 1. The 3 largest numbers (e.g., all positive numbers)
        # 2. The 2 smallest numbers (large negatives) multiplied by the largest number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])