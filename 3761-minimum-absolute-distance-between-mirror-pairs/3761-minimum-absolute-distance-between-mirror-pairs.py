class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            res = 0
            while x > 0:
                res = res * 10 + x % 10
                x //= 10
            return res
        
        rev_seen = {}  # reverse(nums[i]) -> most recent index i
        min_dist = float('inf')
        
        for j, num in enumerate(nums):
            if num in rev_seen:
                min_dist = min(min_dist, j - rev_seen[num])
            
            rev_seen[reverse(num)] = j
        
        return min_dist if min_dist != float('inf') else -1