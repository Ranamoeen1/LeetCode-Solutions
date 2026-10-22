class Solution:
  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)

    # 1. Check if nums is a rotation of the sorted array (Form A)
    is_form_a = True
    k = nums[0]
    for i in range(n):
      if nums[i] != (k + i) % n:
        is_form_a = False
        break

    if is_form_a:
      if k == 0:
        return 0
      return min(n - k, k + 2)

    # 2. Check if nums is a rotation of the reversed sorted array (Form B)
    is_form_b = True
    c = nums[0]
    for i in range(n):
      if (nums[i] + i) % n != c:
        is_form_b = False
        break

    if is_form_b:
      i = (n - 1 - c) % n
      return min(i + 1, n - i + 1)

    # If it belongs to neither group, it's impossible
    return -1