class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lowercase = {}
        first_uppercase = {}
        
        # Iterate through the string to populate the maps
        for i, char in enumerate(word):
            if char.islower():
                last_lowercase[char] = i
            else:
                if char not in first_uppercase:
                    first_uppercase[char] = i
                    
        special_count = 0
        
        # Check all 26 possible English letters
        for ascii_code in range(ord('a'), ord('z') + 1):
            lower_ch = chr(ascii_code)
            upper_ch = lower_ch.upper()
            
            # Condition: both must exist, and the last lowercase must 
            # appear before the first uppercase
            if lower_ch in last_lowercase and upper_ch in first_uppercase:
                if last_lowercase[lower_ch] < first_uppercase[upper_ch]:
                    special_count += 1
                    
        return special_count