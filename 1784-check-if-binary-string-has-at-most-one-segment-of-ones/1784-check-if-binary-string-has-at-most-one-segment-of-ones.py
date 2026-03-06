# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         zero_index = s.find('0')
        
#         if zero_index == -1:
#             return True
        
#         return '1' not in s[zero_index:]

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
     
        found_zero = False
        
        for i in range(len(s)):
            if s[i] == '0':
                found_zero = True
            elif found_zero and s[i] == '1':
                return False
        
        return True