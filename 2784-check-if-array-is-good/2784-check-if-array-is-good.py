class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # The expected 'n' is always length of nums - 1
        n = len(nums) - 1
        
        # A base[n] array must have at least 2 elements (base[1] = [1, 1])
        if n < 1:
            return False
        
        # Sort the input to make comparison easy
        nums.sort()
        
        # Construct the target base[n] array: [1, 2, ..., n-1, n, n]
        # range(1, n) gives [1, ..., n-1]
        # We append [n, n] at the end
        target = list(range(1, n)) + [n, n]
        
        return nums == target