class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Map each digit to its rotated version
        # Invalid digits map to -1
        rotate_map = {
            0: 0, 1: 1, 2: 5, 5: 2, 
            6: 9, 8: 8, 9: 6,
            3: -1, 4: -1, 7: -1
        }
        
        count = 0
        
        # Check each number from 1 to n
        for num in range(1, n + 1):
            valid = True
            changed = False
            temp = num
            
            while temp > 0:
                digit = temp % 10
                if rotate_map[digit] == -1:
                    valid = False
                    break
                # If digit changes when rotated (2,5,6,9)
                if digit in {2, 5, 6, 9}:
                    changed = True
                temp //= 10
            
            # If number is valid and at least one digit changes
            if valid and changed:
                count += 1
        
        return count


# class Solution:
#     def rotatedDigits(self, n: int) -> int:
        
#         count = 0
#         # Check numbers from 1 to n
#         for num in range(1, n + 1):
#             num_str = str(num)
#             # Check if all digits are valid
#             if all(c in '0125689' for c in num_str):
#                 # Check if at least one digit changes (2,5,6,9)
#                 if any(c in '2569' for c in num_str):
#                     count += 1
#         return count


# class Solution:
#     def rotatedDigits(self, n: int) -> int:
#         # Convert n to string for digit DP
#         s = str(n)
#         length = len(s)
        
#         # Digit mapping: 0=valid but same, 1=valid and changes, -1=invalid
#         # valid digits: 0,1,8 (type 0), 2,5,6,9 (type 1), others invalid
#         digit_type = {
#             '0': 0, '1': 0, '8': 0,  # same after rotation
#             '2': 1, '5': 1, '6': 1, '9': 1,  # changes after rotation
#         }
#         # 3,4,7 are invalid (not in dict)
        
#         from functools import lru_cache
        
#         @lru_cache(None)
#         def dp(pos, is_limit, has_changed):
#             """
#             pos: current position we're filling (0 to length)
#             is_limit: whether previous digits match n's prefix (tight bound)
#             has_changed: whether we've used any changing digit (2,5,6,9) so far
#             """
#             if pos == length:
#                 # Reached end - valid if we used at least one changing digit
#                 return 1 if has_changed else 0
            
#             # Determine the maximum digit we can place at this position
#             max_digit = int(s[pos]) if is_limit else 9
#             total = 0
            
#             # Try all possible digits at current position
#             for d in range(max_digit + 1):
#                 digit_char = str(d)
                
#                 # Skip invalid digits
#                 if digit_char not in digit_type:
#                     continue
                
#                 # Check if digit changes when rotated
#                 digit_changes = (digit_type[digit_char] == 1)
                
#                 # Recursive call for next position
#                 total += dp(
#                     pos + 1, 
#                     is_limit and (d == max_digit),  # new is_limit
#                     has_changed or digit_changes      # update has_changed flag
#                 )
            
#             return total
        
#         # Count all good numbers from 1 to n, exclude 0
#         result = dp(0, True, False)
        
#         # Subtract 1 to exclude 0 (if we're counting from 0, but we start from 1)
#         # Since our DP includes 0, we need to remove it if it was counted
#         # But 0 should not be counted anyway because has_changed=False
#         # So result already doesn't count 0
#         return result