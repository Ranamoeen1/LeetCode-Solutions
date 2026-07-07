class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert the integer to string to process its digits
        digits = [d for d in str(n) if d != '0']
        
        # If there are no non-zero digits, x is 0
        if not digits:
            return 0
        
        # Form the integer x by concatenating the non-zero digits
        x = int("".join(digits))
        
        # Calculate the sum of the digits
        # Since they are characters, convert them back to integers to sum
        digit_sum = sum(int(d) for d in digits)
        
        # Return the product of x and the sum
        return x * digit_sum