class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Low score can always be reduced to 0 by making two elements equal.
        # Minimize high score (max - min) by discarding two extreme values:
        return min(
            nums[n - 1] - nums[2],  # drop 2 smallest
            nums[n - 2] - nums[1],  # drop 1 smallest, 1 largest
            nums[n - 3] - nums[0],  # drop 2 largest
        )