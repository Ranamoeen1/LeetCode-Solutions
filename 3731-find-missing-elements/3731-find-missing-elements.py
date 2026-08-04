class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val, max_val = min(nums), max(nums)
        nums_set = set(nums)
        
        return [x for x in range(min_val, max_val + 1) if x not in nums_set]