class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 0
        last = {}
        
        for char in s:
            # new subsequences created by appending current character
            new_added = (dp + 1) % MOD
            
            # update total subsequences count
            dp = (dp + new_added - last.get(char, 0)) % MOD
            
            # update the contribution recorded for this character
            last[char] = new_added
            
        return dp