from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        maxv = max(nums)

        # Step 1: sieve primes
        is_prime = [True] * (maxv + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(maxv ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, maxv + 1, i):
                    is_prime[j] = False

        # Step 2: value → indices compression bucket
        value_to_indices = defaultdict(list)
        for i, v in enumerate(nums):
            value_to_indices[v].append(i)

        # Step 3: prime → precomputed teleport bucket (lazy)
        prime_bucket = {}

        def build_bucket(p: int):
            """Build all indices reachable via prime p"""
            if p in prime_bucket:
                return prime_bucket[p]

            res = []
            for multiple in range(p, maxv + 1, p):
                if multiple in value_to_indices:
                    res.extend(value_to_indices[multiple])

            prime_bucket[p] = res
            return res

        # Step 4: BFS
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0

        used_prime = set()

        while q:
            i = q.popleft()
            d = dist[i]

            if i == n - 1:
                return d

            # adjacent moves
            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = d + 1
                q.append(i + 1)

            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = d + 1
                q.append(i - 1)

            # teleport
            val = nums[i]

            if val <= maxv and is_prime[val] and val not in used_prime:
                used_prime.add(val)

                # O(1) after first build
                for j in build_bucket(val):
                    if dist[j] == -1:
                        dist[j] = d + 1
                        q.append(j)

                # free memory aggressively (important for 1e5 scale)
                prime_bucket[val] = []

        return -1





# from typing import List
# from collections import defaultdict, deque

# class Solution:
#     def minJumps(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return 0

#         MAXV = max(nums)

#         # Step 1: SPF sieve
#         spf = list(range(MAXV + 1))
#         for i in range(2, int(MAXV ** 0.5) + 1):
#             if spf[i] == i:
#                 for j in range(i * i, MAXV + 1, i):
#                     if spf[j] == j:
#                         spf[j] = i

#         def is_prime(x):
#             return x > 1 and spf[x] == x

#         # Step 2: build prime -> indices map
#         prime_to_indices = defaultdict(list)

#         for idx, val in enumerate(nums):
#             x = val
#             seen_primes = set()

#             while x > 1:
#                 p = spf[x]
#                 seen_primes.add(p)
#                 while x % p == 0:
#                     x //= p

#             for p in seen_primes:
#                 prime_to_indices[p].append(idx)

#         # Step 3: BFS
#         q = deque([0])
#         dist = [-1] * n
#         dist[0] = 0

#         while q:
#             i = q.popleft()
#             d = dist[i]

#             if i == n - 1:
#                 return d

#             # adjacent moves
#             for nei in (i - 1, i + 1):
#                 if 0 <= nei < n and dist[nei] == -1:
#                     dist[nei] = d + 1
#                     q.append(nei)

#             # teleportation
#             val = nums[i]
#             if is_prime(val):
#                 p = val
#                 if p in prime_to_indices:
#                     for j in prime_to_indices[p]:
#                         if dist[j] == -1:
#                             dist[j] = d + 1
#                             q.append(j)
#                     # important: avoid reusing this teleport again
#                     del prime_to_indices[p]

#         return -1


# from typing import List
# from collections import defaultdict, deque

# class Solution:
#     def minJumps(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return 0

#         maxv = max(nums)

#         # Step 1: simple prime sieve (boolean only)
#         is_prime = [True] * (maxv + 1)
#         is_prime[0] = is_prime[1] = False

#         for i in range(2, int(maxv ** 0.5) + 1):
#             if is_prime[i]:
#                 for j in range(i * i, maxv + 1, i):
#                     is_prime[j] = False

#         # Step 2: value -> indices mapping (cheap & small)
#         value_pos = defaultdict(list)
#         for i, v in enumerate(nums):
#             value_pos[v].append(i)

#         # Step 3: BFS
#         q = deque([0])
#         dist = [-1] * n
#         dist[0] = 0

#         used_prime = set()

#         while q:
#             i = q.popleft()
#             d = dist[i]

#             if i == n - 1:
#                 return d

#             # adjacent moves
#             for ni in (i - 1, i + 1):
#                 if 0 <= ni < n and dist[ni] == -1:
#                     dist[ni] = d + 1
#                     q.append(ni)

#             val = nums[i]

#             # prime teleportation only if current value is prime
#             if val <= maxv and is_prime[val] and val not in used_prime:
#                 p = val
#                 used_prime.add(p)

#                 # scan all multiples of p
#                 for multiple in range(p, maxv + 1, p):
#                     if multiple in value_pos:
#                         for j in value_pos[multiple]:
#                             if dist[j] == -1:
#                                 dist[j] = d + 1
#                                 q.append(j)

#                 # optional cleanup (saves repeated dictionary lookups)
#                 # value_pos[p].clear()

#         return -1