class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = {}
        stack = []
        
        # Step 1: Precalculate matching bracket pairs
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        # Step 2: Traverse and build the result
        res = []
        curr = 0
        direction = 1  # 1 for forward, -1 for backward
        
        while curr < n:
            if s[curr] in '()':
                curr = pair[curr]    # Jump to matching parenthesis
                direction = -direction # Reverse movement direction
            else:
                res.append(s[curr])  # Append character
            
            curr += direction        # Move to next index in active direction
            
        return "".join(res)




# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         stack = []
        
#         for char in s:
#             if char == ')':
#                 # Collect characters until matching '(' is found
#                 temp = []
#                 while stack and stack[-1] != '(':
#                     temp.append(stack.pop())
#                 # Pop the matching '('
#                 stack.pop()
#                 # Push the reversed characters back onto the stack
#                 stack.extend(temp)
#             else:
#                 stack.append(char)
                
#         return "".join(stack)