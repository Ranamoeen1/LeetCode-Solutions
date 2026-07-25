class Solution:
    def maxProduct(self, n: int) -> int:
        # Convert integer to string of digit characters, then to integer digits
        digits = [int(d) for d in str(n)]
        
        # Sort digits in ascending order
        digits.sort()
        
        # Multiply the two largest digits (the last two elements)
        return digits[-1] * digits[-2]