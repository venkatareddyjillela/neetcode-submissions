# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        stack = [[root]]
        count = 0
        while stack:
            level = []
            tree = stack.pop()
            new_tree = []
            for i in range(len(tree)):
                node = tree[i]
                if node.left:
                    new_tree.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    new_tree.append(node.right)
                    level.append(node.right.val)
            if not level:
                break
            res.append(level)
            stack.append(new_tree)
        return res
