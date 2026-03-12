class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
        self.cnt = n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        self.cnt -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def check(lim: int) -> bool:
            uf = UnionFind(n)
            for u, v, s, _ in edges:
                if s >= lim:
                    uf.union(u, v)
            rem = k
            for u, v, s, _ in edges:
                if s * 2 >= lim and rem > 0:
                    if uf.union(u, v):
                        rem -= 1
            return uf.cnt == 1

        uf = UnionFind(n)
        mn = 10**6
        for u, v, s, must in edges:
            if must:
                mn = min(mn, s)
                if not uf.union(u, v):
                    return -1
        for u, v, _, _ in edges:
            uf.union(u, v)
        if uf.cnt > 1:
            return -1
        l, r = 1, mn
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l



# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n
#         self.components = n
    
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
    
#     def union(self, x, y):
#         px, py = self.find(x), self.find(y)
#         if px == py:
#             return False
#         if self.rank[px] < self.rank[py]:
#             px, py = py, px
#         self.parent[py] = px
#         if self.rank[px] == self.rank[py]:
#             self.rank[px] += 1
#         self.components -= 1
#         return True

# class Solution:
#     def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
#         # Separate mandatory and optional edges
#         mandatory = []  # musti == 1
#         optional = []   # musti == 0
        
#         for u, v, s, must in edges:
#             if must == 1:
#                 mandatory.append((u, v, s))
#             else:
#                 optional.append((u, v, s))
        
#         # Check if mandatory edges form a cycle
#         uf_check = UnionFind(n)
#         for u, v, s in mandatory:
#             if not uf_check.union(u, v):
#                 return -1  # Cycle in mandatory edges
        
#         # Find max possible value for binary search
#         max_strength = 0
#         for u, v, s in mandatory:
#             max_strength = max(max_strength, s)
#         for u, v, s in optional:
#             max_strength = max(max_strength, s * 2)
        
#         # Binary search on answer
#         lo, hi = 0, max_strength + 1
#         ans = -1
        
#         def canAchieve(min_strength):
#             # Check mandatory edges first
#             for u, v, s in mandatory:
#                 if s < min_strength:
#                     return False
            
#             uf = UnionFind(n)
#             edges_used = 0
#             used_upgrades = 0
            
#             # Add all mandatory edges
#             for u, v, s in mandatory:
#                 if uf.union(u, v):
#                     edges_used += 1
            
#             # Collect optional edges that can be used
#             candidates = []
#             for u, v, s in optional:
#                 if s >= min_strength:
#                     candidates.append((0, s, u, v))  # 0 = no upgrade needed
#                 elif 2 * s >= min_strength:
#                     candidates.append((1, s, u, v))  # 1 = upgrade needed
            
#             # Sort: first by upgrade needed (0 before 1), then by strength desc
#             candidates.sort(key=lambda x: (x[0], -x[1]))
            
#             for need_upg, s, u, v in candidates:
#                 if uf.find(u) != uf.find(v):
#                     if need_upg == 1:
#                         if used_upgrades >= k:
#                             continue
#                         used_upgrades += 1
#                     if uf.union(u, v):
#                         edges_used += 1
#                         if edges_used == n - 1:
#                             return True
            
#             return edges_used == n - 1
        
#         while lo <= hi:
#             mid = (lo + hi) // 2
#             if canAchieve(mid):
#                 ans = mid
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
        
#         return ans


