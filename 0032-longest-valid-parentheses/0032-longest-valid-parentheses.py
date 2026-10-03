class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # Base index for boundary calculation
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' is unmatched; set it as the new base boundary
                    stack.append(i)
                else:
                    # Length of current valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len