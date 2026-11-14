class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        
        # Build prefix sums for O(1) range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        min_sum = float('inf')
        
        # Iterate over all possible lengths between l and r
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                sub_sum = prefix[i + length] - prefix[i]
                if sub_sum > 0:
                    min_sum = min(min_sum, sub_sum)
                    
        return min_sum if min_sum != float('inf') else -1