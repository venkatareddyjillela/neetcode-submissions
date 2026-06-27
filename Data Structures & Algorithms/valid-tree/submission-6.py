class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        visit = set()

        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        def has_cycle(node, par):
            if node in visit:
                return True
            
            visit.add(node)
            for nei in adjMap[node]:
                if nei == par:
                    continue
                
                if has_cycle(nei, node):
                    return True

            return False
        
        if has_cycle(0, -1):
            return False
        
        return n == len(visit)