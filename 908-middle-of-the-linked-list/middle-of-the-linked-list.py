# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        
        # Fast pointer moves 2 steps, slow pointer moves 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow