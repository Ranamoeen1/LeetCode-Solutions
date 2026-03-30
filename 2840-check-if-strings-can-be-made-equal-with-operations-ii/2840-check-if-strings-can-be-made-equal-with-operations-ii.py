# class Solution:
#     def checkStrings(self, s1: str, s2: str) -> bool:
#         # Sort even-indexed and odd-indexed characters separately
#         even1 = sorted(s1[::2])
#         even2 = sorted(s2[::2])
#         odd1 = sorted(s1[1::2])
#         odd2 = sorted(s2[1::2])
        
#         return even1 == even2 and odd1 == odd2



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