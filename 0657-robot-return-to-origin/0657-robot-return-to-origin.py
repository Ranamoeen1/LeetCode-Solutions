class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts = Counter(moves)
        return counts['U'] == counts['D'] and counts['L'] == counts['R']


# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         # Count each type of move
#         count = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        
#         for move in moves:
#             count[move] += 1
        
#         # Check if ups match downs and lefts match rights
#         return count['U'] == count['D'] and count['L'] == count['R']




# # class Solution:
# #     def judgeCircle(self, moves: str) -> bool:
# #         # Initialize position
# #         x, y = 0, 0
        
# #         # Process each move
# #         for move in moves:
# #             if move == 'U':
# #                 y += 1
# #             elif move == 'D':
# #                 y -= 1
# #             elif move == 'R':
# #                 x += 1
# #             elif move == 'L':
# #                 x -= 1
        
# #         # Check if back at origin
# #         return x == 0 and y == 0