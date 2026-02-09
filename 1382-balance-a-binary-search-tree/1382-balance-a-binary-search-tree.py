# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Get sorted values from BST using inorder traversal
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        values = inorder_traversal(root)
        
        # Step 2: Build balanced BST from sorted values
        def build_balanced_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = build_balanced_bst(left, mid - 1)
            node.right = build_balanced_bst(mid + 1, right)
            return node
        
        return build_balanced_bst(0, len(values) - 1)