# # class Solution:
# #     def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
# #         max_dist = 0
# #         j = 0
        
# #         for i in range(len(nums1)):
# #             # Move j forward as long as we can satisfy the condition
# #             while j < len(nums2) and nums1[i] <= nums2[j]:
# #                 j += 1
            
# #             # j-1 is the farthest valid index for current i
# #             # We need to ensure i <= j-1 (so that j-1 >= i)
# #             if j - 1 >= i:
# #                 max_dist = max(max_dist, (j - 1) - i)
        
# #         return max_dist


# class Solution:
#     def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
#         max_dist = 0
        
#         for i in range(len(nums1)):
#             # Binary search for the farthest j where nums2[j] >= nums1[i]
#             # Since nums2 is non-increasing, we need to find the rightmost index
#             # where the condition holds
#             left, right = i, len(nums2) - 1
#             farthest = -1
            
#             while left <= right:
#                 mid = (left + right) // 2
                
#                 if nums2[mid] >= nums1[i]:
#                     # This index works, try to go even further right
#                     farthest = mid
#                     left = mid + 1
#                 else:
#                     # Need to go left to find valid indices
#                     right = mid - 1
            
#             if farthest != -1:
#                 max_dist = max(max_dist, farthest - i)
        
#         return max_dist

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            # If current pair is valid, try to move j further
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # Current i doesn't work with j, try next i
                i += 1
                
            # If j is ahead, we might still get better distance
            # But if i catches up to j, we need to move j forward
            if j < i:
                j = i
        
        return max_dist