class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # Precompute powers of 10 modulo 10^9 + 7
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        # pref_x[i] stores the value of non-zero digits in s[0...i-1]
        pref_x = [0] * (n + 1)
        # pref_cnt[i] stores the count of non-zero digits in s[0...i-1]
        pref_cnt = [0] * (n + 1)
        # pref_sum[i] stores the sum of digits in s[0...i-1]
        pref_sum = [0] * (n + 1)
        
        for i in range(n):
            digit = int(s[i])
            if digit != 0:
                pref_x[i+1] = (pref_x[i] * 10 + digit) % MOD
                pref_cnt[i+1] = pref_cnt[i] + 1
            else:
                pref_x[i+1] = pref_x[i]
                pref_cnt[i+1] = pref_cnt[i]
                
            pref_sum[i+1] = pref_sum[i] + digit
            
        ans = []
        for l, r in queries:
            # Count of non-zero digits in the range [l, r]
            cnt = pref_cnt[r+1] - pref_cnt[l]
            
            # Extract x modulo 10^9 + 7
            x = (pref_x[r+1] - pref_x[l] * pow10[cnt]) % MOD
            
            # Extract total sum of digits in the range [l, r]
            digit_sum = pref_sum[r+1] - pref_sum[l]
            
            # Calculate final answer for this query
            ans.append((x * digit_sum) % MOD)
            
        return ans