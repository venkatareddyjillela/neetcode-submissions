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
        # node_height = defaultdict(list)
        output = []
        min_height = n
        for i in range(n):
            res = dfs(i, -1)
            if min_height == res:
                output.append(i)
            elif min_height > res:
                output = [i]
                min_height = res
            # node_height[res].append(i)
            # min_height = min(min_height, res)

        return output
