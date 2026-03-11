class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        # Find the number of bits in n
        # Create a mask with all 1's of the same length
        mask = 1
        while mask <= n:
            mask <<= 1
        
        # mask is now 2^(k) where k is the number of bits in n
        # We need mask - 1 which gives all 1's of length k
        mask -= 1
        
        # XOR with mask flips all bits
        return mask ^ n