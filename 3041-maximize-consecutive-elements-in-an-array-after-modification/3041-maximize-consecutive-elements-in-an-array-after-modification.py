class Solution:
  def maxSelectedElements(self, nums: List[int]) -> int:
    # Sort the array to build consecutive sequences from smallest to largest
    nums.sort()

    # dp[v] stores the max length of a consecutive sequence ending at value v
    dp = {}

    for x in nums:
      # Update dp[x + 1] first so we don't reuse the current element x
      dp[x + 1] = dp.get(x, 0) + 1
      dp[x] = dp.get(x - 1, 0) + 1

    return max(dp.values())