class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        visit = set()

        def has_cycle(node, par):
            visit.add(node)
            for nei in adjMap[node]:
                if nei != par:
                    if nei in visit:
                        return True
                    if has_cycle(nei, node):
                        return True
            visit.remove(node)

            return False

        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
            if has_cycle(a, -1):
                return [a, b]
