# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0, head)
        current = dummy
        
        while current.next:
            if current.next.val == val:
                # Bypass the matching node
                current.next = current.next.next
            else:
                # Advance only if no deletion occurred
                current = current.next
                
        return dummy.next