# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root):
        def preorder(node, list1):
            if not node:
                return
            list1.append(node.val)
            preorder(node.left, list1)
            preorder(node.right, list1)
        
        list1 = []
        preorder(root, list1)
        return list1
