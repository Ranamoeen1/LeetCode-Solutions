class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary for Roman numeral values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        # Traverse through the Roman numeral string
        for i in range(len(s)):
            # If the current symbol's value is less than the next symbol's value, subtract it
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        return total
