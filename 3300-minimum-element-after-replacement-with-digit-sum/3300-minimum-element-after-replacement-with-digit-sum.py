class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float('inf')
        
        for num in nums:
            current_sum = 0
            # Extract digits mathematically
            while num > 0:
                current_sum += num % 10  # Get the last digit
                num //= 10               # Remove the last digit
            
            # Update the minimum sum found
            if current_sum < min_sum:
                min_sum = current_sum
                
        return min_sum




# class Solution:
#     def minElement(self, nums: List[int]) -> int:
#         min_sum = float('inf')
        
#         for num in nums:
#             # Calculate the sum of digits for the current number
#             digit_sum = sum(int(digit) for digit in str(num))
            
#             # Update the minimum encountered so far
#             if digit_sum < min_sum:
#                 min_sum = digit_sum
                
#         return min_sum


