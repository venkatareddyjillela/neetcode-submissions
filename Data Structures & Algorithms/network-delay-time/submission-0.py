class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = defaultdict(list) # src: [dest, dist]
        dist_map = {i: -1 for i in range(1, n+1)}  # dest: dist
        dist_map[k] = 0
        heap = [[0, k]]  # dist, dest
        heapq.heapify(heap)

        for u, v, t in times:
            adj_map[u].append([v, t])
        
        while heap:
            dist, dest = heapq.heappop(heap)

            for v, t in adj_map[dest]:
                new_dist = dist + t
                if dist_map[v] != -1 and dist_map[v] <= new_dist:
                    continue

                dist_map[v] = new_dist
                heapq.heappush(heap, [new_dist, v])
        print("dist_map:", dist_map)
        if min(dist_map.values()) == -1:
            return -1
        
        return max(dist_map.values())
        
        
