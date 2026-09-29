class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Pair each number with its original index and sort by value
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in seen:
#                 return [seen[complement], i]
#             seen[num] = i