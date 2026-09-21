class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = {}  # remainder -> count of subarrays ending at current index
        
        for num in nums:
            val = num % k
            next_dp = {}
            
            # Subarray consisting of just the current element
            next_dp[val] = next_dp.get(val, 0) + 1
            
            # Extend existing subarrays ending at the previous element
            for prev_rem, count in dp.items():
                new_rem = (prev_rem * val) % k
                next_dp[new_rem] = next_dp.get(new_rem, 0) + count
            
            # Accumulate counts into the final answer
            for rem, count in next_dp.items():
                ans[rem] += count
                
            dp = next_dp
            
        return ans