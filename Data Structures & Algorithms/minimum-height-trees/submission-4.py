class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n:
            return []
        if not edges:
            return [0]
        adj_map = defaultdict(set)

        for src, dest in edges:
            adj_map[src].add(dest)
            adj_map[dest].add(src)
        
        edge_cnt = {}
        leaves = deque()

        for src, nei in adj_map.items():
            edge_cnt[src] = len(nei)
            if len(nei) == 1:
                leaves.append(src)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for src, nei in adj_map.items():
                    if node in nei:
                        edge_cnt[src] -= 1
                        if edge_cnt[src] == 1:
                            leaves.append(src)
                




