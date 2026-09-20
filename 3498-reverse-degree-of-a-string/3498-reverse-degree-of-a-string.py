class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for idx, char in enumerate(s, start=1):
            rev_val = 26 - (ord(char) - ord('a'))
            total += rev_val * idx
        return total