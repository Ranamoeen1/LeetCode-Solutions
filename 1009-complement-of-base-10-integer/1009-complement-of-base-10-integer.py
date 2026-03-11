# class Solution:
#     def bitwiseComplement(self, n: int) -> int:
#         if n == 0:
#             return 1
            
#         # Find the number of bits in n
#         # Create a mask with all 1's of the same length
#         mask = 1
#         while mask <= n:
#             mask <<= 1
        
#         # mask is now 2^(k) where k is the number of bits in n
#         # We need mask - 1 which gives all 1's of length k
#         mask -= 1
        
#         # XOR with mask flips all bits
#         return mask ^ n


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        # Convert to binary and remove '0b' prefix
        binary = bin(n)[2:]
        
        # Flip bits by mapping '0' to '1' and '1' to '0'
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        
        # Convert back to integer
        return int(complement, 2)