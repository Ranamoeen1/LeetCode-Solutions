class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = 0
        max_gain = 0
        
        prev_zero = 0
        curr_zero = 0
        seen_one_between = False
        
        for char in s:
            if char == '1':
                total_ones += 1
                if curr_zero > 0:
                    # We hit a '1' after a '0' block
                    if prev_zero > 0 and seen_one_between:
                        max_gain = max(max_gain, prev_zero + curr_zero)
                    prev_zero = curr_zero
                    curr_zero = 0
                    seen_one_between = True
            else:
                curr_zero += 1
                
        # Check for the last pair of '0' blocks at the end of string
        if curr_zero > 0 and prev_zero > 0 and seen_one_between:
            max_gain = max(max_gain, prev_zero + curr_zero)
            
        return total_ones + max_gain





# class Solution:
#     def maxActiveSectionsAfterTrade(self, s: str) -> int:
#         n = len(s)
#         initial_ones = s.count('1')
        
#         # Augment s with '1' at both ends
#         t = '1' + s + '1'
        
#         # Parse the augmented string into alternating block lengths
#         # In t, the first block is guaranteed to be '1's, then '0's, '1's, '0's, etc.
#         blocks = []
#         curr_char = t[0]
#         curr_len = 0
        
#         for char in t:
#             if char == curr_char:
#                 curr_len += 1
#             else:
#                 blocks.append((curr_char, curr_len))
#                 curr_char = char
#                 curr_len = 1
#         blocks.append((curr_char, curr_len))
        
#         max_ones = initial_ones
        
#         # Look for patterns of '0's -> '1's -> '0's in the block array
#         # A valid inner block of '1's will have a preceding '0' block and a succeeding '0' block.
#         for i in range(1, len(blocks) - 1):
#             if blocks[i][0] == '1' and blocks[i-1][0] == '0' and blocks[i+1][0] == '0':
#                 zeroes_left = blocks[i-1][1]
#                 zeroes_right = blocks[i+1][1]
                
#                 # Gain in '1's is zeroes_left + zeroes_right
#                 current_total = initial_ones + zeroes_left + zeroes_right
#                 max_ones = max(max_ones, current_total)
                
#         return max_ones