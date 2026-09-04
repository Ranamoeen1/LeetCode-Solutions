class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute suffix minimums
        # suffix_min[i] stores min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        # Iterate and track prefix maximums on the fly
        # prefix_max tracks max(nums[0..i])
        prefix_max = nums[0]
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            
            # Instability score = max(nums[0..i]) - min(nums[i..n-1])
            instability_score = prefix_max - suffix_min[i]
            
            if instability_score <= k:
                return i
                
        return -1