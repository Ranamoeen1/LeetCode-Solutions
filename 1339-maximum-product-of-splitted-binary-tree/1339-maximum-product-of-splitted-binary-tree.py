# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []

        def get_sum(node):
            if not node:
                return 0
            
            current_sum = node.val + get_sum(node.left) + get_sum(node.right)
            subtree_sums.append(current_sum)
            return current_sum

        total_sum = get_sum(root)
        
        max_prod = 0
        for s in subtree_sums:
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product
        
        return max_prod % (10**9 + 7)