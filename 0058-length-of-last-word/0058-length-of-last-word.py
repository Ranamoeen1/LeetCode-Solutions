class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string by spaces and filter out empty strings
        words = s.split()
        
        # If there are no words, return 0 (though constraints say at least one word)
        if not words:
            return 0
            
        # Return the length of the last word
        return len(words[-1])

if __name__ == "__main__":
    solution = Solution()
    