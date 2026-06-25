# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            a = curr.val
            b = curr.next.val
            x = ListNode(self.gcd(a, b))
            x.next = curr.next
            curr.next = x
            curr = curr.next.next
        return head
            
        

    def gcd(self, a: int, b: int) -> int:
        x = min(a, b)
        for i in range(x, 0, -1):
            if a % i == 0 and b % i == 0:
                return i