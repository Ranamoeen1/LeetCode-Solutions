class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float('inf')
        
        for i, num in enumerate(nums):
            if num == target:
                distance = abs(i - start)
                min_distance = min(min_distance, distance)
        
        return min_distance