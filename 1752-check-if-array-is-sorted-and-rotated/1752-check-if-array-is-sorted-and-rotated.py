class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            # Compare current element with the next element (using modulo for wrap-around)
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                
            # If we find more than one drop, it's not a rotated sorted array
            if count > 1:
                return False
                
        return True