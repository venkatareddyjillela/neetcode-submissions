# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # nodes_len = 0
        # temp = head
        # while temp:
        #     nodes_len += 1
        #     temp = temp.next
        
        # removable_node = nodes_len - n
        # temp = new = ListNode(0, head)
        # curr = 0
        # while temp:
        #     if curr == removable_node:
        #         temp.next = temp.next.next
        #     curr += 1
        #     temp = temp.next
        
        # return new.next
        dummy = left = ListNode(0, head)
        right = head

        while n>0 and right:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
