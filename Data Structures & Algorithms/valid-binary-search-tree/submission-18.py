# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

            # if node.left and not (left < node.left.val < node.val):
            #     return False
            
            # if node.right and not (node.val < node.right.val < right):
            #     return False
            
            # return dfs(node.left, node.val, right) and dfs(node.right, left, node.val)
        
        return dfs(root, -float('inf'), float('inf'))
            

            