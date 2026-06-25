# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if n == 1 and head.next is None:
        #     return head.next
        nodes_len = 0
        temp = head
        while temp:
            nodes_len += 1
            temp = temp.next
        
        removable_node = nodes_len - n
        print("removable_node:", removable_node)
        temp = new = ListNode(0, head)
        curr = 0
        while temp:
            if curr == removable_node:
                temp.next = temp.next.next
            curr += 1
            temp = temp.next
        
        return new.next