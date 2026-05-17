class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum element must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the middle element is less than the rightmost element,
            # the minimum element is either at mid or in the left half.
            elif nums[mid] < nums[right]:
                right = mid
            # If they are equal, we cannot determine the side due to duplicates.
            # We safely increment down the right pointer to narrow the search space.
            else:
                right -= 1
                
        return nums[left]