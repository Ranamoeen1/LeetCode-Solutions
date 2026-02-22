class Solution:
    def binaryGap(self, n: int) -> int:
        # Convert to binary and remove the '0b' prefix
        binary = bin(n)[2:]
        
        # Track positions of 1's
        positions = []
        
        # Find all positions where we have 1's
        for i, bit in enumerate(binary):
            if bit == '1':
                positions.append(i)
        
        # If we have less than 2 ones, return 0
        if len(positions) < 2:
            return 0
        
        # Find maximum distance between consecutive 1's
        max_distance = 0
        for i in range(1, len(positions)):
            distance = positions[i] - positions[i-1]
            max_distance = max(max_distance, distance)
        
        return max_distance


# class Solution:
#     def binaryGap(self, n: int) -> int:
#         binary = bin(n)[2:]
        
#         max_distance = 0
#         last_one_pos = -1
        
#         for i, bit in enumerate(binary):
#             if bit == '1':
#                 if last_one_pos != -1:
#                     distance = i - last_one_pos
#                     max_distance = max(max_distance, distance)
#                 last_one_pos = i
        
#         return max_distance