class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  # Tracks the end index of the last selected palindrome
        
        # Check every possible center (both odd and even lengths)
        for i in range(2 * n - 1):
            l = i // 2
            r = l + i % 2
            
            # Expand outwards from the center (l, r)
            while l >= 0 and r < n and s[l] == s[r]:
                # Check if the length is at least k and it doesn't overlap with the previous selection
                if r - l + 1 >= k and l > last_end:
                    ans += 1
                    last_end = r
                    break  # Move to the next center once a valid short palindrome is picked
                l -= 1
                r += 1
                
        return ans