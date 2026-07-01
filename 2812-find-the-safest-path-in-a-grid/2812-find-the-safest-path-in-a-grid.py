from collections import deque
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If the start or end cell contains a thief, the safeness factor is automatically 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-source BFS to calculate distance to the nearest thief for each cell
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        # Step 2: Use a Max-Heap (Dijkstra-like) to find the path maximizing the minimum safeness factor
        # Python's heapq is a min-heap by default, so we store negative safeness values (-safeness, r, c)
        max_heap = [(-dist[0][0], 0, 0)]
        
        # Track the maximum safeness found for each cell to prevent redundant processing
        max_safeness_to = [[-1] * n for _ in range(n)]
        max_safeness_to[0][0] = dist[0][0]
        
        while max_heap:
            current_safeness, r, c = heapq.heappop(max_heap)
            current_safeness = -current_safeness  # Convert back to positive
            
            # If we reached the bottom-right corner, return the accumulated result
            if r == n - 1 and c == n - 1:
                return current_safeness
                
            # If we already found a better path to this cell, skip it
            if current_safeness < max_safeness_to[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # The safeness factor of the new path is limited by the minimum along its way
                    next_safeness = min(current_safeness, dist[nr][nc])
                    
                    if next_safeness > max_safeness_to[nr][nc]:
                        max_safeness_to[nr][nc] = next_safeness
                        heapq.heappush(max_heap, (-next_safeness, nr, nc))
                        
        return 0



# from collections import deque
# from typing import List

# class Solution:
#     def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
#         n = len(grid)
        
#         # Quick exit check
#         if grid[0][0] == 1 or grid[n-1][n-1] == 1:
#             return 0
            
#         # Step 1: Multi-source BFS to calculate distance to the nearest thief
#         dist = [[-1] * n for _ in range(n)]
#         queue = deque()
        
#         for r in range(n):
#             for c in range(n):
#                 if grid[r][c] == 1:
#                     dist[r][c] = 0
#                     queue.append((r, c))
                    
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         max_possible_safeness = 0
        
#         while queue:
#             r, c = queue.popleft()
#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
#                     dist[nr][nc] = dist[r][c] + 1
#                     max_possible_safeness = max(max_possible_safeness, dist[nr][nc])
#                     queue.append((nr, nc))
        
#         # Step 2: Helper function to check if a path exists with at least 'val' safeness
#         def isValidPath(val: int) -> bool:
#             if dist[0][0] < val or dist[n-1][n-1] < val:
#                 return False
                
#             bfs_queue = deque([(0, 0)])
#             visited = [[False] * n for _ in range(n)]
#             visited[0][0] = True
            
#             while bfs_queue:
#                 r, c = bfs_queue.popleft()
#                 if r == n - 1 and c == n - 1:
#                     return True
                    
#                 for dr, dc in directions:
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= val:
#                         visited[nr][nc] = True
#                         bfs_queue.append((nr, nc))
#             return False

#         # Step 3: Binary Search on the answer range [0, max_possible_safeness]
#         low, high = 0, min(dist[0][0], dist[n-1][n-1])
#         ans = 0
        
#         while low <= high:
#             mid = (low + high) // 2
#             if isValidPath(mid):
#                 ans = mid       # Try to find a larger viable safeness factor
#                 low = mid + 1
#             else:
#                 high = mid - 1  # Reduce safeness criteria
                
#         return ans