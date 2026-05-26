class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Convert to a set for O(1) lookups
        char_set = set(word)
        special_count = 0
        
        # Check all possible lowercase English letters
        for i in range(26):
            lower_char = chr(ord('a') + i)
            upper_char = chr(ord('A') + i)
            
            # If both forms exist in the word, it's a special letter
            if lower_char in char_set and upper_char in char_set:
                special_count += 1
                
        return special_count