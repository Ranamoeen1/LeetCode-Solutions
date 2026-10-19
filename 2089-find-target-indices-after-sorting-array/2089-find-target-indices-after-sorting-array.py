class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = sum(1 for x in nums if x < target)
        count = nums.count(target)
        
        return list(range(less, less + count))


# class Solution:
#     def targetIndices(self, nums: list[int], target: int) -> list[int]:
#         nums.sort()
#         return [i for i, num in enumerate(nums) if num == target]