class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {i: [] for i in range(n)}
        visit = set()

        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)

        def dfs(node, par):
            if node in visit:
                return
            
            visit.add(node)
            for adj in adj_map[node]:
                if adj == par:
                    continue
                dfs(adj, node)

        count = 0
        for node in range(n):
            if node not in visit:
                dfs(node, -1)
                count += 1
        
        return count