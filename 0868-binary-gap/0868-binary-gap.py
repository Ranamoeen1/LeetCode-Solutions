class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        
        max_distance = 0
        last_one_pos = -1
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if last_one_pos != -1:
                    distance = i - last_one_pos
                    max_distance = max(max_distance, distance)
                last_one_pos = i
        
        return max_distance