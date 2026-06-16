# class Solution:
#     def processStr(self, s: str) -> str:
#         result = []
        
#         for char in s:
#             if char == '*':
#                 if result:
#                     result.pop()
#             elif char == '#':
#                 # Duplicate the current result
#                 result = result + result
#             elif char == '%':
#                 # Reverse the current result
#                 result.reverse()
#             else:
#                 # Append lowercase English letter
#                 result.append(char)
                
#         return "".join(result)


from collections import deque

class Solution:
    def processStr(self, s: str) -> str:
        result = deque()
        is_reversed = False
        
        for char in s:
            if char == '*':
                if result:
                    if is_reversed:
                        result.popleft() # If reversed, the "last" char is at the front
                    else:
                        result.pop()     # Otherwise, it's at the back
            elif char == '#':
                # In-place extension is faster than creating a brand new list
                result.extend(list(result))
            elif char == '%':
                # O(1) toggle instead of O(N) physical reversal
                is_reversed = not is_reversed
            else:
                if is_reversed:
                    result.appendleft(char) # Fixed: passed 'char' here
                else:
                    result.append(char)
                    
        res_list = list(result)
        if is_reversed:
            res_list.reverse()
            
        return "".join(res_list)