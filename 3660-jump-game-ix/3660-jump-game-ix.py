class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # suffix minimums
        suf_min = [0] * n
        suf_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suf_min[i] = min(nums[i], suf_min[i + 1])

        ans = [0] * n

        start = 0
        pref_max = nums[0]
        comp_max = nums[0]

        for i in range(n - 1):
            pref_max = max(pref_max, nums[i])
            comp_max = max(comp_max, nums[i])

            # If no inversion exists across the cut,
            # current component ends here
            if pref_max <= suf_min[i + 1]:
                for j in range(start, i + 1):
                    ans[j] = comp_max

                start = i + 1
                pref_max = nums[start]
                comp_max = nums[start]

        # last component
        comp_max = max(nums[start:])
        for j in range(start, n):
            ans[j] = comp_max

        return ans