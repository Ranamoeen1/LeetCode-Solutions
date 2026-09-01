class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # Find the 0-based indices of the minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Identify the smaller index (i) and larger index (j)
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)

        # 1. Remove both from the front
        opt1 = j + 1

        # 2. Remove both from the back
        opt2 = n - i

        # 3. Remove one from the front and one from the back
        opt3 = (i + 1) + (n - j)

        return min(opt1, opt2, opt3)