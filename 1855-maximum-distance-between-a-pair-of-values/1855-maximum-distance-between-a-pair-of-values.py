class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        j = 0
        
        for i in range(len(nums1)):
            # Move j forward as long as we can satisfy the condition
            while j < len(nums2) and nums1[i] <= nums2[j]:
                j += 1
            
            # j-1 is the farthest valid index for current i
            # We need to ensure i <= j-1 (so that j-1 >= i)
            if j - 1 >= i:
                max_dist = max(max_dist, (j - 1) - i)
        
        return max_dist