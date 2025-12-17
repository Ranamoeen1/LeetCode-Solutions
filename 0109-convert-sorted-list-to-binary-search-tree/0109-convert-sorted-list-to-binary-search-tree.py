# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
            
        self.head = head
        
        def convert(n):
            if n <= 0:
                return None
            left = convert(n // 2)
            
            root = TreeNode(self.head.val)
            self.head = self.head.next
            
            root.left = left
            
         
            root.right = convert(n - 1 - n // 2)
            
            return root
        
        return convert(count)