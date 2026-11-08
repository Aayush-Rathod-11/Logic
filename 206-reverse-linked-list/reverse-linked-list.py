# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head
        
        while current:
            # Temporarily store the next node
            next_node = current.next
            # Reverse the current node's pointer to point backward
            current.next = prev
            # Shift prev and current one step forward
            prev = current
            current = next_node
            
        # prev ends up pointing to the new head of the reversed list
        return prev