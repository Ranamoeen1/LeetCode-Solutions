# class Solution:
#     def rotatedDigits(self, n: int) -> int:
#         # Map each digit to its rotated version
#         # Invalid digits map to -1
#         rotate_map = {
#             0: 0, 1: 1, 2: 5, 5: 2, 
#             6: 9, 8: 8, 9: 6,
#             3: -1, 4: -1, 7: -1
#         }
        
#         count = 0
        
#         # Check each number from 1 to n
#         for num in range(1, n + 1):
#             valid = True
#             changed = False
#             temp = num
            
#             while temp > 0:
#                 digit = temp % 10
#                 if rotate_map[digit] == -1:
#                     valid = False
#                     break
#                 # If digit changes when rotated (2,5,6,9)
#                 if digit in {2, 5, 6, 9}:
#                     changed = True
#                 temp //= 10
            
#             # If number is valid and at least one digit changes
#             if valid and changed:
#                 count += 1
        
#         return count


class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        count = 0
        # Check numbers from 1 to n
        for num in range(1, n + 1):
            num_str = str(num)
            # Check if all digits are valid
            if all(c in '0125689' for c in num_str):
                # Check if at least one digit changes (2,5,6,9)
                if any(c in '2569' for c in num_str):
                    count += 1
        return count