# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        currM = root.val
        res = [0]
        
        def dfs(node, currM):
            if not node:
                return
            if node.val >= currM:
                res[0] += 1
                currM = node.val
            dfs(node.left, currM)
            dfs(node.right, currM)
        dfs(root, currM)
        return res[0]
        