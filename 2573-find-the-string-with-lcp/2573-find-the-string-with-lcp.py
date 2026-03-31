class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        # Step 1: Basic validation
        for i in range(n):
            if lcp[i][i] != n - i:  # Diagonal must be n-i
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:  # Must be symmetric
                    return ""
                if lcp[i][j] > n - max(i, j):  # Can't exceed remaining length
                    return ""
                if lcp[i][j] < 0:
                    return ""
        
        # Step 2: Union-Find to group positions with same character
        # If lcp[i][j] > 0, then word[i] == word[j]
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # Group positions that must have same character
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)
        
        # Step 3: Check consistency - if lcp[i][j] == 0, they must be in different groups
        for i in range(n):
            for j in range(n):
                if lcp[i][j] == 0 and find(i) == find(j):
                    return ""
        
        # Step 4: Assign characters to groups (lexicographically smallest)
        # Map each root to a character, assign 'a', 'b', 'c', ... in order of first appearance
        char_map = {}  # root -> char
        word = [''] * n
        
        for i in range(n):
            root = find(i)
            if root not in char_map:
                # Assign next available character
                if len(char_map) >= 26:  # More than 26 groups, impossible
                    return ""
                char_map[root] = chr(ord('a') + len(char_map))
            word[i] = char_map[root]
        
        # Step 5: Verify by computing LCP from our word
        # Compute actual LCP matrix from constructed word
        def compute_lcp(s):
            m = len(s)
            res = [[0] * m for _ in range(m)]
            # Fill from bottom-right to top-left
            for i in range(m - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    if s[i] == s[j]:
                        if i + 1 < m and j + 1 < m:
                            res[i][j] = 1 + res[i + 1][j + 1]
                        else:
                            res[i][j] = 1
                    else:
                        res[i][j] = 0
            return res
        
        actual_lcp = compute_lcp(word)
        
        if actual_lcp != lcp:
            return ""
        
        return ''.join(word)