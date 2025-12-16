# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorder_helper(root, result)
        return result

    def _inorder_helper(self, node: Optional[TreeNode], result: List[int]):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.val)
            self._inorder_helper(node.right, result)
