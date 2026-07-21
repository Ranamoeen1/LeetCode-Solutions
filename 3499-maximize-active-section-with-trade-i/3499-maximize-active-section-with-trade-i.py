class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        initial_ones = s.count('1')
        
        # Augment s with '1' at both ends
        t = '1' + s + '1'
        
        # Parse the augmented string into alternating block lengths
        # In t, the first block is guaranteed to be '1's, then '0's, '1's, '0's, etc.
        blocks = []
        curr_char = t[0]
        curr_len = 0
        
        for char in t:
            if char == curr_char:
                curr_len += 1
            else:
                blocks.append((curr_char, curr_len))
                curr_char = char
                curr_len = 1
        blocks.append((curr_char, curr_len))
        
        max_ones = initial_ones
        
        # Look for patterns of '0's -> '1's -> '0's in the block array
        # A valid inner block of '1's will have a preceding '0' block and a succeeding '0' block.
        for i in range(1, len(blocks) - 1):
            if blocks[i][0] == '1' and blocks[i-1][0] == '0' and blocks[i+1][0] == '0':
                zeroes_left = blocks[i-1][1]
                zeroes_right = blocks[i+1][1]
                
                # Gain in '1's is zeroes_left + zeroes_right
                current_total = initial_ones + zeroes_left + zeroes_right
                max_ones = max(max_ones, current_total)
                
        return max_ones