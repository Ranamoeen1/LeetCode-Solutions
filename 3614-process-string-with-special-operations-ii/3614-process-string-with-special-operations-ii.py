class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Array to store lengths after each operation
        lengths = []
        curr_len = 0
        
        for char in s:
            if char.isalpha():
                curr_len += 1
            elif char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass # Reversing doesn't change the length
            lengths.append(curr_len)
        
        # Out of bounds check
        if k < 0 or k >= curr_len:
            return '.'
            
        # Backtrack from the end to find the character at index k
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            prev_len = lengths[i-1] if i > 0 else 0
            
            if char.isalpha():
                if k == prev_len:
                    return char
            elif char == '*':
                # If a '*' happened, the string was longer before it.
                # Since k is valid for the final string, we don't need to adjust k's value,
                # because the deleted character was at an index >= final length.
                pass
            elif char == '#':
                # If k is in the duplicated part, wrap it around
                if k >= prev_len:
                    k %= prev_len
            elif char == '%':
                # Reverse mapping: new_index = length - 1 - old_index
                k = curr_len - 1 - k
                
            curr_len = prev_len
            
        return '.'