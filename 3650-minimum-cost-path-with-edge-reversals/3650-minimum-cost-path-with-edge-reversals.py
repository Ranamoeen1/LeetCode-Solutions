class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        outgoing = [[] for _ in range(n)]
        incoming = [[] for _ in range(n)]
        
        for u, v, w in edges:
            outgoing[u].append((v, w))
            incoming[v].append((u, w))
        
        INF = float('inf')
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0
        
        pq = [(0, 0, 0)]  
        
        while pq:
            cost, u, used = heapq.heappop(pq)
            
            if cost > dist[u][used]:
                continue
            
            if u == n - 1:
                return cost
            
            for v, w in outgoing[u]:
                new_cost = cost + w
                if new_cost < dist[v][0]:
                    dist[v][0] = new_cost
                    heapq.heappush(pq, (new_cost, v, 0))
    
            if used == 0:
                for v, w in incoming[u]:  
                    new_cost = cost + 2 * w
                  
                    if new_cost < dist[v][0]:
                        dist[v][0] = new_cost
                        heapq.heappush(pq, (new_cost, v, 0))
               
                if cost < dist[u][1]:
                    dist[u][1] = cost
                    heapq.heappush(pq, (cost, u, 1))
        
        result = min(dist[n-1])
        return result if result != INF else -1