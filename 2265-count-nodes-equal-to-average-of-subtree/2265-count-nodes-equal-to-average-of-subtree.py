# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count_matching = 0
        
        def dfs(node):
            if not node:
                return (0, 0)  # (sum, count)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            # Use integer division (//) for rounding down to the nearest integer
            if total_sum // total_count == node.val:
                self.count_matching += 1
                
            return (total_sum, total_count)
        
        dfs(root)
        return self.count_matching