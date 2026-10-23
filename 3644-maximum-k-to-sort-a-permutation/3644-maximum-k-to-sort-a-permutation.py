from functools import reduce
from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Start with -1 (all bits set to 1) and cumulatively AND only the misplaced elements
        ans = reduce(lambda acc, pair: acc & pair[1] if pair[0] != pair[1] else acc, enumerate(nums), -1)
        return max(ans, 0)





# class Solution:
#     def sortPermutation(self, nums: List[int]) -> int:
#         k = None
        
#         for i, val in enumerate(nums):
#             if val != i:
#                 if k is None:
#                     k = val
#                 else:
#                     k &= val
        
#         # If the array was already sorted, k remains None, so return 0
#         return k if k is not None else 0