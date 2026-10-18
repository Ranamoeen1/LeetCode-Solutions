import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            l_len, r_len = len(left), len(right)
            
            # Number of ways to interleave left and right subtrees while preserving relative order
            ways = math.comb(l_len + r_len, l_len) % MOD
            
            return (ways * dfs(left) * dfs(right)) % MOD

        # Subtract 1 to exclude the original ordering itself
        return (dfs(nums) - 1) % MOD