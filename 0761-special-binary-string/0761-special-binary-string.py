class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ""
        
        count = 0
        i = 0
        result = []
        
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                result.append('1' + self.makeLargestSpecial(s[i+1:j]) + '0')
                i = j + 1
        
        result.sort(reverse=True)
        
        return ''.join(result)