class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjMap = defaultdict(list)
        for src, dest in edges:
            adjMap[src].append(dest)
            adjMap[dest].append(src)
            
        visit = set()
        def dfs(edge):
            visit.add(edge)
            for nei in adjMap[edge]:
                if nei not in visit:
                    dfs(nei)
            return

        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count
