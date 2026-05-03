# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         if len(s) != len(goal):
#             return False
#         return goal in (s + s)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        n = len(s)
        
        # Try all possible shifts
        for i in range(n):
            # Check if shifting s by i positions gives goal
            # A shift by i means: s[i:] + s[:i]
            if s[i:] + s[:i] == goal:
                return True
        
        return False