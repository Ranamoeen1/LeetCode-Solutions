class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: odd length strings can never be balanced
        if len(s) % 2 != 0:
            return False
            
        stack = []
        matching_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_map:
                # Pop the top element if stack is non-empty, else assign dummy value
                top_element = stack.pop() if stack else '#'
                if matching_map[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)
                
        # If stack is empty, all brackets were validly matched
        return len(stack) == 0