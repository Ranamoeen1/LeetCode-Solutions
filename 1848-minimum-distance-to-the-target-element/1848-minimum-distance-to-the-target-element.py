# class Solution:
#     def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
#         min_distance = float('inf')
        
#         for i, num in enumerate(nums):
#             if num == target:
#                 distance = abs(i - start)
#                 min_distance = min(min_distance, distance)
        
#         return min_distance

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        
        # Check outward from start index
        for distance in range(n):
            # Check left side
            left_idx = start - distance
            if left_idx >= 0 and nums[left_idx] == target:
                return distance
            
            # Check right side
            right_idx = start + distance
            if right_idx < n and nums[right_idx] == target:
                return distance
        
        return -1  # Should never reach here as target is guaranteed to exist