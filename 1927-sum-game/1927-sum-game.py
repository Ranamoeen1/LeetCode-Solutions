class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        s1 = sum(int(c) for c in num[:half] if c != '?')
        s2 = sum(int(c) for c in num[half:] if c != '?')
        
        q1 = num[:half].count('?')
        q2 = num[half:].count('?')
        
        # Alice wins if the total count of '?' is odd
        if (q1 + q2) % 2 != 0:
            return True
        
        # Bob wins if and only if the difference in known sums 
        # offsets the difference in '?' counts scaled by 9/2
        return (s1 - s2) != (q2 - q1) * 9 // 2