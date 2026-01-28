class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18
        
        dist = [[[INF] * (k + 1) for _ in range(n)] for __ in range(m)]
        dist[0][0][0] = 0
        
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        
        ptr = [0] * (k + 1)
        
        pq = [(0, 0, 0, 0)]
        
        while pq:
            cost, r, c, t = heapq.heappop(pq)
            if cost > dist[r][c][t]:
                continue
            
            if r == m - 1 and c == n - 1:
                return cost
            
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + grid[nr][nc]
                    if new_cost < dist[nr][nc][t]:
                        dist[nr][nc][t] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc, t))
            
            if t < k:
                v = grid[r][c]
                p = ptr[t + 1]
                
                while p < len(cells) and cells[p][0] <= v:
                    _, x, y = cells[p]
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
                    p += 1
                
                ptr[t + 1] = p
        
        return -1
