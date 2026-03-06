# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         zero_index = s.find('0')
        
#         if zero_index == -1:
#             return True
        
#         return '1' not in s[zero_index:]

# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
     
#         found_zero = False
        
#         for i in range(len(s)):
#             if s[i] == '0':
#                 found_zero = True
#             elif found_zero and s[i] == '1':
#                 return False
        
#         return True


# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         count_01 = 0
        
#         for i in range(len(s) - 1):
#             if s[i] == '0' and s[i+1] == '1':
#                 count_01 += 1
       
#         return count_01 == 0



# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         import re
#         return bool(re.match(r'^1+0*$', s))


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        compressed = []
        for i in range(len(s)):
            if i == 0 or s[i] != s[i-1]:
                compressed.append(s[i])
        
        ones_count = compressed.count('1')
        
        return ones_count <= 1