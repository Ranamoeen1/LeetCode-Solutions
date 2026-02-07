class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        total_a = s.count('a')
        b_left = 0
        min_del = float('inf')
        
        min_del = total_a
        
        for i in range(n):
            if s[i] == 'b':
                b_left += 1
            a_left = (i + 1) - b_left
            a_right = total_a - a_left
            cost = b_left + a_right
            min_del = min(min_del, cost)
        
        return min_del