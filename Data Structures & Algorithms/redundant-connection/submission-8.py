class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_map = {i: [] for i in range(1, len(edges)+1)}

        def detect_cycle(node, par):
            if node in visit:
                return True
            
            visit.add(node)
            for adj in adj_map[node]:
                if adj == par:
                    continue
                if detect_cycle(adj, node):
                    return True
            
            return False
        
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
            visit = set()
            if detect_cycle(a, -1):
                return [a, b]
        
        return []