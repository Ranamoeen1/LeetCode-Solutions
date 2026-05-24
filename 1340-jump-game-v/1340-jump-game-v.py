class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        
        def dfs(i: int) -> int:
            # If already calculated, return the stored result
            if dp[i] != 0:
                return dp[i]
            
            max_visited = 1 # At minimum, we can just visit index i itself
            
            # Jump to the right: i + x
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break  # Blocked by boundary or a larger/equal element
                max_visited = max(max_visited, 1 + dfs(j))
                
            # Jump to the left: i - x
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break  # Blocked by boundary or a larger/equal element
                max_visited = max(max_visited, 1 + dfs(j))
                
            dp[i] = max_visited
            return dp[i]
        
        # We can start at any index, so find the max among all possible starting points
        return max(dfs(i) for i in range(n))