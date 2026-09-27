class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Collect characters until matching '(' is found
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the matching '('
                stack.pop()
                # Push the reversed characters back onto the stack
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)