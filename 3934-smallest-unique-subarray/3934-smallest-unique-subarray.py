from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mod1, base1 = 10**9 + 7, 911382323
        mod2, base2 = 10**9 + 9, 972663749

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + val) % mod1
            pref2[i + 1] = (pref2[i] * base2 + val) % mod2

        def has_unique_of_length(length: int) -> bool:
            hashes = []
            for start in range(n - length + 1):
                end = start + length
                h1 = (pref1[end] - pref1[start] * pow1[length]) % mod1
                h2 = (pref2[end] - pref2[start] * pow2[length]) % mod2
                hashes.append((h1, h2))
            return any(count == 1 for count in Counter(hashes).values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_length(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans