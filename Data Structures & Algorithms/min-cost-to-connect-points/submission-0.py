class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_map = defaultdict(list)
        cost = 0
        visit = set()
        heap = [[0, 0]]
        heapq.heapify(heap)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj_map[i].append([dist, j])

        while heap and len(visit) < n:
            dist, src = heapq.heappop(heap)
            if src in visit:
                continue
            visit.add(src)
            cost += dist

            for dst, dest in adj_map[src]:
                if dest in visit:
                    continue
                heapq.heappush(heap, [dst, dest])
        
        return cost





