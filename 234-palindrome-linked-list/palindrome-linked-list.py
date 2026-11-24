# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True

        # 1. Find middle of the linked list using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half in place
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Compare first half and reversed second half
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True