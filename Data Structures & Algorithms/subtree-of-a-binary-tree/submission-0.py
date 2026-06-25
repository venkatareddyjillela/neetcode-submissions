# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        def dfs(node):
            if not node:
                return False
                
            if self.same_tree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)
            
        return dfs(root) 

    def same_tree(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.same_tree(node1.left, node2.left) and self.same_tree(node1.right, node2.right)
        else:
            return False
            