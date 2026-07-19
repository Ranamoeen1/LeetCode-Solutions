class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Find the last occurrence index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        visited = set()  # Keeps track of characters currently in our stack
        
        for i, char in enumerate(s):
            # If the character is already in our answer, we skip it
            if char in visited:
                continue
                
            # Pop characters from the stack if they are lexicographically larger
            # than the current character AND appear again later in the string
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                visited.remove(removed_char)
                
            # Add the current character to our stack and mark it as visited
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)