class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str],
                    cost: List[int]) -> int:

        n = len(source)

        strings = set(original) | set(changed)
        idx = {s: i for i, s in enumerate(strings)}
        m = len(strings)

        dist = [[math.inf] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            i, j = idx[o], idx[c]
            dist[i][j] = min(dist[i][j], w)

        for k in range(m):
            for i in range(m):
                if dist[i][k] == math.inf:
                    continue
                for j in range(m):
                    if dist[k][j] == math.inf:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  
        by_len = {}
        for o in strings:
            for c in strings:
                d = dist[idx[o]][idx[c]]
                if d < math.inf and len(o) == len(c):
                    L = len(o)
                    by_len.setdefault(L, []).append((o, c, d))

        dp = [math.inf] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            for L, rules in by_len.items():
                if i + L > n:
                    continue
                for o, c, w in rules:
                    if source.startswith(o, i) and target.startswith(c, i):
                        dp[i] = min(dp[i], w + dp[i + L])

        return -1 if dp[0] == math.inf else dp[0]
