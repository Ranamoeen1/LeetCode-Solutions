# class Solution:
#     def minMirrorPairDistance(self, nums: List[int]) -> int:
#         def reverse(x: int) -> int:
#             res = 0
#             while x > 0:
#                 res = res * 10 + x % 10
#                 x //= 10
#             return res
        
#         rev_seen = {}  # reverse(nums[i]) -> most recent index i
#         min_dist = float('inf')
        
#         for j, num in enumerate(nums):
#             if num in rev_seen:
#                 min_dist = min(min_dist, j - rev_seen[num])
            
#             rev_seen[reverse(num)] = j
        
#         return min_dist if min_dist != float('inf') else -1


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev_seen = {}
        min_dist = 10**9  # faster than float('inf')
        
        for j, x in enumerate(nums):
            # check if current number matches any previous reversed
            if x in rev_seen:
                dist = j - rev_seen[x]
                if dist < min_dist:
                    min_dist = dist
            
            # inline reverse (avoids function call overhead)
            rev = 0
            temp = x
            while temp:
                rev = rev * 10 + temp % 10
                temp //= 10
            
            rev_seen[rev] = j
        
        return min_dist if min_dist != 10**9 else -1