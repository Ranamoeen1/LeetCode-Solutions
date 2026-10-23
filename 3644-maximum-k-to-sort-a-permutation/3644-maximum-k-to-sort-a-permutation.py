class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = None
        
        for i, val in enumerate(nums):
            if val != i:
                if k is None:
                    k = val
                else:
                    k &= val
        
        # If the array was already sorted, k remains None, so return 0
        return k if k is not None else 0