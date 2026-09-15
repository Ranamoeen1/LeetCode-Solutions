class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Base transition: do not pick a palindrome ending at index i - 1
            dp[i] = dp[i - 1]
            
            # Check for a palindrome of length k ending at s[i-1]
            if i >= k and s[i - k : i] == s[i - k : i][::-1]:
                dp[i] = max(dp[i], dp[i - k] + 1)
            
            # Check for a palindrome of length k + 1 ending at s[i-1]
            if i >= k + 1 and s[i - k - 1 : i] == s[i - k - 1 : i][::-1]:
                dp[i] = max(dp[i], dp[i - k - 1] + 1)
                
        return dp[n]



# class Solution:
#     def maxPalindromes(self, s: str, k: int) -> int:
#         n = len(s)
#         ans = 0
#         last_end = -1  # Tracks the end index of the last selected palindrome
        
#         # Check every possible center (both odd and even lengths)
#         for i in range(2 * n - 1):
#             l = i // 2
#             r = l + i % 2
            
#             # Expand outwards from the center (l, r)
#             while l >= 0 and r < n and s[l] == s[r]:
#                 # Check if the length is at least k and it doesn't overlap with the previous selection
#                 if r - l + 1 >= k and l > last_end:
#                     ans += 1
#                     last_end = r
#                     break  # Move to the next center once a valid short palindrome is picked
#                 l -= 1
#                 r += 1
                
#         return ans