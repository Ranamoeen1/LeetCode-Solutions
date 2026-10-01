class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
        
        # Path must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        max_balance = (m + n - 1) // 2
        
        # visited keeps track of (row, col, balance) states
        visited = set()
        
        # Queue/Stack for traversal: (r, c, balance)
        stack = [(0, 0, 1)]
        visited.add((0, 0, 1))
        
        while stack:
            r, c, bal = stack.pop()
            
            # Reached destination with a balanced parentheses string
            if r == m - 1 and c == n - 1 and bal == 0:
                return True
                
            for dr, dc in ((1, 0), (0, 1)):
                nr, nc = r + dr, c + dc
                if nr < m and nc < n:
                    nbal = bal + (1 if grid[nr][nc] == '(' else -1)
                    
                    # Balance cannot be negative or exceed half the path length
                    if 0 <= nbal <= max_balance:
                        if (nr, nc, nbal) not in visited:
                            visited.add((nr, nc, nbal))
                            stack.append((nr, nc, nbal))
                            
        return False