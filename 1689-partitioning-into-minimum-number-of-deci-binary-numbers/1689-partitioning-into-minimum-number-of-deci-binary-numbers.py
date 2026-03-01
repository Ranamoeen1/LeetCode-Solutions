class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = '0'
        for char in n:
            if char > max_digit:
                max_digit = char
                # Early exit if we find '9' (maximum possible)
                if max_digit == '9':
                    return 9
        return int(max_digit)