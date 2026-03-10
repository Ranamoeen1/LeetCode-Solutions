# class Solution:
#     def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
#         MOD = 10**9 + 7
        
#         # dp0[i][j] = number of valid arrays with i zeros, j ones, ending with 0
#         # dp1[i][j] = number of valid arrays with i zeros, j ones, ending with 1
        
#         dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
#         dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
#         # Prefix sums for O(1) range queries
#         # col_sum1[i][j] = sum of dp1[0..i][j] (prefix sum down column j)
#         col_sum1 = [[0] * (one + 1) for _ in range(zero + 1)]
#         # row_sum0[i][j] = sum of dp0[i][0..j] (prefix sum across row i)
#         row_sum0 = [[0] * (one + 1) for _ in range(zero + 1)]
        
#         for i in range(zero + 1):
#             for j in range(one + 1):
#                 if i == 0 and j == 0:
#                     continue
                
#                 # Base case: only zeros
#                 if j == 0:
#                     # Can only form array if i <= limit (no more than limit consecutive zeros)
#                     if 1 <= i <= limit:
#                         dp0[i][j] = 1
#                     # dp1[i][j] stays 0 (can't end with 1 if no ones)
                
#                 # Base case: only ones
#                 elif i == 0:
#                     # Can only form array if j <= limit
#                     if 1 <= j <= limit:
#                         dp1[i][j] = 1
#                     # dp0[i][j] stays 0
                
#                 # General case: both zeros and ones present
#                 else:
#                     # To end with 0: we add k consecutive zeros (1 <= k <= limit) 
#                     # after an array ending with 1
#                     # dp0[i][j] = sum(dp1[i-k][j] for k in 1..limit)
#                     low_i = max(0, i - limit)
#                     high_i = i - 1
#                     # Sum dp1[low_i .. high_i][j]
#                     dp0[i][j] = col_sum1[high_i][j]
#                     if low_i > 0:
#                         dp0[i][j] = (dp0[i][j] - col_sum1[low_i - 1][j]) % MOD
                    
#                     # To end with 1: we add k consecutive ones (1 <= k <= limit)
#                     # after an array ending with 0
#                     # dp1[i][j] = sum(dp0[i][j-k] for k in 1..limit)
#                     low_j = max(0, j - limit)
#                     high_j = j - 1
#                     # Sum dp0[i][low_j .. high_j]
#                     dp1[i][j] = row_sum0[i][high_j]
#                     if low_j > 0:
#                         dp1[i][j] = (dp1[i][j] - row_sum0[i][low_j - 1]) % MOD
                
#                 # Update prefix sums
#                 col_sum1[i][j] = dp1[i][j]
#                 if i > 0:
#                     col_sum1[i][j] = (col_sum1[i][j] + col_sum1[i-1][j]) % MOD
                
#                 row_sum0[i][j] = dp0[i][j]
#                 if j > 0:
#                     row_sum0[i][j] = (row_sum0[i][j] + row_sum0[i][j-1]) % MOD
        
#         return (dp0[zero][one] + dp1[zero][one]) % MOD



class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        max_n = max(zero, one)
        
        # dp[k][n] = ways to write n as sum of k positive integers, each in [1, limit]
        dp = [[0] * (max_n + 1) for _ in range(max_n + 2)]
        dp[0][0] = 1
        
        for k in range(1, max_n + 1):
            # prefix[i] = sum of dp[k-1][0..i]
            prefix = [0] * (max_n + 1)
            cur = 0
            for i in range(max_n + 1):
                cur = (cur + dp[k-1][i]) % MOD
                prefix[i] = cur
            
            for n in range(k, max_n + 1):  # minimum sum with k terms is k (all 1s)
                # sum of dp[k-1][n-t] for t in [1, limit] = sum of dp[k-1][n-limit .. n-1]
                left = n - limit
                right = n - 1
                if left <= 0:
                    dp[k][n] = prefix[right]
                else:
                    dp[k][n] = (prefix[right] - prefix[left - 1]) % MOD
        
        ans = 0
        
        # Enumerate number of runs
        for num_zero_runs in range(1, zero + 1):
            for num_one_runs in range(1, one + 1):
                if abs(num_zero_runs - num_one_runs) > 1:
                    continue
                
                w0 = dp[num_zero_runs][zero]
                w1 = dp[num_one_runs][one]
                
                if w0 == 0 or w1 == 0:
                    continue
                
                # |a-b| <= 1, so runs can alternate
                if num_zero_runs == num_one_runs:
                    # Can start with 0 or start with 1: 2 ways
                    ans = (ans + 2 * w0 * w1) % MOD
                else:
                    # |a-b| = 1, forced which type starts and ends
                    ans = (ans + w0 * w1) % MOD
        
        return ans % MOD