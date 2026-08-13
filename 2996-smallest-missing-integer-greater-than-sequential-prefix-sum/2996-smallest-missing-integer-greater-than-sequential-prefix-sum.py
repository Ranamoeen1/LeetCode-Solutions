class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Calculate the sum of the longest sequential prefix
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
        
        # Step 2: Store elements in a set for O(1) lookups
        num_set = set(nums)
        
        # Step 3: Find the smallest missing integer >= prefix_sum
        x = prefix_sum
        while x in num_set:
            x += 1
            
        return x