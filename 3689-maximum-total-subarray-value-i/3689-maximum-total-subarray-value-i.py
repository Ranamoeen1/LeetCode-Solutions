# class Solution:
#     def maxTotalValue(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)
        
#         total_value = 0
#         left = 0
#         right = n - 1
        
#         # We need to pair up elements k times
#         while k > 0 and left < right:
#             # The maximum possible contribution from the current pair
#             diff = nums[right] - nums[left]
            
#             # If the difference is 0 or negative, no further gains can be made
#             if diff <= 0:
#                 break
                
#             # We can reuse this pair or elements from it.
#             # However, since we want to maximize the gain, we take as much as we can.
#             # But wait, we can just use the absolute best pair (nums[-1] - nums[0]) 
#             # up to k times if we want, because the problem states:
#             # "the exact same subarray (same l and r) can be chosen more than once."
            
#             # This means nums[0..n-1] contains both the absolute global minimum 
#             # and the absolute global maximum of the entire array. 
#             # We can simply choose this exact same global subarray k times!
            
#             return (nums[-1] - nums[0]) * k
            
#         return (nums[-1] - nums[0]) * k


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
            
        # Find the global minimum and maximum in O(n) time
        min_val = nums[0]
        max_val = nums[0]
        
        for num in nums:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
                
        # The optimal strategy is to pick the subarray containing both 
        # min_val and max_val exactly k times.
        return (max_val - min_val) * k