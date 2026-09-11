from typing import List
from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = Counter(digits)
        
        def backtrack(depth: int, current_num: int) -> int:
            valid_count = 0
            
            for d in list(counts.keys()):
                if counts[d] == 0:
                    continue
                
                # Rule 1: First digit cannot be 0 (no leading zeros)
                if depth == 0 and d == 0:
                    continue
                
                # Rule 2: Third digit must be even
                if depth == 2 and d % 2 != 0:
                    continue
                
                # Choose digit
                counts[d] -= 1
                
                if depth == 2:
                    valid_count += 1
                else:
                    valid_count += backtrack(depth + 1, current_num * 10 + d)
                
                # Backtrack
                counts[d] += 1
                
            return valid_count

        return backtrack(0, 0)




# from typing import List
# from collections import Counter

# class Solution:
#     def totalNumbers(self, digits: List[int]) -> int:
#         freq = Counter(digits)
#         count = 0
        
#         # Iterate over all possible 3-digit even numbers
#         for num in range(100, 1000, 2):
#             # Extract individual digits
#             d1 = num // 100
#             d2 = (num // 10) % 10
#             d3 = num % 10
            
#             # Count the frequency of required digits for the current number
#             req = Counter([d1, d2, d3])
            
#             # Check if all required digits can be supplied by `freq`
#             if all(freq[digit] >= req_count for digit, req_count in req.items()):
#                 count += 1
                
#         return count