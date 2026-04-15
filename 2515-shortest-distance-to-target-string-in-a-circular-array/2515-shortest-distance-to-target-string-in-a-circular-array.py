class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        
        # Check if target exists at start position
        if words[startIndex] == target:
            return 0
        
        # Search outward from startIndex
        for distance in range(1, n):
            # Check right
            right_idx = (startIndex + distance) % n
            if words[right_idx] == target:
                return distance
            
            # Check left
            left_idx = (startIndex - distance + n) % n
            if words[left_idx] == target:
                return distance
        
        return -1



# # class Solution:
# #     def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
# #         n = len(words)
# #         min_distance = float('inf')
        
# #         # Check each index in the array
# #         for i in range(n):
# #             if words[i] == target:
# #                 # Calculate clockwise distance
# #                 clockwise = (i - startIndex + n) % n
# #                 # Calculate counter-clockwise distance
# #                 counter_clockwise = (startIndex - i + n) % n
# #                 # Take the minimum of both directions for this occurrence
# #                 distance = min(clockwise, counter_clockwise)
# #                 # Update the global minimum
# #                 min_distance = min(min_distance, distance)
        
# #         return min_distance if min_distance != float('inf') else -1



# class Solution:
#     def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
#         n = len(words)
#         min_distance = float('inf')
        
#         # Check if target exists at start position
#         if words[startIndex] == target:
#             return 0
        
#         # Search in both directions simultaneously
#         for i in range(1, n):
#             # If we've found a distance smaller than current i, we can stop
#             if min_distance <= i:
#                 break
                
#             # Check right direction
#             right_idx = (startIndex + i) % n
#             if words[right_idx] == target:
#                 min_distance = min(min_distance, i)
            
#             # Check left direction
#             left_idx = (startIndex - i + n) % n
#             if words[left_idx] == target:
#                 min_distance = min(min_distance, i)
        
#         return min_distance if min_distance != float('inf') else -1