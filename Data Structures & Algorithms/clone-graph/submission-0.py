"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        map_nodes = {}
        def dfs(node):
            if node in map_nodes:
                return map_nodes[node]
            
            copy = Node(node.val)
            map_nodes[node] = copy
            for node in node.neighbors:
                copy.neighbors.append(dfs(node))

            return copy
        
        return dfs(node) if node else None
        