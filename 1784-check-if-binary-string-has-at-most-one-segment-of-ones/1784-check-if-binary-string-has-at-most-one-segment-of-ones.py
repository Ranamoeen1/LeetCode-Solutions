class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        zero_index = s.find('0')
        
        if zero_index == -1:
            return True
        
        return '1' not in s[zero_index:]