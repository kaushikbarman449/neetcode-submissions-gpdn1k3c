# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # get list length
        count = 1
        current = head

        while current.next:
            count += 1
            current = current.next

        k = k % count  # k = 3
        if k == 0:
            return head

        # make the list circular
        current.next = head

        temp = head
        i = 1

        while i < count - k:
            temp = temp.next
            i += 1

        # make temp new tail
        newHead = temp.next
        temp.next = None

        return newHead