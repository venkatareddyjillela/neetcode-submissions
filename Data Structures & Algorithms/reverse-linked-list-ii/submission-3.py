# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        n = 1
        dummy = tail = ListNode()
        dummy.next = head
        while n < left:
            tail = tail.next
            n += 1

        start = end = tail.next
        tail.next = None

        while n < right:
            end = end.next
            n += 1
        
        last = end.next
        end.next = None

        curr = start
        prev = last
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        tail.next = prev

        return dummy.next
        
