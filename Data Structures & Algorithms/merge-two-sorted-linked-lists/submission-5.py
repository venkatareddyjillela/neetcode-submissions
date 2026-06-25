# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        head = tail = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            else:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return head.next
            
