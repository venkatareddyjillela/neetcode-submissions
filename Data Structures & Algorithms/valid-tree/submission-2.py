class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set() 

        adjMap = [[] for _ in range(n)]
        for e1, e2 in edges:
            adjMap[e1].append(e2)
            adjMap[e2].append(e1)

        def no_cycle(node, par):
            if node in visit:
                return False

            visit.add(node)
            for adj in adjMap[node]:
                if adj == par:
                    continue
                if not no_cycle(adj, node):
                    return False
            
            return True
        
        return no_cycle(0, -1) and len(visit) == n
        
