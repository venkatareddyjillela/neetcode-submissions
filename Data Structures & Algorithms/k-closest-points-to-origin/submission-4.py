

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(res, [dist, [x, y]])
        
        output = []
        for i in range(k):
            dist, point = heapq.heappop(res)
            output.append(point)
        
        return output