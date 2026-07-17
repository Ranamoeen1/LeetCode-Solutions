from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Step 1: Direct frequency map using a flat array (much faster than collections.Counter)
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        # Step 2: Compute how many numbers are multiples of each i
        cnt = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                cnt[i] += freq[j]
                
        # Step 3: Compute the exact number of pairs with GCD equal to i
        # Iterating backwards allows us to subtract counts of larger multiples in-place
        exact_pairs = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            c = cnt[i]
            total_pairs = (c * (c - 1)) // 2
            
            # Fast inner loop subtraction
            for j in range(2 * i, max_val + 1, i):
                total_pairs -= exact_pairs[j]
                
            exact_pairs[i] = total_pairs
            
        # Step 4: Create a prefix sum array of the counts
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + exact_pairs[i]
            
        # Step 5: Answer each query using binary search
        # List comprehension provides a slight C-level optimization over standard for loops
        return [bisect.bisect_right(prefix_sums, q) for q in queries]



# from typing import List
# import collections
# import bisect

# class Solution:
#     def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
#         max_val = max(nums)
        
#         # Step 1: Count frequency of each number
#         freq = collections.Counter(nums)
        
#         # Step 2: Count how many numbers are multiples of each value i
#         cnt = [0] * (max_val + 1)
#         for i in range(1, max_val + 1):
#             for j in range(i, max_val + 1, i):
#                 cnt[i] += freq[j]
                
#         # Step 3: Compute the exact number of pairs with GCD equal to i
#         # We process in reverse order to subtract counts of higher multiples
#         exact_pairs = [0] * (max_val + 1)
#         for i in range(max_val, 0, -1):
#             total_pairs = (cnt[i] * (cnt[i] - 1)) // 2
#             # Subtract pairs that have a GCD that is a strict multiple of i
#             for j in range(2 * i, max_val + 1, i):
#                 total_pairs -= exact_pairs[j]
#             exact_pairs[i] = total_pairs
            
#         # Step 4: Create a prefix sum of the pair counts to find the index ranges
#         prefix_sums = [0] * (max_val + 1)
#         for i in range(1, max_val + 1):
#             prefix_sums[i] = prefix_sums[i - 1] + exact_pairs[i]
            
#         # Step 5: Answer each query using binary search
#         ans = []
#         for q in queries:
#             # bisect_right finds the first position where prefix_sums[idx] > q
#             idx = bisect.bisect_right(prefix_sums, q)
#             ans.append(idx)
            
#         return ans