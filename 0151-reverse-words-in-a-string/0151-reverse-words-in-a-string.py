class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print (words)
        words.reverse()
        print (words)
        return " ".join(words)