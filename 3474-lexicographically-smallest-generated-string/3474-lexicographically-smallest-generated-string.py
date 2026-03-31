class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1
        
        # res[i] = -1 means not set yet
        res = [-1] * L
        
        # Step 1: Apply all 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    c = ord(str2[j])
                    if res[pos] == -1:
                        res[pos] = c
                    elif res[pos] != c:
                        return ""  # Conflict between T constraints
        
        # Track which positions are fixed by 'T'
        fixed = [r != -1 for r in res]
        
        # Step 2: Initialize unset positions to 'a'
        for i in range(L):
            if res[i] == -1:
                res[i] = ord('a')
        
        # Step 3: Fix 'F' constraints that are violated
        for i in range(n):
            if str1[i] == 'F':
                # Check if substring equals str2
                match = True
                for j in range(m):
                    if res[i + j] != ord(str2[j]):
                        match = False
                        break
                
                if match:
                    # Need to change rightmost unfixed position to 'b'
                    found = False
                    for pos in range(i + m - 1, i - 1, -1):
                        if not fixed[pos]:
                            res[pos] = ord('b')
                            fixed[pos] = True  # Now fixed for remaining constraints
                            found = True
                            break
                    
                    if not found:
                        return ""  # Cannot satisfy this F constraint
        
        return "".join(chr(c) for c in res)