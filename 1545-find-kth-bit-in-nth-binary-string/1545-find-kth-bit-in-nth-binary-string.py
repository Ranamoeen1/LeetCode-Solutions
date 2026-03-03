class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = (1 << n) - 1  # 2^n - 1
        mid = (length // 2) + 1  # Middle position (1-indexed)
        
        if k == mid:
            return "1"
        elif k < mid:
            # k is in the left half
            return self.findKthBit(n - 1, k)
        else:
       
            corresponding_bit = self.findKthBit(n - 1, length - k + 1)
            return "1" if corresponding_bit == "0" else "0"



# class Solution:
#     def findKthBit(self, n: int, k: int) -> str:
#         # Convert k to 0-indexed for easier bit manipulation
#         k -= 1
        
#         # Track if we need to invert the result
#         invert_count = 0
        
#         # Process from the largest length down to S1
#         for i in range(n, 1, -1):
#             length = (1 << i) - 1  # 2^i - 1
#             mid = length // 2      # Middle position (0-indexed)
            
#             if k == mid:
#                 # If we're at middle position, return '1' (inverted if odd number of flips)
#                 return '1' if invert_count % 2 == 0 else '0'
#             elif k > mid:
#                 # In right half: mirror position and prepare to invert
#                 k = length - 1 - k
#                 invert_count += 1
        
#         # Base case: S1 = "0"
#         return '0' if invert_count % 2 == 0 else '1'