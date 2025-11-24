
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)
        dummy=root.right
        root.right=root.left
        root.left=dummy
        return root