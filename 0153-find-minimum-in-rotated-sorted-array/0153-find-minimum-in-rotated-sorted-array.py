class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # it means the rotation point (and the minimum) is to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is either at mid or to the left of mid.
            else:
                right = mid
                
        return nums[left]