class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Convert the number to string to reverse its digits
        str_n = str(n)
        # Reverse the string and convert back to integer (handles leading zeros)
        reversed_n = int(str_n[::-1])
        # Calculate absolute difference
        return abs(n - reversed_n)