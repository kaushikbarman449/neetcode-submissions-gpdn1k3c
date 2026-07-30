# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return
        
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if current.val != val:
                prev = current
            else:
                prev.next = current.next

            current = current.next
        
        return dummy.next