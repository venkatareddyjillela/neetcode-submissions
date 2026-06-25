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

        if not subRoot or not root:
            return False

        match = False
        
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.val == subRoot.val:
                    res = self.isSameTree(node, subRoot)
                    match = match or res
                    if match:
                        return match
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

        return match

        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if (not node1 and node2) or (node1 and not node2):
                return False
            if not node1 and not node2:
                return True
            
            if node1.val != node2.val:
                return False
            
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right

        return dfs(p, q)
