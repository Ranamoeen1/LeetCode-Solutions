# # # # # class Solution:
# # # # #     def bitwiseComplement(self, n: int) -> int:
# # # # #         if n == 0:
# # # # #             return 1
            
# # # # #         # Find the number of bits in n
# # # # #         # Create a mask with all 1's of the same length
# # # # #         mask = 1
# # # # #         while mask <= n:
# # # # #             mask <<= 1
        
# # # # #         # mask is now 2^(k) where k is the number of bits in n
# # # # #         # We need mask - 1 which gives all 1's of length k
# # # # #         mask -= 1
        
# # # # #         # XOR with mask flips all bits
# # # # #         return mask ^ n


# # # # class Solution:
# # # #     def bitwiseComplement(self, n: int) -> int:
# # # #         if n == 0:
# # # #             return 1
            
# # # #         # Convert to binary and remove '0b' prefix
# # # #         binary = bin(n)[2:]
        
# # # #         # Flip bits by mapping '0' to '1' and '1' to '0'
# # # #         complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        
# # # #         # Convert back to integer
# # # #         return int(complement, 2)


# # # class Solution:
# # #     def bitwiseComplement(self, n: int) -> int:
# # #         if n == 0:
# # #             return 1
        
# # #         # Find the smallest power of 2 greater than n
# # #         power = 1
# # #         while power <= n:
# # #             power <<= 1
        
# # #         # For a number with k bits, its complement = (2^k - 1) - n
# # #         return power - 1 - n

# # import math

# # class Solution:
# #     def bitwiseComplement(self, n: int) -> int:
# #         if n == 0:
# #             return 1
        
# #         # Find the number of bits needed to represent n
# #         bit_length = math.floor(math.log2(n)) + 1
        
# #         # Create a mask with bit_length number of 1's
# #         mask = (1 << bit_length) - 1
        
# #         # XOR with mask to flip all bits
# #         return mask ^ n

# class Solution:
#     def bitwiseComplement(self, n: int) -> int:
#         if n == 0:
#             return 1
        
#         # Python's built-in method to get bit length
#         bit_length = n.bit_length()
        
#         # Create mask and XOR
#         mask = (1 << bit_length) - 1
#         return mask ^ n

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        result = 0
        power = 1
        
        while n > 0:
            # Get the last bit and flip it
            last_bit = n & 1
            flipped_bit = last_bit ^ 1
            
            # Add the flipped bit to result at the correct position
            result += flipped_bit * power
            
            # Move to next bit
            power <<= 1
            n >>= 1
        
        return result