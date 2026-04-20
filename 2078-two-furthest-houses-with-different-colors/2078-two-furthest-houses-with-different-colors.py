# # class Solution:
# #     def maxDistance(self, colors: List[int]) -> int:
# #         n = len(colors)
# #         max_dist = 0
        
# #         # Check distances from first house to all other houses
# #         for i in range(n):
# #             if colors[i] != colors[0]:
# #                 max_dist = max(max_dist, i - 0)
        
# #         # Check distances from last house to all other houses
# #         for i in range(n):
# #             if colors[i] != colors[n-1]:
# #                 max_dist = max(max_dist, (n-1) - i)
        
# #         return max_dist


# class Solution:
#     def maxDistance(self, colors: List[int]) -> int:
#         n = len(colors)
        
#         # Find the farthest index from the start that has a different color
#         left_dist = 0
#         for i in range(n - 1, -1, -1):
#             if colors[i] != colors[0]:
#                 left_dist = i
#                 break
        
#         # Find the farthest index from the end that has a different color
#         right_dist = 0
#         for i in range(n):
#             if colors[i] != colors[n - 1]:
#                 right_dist = n - 1 - i
#                 break
        
#         return max(left_dist, right_dist)


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        # Check from left: find rightmost house with different color from first
        i = n - 1
        while i >= 0 and colors[i] == colors[0]:
            i -= 1
        max_dist = i if i >= 0 else 0
        
        # Check from right: find leftmost house with different color from last
        j = 0
        while j < n and colors[j] == colors[n - 1]:
            j += 1
        
        return max(max_dist, n - 1 - j)