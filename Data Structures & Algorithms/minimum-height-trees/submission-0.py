class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        for src, dst in edges:
            adjMap[src].append(dst)
            adjMap[dst].append(src)

        def dfs(node, parent):
            res = 0
            for nei in adjMap[node]:
                if nei == parent:
                    continue
                res = max(res, 1 + dfs(nei, node))
                
            return res
        node_height = defaultdict(list)
        min_height = n
        for i in range(n):
            res = dfs(i, -1)
            node_height[res].append(i)
            min_height = min(min_height, res)

        return node_height[min_height]
        
        
