from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        MAXV = max(nums)

        # Step 1: SPF sieve
        spf = list(range(MAXV + 1))
        for i in range(2, int(MAXV ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAXV + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x):
            return x > 1 and spf[x] == x

        # Step 2: build prime -> indices map
        prime_to_indices = defaultdict(list)

        for idx, val in enumerate(nums):
            x = val
            seen_primes = set()

            while x > 1:
                p = spf[x]
                seen_primes.add(p)
                while x % p == 0:
                    x //= p

            for p in seen_primes:
                prime_to_indices[p].append(idx)

        # Step 3: BFS
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0

        while q:
            i = q.popleft()
            d = dist[i]

            if i == n - 1:
                return d

            # adjacent moves
            for nei in (i - 1, i + 1):
                if 0 <= nei < n and dist[nei] == -1:
                    dist[nei] = d + 1
                    q.append(nei)

            # teleportation
            val = nums[i]
            if is_prime(val):
                p = val
                if p in prime_to_indices:
                    for j in prime_to_indices[p]:
                        if dist[j] == -1:
                            dist[j] = d + 1
                            q.append(j)
                    # important: avoid reusing this teleport again
                    del prime_to_indices[p]

        return -1