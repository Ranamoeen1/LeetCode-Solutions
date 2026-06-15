# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge Case: If the list has only one node, deleting it leaves an empty list.
        if not head or not head.next:
            return None
        
        # Initialize pointers
        # By starting 'fast' two steps ahead, 'slow' will stop exactly 
        # at the node BEFORE the middle node.
        slow = head
        fast = head.next.next
        
        # Move 'fast' at 2x speed and 'slow' at 1x speed
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Skip the middle node
        slow.next = slow.next.next
        
        return head