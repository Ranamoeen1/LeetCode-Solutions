class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         if len(s) != len(goal):
#             return False
        
#         n = len(s)
        
#         # Try all possible shifts
#         for i in range(n):
#             # Check if shifting s by i positions gives goal
#             # A shift by i means: s[i:] + s[:i]
#             if s[i:] + s[:i] == goal:
#                 return True
        
#         return False

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         if len(s) != len(goal):
#             return False
#         if len(s) == 0:
#             return True
        
#         n = len(s)
        
#         # Find all starting positions where s[0] matches goal[k]
#         matches = []
#         for i in range(n):
#             if goal[i] == s[0]:
#                 matches.append(i)
        
#         # For each possible rotation point, check if it's valid
#         for start in matches:
#             # Check if rotating s by (n - start) positions gives goal
#             valid = True
#             for i in range(n):
#                 # s[i] should match goal[(start + i) % n]
#                 if s[i] != goal[(start + i) % n]:
#                     valid = False
#                     break
#             if valid:
#                 return True
        
#         return False