class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        insertions_needed = 0

        for char in s:
            if char == '(':
                open_needed += 1
            else:
                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions_needed += 1

        return open_needed + insertions_needed