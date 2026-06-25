class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(n)}

        for a, b in edges:
            pre_map[a].append(b)
            pre_map[b].append(a)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for dep in pre_map[node]:
                if dep == par:
                    continue
                if not dfs(dep, node):
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visit) == n