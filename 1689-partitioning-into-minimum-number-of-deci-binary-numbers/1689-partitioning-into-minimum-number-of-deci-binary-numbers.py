class Solution:
    def minPartitions(self, n: str) -> int:
        from functools import reduce
        
        # Use reduce to find maximum digit
        def get_max(a, b):
            return a if a > int(b) else int(b)
        
        return reduce(get_max, n, 0)

# class Solution:
#     def minPartitions(self, n: str) -> int:
#         # Convert string to list of integers and find max
#         digits = [int(d) for d in n]
#         return max(digits)

# class Solution:
#     def minPartitions(self, n: str) -> int:
#         result = 0
#         for digit in n:
#             # Convert char to int and update maximum
#             current = ord(digit) - ord('0')
#             if current > result:
#                 result = current
#             # Early termination if we found the maximum possible digit
#             if result == 9:
#                 return 9
#         return result

# class Solution:
#     def minPartitions(self, n: str) -> int:
#         # Find the maximum character and convert to integer
#         return int(max(n, key=lambda x: int(x)))


# class Solution:
#     def minPartitions(self, n: str) -> int:
#         max_digit = '0'
#         for char in n:
#             if char > max_digit:
#                 max_digit = char
#                 # Early exit if we find '9' (maximum possible)
#                 if max_digit == '9':
#                     return 9
#         return int(max_digit)