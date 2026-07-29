class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        m = n // 2
        
        # Middle character for odd length palindromes
        mid = s[m] if n % 2 != 0 else ""
        
        # Character counts for the first half of the palindrome
        counts = [0] * 26
        for i in range(m):
            counts[ord(s[i]) - ord('a')] += 1
            
        def nCr(n: int, r: int, limit: int) -> int:
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n - r:
                r = n - r
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res > limit:
                    return limit
            return res

        def count_permutations(counts: list, limit: int) -> int:
            total = sum(counts)
            res = 1
            rem = total
            for c in counts:
                if c > 0:
                    res *= nCr(rem, c, limit)
                    if res >= limit:
                        return limit
                    rem -= c
            return res

        # Check if the total distinct palindromes available is less than k
        if count_permutations(counts, k) < k:
            return ""

        # Construct the first half character-by-character
        left = []
        for _ in range(m):
            for c in range(26):
                if counts[c] > 0:
                    counts[c] -= 1
                    perms = count_permutations(counts, k)
                    if perms >= k:
                        left.append(chr(ord('a') + c))
                        break
                    else:
                        k -= perms
                        counts[c] += 1

        left_str = "".join(left)
        return left_str + mid + left_str[::-1]