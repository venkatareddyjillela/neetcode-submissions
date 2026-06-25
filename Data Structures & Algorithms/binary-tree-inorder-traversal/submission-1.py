# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        # q = deque([root])
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         res.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        
        # return res

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
