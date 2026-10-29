class SegmentTree:
    def __init__(self, n: int, init_vals: list[int]):
        self.n = n
        self.tree = [0] * (4 * n)
        if init_vals:
            self._build(1, 0, n - 1, init_vals)

    def _build(self, node: int, l: int, r: int, vals: list[int]):
        if l == r:
            self.tree[node] = vals[l]
            return
        mid = (l + r) // 2
        self._build(2 * node, l, mid, vals)
        self._build(2 * node + 1, mid + 1, r, vals)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self.query(2 * node, l, mid, ql, qr) ^ self.query(2 * node + 1, mid + 1, r, ql, qr)


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        import sys
        sys.setrecursionlimit(200000)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        sz = [0] * n

        def dfs1(u: int, p: int, d: int) -> int:
            parent[u] = p
            depth[u] = d
            size = 1
            max_subtree_sz = 0
            for v in adj[u]:
                if v != p:
                    sub_sz = dfs1(v, u, d + 1)
                    size += sub_sz
                    if sub_sz > max_subtree_sz:
                        max_subtree_sz = sub_sz
                        heavy[u] = v
            sz[u] = size
            return size

        dfs1(0, -1, 0)

        cur_pos = 0
        def dfs2(u: int, h: int):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)

        dfs2(0, 0)

        init_vals = [0] * n
        for i in range(n):
            init_vals[pos[i]] = 1 << (ord(s[i]) - ord('a'))

        seg = SegmentTree(n, init_vals)

        def path_xor(u: int, v: int) -> int:
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res ^= seg.query(1, 0, n - 1, pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= seg.query(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                ui = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                seg.update(1, 0, n - 1, pos[ui], new_mask)
            else:
                ui = int(parts[1])
                vi = int(parts[2])
                mask = path_xor(ui, vi)
                # Check if at most one bit is set
                is_palindrome = (mask == 0) or ((mask & (mask - 1)) == 0)
                ans.append(is_palindrome)

        return ans