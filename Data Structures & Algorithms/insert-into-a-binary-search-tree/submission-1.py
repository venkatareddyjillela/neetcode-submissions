# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        insert_node = TreeNode(val)
        if not root:
            return insert_node
        dummy = root
        while dummy:
            if dummy.val < val:
                if dummy.right:
                    dummy = dummy.right
                else:
                    dummy.right = insert_node
                    break
            else:
                if dummy.left:
                    dummy = dummy.left
                else:
                    dummy.left = insert_node
                    break
        return root
