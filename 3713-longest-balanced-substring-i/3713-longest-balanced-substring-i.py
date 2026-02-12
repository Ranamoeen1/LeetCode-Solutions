class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_length = 0
        
        for i in range(n):
            freq = {}
            
            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                
                if len(freq) > 0:
                    values = list(freq.values())
                    if len(set(values)) == 1:
                        max_length = max(max_length, j - i + 1)
        
        return max_length