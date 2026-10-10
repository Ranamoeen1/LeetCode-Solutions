class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        total_k = k1 + k2
        if sum(diff) <= total_k:
            return 0
            
        max_val = max(diff)
        count = [0] * (max_val + 1)
        for d in diff:
            count[d] += 1
            
        for d in range(max_val, 0, -1):
            if count[d] > 0:
                take = min(count[d], total_k)
                count[d] -= take
                count[d - 1] += take
                total_k -= take
                if total_k == 0:
                    break
                    
        ans = 0
        for d in range(max_val + 1):
            if count[d] > 0:
                ans += count[d] * (d * d)
                
        return ans