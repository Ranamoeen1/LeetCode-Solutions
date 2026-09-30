class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Assign based on the current depth parity, then increment
                ans.append(depth % 2)
                depth += 1
            else: # char == ')'
                # Decrement depth first to match its corresponding '(' parity
                depth -= 1
                ans.append(depth % 2)
                
        return ans