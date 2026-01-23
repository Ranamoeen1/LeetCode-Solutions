from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        left = [i - 1 for i in range(n)]
        right = [i + 1 for i in range(n)]
        right[-1] = -1
        alive = [True] * n

        # Count initial violations
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1
        if bad == 0:
            return 0

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while heap:
            pair_sum, i = heapq.heappop(heap)
            j = right[i]

            if (
                j == -1 or
                not alive[i] or
                not alive[j] or
                pair_sum != nums[i] + nums[j]
            ):
                continue

            li = left[i]
            rj = right[j]

            # Remove old violations
            if li != -1 and nums[li] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if rj != -1 and nums[j] > nums[rj]:
                bad -= 1

            # Merge
            nums[i] += nums[j]
            alive[j] = False
            right[i] = rj
            if rj != -1:
                left[rj] = i

            # Add new violations
            if li != -1 and nums[li] > nums[i]:
                bad += 1
            if rj != -1 and nums[i] > nums[rj]:
                bad += 1

            # Push new adjacent pairs
            if li != -1:
                heapq.heappush(heap, (nums[li] + nums[i], li))
            if rj != -1:
                heapq.heappush(heap, (nums[i] + nums[rj], i))

            ops += 1
            if bad == 0:
                return ops

        return ops
