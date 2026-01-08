class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-float('inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                current_product = nums1[i] * nums2[j]
                
         
                if i > 0 and j > 0:
                    dp[i][j] = max(current_product, current_product + dp[i-1][j-1])
                else:
                    dp[i][j] = current_product
                
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        return dp[n-1][m-1]