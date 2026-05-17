class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = {start}
        n = len(arr)
        
        while stack:
            curr = stack.pop()
            
            # If we find a target index with value 0, return True
            if arr[curr] == 0:
                return True
            
            # Explore both possible jump directions
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    stack.append(next_idx)
                    
        return False