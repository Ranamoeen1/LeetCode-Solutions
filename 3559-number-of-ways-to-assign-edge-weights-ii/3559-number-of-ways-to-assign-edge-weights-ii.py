from collections import defaultdict
import sys

# Increase recursion depth for deep trees during DFS
sys.setrecursionlimit(300000)

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        MOD = 10**9 + 7
        
        # Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary lifting table and depth array
        # LOG is enough to cover n <= 10^5 (2^17 = 131072)
        LOG = 18
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # Iterative DFS to avoid stack overflow and populate depth and up[u][0]
        stack = [1]
        visited = {1}
        parent = {1: 1}
        depth[1] = 0
        
        # Post-order or simple traversal to establish tree structure
        queue = [1]
        order = []
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            order.append(curr)
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    depth[neighbor] = depth[curr] + 1
                    up[neighbor][0] = curr
                    queue.append(neighbor)
                    
        up[1][0] = 1 # Root's parent is itself
        
        # Fill the binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # Helper function to find LCA
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Bring both nodes to the same depth
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Lift both nodes simultaneously
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]

        # Precompute powers of 2 for O(1) retrieval
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD

        # Process queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                lca = get_lca(u, v)
                k = depth[u] + depth[v] - 2 * depth[lca]
                # If k edges, number of odd-sum configurations is 2^(k-1)
                ans.append(pow2[k - 1])
                
        return ans