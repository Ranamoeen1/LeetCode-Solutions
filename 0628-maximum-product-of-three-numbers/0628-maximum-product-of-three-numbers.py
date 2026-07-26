class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Track the three largest values
        max1 = max2 = max3 = float('-inf')
        # Track the two smallest values
        min1 = min2 = float('inf')
        
        for n in nums:
            # Update three maximums
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
                
            # Update two minimums
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
        
        return max(max1 * max2 * max3, min1 * min2 * max1)






# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         nums.sort()
        
#         # The maximum product can come from either:
#         # 1. The 3 largest numbers (e.g., all positive numbers)
#         # 2. The 2 smallest numbers (large negatives) multiplied by the largest number
#         return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])