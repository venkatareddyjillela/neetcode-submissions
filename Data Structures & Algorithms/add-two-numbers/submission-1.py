# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = tail = ListNode()
        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = 0
            if value >= 10:
                carry = value // 10
                value = value % 10
                
            tail.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
        
        while l1:
            value = l1.val + carry
            carry = 0
            if value >= 10:
                carry = value // 10
                value = value % 10
            tail.next = ListNode(value)
            l1 = l1.next
            tail = tail.next

        while l2:
            value = l2.val + carry
            carry = 0
            if value >= 10:
                carry = value // 10
                value = value % 10
            tail.next = ListNode(value)
            l2 = l2.next
            tail = tail.next

        if carry:
            tail.next = ListNode(carry)

        return dummy.next
