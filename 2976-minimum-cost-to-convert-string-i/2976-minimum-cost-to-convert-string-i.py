class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**15
        dist = [[INF] * 26 for _ in range(26)]
        
        # Distance from a node to itself is 0
        for i in range(26):
            dist[i][i] = 0
        
        # Add given edges
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        # Floyd-Warshall for all pairs shortest path
        for k in range(26):
            for i in range(26):
                if dist[i][k] < INF:
                    for j in range(26):
                        if dist[k][j] < INF:
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        total = 0
        for sc, tg in zip(source, target):
            if sc == tg:
                continue
            u = ord(sc) - ord('a')
            v = ord(tg) - ord('a')
            if dist[u][v] >= INF:
                return -1
            total += dist[u][v]
        
        return total