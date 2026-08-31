# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        index = 1

        first_critical_idx = -1
        last_critical_idx = -1
        min_distance = float('inf')

        while curr.next:
            next_node = curr.next
            
            # Check if current node is a local maxima or minima
            is_maxima = curr.val > prev.val and curr.val > next_node.val
            is_minima = curr.val < prev.val and curr.val < next_node.val

            if is_maxima or is_minima:
                if first_critical_idx == -1:
                    first_critical_idx = index
                else:
                    # Update minimum distance using the previous critical point
                    min_distance = min(min_distance, index - last_critical_idx)
                
                last_critical_idx = index

            prev = curr
            curr = curr.next
            index += 1

        # If we found fewer than 2 critical points
        if min_distance == float('inf'):
            return [-1, -1]

        max_distance = last_critical_idx - first_critical_idx
        return [min_distance, max_distance]