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
        if not root and subRoot:
            return False
        
        def dfs(node):
            if not node:
                return False
            matched = False
            if node.val == subRoot.val:
                matched = self.isSameTree(node, subRoot)
            return matched or dfs(node.left) or dfs(node.right)
        return dfs(root)
        

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right