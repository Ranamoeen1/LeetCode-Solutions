class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda t: t[1])
        
        # Sort queries while preserving their original indices
        indexed_queries = sorted(enumerate(queries), key=lambda t: t[1])
        
        ans = [0] * len(queries)
        server_count = [0] * (n + 1)
        active_servers = 0
        
        j = 0  # pointer for adding logs with time <= q
        i = 0  # pointer for removing logs with time < q - x
        
        for orig_idx, q in indexed_queries:
            low = q - x
            
            # Include logs whose time is <= q
            while j < len(logs) and logs[j][1] <= q:
                srv, _ = logs[j]
                if server_count[srv] == 0:
                    active_servers += 1
                server_count[srv] += 1
                j += 1
                
            # Exclude logs whose time is outside the window (< q - x)
            while i < j and logs[i][1] < low:
                srv, _ = logs[i]
                server_count[srv] -= 1
                if server_count[srv] == 0:
                    active_servers -= 1
                i += 1
                
            # Servers with 0 requests in [q - x, q]
            ans[orig_idx] = n - active_servers
            
        return ans