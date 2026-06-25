class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjMap = defaultdict(list)
        for src, dest in edges:
            adjMap[src].append(dest)
            adjMap[dest].append(src)
        visit = set()
        def dfs(edge, parent):
            visit.add(edge)
            for nei in adjMap[edge]:
                if nei == parent:
                    continue
                if nei not in visit:
                    dfs(nei, edge)
            
            return
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                count += 1
        
        return count
