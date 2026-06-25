# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dq = deque([root])

        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                    return node
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)