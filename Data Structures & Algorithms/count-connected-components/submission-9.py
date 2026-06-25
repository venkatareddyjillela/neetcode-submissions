class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {i: [] for i in range(n)}
        visit = set()

        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)

        def dfs(node):
            visit.add(node)
            for adj in adj_map[node]:
                if adj not in visit:
                    dfs(adj)

        count = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                count += 1
        
        return count