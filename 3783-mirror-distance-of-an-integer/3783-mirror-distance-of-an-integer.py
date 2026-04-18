# class Solution:
#     def mirrorDistance(self, n: int) -> int:
#         # Convert the number to string to reverse its digits
#         str_n = str(n)
#         # Reverse the string and convert back to integer (handles leading zeros)
#         reversed_n = int(str_n[::-1])
#         # Calculate absolute difference
#         return abs(n - reversed_n)

class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        reversed_n = 0
        
        # Reverse the number mathematically
        while n > 0:
            reversed_n = reversed_n * 10 + (n % 10)
            n //= 10
        
        return abs(original - reversed_n)