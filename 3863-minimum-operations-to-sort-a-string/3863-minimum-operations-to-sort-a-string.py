class Solution:
  def minOperations(self, s: str) -> int:
    # Case 0: Already sorted
    if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
      return 0

    # Case -1: Length 2 strings that aren't sorted cannot be fixed
    if len(s) == 2:
      return -1

    mn, mx = min(s), max(s)

    # Case 1: Min is at the start or max is at the end
    if s[0] == mn or s[-1] == mx:
      return 1

    # Case 2: Min or max exists in the interior
    if any(c in (mn, mx) for c in s[1:-1]):
      return 2

    # Case 3: Otherwise, it takes at most 3 operations
    return 3



# class Solution:
#   def minOperations(self, s: str) -> int:
#     if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
#       return 0
#     if len(s) == 2:
#       return -1

#     mn, mx = min(s), max(s)
#     if s[0] == mn or s[-1] == mx:
#       return 1

#     if any(c in (mn, mx) for c in s[1:-1]):
#       return 2

#     return 3