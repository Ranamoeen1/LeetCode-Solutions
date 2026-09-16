class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate C(n + k - 1, 2 * k) % MOD
        N = n + k - 1
        R = 2 * k
        
        if R > N:
            return 0
        
        # Using math.comb available in Python 3.8+
        import math
        return math.comb(N, R) % MOD