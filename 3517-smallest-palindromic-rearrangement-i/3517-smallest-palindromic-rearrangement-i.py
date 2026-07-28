class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        
        left_half = []
        middle = ""
        
        # Characters in Counter/dict order can be sorted alphabetically
        for char in sorted(freq.keys()):
            count = freq[char]
            
            # If the count is odd, store the single middle character
            if count % 2 != 0:
                middle = char
                
            # Add half of the character's occurrences to the left half
            left_half.append(char * (count // 2))
            
        left_str = "".join(left_half)
        
        # Palindrome = Left Half + Middle + Reversed Left Half
        return left_str + middle + left_str[::-1]