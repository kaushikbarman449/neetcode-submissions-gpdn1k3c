# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currentA = l1
        currentB = l2
        carry = 0

        # resultant node
        dummy = ListNode(0)
        tail = dummy

        while currentA or currentB or carry:
            val1 = currentA.val if currentA else 0
            val2 = currentB.val if currentB else 0

            total_sum = val1 + val2 + carry

            # store new digit
            digit = total_sum % 10
            carry = total_sum // 10

            # append the digit to new list
            tail.next = ListNode(digit)
            tail = tail.next

            if currentA:
                currentA = currentA.next
            
            if currentB:
                currentB = currentB.next

        return dummy.next
























