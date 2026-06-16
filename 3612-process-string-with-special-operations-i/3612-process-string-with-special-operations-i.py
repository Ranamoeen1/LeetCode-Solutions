class Solution:
    def processStr(self, s: str) -> str:
        result = []
        
        for char in s:
            if char == '*':
                if result:
                    result.pop()
            elif char == '#':
                # Duplicate the current result
                result = result + result
            elif char == '%':
                # Reverse the current result
                result.reverse()
            else:
                # Append lowercase English letter
                result.append(char)
                
        return "".join(result)