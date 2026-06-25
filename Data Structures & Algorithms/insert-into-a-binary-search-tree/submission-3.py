# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node
        dummy = root

        while root:
            if root.val > val:
                if root.left:
                    root = root.left
                else:
                    root.left = new_node
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = new_node
                    break
        
        return dummy