class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        # Separate even and odd indexed characters for both strings
        s1_even = s1[0::2]  # characters at indices 0, 2, 4, ...
        s1_odd = s1[1::2]   # characters at indices 1, 3, 5, ...
        
        s2_even = s2[0::2]
        s2_odd = s2[1::2]
        
        # Check if both multisets match
        return Counter(s1_even) == Counter(s2_even) and Counter(s1_odd) == Counter(s2_odd)