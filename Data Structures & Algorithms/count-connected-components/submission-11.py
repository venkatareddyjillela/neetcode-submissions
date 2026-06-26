class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = defaultdict(list)
        visit = set()
        count = 0

        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        def dfs(node, par):
            if node in visit:
                return
            visit.add(node)

            for nei in adjMap[node]:
                if nei == par:
                    continue
                
                dfs(nei, node)
            
        for node in range(n):
            if node not in visit:
                dfs(node, -1)
                count += 1
        
        return count