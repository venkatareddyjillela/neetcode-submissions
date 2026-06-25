# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        single, double = head, head.next

        while double and double.next:
            if single == double:
                return True
            single = single.next
            double = double.next.next
        
        return False