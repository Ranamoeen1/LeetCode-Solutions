class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: k equals the length of the array
        if k == n:
            return max(nums)
            
        # Case 2: k == 1
        if k == 1:
            ans = -1
            for x in set(nums):
                if nums.count(x) == 1:
                    ans = max(ans, x)
            return ans
            
        # Case 3: 1 < k < n
        # Only boundary elements (nums[0] and nums[n - 1]) can appear in exactly 1 subarray.
        ans = -1
        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])
        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])
            
        return ans