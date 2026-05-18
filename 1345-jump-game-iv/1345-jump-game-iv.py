from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Graph to store the indices of identical values
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # BFS setup
        queue = deque([(0, 0)])  # (current_index, steps)
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            # If we reached the last index, return the steps
            if idx == n - 1:
                return steps
            
            # 1. Jump to indices with the same value
            for neighbor in graph[arr[idx]]:
                if neighbor not in visited:
                    if neighbor == n - 1:
                        return steps + 1
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
            
            # Crucial optimization: clear the list for this value 
            # to prevent redundant O(N) scans in future steps
            graph[arr[idx]] = []
            
            # 2. Jump to the next index (i + 1)
            if idx + 1 < n and (idx + 1) not in visited:
                if idx + 1 == n - 1:
                    return steps + 1
                visited.add(idx + 1)
                queue.append((idx + 1, steps + 1))
                
            # 3. Jump to the previous index (i - 1)
            if idx - 1 >= 0 and (idx - 1) not in visited:
                visited.add(idx - 1)
                queue.append((idx - 1, steps + 1))
                
        return -1