# class Solution:
#     def isGood(self, nums: List[int]) -> bool:
#         # The expected 'n' is always length of nums - 1
#         n = len(nums) - 1
        
#         # A base[n] array must have at least 2 elements (base[1] = [1, 1])
#         if n < 1:
#             return False
        
#         # Sort the input to make comparison easy
#         nums.sort()
        
#         # Construct the target base[n] array: [1, 2, ..., n-1, n, n]
#         # range(1, n) gives [1, ..., n-1]
#         # We append [n, n] at the end
#         target = list(range(1, n)) + [n, n]
        
#         return nums == target


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        # If the array is empty or too small, it can't be 'base[n]'
        if n < 1: 
            return False
        
        # Frequency array to store counts of numbers 1 to n
        # We use n + 1 size to accommodate the index 'n'
        counts = [0] * (n + 1)
        
        for x in nums:
            # If any number is greater than n, it's immediately invalid
            if x > n:
                return False
            counts[x] += 1
            
        # Check counts: 1 to n-1 must appear once
        for i in range(1, n):
            if counts[i] != 1:
                return False
        
        # The number n must appear exactly twice
        return counts[n] == 2