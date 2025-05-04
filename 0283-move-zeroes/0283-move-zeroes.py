class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0  # Position to place the next non-zero element

        # First pass: move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Second pass: fill the rest with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
