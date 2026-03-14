# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:
#         self.result = ""
#         self.count = 0
        
#         def backtrack(current):
#             if self.result:
#                 return
            
#             if len(current) == n:
#                 self.count += 1
#                 if self.count == k:
#                     self.result = current
#                 return
            
#             for char in ['a', 'b', 'c']:
#                 if current and current[-1] == char:
#                     continue
#                 backtrack(current + char)
        
#         backtrack("")
#         return self.result   


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Total number of happy strings of length n = 3 * 2^(n-1)
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""
        
        result = []
        
        # Available choices for each position
        # For first character: all 3 letters
        # For subsequent characters: any letter except the previous one
        choices = ['a', 'b', 'c']
        
        # Build the string character by character
        for i in range(n):
            # Try each possible character in lexicographical order
            for c in choices:
                # Skip if this character is the same as the last character
                if result and result[-1] == c:
                    continue
                
                # Calculate how many strings would start with this prefix
                if i == 0:
                    # For first character: each choice leads to 2^(n-1) strings
                    count = 1 << (n - 1)
                else:
                    # For other characters: each choice leads to 2^(n-i-1) strings
                    count = 1 << (n - i - 1)
                
                if k > count:
                    # Skip all strings starting with this prefix
                    k -= count
                else:
                    # This prefix leads to the kth string
                    result.append(c)
                    break
        
        return ''.join(result)