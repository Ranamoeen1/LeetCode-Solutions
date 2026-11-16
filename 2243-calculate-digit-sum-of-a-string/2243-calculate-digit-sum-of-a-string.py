class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_s = []
            for i in range(0, len(s), k):
                group = s[i:i + k]
                group_sum = sum(int(digit) for digit in group)
                next_s.append(str(group_sum))
            s = "".join(next_s)
        return s




# class Solution:
#     def digitSum(self, s: str, k: int) -> str:
#         # Convert characters to raw integers once upfront (O(N) space, zero substring slicing later)
#         digits = [ord(ch) - 48 for ch in s]
        
#         while len(digits) > k:
#             next_digits = []
#             curr_sum = 0
#             count = 0
            
#             for d in digits:
#                 curr_sum += d
#                 count += 1
                
#                 if count == k:
#                     # Unpack the integer sum into individual base-10 digits directly
#                     if curr_sum >= 100:
#                         next_digits.append(curr_sum // 100)
#                         next_digits.append((curr_sum // 10) % 10)
#                         next_digits.append(curr_sum % 10)
#                     elif curr_sum >= 10:
#                         next_digits.append(curr_sum // 10)
#                         next_digits.append(curr_sum % 10)
#                     else:
#                         next_digits.append(curr_sum)
                    
#                     curr_sum = 0
#                     count = 0
            
#             # Flush any remaining partial group at the end
#             if count > 0:
#                 if curr_sum >= 100:
#                     next_digits.append(curr_sum // 100)
#                     next_digits.append((curr_sum // 10) % 10)
#                     next_digits.append(curr_sum % 10)
#                 elif curr_sum >= 10:
#                     next_digits.append(curr_sum // 10)
#                     next_digits.append(curr_sum % 10)
#                 else:
#                     next_digits.append(curr_sum)
                    
#             digits = next_digits
            
#         return "".join(chr(d + 48) for d in digits)

