class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        def detected_cycle(node, parent):
            if node in visit:
                return True
            visit.add(node)
            for nei in adjMap[node]:
                if nei == parent:
                    continue
                if detected_cycle(nei, node):
                    return True
            return False

        for src, dest in edges:
            adjMap[src].append(dest)
            adjMap[dest].append(src)
            visit = set()

            if detected_cycle(src, -1):
                return [src, dest]
        
        return []
