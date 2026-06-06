from itertools import accumulate

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        
        # accumulate(nums) gives a running total: [nums[0], nums[0]+nums[1], ...]
        return [abs(2 * prefix - num - total) for num, prefix in zip(nums, accumulate(nums))]






# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         left_sum = 0
#         right_sum = sum(nums)
#         answer = []
        
#         for num in nums:
#             # Current number is neither to the left nor to the right of itself
#             right_sum -= num
            
#             # Calculate the absolute difference
#             answer.append(abs(left_sum - right_sum))
            
#             # Current number now becomes part of the left sum for the next elements
#             left_sum += num
            
#         return answer