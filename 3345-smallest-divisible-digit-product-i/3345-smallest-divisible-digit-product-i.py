class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # Calculate the product of digits of the current number
            prod = 1
            for digit in str(n):
                prod *= int(digit)
            
            # Check if the digit product is divisible by t
            if prod % t == 0:
                return n
            
            # Move to the next number
            n += 1