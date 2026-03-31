# class Solution:
#     def generateString(self, str1: str, str2: str) -> str:
#         n = len(str1)
#         m = len(str2)
#         L = n + m - 1
        
#         # res[i] = -1 means not set yet
#         res = [-1] * L
        
#         # Step 1: Apply all 'T' constraints
#         for i in range(n):
#             if str1[i] == 'T':
#                 for j in range(m):
#                     pos = i + j
#                     c = ord(str2[j])
#                     if res[pos] == -1:
#                         res[pos] = c
#                     elif res[pos] != c:
#                         return ""  # Conflict between T constraints
        
#         # Track which positions are fixed by 'T'
#         fixed = [r != -1 for r in res]
        
#         # Step 2: Initialize unset positions to 'a'
#         for i in range(L):
#             if res[i] == -1:
#                 res[i] = ord('a')
        
#         # Step 3: Fix 'F' constraints that are violated
#         for i in range(n):
#             if str1[i] == 'F':
#                 # Check if substring equals str2
#                 match = True
#                 for j in range(m):
#                     if res[i + j] != ord(str2[j]):
#                         match = False
#                         break
                
#                 if match:
#                     # Need to change rightmost unfixed position to 'b'
#                     found = False
#                     for pos in range(i + m - 1, i - 1, -1):
#                         if not fixed[pos]:
#                             res[pos] = ord('b')
#                             fixed[pos] = True  # Now fixed for remaining constraints
#                             found = True
#                             break
                    
#                     if not found:
#                         return ""  # Cannot satisfy this F constraint
        
#         return "".join(chr(c) for c in res)

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1
        
        # Build adjacency: which positions must equal each other (from T constraints)
        # And which positions are forced to specific values
        
        # Actually, let's use a simpler but efficient approach:
        # For each position, determine the set of possible characters
        
        # Step 1: Determine forced equalities and forced values from T's
        parent = list(range(L))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # Values forced by T constraints: forced_val[i] = char or None
        forced_val = [None] * L
        
        # Process T constraints: positions i+j must equal str2[j]
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    c = str2[j]
                    if forced_val[pos] is None:
                        forced_val[pos] = c
                    elif forced_val[pos] != c:
                        return ""  # Conflict
        
        # Step 2: For F constraints, we need to ensure at least one position differs
        # This is tricky - instead, let's use the "a-then-fix" approach but more carefully
        
        res = ['a'] * L
        
        # Apply forced values
        for i in range(L):
            if forced_val[i] is not None:
                res[i] = forced_val[i]
        
        # Track which positions can be changed (not forced by T)
        changeable = [forced_val[i] is None for i in range(L)]
        
        # For each F constraint, ensure it's not equal to str2
        for i in range(n):
            if str1[i] == 'F':
                # Check if it matches
                matches = all(res[i+j] == str2[j] for j in range(m))
                if matches:
                    # Find rightmost changeable position to bump
                    changed = False
                    for j in range(m-1, -1, -1):
                        pos = i + j
                        if changeable[pos]:
                            # Try to make it different from str2[j]
                            # We want smallest char > 'a' that works, or just 'b' if 'a' was set
                            # Since we set to 'a', use 'b'
                            res[pos] = 'b'
                            changeable[pos] = False  # Now fixed
                            changed = True
                            break
                    if not changed:
                        return ""
        
        return ''.join(res)