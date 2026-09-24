class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            # Calculate the sum of digits of num
            digit_sum = sum(int(digit) for digit in str(num))
            
            # Check if digit sum equals current index
            if digit_sum == i:
                return i
                
        return -1