

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, [-dist, [x, y]])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        output = []
        for _, point in min_heap:
            output.append(point)
        
        return output