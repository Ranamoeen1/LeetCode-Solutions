class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count occurrences of each vital character
        b = text.count('b')
        a = text.count('a')
        l = text.count('l') // 2  # 'balloon' requires 2 'l's
        o = text.count('o') // 2  # 'balloon' requires 2 'o's
        n = text.count('n')
        
        # The limiting character determines the maximum number of words
        return min(b, a, l, o, n)