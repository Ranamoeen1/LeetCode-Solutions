# class Solution:
#     def uniqueXorTriplets(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n <= 2:
#             return n
#         return 1 << n.bit_length()



import math

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # Calculate the number of bits needed to represent n
        highest_bit_index = int(math.log2(n)) + 1
        
        # 2^highest_bit_index
        return 1 << highest_bit_index