class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        # If the minimum value is odd, we can make all elements odd
        if min_val % 2 != 0:
            return True
        
        # If the minimum value is even, all elements must already be even
        return all(x % 2 == 0 for x in nums1)